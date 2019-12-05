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

from pagebot.constants import (FILETYPE_PDF, FILETYPE_JPG, FILETYPE_SVG,
        FILETYPE_PNG, FILETYPE_GIF, LEFT, DEFAULT_FILETYPE, RGB)
from pagebot.contexts.base.basecontext import BaseContext
from pagebot.contexts.flatcontext.flatbuilder import flatBuilder
from pagebot.contexts.flatcontext.flatbezierpath import FlatBezierPath
from pagebot.contexts.flatcontext.flatstring import FlatString
from pagebot.errors import PageBotFileFormatError
from pagebot.filepaths import ROOT_FONT_PATHS
from pagebot.fonttoolbox.fontpaths import getFontPathOfFont
from pagebot.mathematics import to255
from pagebot.mathematics.transform3d import Transform3D
from pagebot.style import makeStyle
from pagebot.toolbox.color import color, Color, noColor
from pagebot.toolbox.units import pt, upt, point2D

class FlatContext(BaseContext):
    """The FlatContext implements the Flat functionality within the PageBot
    framework.

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

    # Used by the generic BaseContext.newString( )
    STRING_CLASS = FlatString
    EXPORT_TYPES = (FILETYPE_PDF, FILETYPE_SVG, FILETYPE_PNG, FILETYPE_JPG)

    # Default is point document, should not be changed. Units render to points.
    UNITS = 'pt'

    def __init__(self):
        """Constructor of Flat context.

        >>> context = FlatContext()
        >>> context.newDrawing(100, 100)
        >>> context.doc.__class__.__name__
        'document'
        """
        super().__init__()
        self.name = self.__class__.__name__
        self.b = flatBuilder
        self.save() # Save current set of values on gState stack.
        self.shape = None # Current open shape
        #self.flatString = None
        self.fileType = DEFAULT_FILETYPE
        self._pages = []
        self.originTop = False
        self.transform3D = Transform3D()

    #   D O C U M E N T

    def newDrawing(self, w=None, h=None, size=None, doc=None, originTop=False):
        """Creates a new self.doc Flat canvas to draw on. Flipped `y`-axis by
        default to conform to DrawBot's drawing methods.

        NOTE: not to be confused with pagebot.document.Document.

        >>> context = FlatContext()
        >>> context.newDrawing(100, 100)
        >>> int(context.doc.width), int(context.doc.height)
        (100, 100)
        """
        if doc is not None:
            w = doc.w
            h = doc.h
        elif size is not None:
            w, h = size

        self.originTop = originTop

        # Converts units to point values. Stores width and height information
        # in Flat document.
        wpt, hpt = upt(w, h)
        self.doc = self.b.document(wpt, hpt, units=self.UNITS)
        self.newPage()

    def endDrawing(self, doc=None):
        pass

    def getX(self, x):
        """Calculates `x`-coordinate based translation."""
        return self._ox + x

    def getY(self, y):
        """Calculates `y`-coordinate based on origin and translation."""
        y = self._oy + y

        if self.originTop:
            return y
        else:
            y = self.doc.height - y
            return y

    def getTransformed(self, x, y):
        """
        >>> context = FlatContext()
        >>> w = 800
        >>> h = 600
        >>> dx = 6 
        >>> dy = 8
        >>> context.newDrawing(w, h) 
        >>> x, y = 4, 5
        >>> context.translate(dx, dy)
        >>> p1 = context.getTransformed(x, y)
        >>> p1
        (10.0, 587.0)
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
        (14.0, 582.0)
        """
        z = 0
        p0 = (x, y, z)
        p1 = self.transform3D.transformPoint(p0)
        x1, y1, _ = p1

        if not self.originTop:
            y1 = self.doc.height - y1

        return x1, y1

    def saveDocument(self, path, multiPage=True):
        """Save the current document to file(s)

        >>> import os
        >>> from pagebot import getRootPath
        >>> from pagebot.toolbox.color import blackColor
        >>> exportPath = getRootPath() + '/_export' # _export/* Files are ignored in git
        >>> if not os.path.exists(exportPath): os.makedirs(exportPath)
        >>> context = FlatContext()
        >>> w = h = pt(100)
        >>> x = y = pt(0)
        >>> c = blackColor
        """

        """
        FIX
        >>> context.fileType = FILETYPE_JPG
        >>> context.newDrawing(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        # Flat is too strict with color-format match?
        >>> context.saveDocument(exportPath + '/MyTextDocument_F.%s' % FILETYPE_JPG)
        >>> context.fileType = FILETYPE_PDF
        >>> context.newDrawing(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        # Flat is too strict with color-format match?
        >>> context.saveDocument(exportPath + '/MyTextDocument_F.%s' % FILETYPE_PDF)
        >>> context.fileType = FILETYPE_PNG
        >>> context.newDrawing(w, h)
        >>> context.fill(c)
        >>> context.rect(x, y, w-20, h-20)
        >>> context.saveDocument(exportPath + '/MyTextDocument_F.%s' % FILETYPE_PNG)
        >>> context.saveDocument(exportPath + '/MyTextDocument_F.gif')
        [FlatContext] Gif not yet implemented for "MyTextDocument_F.gif"
        """
        # In case path starts with "_export", make sure that the directory
        # exists.
        self.checkExportPath(path)
        self.fileType = path.split('.')[-1].lower()

        if self.fileType == FILETYPE_PNG:
            if len(self.pages) == 1 or not multiPage:
                im = self.pages[0].image(kind=RGB)
                im.png(path)
            else:
                for n, p in enumerate(self.pages):
                    pagePath = path.replace('.'+FILETYPE_PNG, '%03d.%s' % (n, FILETYPE_PNG))
                    p.image(kind=RGB).png(pagePath)

        elif self.fileType == FILETYPE_JPG:
            if len(self.pages) == 1 or not multiPage:
                self.pages[0].image(kind=RGB).jpeg(path)
            else:
                for n, p in enumerate(self.pages):
                    pagePath = path.replace('.'+FILETYPE_PNG, '%03d.%s' % (n, FILETYPE_PNG))
                    p.image(kind=RGB).jpeg(pagePath)
        elif self.fileType == FILETYPE_SVG:
            if len(self.pages) == 1 or not multiPage:
                self.pages[0].svg(path)
            else:
                for n, p in enumerate(self.pages):
                    pagePath = path.replace('.'+FILETYPE_SVG, '%03d.%s' % (n, FILETYPE_SVG))
                    p.svg(pagePath)
        elif self.fileType == FILETYPE_PDF:
            self.doc.pdf(path)
        elif self.fileType == FILETYPE_GIF:
            msg = '[FlatContext] Gif not yet implemented for "%s"' % path.split('/')[-1]
            print(msg)
        else:
            msg = '[FlatContext] File format "%s" is not implemented' % path.split('/')[-1]
            raise NotImplementedError(msg)

    saveImage = saveDocument # Compatible API with DrawBot

    def getDocument(self):
        return self.doc

    def newPage(self, w=None, h=None, doc=None):
        """Other page sizes than default in self.doc, are ignored in Flat.

        NOTE: this generates a flat.page, not to be confused with PageBot page.
        FIXME: test units, page auto-sizes to parent doc.

        >>> context = FlatContext()
        >>> w = h = pt(100)
        >>> context.newDrawing(w, h)
        """
        if doc is not None:
            w = w or doc.w
            h = h or doc.h

        self.page = self.doc.addpage()
        self.pages.append(self.page)

    #   S T A T E

    def saveGraphicState(self):
        """Save the current graphic state.

        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> context = FlatContext()
        >>> context._font.endswith('Roboto-Regular.ttf')
        True
        >>> context.save()
        >>> boldFont = findFont('Roboto-Bold')
        >>> context.font(boldFont) # Set by Font instance
        >>> context._font.endswith('Roboto-Bold.ttf')
        True
        >>> context.restore() # Restore to original graphic state values
        >>> context._font.endswith('Roboto-Regular.ttf')
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
                if not self.originTop:
                    y = -y
                self.getGlyphPath(componentGlyph, (px+x, py+y), path)

        return path

    #   A N I M A T I O N

    def frameDuration(self, secondsPerFrame, **kwargs):
        """Set the frame duretion for animated gifs to a number of seconds per
        frame."""
        self._frameDuration = secondsPerFrame

    #   T E X T

    def text(self, fs, p):
        """Places the babelstring instance at position p. The position can be
        any 2D or 3D points tuple. Currently the z-axis is ignored. The
        FlatContext version of the BabelString should contain Flat.text.

        NOTE: in the Flat model the position is an attribute of the string,
        therefore strings cannot be reused to be displayed on multiple
        positions.

        >>> context = FlatContext()
        >>> style = dict(font='Roboto-Regular', fontSize=pt(12))
        >>> fs = context.newString('ABC', style=style)
        >>> fs.__class__.__name__
        'FlatString'
        >>> context.newDrawing(1000, 1000)
        >>> context.text(fs, (100, 100))

        """
        if isinstance(fs, str):
            # Creates a new string with default styles.
            style = {'fontSize': self._fontSize}
            style = makeStyle(style=style)
            fs = self.newString(fs, style=style)
        elif not isinstance(fs, FlatString):
            raise PageBotFileFormatError('type is %s' % type(fs))

        assert self.page is not None, 'FlatString.text: self.page is not set.'

        # TODO: move to flat string, which should keep track of multiple placed
        # text parts.

        placedText = self.page.place(fs.text)
        xpt, ypt = point2D(upt(p))
        xpt = self.getX(xpt)
        ypt = self.getY(ypt)

        if not self.originTop:
            lineHeight = fs.getLineHeight()
            ypt -= lineHeight

        if 'textFill' in fs.style:
            c = fs.style['textFill']
            c = color(rgb=c)
            self.textFill(c)

        # Renders unit tuple to value tuple.
        placedText.position(xpt, ypt)

    def textBox(self, fs, r=None, clipPath=None, align=None):
        """Places the babelstring instance inside rectangle `r`. The rectangle
        can be any 2D or 3D points tuple. Currently the z-axis is ignored. The
        FlatContext version of the BabelString should contain Flat.text.

        TODO: make clipPath work
        TODO: make align
        TODO: wrap placedText so we can derive length of text without overflow and
        print the result.

        See also drawBot.contexts.baseContext textbox()

        >>> from pagebot.contributions.filibuster.blurb import Blurb
        >>> w = 400
        >>> h = 300
        >>> from pagebot import getContext
        >>> context = getContext('Flat')
        >>> context.newDrawing(w, h)
        >>> style = {'fontSize': 14}
        >>> style = makeStyle(style=style)
        >>> blurb = Blurb()
        >>> s = blurb.getBlurb('stylewars_bluray')
        >>> fs = context.newString(s, style=style)
        >>> r = (10, 262, 400, 313)
        >>> of = context.textBox(fs, r)
        >>> of
        'without hurting the beautiful sensual quality of the original film; Gerry Gershman shepherded us through the process of acquiring all the music rights; Philippe Deneree selected the best outtakes and edited them into an exciting new document; Victor Kanefsky contributed the footage of a film bring shot at his studio, Valkhn Films, in 1983 while he and Sam Pollard were editing Style Wars. Victor and Philippe have put together that footage to make a 21 minute film about the editing of Style Wars. Lisa and I are very grateful to the Public Art Films board members, Carlos, Raquel, Sacha and Brian, for the bottomless well of their support for this project. Style Wars, the BluRay, is dedicated to the loving memory of Tony Silver, Burleigh Wartes, Jim Szalapski, Kippy Dee, Dondi, Shy 147, Kase 2, Rammellzee, and Iz the Wiz.'
        """
        if isinstance(fs, str):
            # Creates a new string with default styles.
            style = {'fontSize': self._fontSize}
            style = makeStyle(style=style)
            fs = self.newString(fs, style=style)
        elif not isinstance(fs, FlatString):
            raise PageBotFileFormatError('type is %s' % type(fs))

        assert self.page is not None, 'FlatString.text: self.page is not set.'

        assert r is not None
        xpt, ypt, wpt, hpt = upt(r)

        if self.originTop:
            ypt = self.doc.height - hpt
        else:
            ypt = self.doc.height - ypt - hpt

        box = (xpt, ypt, wpt, hpt)
        return fs.textBox(self.page, box)

    def textOverflow(self, fs, box, align=LEFT):
        """Answers the the box overflow as a new FlatString in the
        current context.
        
        >>> from pagebot.contributions.filibuster.blurb import Blurb
        >>> w = 400
        >>> h = 300
        >>> from pagebot import getContext
        >>> context = getContext('Flat')
        >>> context.newDrawing(w, h)
        >>> style = {'fontSize': 14}
        >>> style = makeStyle(style=style)
        >>> blurb = Blurb()
        >>> s = blurb.getBlurb('stylewars_bluray')
        >>> fs = context.newString(s, style=style)
        >>> r = (10, 262, 400, 313)
        >>> of = context.textOverflow(fs, r)
        >>> of
        'without hurting the beautiful sensual quality of the original film; Gerry Gershman shepherded us through the process of acquiring all the music rights; Philippe Deneree selected the best outtakes and edited them into an exciting new document; Victor Kanefsky contributed the footage of a film bring shot at his studio, Valkhn Films, in 1983 while he and Sam Pollard were editing Style Wars. Victor and Philippe have put together that footage to make a 21 minute film about the editing of Style Wars. Lisa and I are very grateful to the Public Art Films board members, Carlos, Raquel, Sacha and Brian, for the bottomless well of their support for this project. Style Wars, the BluRay, is dedicated to the loving memory of Tony Silver, Burleigh Wartes, Jim Szalapski, Kippy Dee, Dondi, Shy 147, Kase 2, Rammellzee, and Iz the Wiz.'
        """
        assert self.page is not None, 'FlatString.text: self.page is not set.'
        # FIXME: this actually shows the text?
        s = fs.textOverflow(self.page, box, align=align)
        return s

    def textSize(self, bs, w=None, h=None):
        """Answers the size tuple (w, h) of the current text. Answer (0, 0) if
        no text is defined. Answers the height of the string if the width w is
        given.

        TODO: returns frame size, not actual text size like DrawBot.

        >>> w = h = 500 # Default to pt-units
        >>> x = y = 0
        >>> from pagebot import getContext
        >>> context = getContext('Flat')
        >>> print(context)
        <FlatContext>
        >>> context.newDrawing(w, h)
        >>> style = dict(font='Roboto-Regular', fontSize=12) # Number defaults to pt-unit
        >>> print(style)
        {'font': 'Roboto-Regular', 'fontSize': 12}
        >>> bs = context.newString('ABC ', style=style)
        >>> print(type(bs))
        <class 'pagebot.contexts.flatcontext.flatstring.FlatString'>
        >>> #context.textSize(bs)
        #(201.53pt, 16.8pt)
        >>> #bs.size
        #(201.53pt, 16.8pt)
        >>> t = context.page.place(bs.text)
        >>> t = t.frame(x, y, w, h) # Numbers default to pt-units
        >>> t.overflow()
        False
        >>> bs = context.newString('ABC ' * 100000, style=style)
        >>> t = context.page.place(bs.text)
        >>> t = t.frame(x, y, w, h)
        >>> t.overflow()
        True
        >>> lines = t.lines()
        >>> #len(lines)
        35
        """
        return bs.size

    def textBoxBaseLines(self, txt, box):
        raise NotImplementedError

    #   F O N T

    def font(self, font, fontSize=None):
        """Set the current font, in case it is not defined in a formatted
        string. Font can be a Font instance, or a full font file path, or an
        abbreveation that can be found by family or by findFont.

        >>> from pagebot.fonttoolbox.objects.font import findFont
        >>> from pagebot.fonttoolbox.fontpaths import *
        >>> from pagebot.filepaths import DEFAULT_FONT_PATH
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
        >>> context.font('OtherFont', 12) # If doesn't exists, path is set to default.
        >>> context._font == DEFAULT_FONT_PATH
        True
        >>> context._fontSize # Renders to pt-unit
        12
        """
        self._font = getFontPathOfFont(font) # Convert name or path to font path.
        if fontSize is not None:
            self._fontSize = upt(fontSize)

    def fontSize(self, fontSize):
        """Sets the current fontSize in case it is not defined in a formatted
        string.

        >>> from pagebot.toolbox.units import p
        >>> context = FlatContext()
        >>> context.fontSize(p(1)) # Set a unit
        >>> context._fontSize # Defaults to pt-unit
        12
        >>> context.fontSize(14) # Set a number
        >>> context._fontSize # Defaults to pt-unit
        14
        """
        self._fontSize = upt(fontSize)

    def newBulletString(self, bullet, e=None, style=None):
        return self.newString(bullet, e=e, style=style)

    def language(self, language):
        self._language = language

    def hyphenation(self, onOff):
        # TODO: Implementation in Flat should use PageBot hyphenation?
        self._hyphenation = onOff

    #   I M A G E

    def imagePixelColor(self, path, p):
        return self.b.imagePixelColor(path, p)

    def imageSize(self, path):
        """Answers the (w, h) image size of the image file at path.

        >>> from pagebot import getResourcesPath
        >>> imagePath = getResourcesPath() + '/images/peppertom_lowres_398x530.png'
        >>> context = FlatContext()
        >>> context.imageSize(imagePath)
        (398pt, 530pt)
        """
        img = self.b.image.open(path)
        # Answer units of the same time as the document.w was defined.
        return pt(img.width), pt(img.height)

    def image(self, path, p=None, alpha=1, pageNumber=None, w=None, h=None,
            scaleType=None, e=None):
        """Draws the image. If position is none, sets x and y to the origin. If
        w or h is defined, then scale the image to fit."""
        if p is None:
            p = 0, 0

        xpt, ypt = point2D(upt(p))
        xpt = self.getX(xpt)
        ypt = self.getY(ypt)
        self.save()
        img = self.b.image.open(path)

        # TODO: calculate other if one is None.
        # TODO: maybe use PIL for resizing, cache result.
        if not w is None and not h is None:
            img.resize(width=int(w.pt), height=int(h.pt))

        if self.originTop:
            ypt -= h.pt

        placed = self.page.place(img)
        placed.position(xpt, ypt)
        self.restore()

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
            return None

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

        if shape is not None:
            x1 = x + w
            y1 = y + h
            p0 = (x, y)
            p1 = (x1, y)
            p2 = (x1, y1)
            p3 = (x, y1)
            x, y = self.getTransformed(*p0)
            x1, y1 = self.getTransformed(*p1)
            x2, y2 = self.getTransformed(*p2)
            x3, y3 = self.getTransformed(*p3)
            coordinates = (x, y, x1, y1, x2, y2, x3, y3) 
            r = shape.polygon(coordinates)
            self.page.place(r)

    def oval(self, x, y, w, h):
        """Draws an oval in a rectangle, where (x, y) is the bottom left origin
        and (w, h) is the size. This default DrawBot behavior, different from
        default Flat, where the (x, y) is the middle of the oval. Compensate
        for the difference.
        
        TODO: don't scale width / height but calculate points before
        transforming. Also convert to a path so we can rotate.
        """
        shape = self._getShape()

        if shape is not None:
            path = self.newPath()

            # Control point offsets.
            kappa = .5522848
            offsetX = (w / 2) * kappa
            offsetY = (h / 2) * kappa
       
            # Middle and other extreme points.
            x0 = x + (w / 2)
            y0 = y + (h / 2)
            x1 = x + w
            y1 = y + h

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

    def circle(self, x, y, r):
        """Draws a circle in a square with radius r and (x, y) as center.
        
        TODO: don't scale width / height but calculate points before transforming.
        """
        shape = self._getShape()

        if shape is not None:
            x, y = self.getTransformed(x, y)
            r = r * self._sx
            self.page.place(shape.circle(x, y, r))

    def line(self, p0, p1):
        """Draws a line from point p0 to point p1."""
        shape = self._getShape()

        if shape is not None:
            x0, y0 = self.getTransformed(*p0)
            x1, y1 = self.getTransformed(*p1)
            self.page.place(shape.line(x0, y0, x1, y1))

    #   P A T H

    def newPath(self):
        """Creates a new Bézier path object to store subsequent path commands."""
        self._bezierpath = FlatBezierPath(self.b)
        return self._bezierpath

    def drawPath(self, path=None, p=None, sx=1, sy=None):
        """Renders the path object as a Flat vector graphic."""
        # FIXME: path parameter not used.
        shape = self._getShape()

        if shape is not None:
            self.page.place(shape.path(self._bezierpath.commands))

    def moveTo(self, p):
        assert self._bezierpath is not None
        self._bezierpath.moveTo(p)

    def lineTo(self, p):
        assert self._bezierpath is not None
        self._bezierpath.lineTo(p)

    def quadTo(self, bcp, p):
        assert self._bezierpath is not None
        self._bezierpath.quadTo(bcp, p)

    def curveTo(self, bcp1, bcp2, p):
        assert self._bezierpath is not None
        self._bezierpath.curveTo(bcp1, bcp2, p)

    def closePath(self):
        assert self._bezierpath is not None
        self._bezierpath.closePath()

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
        >>> context.newDrawing(w, h) 
        >>> x, y = 40, 50
        >>> context.rotate(angle)
        >>> p1 = context.getTransformed(x, y)
        """
        angle = math.radians(angle)
        self._rotationCenter = center # Sum of points?
        self._rotate = self._rotate + angle # Sum?

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
        """Answers the list of all fonts (name or path) that are installed on the
        OS.
        TODO: parse font paths.
        TODO: check pattern

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
        Flat function?

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
