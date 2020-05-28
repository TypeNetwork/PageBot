#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     flatcontext.py
#
import math
from sys import platform
from os import listdir
from os.path import exists
from flat import rgb

from pagebot.constants import (DEFAULT_FONT, DEFAULT_FONT_SIZE, FILETYPE_PDF,
        FILETYPE_JPG, FILETYPE_SVG, FILETYPE_PNG, FILETYPE_GIF, LEFT,
        DEFAULT_FILETYPE, RGB)
from pagebot.contexts.basecontext.basecontext import BaseContext
from pagebot.contexts.basecontext.babelstring import BabelString, BabelLineInfo
from pagebot.contexts.flatcontext.flatbuilder import flatBuilder
from pagebot.contexts.flatcontext.flatbezierpath import FlatBezierPath
from pagebot.filepaths import ROOT_FONT_PATHS
from pagebot.fonttoolbox.fontpaths import getFontPathOfFont
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.mathematics import to255
from pagebot.mathematics.transform3d import Transform3D
from pagebot.style import makeStyle
from pagebot.toolbox.color import color, Color, noColor, blackColor
from pagebot.toolbox.units import pt, em, upt, point2D, units


HAS_PIL = True

try:
    from PIL import Image
except:
    print('FlatContext: Warning, missing PIL')
    HAS_PIL = False

class FlatBabelData:
    """Class to store cached information in BabelString._cs."""
    def __init__(self, doc, page, tx, pt, runs):
        self.doc = doc # Flat.document instance
        self.page = page # Flat.page instance
        self.tx = tx # Flat.txt instance
        self.pt = pt # Flat.placedText instance
        self.runs = runs # List of FlatRunData instances

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

class FlatRunData:
    """Class to store cached information in FlatBabelData.runs."""
    def __init__(self, st, pars):
        self.st = st # Current strike for this run
        self.pars = pars # Current list of paragraphs that share the same strike

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

class FlatContext(BaseContext):
    """The FlatContext implements the Flat functionality within the PageBot
    framework.

    TODO: merge getTransformed() and translatePoint()?

    * xxyxyz.org/flat

    Text behavior:

    st = strike(font)
        st.size(size, leading=0.0, units=Pt.UNIT)
        st.color(color)
        st.width(string)

        sp = st.span(string)
        par = st.paragraph(string)
        tx = st.text(string)

    placed = page.place()
    outl = outlines(string)

    par = paragraph(spans)

    placed = placetext()
        placed.position(x, y)
        placed.frame(x, y, w, h)
        placed.overflow()
        placed.lines()

    """

    EXPORT_TYPES = (FILETYPE_PDF, FILETYPE_SVG, FILETYPE_PNG, FILETYPE_JPG)

    # Default is point document, should not be changed. Units render to points.
    UNITS = 'pt'

    def __init__(self):
        """Constructor of Flat context.

        >>> context = FlatContext()
        >>> context.newPage(100, 100)
        >>> context.drawing.__class__.__name__
        'document'
        """
        super().__init__()
        self.b = flatBuilder

        # Save current set of values on gState stack.
        self.save()

        # Current open shape.
        self.shape = None
        self.fileType = DEFAULT_FILETYPE
        self.transform3D = Transform3D()
        self.drawing = None
        self.w = None
        self.h = None
        self._numberOfPages = 0
        self._flatFonts = {} # Caching of {font.path:flatFont}

    #   Drawing.

    def newDrawing(self, w=None, h=None, size=None, doc=None):
        """Creates a new Flat canvas to draw on. Flipped `y`-axis by default to
        conform to DrawBot's drawing methods.

        >>> context = FlatContext()
        >>> context.newPage(100, 100)
        >>> int(context.drawing.width), int(context.drawing.height)
        (100, 100)
        """

        if self.drawing:
            self.clear()

        #self.originTop = originTop
        #self.originTop = False

        if doc is not None:
            w = doc.w
            h = doc.h
        elif size is not None:
            w, h = size

        if w is None:
            w = self.w
        if h is None:
            h = self.h

        # Dimensions not allowed to be None or Flat document won't render.
        assert w is not None
        assert h is not None

        # Converts units to point values. Stores width and height information
        # in Flat document.
        wpt, hpt = upt(w, h)
        self.drawing = self.b.document(wpt, hpt, units=self.UNITS)
        #self.drawing.size(wpt, hpt, units=self.UNITS)
        #self.drawing.pages = []

    def saveDrawing(self, path, multiPage=True):
        """Save the current document to file(s)

        >>> import os
        >>> from pagebot.toolbox.units import pt
        >>> from pagebot.filepaths import getRootPath
        >>> from pagebot.toolbox.color import blackColor
        >>> # _export/* Files are ignored in git.
        >>> exportPath = getRootPath() + '/_export'
        >>> if not exists(exportPath): os.makedirs(exportPath)
        >>> context = FlatContext()
        >>> w = h = pt(100)
        >>> x = y = pt(0)
        >>> c = blackColor
        """

        """
        FIX
        >>> context.fileType = FILETYPE_JPG
        >>> context.newPage(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        # Flat is too strict with color-format match?
        >>> context.saveDrawing(exportPath + '/MyTextDocument_F.%s' % FILETYPE_JPG)
        >>> context.fileType = FILETYPE_PDF
        >>> context.newPage(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        # Flat is too strict with color-format match?
        >>> context.saveDrawing(exportPath + '/MyTextDocument_F.%s' % FILETYPE_PDF)
        >>> context.fileType = FILETYPE_PNG
        >>> context.newPage(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        >>> context.saveDrawing(exportPath + '/MyTextDocument_F.%s' % FILETYPE_PNG)
        >>> context.saveDrawing(exportPath + '/MyTextDocument_F.gif')
        [FlatContext] Gif not yet implemented for "MyTextDocument_F.gif"
        """
        # In case path starts with "_export", make sure that the directory
        # exists.
        self.checkExportPath(path)
        self.fileType = path.split('.')[-1].lower()

        if self.fileType == FILETYPE_PNG:
            if len(self.drawing.pages) == 1 or not multiPage:
                im = self.drawing.pages[0].image(kind=RGB)
                im.png(path)
            else:
                for n, p in enumerate(self.drawing.pages):
                    pagePath = path.replace('.'+FILETYPE_PNG, '%03d.%s' % (n, FILETYPE_PNG))
                    p.image(kind=RGB).png(pagePath)

        elif self.fileType == FILETYPE_JPG:
            if len(self.drawing.pages) == 1 or not multiPage:
                self.drawing.pages[0].image(kind=RGB).jpeg(path)
            else:
                for n, p in enumerate(self.drawing.pages):
                    pagePath = path.replace('.'+FILETYPE_PNG, '%03d.%s' % (n, FILETYPE_PNG))
                    p.image(kind=RGB).jpeg(pagePath)
        elif self.fileType == FILETYPE_SVG:
            if len(self.drawing.pages) == 1 or not multiPage:
                self.drawing.pages[0].svg(path)
            else:
                for n, p in enumerate(self.drawing.pages):
                    pagePath = path.replace('.'+FILETYPE_SVG, '%03d.%s' % (n, FILETYPE_SVG))
                    p.svg(pagePath)
        elif self.fileType == FILETYPE_PDF:
            self.drawing.pdf(path) # Cannot render rgba.
        elif self.fileType == FILETYPE_GIF:
            msg = '[FlatContext] Gif not yet implemented for "%s"' % path.split('/')[-1]
            print(msg)
        else:
            msg = '[FlatContext] File format "%s" is not implemented' % path.split('/')[-1]
            raise NotImplementedError(msg)

    def scaleImage(self, path, w, h, index=None, showImageLoresMarker=False,
            exportExtension=None, force=False):

        '''
        # If default _scaled directory does not exist, then create it.
        cachePath, fileName = self.path2ScaledImagePath(path, w, h, index, exportExtension)

        if not exists(cachePath):
            os.makedirs(cachePath)
        cachedFilePath = cachePath + fileName

        if force or not os.path.exists(cachedFilePath):
            # Clean the drawing stack.
            self.newDrawing()
            self.newPage(w=w, h=h)
            self.image(path, (0, 0), w=w, h=h, pageNumber=index or 0)
            if showImageLoresMarker:
                bs = self.newString('LO-RES',
                        style=dict(font=DEFAULT_FALLBACK_FONT_PATH,
                            fontSize=pt(64), fill=color(0, 1, 1),
                            textFill=color(1, 0, 0)))
                tw, th = bs.size
                self.text(bs, (w/2-tw/2, h/2-th/4))
            self.saveImage(cachedFilePath)

            # Clean the drawing stack again.
            self.newDrawing()
        return cachedFilePath
        '''
        return path

    # Compatible API with DrawBot.
    saveImage = saveDrawing

    def endDrawing(self, doc=None):
        self.drawing = None

    def clear(self):
        self.endDrawing()
        self._numberOfPages = 0

    def getDrawing(self):
        return self.drawing

    def _getValidSize(self, w, h):
        """Answer a valid size for FlatContext document and pages."""
        if w is None or w < 0:
            w = pt(1000) # Make default page size, similar to DrawBot. 
        if h is None or h < 0:
            h = pt(1000)
        return units(w), units(h)

    def setSize(self, w=None, h=None):
        """Set the initial page size of the context, in case something is drawn before
        a document or page is created.

        >>> from pagebot.toolbox.units import mm, cm
        >>> context = FlatContext()
        >>> context.w, context.h
        (None, None)
        >>> context.setSize()
        >>> context.w, context.h
        (1000pt, 1000pt)
        >>> context.setSize(100, 200)
        >>> context.w, context.h
        (100pt, 200pt)
        >>> context.setSize(mm(100), cm(200))
        >>> context.w, context.h
        (100mm, 200cm)
        """
        self.w, self.h = self._getValidSize(w, h)

    def newPage(self, w=None, h=None, doc=None):
        """Other page sizes than default in self.drawing, are ignored in Flat.

        NOTE: this generates a flat.page, not to be confused with PageBot page.
        FIXME: test units, page auto-sizes to parent doc.
        TODO: when size changes, we need to keep track of multiple Flat
        documents::

            if w != self.w:
                <add document to stack>
            if h != self.h
                <add document to stack>

        >>> from pagebot.toolbox.units import pt
        >>> context = FlatContext()
        >>> w = h = pt(100)
        >>> context.newPage(w, h)
        """
        w, h = self._getValidSize(w, h)

        if not self.drawing:
            self.newDrawing(w=w, h=h)

        assert self.drawing

        self.w = w
        self.h = h
        self._numberOfPages += 1
        self.drawing.addpage()

    def getTmpPage(self, w, h):
        drawing = self.b.document(w, h, units=self.UNITS)
        drawing.addpage()
        return drawing.pages[0]

    def _get_page(self):
        W = 800
        H = 600

        if self.drawing is None:
            self.newDrawing(w=W, h=H)
            #return None
        if self._numberOfPages == 0:
            self.newPage(w=W, h=H)

        assert self.drawing
        assert self.drawing.pages
        return self.drawing.pages[-1]
    page = property(_get_page)

    def _get_height(self):
        return self.h
    height = property(_get_height)

    def _get_width(self):
        return self.w
    width = property(_get_width)

    def getTransformed(self, x, y):
        """
        >>> context = FlatContext()
        >>> w = 800
        >>> h = 600
        >>> dx = 6
        >>> dy = 8
        >>> context.newPage(w, h)
        >>> x, y = 4, 5
        >>> context.translate(dx, dy)
        >>> p1 = context.getTransformed(x, y)
        >>> p1
        (10.0, 587)
        >>> p1[0] == 4 + dx
        True
        >>> p1[1] == h - (dy + 5)
        True
        >>> context.scale(2)
        >>> p2 = context.getTransformed(x, y)
        >>> p2[0] == (4 * 2) + dx
        True
        >>> p2[1] == h - ((5 * 2) + dy)
        True
        >>> p2
        (14.0, 582)
        """
        z = 0
        p0 = (x, y, z)
        p1 = self.transform3D.transformPoint(p0)
        x1, y1, _ = p1

        #if not self.originTop:
        y1 = self.height - y1

        return upt(x1, y1)

    #   S T A T E

    def saveGraphicState(self):
        """Save the current graphic state.

        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> context = FlatContext()
        >>> context._font.endswith('PageBot-Regular.ttf')
        True
        >>> context.save()
        >>> boldFont = findFont('Roboto-Bold')
        >>> # Set by Font instance.
        >>> context.font(boldFont)
        >>> context._font.endswith('Roboto-Bold.ttf')
        True
        >>> # Restore to original graphic state values.
        >>> context.restore()
        >>> context._font.endswith('PageBot-Regular.ttf')
        True
        """
        gState = dict(
            font=self._font,
            fontSize=self._fontSize,
            fill=self._fill,
            stroke=self._stroke,
            strokeWidth=self._strokeWidth,
            ox=self._ox,
            oy=self._oy,
            rotate=self._rotate,
            rotationCenter=self._rotationCenter,
        )
        self._gState.append(gState)

    save = saveGraphicState

    def restoreGraphicState(self):
        gState = self._gState.pop()
        self._font = gState['font']
        self._fontSize = gState['fontSize']
        self._fill = gState['fill']
        self._stroke = gState['stroke']
        self._strokeWidth = gState['strokeWidth']
        self._ox = gState['ox']
        self._oy = gState['oy']
        self._rotate = gState['rotate']
        self._rotationCenter = gState['rotationCenter']

    restore = restoreGraphicState

    #   F O N T S

    def listOpenTypeFeatures(self, fontName=None):
        """Answers the list of opentype features available in the named font.
        TODO: To be implemented."""
        #return self.b.listOpenTypeFeatures(fontName)
        return []

    def getGlyphPath(self, glyph, p=None, path=None):
        """Converts the cubic commands to a drawable path."""
        if path is None:
            path = self.newPath()

        if p is None:
            px = py = 0
        else:
            px = p[0]
            py = p[1]

        for command, t in glyph.cubic:
            # TODO: quadTo()

            if command == 'moveTo':
                x, y = t
                px0, py0 = self.getTransformed(px+x, py+y)
                path.moveTo((px0, py0))
            elif command == 'lineTo':
                x, y = t
                px0, py0 = self.getTransformed(px+x, py+y)
                path.lineTo((px0, py0))
            elif command == 'closePath':
                path.closePath()
            elif command == 'curveTo':
                p0, p1, p = t
                x0, y0 = p0
                x1, y1 = p1
                x, y = p
                x0, y0 = self.getTransformed(px + x0, py + y0)
                x1, y1 = self.getTransformed(px + x1, py + y1)
                x, y = self.getTransformed(px + x, py + y)
                path.curveTo((x0, y0), (x1, y1), (x, y))
            elif command == 'component':
                (x, y), componentGlyph = t
                #if not self.originTop:
                y = -y
                self.getGlyphPath(componentGlyph, (px+x, py+y), path)

        return path

    #   A N I M A T I O N

    def frameDuration(self, secondsPerFrame, **kwargs):
        """Set the frame duretion for animated gifs to a number of seconds per
        frame."""
        self._frameDuration = secondsPerFrame

    #   T E X T

    def text(self, bs, p):
        """Places the Babelstring instance at position p. The position can be
        any 2D or 3D points tuple. Currently the z-axis is ignored. The
        FlatContext version of the BabelString should contain Flat.text.

        >>> from pagebot.toolbox.units import pt
        >>> context = FlatContext()
        >>> style1 = dict(font='PageBot-Regular', fontSize=pt(100), textFill=(1, 0, 0))
        >>> style2 = dict(font='PageBot-Bold', fontSize=pt(50), textFill=(0, 1, 0.5))
        >>> bs = context.newString('ABCD', style=style1)
        >>> bs.add('EFGH', style=style2)
        >>> bs, bs.__class__.__name__
        ($ABCDEFGH$, 'BabelString')

        >>> context.newPage(1000, 1000)
        >>> context.fill(None)
        >>> context.stroke(0, 0.5)
        >>> context.rect(10, 500, 20, 20)
        >>> context.text(bs, (10, 500))
        >>> context.saveDrawing('_export/Flat-Text.pdf')
        """
        assert self.page is not None, 'FlatContext.text: self.page is not set.'
        xpt, ypt = self.translatePoint(p)
        self._place(bs, xpt, ypt)

    def _getFlatFont(self, font):
        """Answer the (cache) FlatFont that corresponds with font.

        >>> import flat
        >>> context = FlatContext()
        >>> font = findFont('PageBot-Regular')
        >>> context._getFlatFont(font)[0].__class__.__name__
        'font'
        """
        if isinstance(font, str):
            font = findFont(font)
        if font is None:
            font = findFont(DEFAULT_FONT)
        if not font.path in self._flatFonts:
            self._flatFonts[font.path] = self.b.font.open(font.path)
        return self._flatFonts[font.path], font

    def _place(self, bs, x, y):
        """Places the styled Flat text on a page, transform vertical
        position to position on baseline.

        """
        spans = []
        maxAscender = 0
        maxFontSize = 0
        """
        for run in bs.runs:
            flatFont, font = self._getFlatFont(run.style.get('font'))
            fontSize = run.style.get('fontSize', DEFAULT_FONT_SIZE)
            ascender = fontSize * font.info.typoAscender / font.info.unitsPerEm
            leading = upt(run.style.get('leading',em(1.2)), base=fontSize)
            textColor = color(run.style.get('textFill', blackColor))
            flatColor = rgb(*self._asFlatColor(textColor))
            strike = self.b.strike(flatFont).size(fontSize, leading).color(flatColor)
            spans.append(strike.span(run.s))
            maxAscender = max(maxAscender, ascender)
            maxFontSize = max(maxFontSize, fontSize)
        """
        #paragraphs = [self.b.paragraph(spans)]
        #placedText = self.page.place(self.b.text(paragraphs))
        #placedText.frame(x, y-maxAscender+200, placedText.width, fontSize)
        placedText = self.page.place(bs.cs.tx)
        placedText.frame(x, y, bs.tw, bs.th)

    def _asFlatColor(self, pbColor):
        # Make this dependent on type of export.
        r, g, b = pbColor.rgb
        return r*256, g*256, b*256

    def textBox(self, bs, r=None, clipPath=None, align=None):
        """Places the babelstring instance inside rectangle `r`. The rectangle
        can be any 2D or 3D points tuple. Currently the z-axis is ignored. The
        FlatContext version of the BabelString should contain Flat.text.

        FIXME: DEPRECATED
        TODO: make clipPath work.
        TODO: make align work.
        TODO: wrap placedText so we can derive length of text without overflow and
        print the result.
        TODO: use PageBot hyphenation.

        See also drawBot.contexts.baseContext textbox()

        >>> from pagebot.toolbox.units import pt
        >>> from pagebot import getContext
        >>> from pagebot.contributions.filibuster.blurb import Blurb
        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> w = 400
        >>> h = 300
        >>> context = getContext('Flat')
        >>> context.newPage(w, h)
        >>> txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean hendrerit auctor dolor eu interdum. '
        >>> font = findFont('Roboto-Regular')
        >>> style = dict(font=font, fontSize=pt(20))
        >>> style = makeStyle(style=style)
        >>> bs = context.newString(txt * 7, style=style)
        >>> bs
        $Lorem ipsu...$
        >>> r = (10, 262, 200, 300)
        >>> #of = context.textBox(bs, r) # Calculate overflow in the box
        >>> #of
        'dolor eu interdum. '
        """
        if isinstance(bs, str):
            # Creates a new string with default styles.
            style = dict(self._font or DEFAULT_FONT, fontSize=self._fontSize or self.DEFAULT_FONT_SIZE)
            style = makeStyle(style=style)
            bs = self.newString(bs, style)
        elif not isinstance(bs, BabelString):
            raise PageBotFileFormatError('FlatContext.textBox:type is %s' % bs.__class__.__name__)

        assert self.page is not None, 'FlatString.text: self.page is not set.'
        assert r is not None
        xpt, ypt, wpt, hpt = upt(r)

        return self.page.place(bs.cs.tx).frame(xpt, ypt, wpt, hpt)

    def textOverflow(self, s, box, align=LEFT):
        """Answers the the box overflow as a new FlatString in the current
        context.
        """

        """
        >>> from pagebot import getContext
        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> w, h = 400, 300
        >>> r = (10, 262, 400, 313)
        >>> context = getContext('Flat')
        >>> context.newPage(w, h)
        >>> font = findFont('Roboto-Regular')
        >>> style = {'font': font, 'fontSize': 14}
        >>> style = makeStyle(style=style)
        >>> txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin venenatis sit amet libero at finibus. '
        >>> bs = context.newString(txt * 4, style)
        >>> of = context.textOverflow(bs, r)
        """

        """
        >>> fs = context.newString(pbs, style=style)
        >>> of = context.textOverflow(fs, r)
        >>> of

        >>> of.startswith('fortune, we engaged Chris Woods who did the digital restoration')
        True
        """
        assert self.page is not None, 'FlatString.text: self.page is not set.'
        fs = self.fromBabelString(s)

        # FIXME: this actually shows the text?
        s = fs.textOverflow(self.page, box, align=align)
        return s

    def getTextSize(self, bs, w=None, h=None):
        tw = 0
        th = 0
        placedText = bs.cs.pt
        if placedText.width != w or placedText.height != h:
            # Make reflow on this new (w, h). Otherwise use the layout.runs
            # as already cached by placedText.
            placedText.frame(0, 0, w or bs.w or math.inf, h or bs.h or math.inf)

        for rIndex, (height, run) in enumerate(placedText.layout.runs()):
            rw = 0
            for style, s in run:
                rw += style.width(s)
            tw = max(tw, rw)
            if rIndex == 0:
                th += style.ascender()
            else:
                th += height
        return pt(tw, th)

    def getTextLines(self, bs, w=None, h=None):
        """Answer a list of BabeLineInfo instances

        >>> from pagebot.toolbox.units import pt
        >>> context = FlatContext()
        >>> style = dict(font='PageBot-Regular', fontSize=pt(20))
        >>> bs = context.newString('ABCD ' * 100, style, w=pt(200))
        >>> lines = context.getTextLines(bs)
        >>> len(lines)
        34
        >>> line = lines[10]
        >>> line
        <BabelLineInfo y=230.96pt>
        """
        placedText = bs.cs.pt
        lines = []
        if placedText.width != w or placedText.height != h:
            # Make reflow on this new (w, h)
            placedText.frame(0, 0, w or bs.w or math.inf, h or bs.h or math.inf)
        x = y = pt(0) # Relative vertical position
        for height, run in placedText.layout.runs(): # In Flat "run" is native data for line
            lines.append(BabelLineInfo(x, y, context=self, cLine=run))
            y += height
        return lines

    def getBaseLines(self, txt, box):
        raise NotImplementedError

    def fromBabelString(self, bs):
        """Convert the "public" data in BabelString to FlatStringData instance
        and FlatRunData for each run in bs.runs. Then answer it, probably to
        be stored in bs._cs.
        We are storing the Flat parts in cache, to avoid building them up again.

        >>> from pagebot.contexts import getContext
        >>> context = getContext('Flat')
        >>> style = dict(font='PageBot-Regular', fontSize=24)
        >>> bs = context.newString('ABCD', style)
        >>> fData = context.fromBabelString(bs)
        >>> fData
        <FlatBabelData>
        >>> bs.cs # Invokes context.fromBabelString(bs)
        <FlatBabelData>
        >>> bs.cs.page.width == fData.page.width
        True
        """
        fDoc = self.b.document(10, 10, 'pt') # Create a dummy document
        fPage = fDoc.addpage() # Create a dummy page, used for measuring on placedText
        fParagraphs = []
        fRuns = []
        for run in bs.runs:
            font = findFont(bs.style.get('font', DEFAULT_FONT))
            flatFont = self.b.font.open(font.path)
            fontSize = bs.style.get('fontSize', DEFAULT_FONT_SIZE)
            leading = upt(bs.style.get('leading', em(1.2)), base=fontSize)
            # Keep as multiplication factor to fontSize for Flat.
            tracking = em(bs.style.get('tracking', 0)).v
            st = self.b.strike(flatFont).size(upt(fontSize), leading=leading)
            st.tracking(tracking)
            r, g, b = self._asFlatColor(color(bs.style.get('textFill', blackColor)))
            # FIXME: We need to know the export file type here in advance...
            #try:
            #    st.color(self.b.rgba(r, g, b, a)) # Does not work for Flat PDF
            #except NotImplementedError:
            st.color(self.b.rgb(r, g, b)) # Hmm, how to get Flat PDF tranparancy
            # Now we have a strike that represents the style of this run.
            pars = []
            for txt in run.s.split('\n'):
                par = st.paragraph(txt)
                pars.append(par)
                fParagraphs.append(par)
            fRuns.append(FlatRunData(st=st, pars=pars))
        tx = self.b.text(fParagraphs)
        pt = fPage.place(tx)
        # Stored typically as BabelString.cs in FlatContext mode.
        return FlatBabelData(doc=fDoc, page=fPage, tx=tx, pt=pt, runs=fRuns)

    #   F O N T

    def font(self, font, fontSize=None):
        """Set the current font, in case it is not defined in a formatted
        string. Font can be a Font instance, or a full font file path, or an
        abbreveation that can be found by family or by findFont.

        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> from pagebot.fonttoolbox.fontpaths import *
        >>> from pagebot.fonttoolbox.fontpaths import getDefaultFontPath
        >>> pbFonts = getPageBotFontPaths()
        >>> print(len(pbFonts))
        59
        >>> font = findFont('Roboto-Regular')
        >>> print(font)
        <Font Roboto-Regular>
        >>> context = FlatContext()
        >>> print(context)
        <FlatContext>
        >>> context.font(font.path)
        >>> context._font.endswith('/Roboto-Regular.ttf')
        True
        >>> # If doesn't exists, path is set to default.
        >>> context.font('OtherFont', 12)
        >>> context._font == getDefaultFontPath()
        True
        >>> # Renders to pt-unit.
        >>> context._fontSize
        12
        """
        # Convert name or path to font path.
        self._font = getFontPathOfFont(font)

        if fontSize is not None:
            self._fontSize = upt(fontSize)

    def fontSize(self, fontSize):
        """Sets the current fontSize in case it is not defined in a formatted
        string.

        >>> from pagebot.toolbox.units import p
        >>> context = FlatContext()
        >>> # Set a unit.
        >>> context.fontSize(p(1))
        >>> # Defaults to pt-unit.
        >>> context._fontSize
        12
        >>> # Set a number.
        >>> context.fontSize(14)
        >>> # Defaults to pt-unit.
        >>> context._fontSize
        14
        """
        self._fontSize = upt(fontSize)

    def newBulletString(self, bullet, style=None):
        return self.newString(bullet, style=style)

    def language(self, language):
        self._language = language

    def hyphenation(self, onOff):
        self._hyphenation = onOff

    #   I M A G E

    def getResizedPathName(self, path, w, h):
        parts = path.split('.')
        pre = '.'.join(parts[:-1])
        ext = parts[-1]
        return '%s-%sx%s.%s' % (pre, w, h, ext)

    def image(self, path, p=None, alpha=1, pageNumber=None, w=None, h=None,
            scaleType=None, e=None):
        """Draws the image. If position is none, sets x and y to the origin. If
        w or h is defined, then scale the image to fit."""
        if p is None:
            p = 0, 0

        # Renders unit tuple to value tuple.
        xpt, ypt = self.translatePoint(p)
        self.save()

        doScale = w is not None or h is not None

        if HAS_PIL:
            # TODO: move to scaleImage.
            im = Image.open(path)


            # NOTE: using PIL for resizing, much faster than Flat.
            # TODO: cache result.
            if doScale:
                path = self.getResizedPathName(path, w, h)
                if not exists(path):
                    im = im.resize((w, h))
                    im.save(path, 'jpeg')
                doScale = False
        else:
            # TODO: slow scale without PIL.
            print('FlatContext.image: Missing PIL, slow context scaling instead.')
            pass

        img = self.b.image.open(path)
        if doScale:
            img.resize(width=w or 0, height=h or 0)
        placed = self.page.place(img)
        placed.position(xpt, ypt-placed.height)
        self.restore()

        # Debugging.
        #xpt, ypt = point2D(upt(p))
        #self.marker(xpt, ypt)
        #self.stroke((1, 0, 0))
        #self.fill(None)
        #self.rect(xpt, ypt, w.pt, h.pt)

    def imagePixelColor(self, path, p):
        return self.b.imagePixelColor(path, p)

    #   D R A W I N G

    def getFlatRGB(self, c):
        """Answers the color tuple that is valid for self.fileType, otherwise
        Flat gives an error.

        TODO: Make better match for all file types, transparency and spot
        color."""
        return rgb(*to255(c.rgb))

    def _getShape(self):
        """Renders Pagebot FlatBuilder shape to a Flat shape."""
        if self._fill is noColor and self._stroke is noColor:
            self._fill = blackColor

        shape = self.b.shape()

        if self._fill and self._fill != noColor:
            shape.fill(self.getFlatRGB(self._fill))
        else:
            shape.nofill()

        if self._stroke and self._stroke != noColor:
            shape.stroke(self.getFlatRGB(self._stroke)).width(self._strokeWidth)
        else:
            shape.nostroke()

        return shape

    def rect(self, x, y, w, h):
        """Calculates rectangle points by combining (x, y) with width and
        height, then runs the points through the affine transform and passes
        the coordinates to a Flat polygon to be rendered."""

        shape = self._getShape()
        x, y, w, h = upt(x, y, w, h)
        r = shape.rectangle(x, self.page.height-y-h, w, h)
        self.page.place(r)

        """
        # FIXED: Better to use Flat.rectangle

        if shape is not None:
            x1 = upt(x + w)
            y1 = upt(y + h)
            p0 = upt(x, y)
            p1 = upt(x1, y)
            p2 = upt(x1, y1)
            p3 = upt(x, y1)
            x, y = self.getTransformed(*p0)
            x1, y1 = self.getTransformed(*p1)
            x2, y2 = self.getTransformed(*p2)
            x3, y3 = self.getTransformed(*p3)
            coordinates = x, y, x1, y1, x2, y2, x3, y3
            r = shape.polygon(coordinates)
            self.page.place(r)
        """
    def oval(self, x, y, w, h):
        """Draws an oval in a rectangle, where (x, y) is the bottom left origin
        and (w, h) is the size. This default DrawBot behavior, different from
        default Flat, where the (x, y) is the middle of the oval. Compensate
        for the difference.
        """
        shape = self._getShape()
        x, y, w, h = upt(x, y, w, h)
        r = shape.ellipse(x+w/2, self.page.height-y-h/2, w/2, h/2)
        self.page.place(r)


        """
        Better to use Flat.ellipse for this.
        TODO: don't scale width / height but calculate points before
        transforming. Also convert to a path so we can rotate.

        shape = self._getShape()

        if shape is not None:
            path = self.newPath()

            # Control point offsets.
            kappa = .5522848
            offsetX = upt(w / 2) * kappa
            offsetY = upt(h / 2) * kappa

            # Middle and other extreme points.
            x0 = upt(x + (w / 2))
            y0 = upt(y + (h / 2))
            x1 = upt(x + w)
            y1 = upt(y + h)

            px0, py0 = self.getTransformed(x, y0)
            path.moveTo((px0, py0))

            cp1 = self.getTransformed(x, y0 - offsetY)
            cp2 = self.getTransformed(x0 - offsetX, y)
            p = self.getTransformed(x0, y)
            path.curveTo(cp1, cp2, p)

            cp1 = self.getTransformed(x0 + offsetX, y)
            cp2 = self.getTransformed(x1, y0 - offsetY)
            p = self.getTransformed(x1, y0)
            path.curveTo(cp1, cp2, p)

            cp1 = self.getTransformed(x1, y0 + offsetY)
            cp2 = self.getTransformed(x0 + offsetX, y1)
            p = self.getTransformed(x0, y1)
            path.curveTo(cp1, cp2, p)

            cp1 = self.getTransformed(x0 - offsetX, y1)
            cp2 = self.getTransformed(x, y0 + offsetY)
            p = self.getTransformed(x, y0)
            path.curveTo(cp1, cp2, p)
            self.drawPath()
        """

    def circle(self, x, y, r):
        """Draws a circle in a square with radius r and (x, y) as center.

        TODO: don't scale width and height but calculate points before
        transforming.
        """
        shape = self._getShape()

        if shape is not None:
            x, y = self.getTransformed(x, y)
            r = r * self._sx
            ptx, pty, pr = upt(x, y, r)
            self.page.place(shape.circle(ptx, pty, pr))

    def line(self, p0, p1):
        """Draws a line from point p0 to point p1."""
        shape = self._getShape()

        if shape is not None:
            x0, y0 = self.getTransformed(*p0)
            x1, y1 = self.getTransformed(*p1)
            ptx0, pty0, ptx1, ptt1 = upt(x0, y0, x1, y1)
            self.page.place(shape.line(x0, y0, x1, y1))

    #   P A T H

    def newPath(self):
        """Creates a new Bézier path object to store subsequent path
        commands."""
        self._bezierpath = FlatBezierPath(self.b)
        return self._bezierpath

    def drawPath(self, path=None, p=None, sx=1, sy=None):
        """Renders the path object as a Flat vector graphic."""
        # FIXME: path parameter not used.
        shape = self._getShape()

        if shape is not None:
            self.page.place(shape.path(self._bezierpath.commands))

    def translatePoint(self, p):
        x, y = point2D(upt(p))
        x = self._ox + x
        y = self.height - self._oy + y # Flip vertical
        return upt(x, y)


    def moveTo(self, p):
        p = self.translatePoint(p)
        super().moveTo(p)

    def curveTo(self, bcp1, bcp2, p):
        bcp1 = self.translatePoint(bcp1)
        bcp2 = self.translatePoint(bcp2)
        p = self.translatePoint(p)
        super().curveTo(bcp1, bcp2, p)


    '''
    def quadTo(self, bcp, p):
        bcp = self.translatePoint(bcp)
        p = self.translatePoint(p)
        super().quadTo(bcp, p)
    '''

    def qCurveTo(self, *points):
        pass

    def arc(self, center, radius, startAngle, endAngle, clockwise):
        pass

    def arcTo(self, xy1, xy2, radius):
        pass

    def lineTo(self, p):
        p = self.translatePoint(p)
        super().lineTo(p)

    def bezierPathByFlatteningPath(self, path):
        """TODO: Make our own version of the NSBezier flatten path function."""
        return None

    #   S H A D O W  &  G R A D I E N T

    def setShadow(self, eShadow):
        """Sets the DrawBot graphics state for shadow if all parameters are
        set."""

    def setGradient(self, gradient, origin, w, h):
        wpt, hpt = upt(w, h)

    def lineDash(self, *lineDash):
        pass # Not implemented?

    #   C O L O R

    def textFill(self, c):
        self.fill(c)

    setTextFillColor = textFill

    def fill(self, c):
        """Set the color for global or the color of the formatted string.
        See: http://xxyxyz.org/flat, color.py.

        """
        if c is None:
            c = noColor
        elif isinstance(c, (tuple, list)):
            c = color(*c)
        elif isinstance(c, (int, float)):
            c = color(c)

        msg = 'FlatContext.fill: Color "%s" is not Color instance'
        assert isinstance(c, Color), (msg % str(c))
        self._fill = c

    def stroke(self, c, w=None):
        """Set global stroke color or the color of the formatted string."""
        if c is None:
            c = noColor
        elif isinstance(c, (tuple, list)):
            c = color(*c)
        elif isinstance(c, (int, float)):
            c = color(c)

        msg = 'FlatContext.stroke: Color "%s" is not Color instance'
        assert isinstance(c, Color), (msg % c)
        self._stroke = c

        if w is not None:
            self.strokeWidth(w)

    def textStroke(self, c, w=None):
        """
        Flat function?
        """
        msg = 'FlatContext.textStroke: Color "%s" is not Color instance'
        assert isinstance(c, Color), (msg % c)
        self.stroke(c, w)

    setTextStrokeColor = textStroke

    def strokeWidth(self, w):
        self._strokeWidth = upt(w)

    # Transform.

    def transform(self, matrix, center=(0, 0)):
        """
        NOTE: not used, implemented as a transform3D object for now.
        """

    def translate(self, dx, dy):
        """Translates the origin by (dx, dy).
        """
        self._ox += dx
        self._oy += dy
        self.transform3D = self.transform3D.translate(dx, dy, 0)

    def rotate(self, angle, center=None):
        """Rotates by angle.
        TODO: use transform matrix.
        FIXME: implement off-center rotation.

        >>> context = FlatContext()
        >>> w = 800
        >>> h = 600
        >>> angle = 5
        >>> context.newPage(w, h)
        >>> x, y = 40, 50
        >>> context.rotate(angle)
        >>> p1 = context.getTransformed(x, y)
        """
        angle = math.radians(angle)
        # Sum of points?
        self._rotationCenter = center
        # Sum?
        self._rotate = self._rotate + angle

        if center is None or center == (0, 0):
            self.transform3D = self.transform3D.rotate(angle)
        else:
            cx, cy = center
            self.translate(cx, cy)
            self.transform3D = self.transform3D.rotate(angle)
            self.translate(-cx, -cy)

    def scale(self, sx=1, sy=None, center=(0, 0)):
        """
        TODO: add to graphics state.
        """
        self._sx = self._sx * sx
        sy = sy or sx
        self._sy = self._sy * sy

        self._scaleCenter = center
        self._strokeWidth = self._strokeWidth * sx

        if center is None or center == (0, 0):
            self.transform3D = self.transform3D.scale(sx, sy)
        else:
            cx, cy = center
            self.translate(cx, cy)
            self.transform3D = self.transform3D.scale(sx, sy)
            self.translate(-cx, -cy)

    def skew(self, angle1, angle2=0, center=(0, 0)):
        """"""
        angle1 = math.radians(angle1)
        angle2 = math.radians(angle2)
        if center is None or center == (0, 0):
            self.transform3D = self.transform3D.skew(angle1, angle2)
        else:
            cx, cy = center
            self.translate(cx, cy)
            self.transform3D = self.transform3D.skew(angle1, angle2)
            self.translate(-cx, -cy)

    # System fonts listing, installation, font properties.

    def installedFonts(self, patterns=None):
        """Answers the list of all fonts (name or path) that are installed on
        the OS.
        TODO: parse font paths.
        TODO: check patterns.

        >>> from pagebot import getContext
        >>> context = getContext('Flat')
        >>> installed = context.installedFonts()
        >>> len(installed) > 0
        True
        """
        files = []
        paths = ROOT_FONT_PATHS[platform]

        for path in paths:
            if exists(path):
                for f in listdir(path):
                    files.append(path + f)

        return files

    def installFont(self, fontOrName):
        """Should install the font in the context. fontOrName can be a Font
        instance (in which case the path is used) or a full font path."""

    def uninstallFont(self, fontOrName):
        pass

    def fontContainsCharacters(self, characters):
        pass

    def fontContainsGlyph(self, glyphName):
        pass

    def fontFilePath(self):
        pass

    def listFontGlyphNames(self):
        pass

    def fontAscender(self):
        pass

    def fontDescender(self):
        pass

    def fontXHeight(self):
        pass

    def fontCapHeight(self):
        pass

    def fontLeading(self):
        pass

    def fontLineHeight(self):
        pass


    #   E X P O R T

    def create_gif(self, filenames, duration):
        """
        TODO: Not implement yet.
        ::

            images = []

            for filename in filenames:
                images.append(imageio.imread(filename))
            output_file = 'Gif-%s.gif' % datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
            imageio.mimsave(output_file, images, duration=duration)

        """

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
