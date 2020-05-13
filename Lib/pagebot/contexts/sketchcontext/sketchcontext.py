#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#  P A G E B O T
#
#  Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#  www.pagebot.io
#  Licensed under MIT conditions
#
#  Supporting DrawBot, www.drawbot.com
#  Supporting Flat, xxyxyz.org/flat
#  Supporting Sketch, https://github.com/Zahlii/python_sketch_api
# -----------------------------------------------------------------------------
#
#  sketchcontext.py
#
#  Inspace sketch file:
#  https://xaviervia.github.io/sketch2json/
#
#  https://gist.github.com/xaviervia/edbea95d321feacaf0b5d8acd40614b2
#  This description is not complete.
#  Additions made where found in the Reading specification of this context.
#
#  Equivalent classes on PageBot <--> SketchApp2Py
#  Publication       SketchApi/Sketch file
#  Document          SketchPage
#  Document.pages    SketchArtBoard[]
#  Page.elements     SketchArtBoard.layers
#
#  The SketchContext is, similar to the HDMLContext, capable of reading and
#  writing data into the designated file format.
#
import os

from pagebot.document import Document
from pagebot.constants import FILETYPE_SKETCH, A4
from pagebot.contexts.basecontext.basecontext import BaseContext
from pagebot.contexts.basecontext.babelstring import BabelString
from pagebot.elements import *
from pagebot.constants import *
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, units, upt, em
from pagebot.toolbox.transformer import asIntOrNone
from pagebot.fonttoolbox.objects.font import findFont

from pagebot.contexts.sketchcontext.sketchbuilder import SketchBuilder
from sketchapp2py.sketchclasses import *

class SketchContext(BaseContext):

    '''
    Lib/pagebot/contexts/sketchcontext/sketchcontext.py:254:15: W0631: Using possibly undefined loop variable 'pIndex' (undefined-loop-variable)
    '''

    W, H = A4 # Default size of a document, as SketchApp has infinite canvas.

    DOCUMENT_CLASS = Document

    def __init__(self, path=None):
        """Constructor of Sketch context.

        >>> import sketchapp2py
        >>> from pagebot.toolbox.transformer import path2Dir
        >>> from pagebot.document import Document
        >>> from pagebot.contexts import getContext
        >>> path = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateSquare.sketch'
        >>> context = SketchContext(path) # Instead of context = getContext('Sketch')
        >>> # Context now interacts with the file.
        >>> # Create a PageBot Document instance, reading the Sketch file data as source.
        >>> doc = Document(context=context)
        >>> context.readDocument(doc)
        >>> page = doc[1]
        >>> page
        <Page #1 default (576pt, 783pt) E(7)>
        """

        """
        >>> # FIXME: Try reading the PageBot elements library
        >>> import pagebot
        >>> path = path2Dir(pagebot.__file__) + '/resources/sketchapp/PageBotElements.sketch'
        >>> context = SketchContext(path) # Instead of context = getContext('Sketch')
        >>> # Context now interacts with the file.
        >>> # Create a PageBot Document instance, reading the Sketch file data as source.
        >>> doc = Document(context=context)
        >>> context.readDocument(doc)
        """
        super().__init__()
        self.name = self.__class__.__name__
        # Keep open connector to the file data. If path is None, a default resource
        # file is opened.
        self.setPath(path) # Sets self.b to SketchBuilder(path)
        self.fileType = FILETYPE_SKETCH
        self.shape = None # Current open shape
        self.w = self.h = None # Optional default context size, overwriting the Sketch document.

    def installedFonts(self, patterns=None):
        # TODO: share with Flat context.
        pass

    def setStyles(self, styles):
        pass

    def newPath(self):
        pass

    def text(self, bs, p):
        pass

    def textSize(self, bs, w=None, h=None):
        pass

    def textOverflow(self, bsOrFs, box, align=LEFT):
        pass

    def textBox(self, fs, r=None, clipPath=None, align=None):
        pass

    def getDrawing(self):
        pass

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

    def endDrawing(self, doc=None):
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

    def setSize(self, w=None, h=None):
        """Optional default document size. If not None, overwriting the size of the
        open Sketch document.

        >>> context = SketchContext()
        >>> context.w is None and context.h is None
        True
        >>> context.setSize(w=300)
        >>> context.w
        300pt
        """
        self.w = units(w)
        self.h = units(h)

    def setPath(self, path):
        """Set the self.b builder to SketchBuilder(path), answering self.b.sketchApi.

        >>> import sketchapp2py
        >>> context = SketchContext() # Context now interacts with the default Resource file.
        >>> context.b.sketchApi.filePath.split('/')[-1]
        'Template.sketch'
        >>> from pagebot.toolbox.transformer import path2Dir
        >>> path = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateSquare.sketch'
        >>> api = context.setPath(path)
        >>> api.filePath.split('/')[-1] # Listening to another file now.
        'TemplateSquare.sketch'
        """
        self.b = SketchBuilder(path)
        return self.b.sketchApi

    def getNameTree(self, layer, t=None, tab=0):
        if t is None:
            t = ''
        t += '%s%s\n' % (tab*'\t', layer)
        if hasattr(layer, 'layers'):
            for child in layer.layers:
                self.getNameTree(child, t, tab+1)
        return t

    def _extractFill(self, layer):
        if hasattr(layer, 'style') and hasattr(layer.style, 'fills') and layer.style.fills:
            sketchColor = layer.style.fills[0].color
            return color(r=sketchColor.red, g=sketchColor.green, b=sketchColor.blue, a=sketchColor.alpha)
        return color(0.5)

    def _layerName2FilePathIndex(self, name):
        """Answer the path of a referenced file and the index in the overflow sequence.
        Format: "MyContextFile.md #1"
        """
        parts = name.split('#')
        if len(parts) == 2:
            filePath = parts[0].strip()
            index = asIntOrNone(parts[1].strip())
            if os.path.exists(filePath) and index is not None:
                return filePath, index
        return None, None

    def _createElements(self, sketchLayer, e):
        """Copy the attributes of the sketchLayer into the element where
        necessary.

        """
        for layer in sketchLayer.layers:

            frame = layer.frame

            if layer.name == 'Mask':
                """Will be used as mask by images that have the same parent.
                (x,y) is defined in the parent group e."""
                frame = layer.frame
                mask = newMask(name=layer.name, parent=e, sId=layer.do_objectID,
                    x=0, y=0, w=frame.w, h=frame.h)

            elif isinstance(layer, (SketchGroup, SketchShapeGroup, SketchSlice)):
                frame = layer.frame
                y = e.h - frame.h - frame.y # Flip the y-axis
                fillColor = self._extractFill(layer)
                child = newGroup(name=layer.name, parent=e, sId=layer.do_objectID,
                    x=frame.x, y=y, w=frame.w, h=frame.h)
                self._createElements(layer, child)

            elif isinstance(layer, SketchRectangle):
                y = e.h - frame.h - frame.y # Flip the y-axis
                fillColor = self._extractFill(sketchLayer) # Sketch color is defined in parent
                newRect(name=layer.name, parent=e, sId=layer.do_objectID,
                    x=frame.x, y=y, w=frame.w, h=frame.h, fill=fillColor)

            elif isinstance(layer, SketchOval):
                y = e.h - frame.h - frame.y # Flip the y-axis
                fillColor = self._extractFill(sketchLayer) # Sketch color is defined in parent
                newOval(name=layer.name, parent=e, sId=layer.do_objectID,
                    x=frame.x, y=y, w=frame.w, h=frame.h, fill=fillColor)

            elif isinstance(layer, SketchShapePath):
                y = e.h - frame.h - frame.y # Flip the y-axis
                fillColor = self._extractFill(sketchLayer) # Sketch color is defined in parent
                if len(layer.points):
                    p1 = layer.points[0].point
                    p2 = layer.points[-1].point
                    print('sdsdsdsdsd', p1, p2)
                    Line(parent=e, x=p1.x, y=p1.x, w=p2.x - p1.x, h=p2.y - p1.y,
                            stroke=fillColor, strokeWidth=0.5)

                # '_class': 'shapePath', 
                # '_parent': None, 
                #'booleanOperation': -1, 
                #'isFixedToViewport': False, 
                #'isFlippedVertical': False, 
                #'resizingConstraint': 63, 
                #'resizingType': 0, 
                #'rotation': 0, 
                #'shouldBreakMaskChain': False, 
                #'edited': True, 
                #'isClosed': False, 
                #'pointRadiusBehaviour': 1, 
                #'points': [
                #   {'_class': 'curvePoint', 'cornerRadius': 0, 'curveFrom': '{0.0017391304347826092, 0.66666666666666674}', 'curveMode': 1, 'curveTo': '{0.0017391304347826092, 0.66666666666666674}', 'hasCurveFrom': False, 'hasCurveTo': False, 'point': '{0.0008695652173913046, 0.50000000000000022}'}, 
                #   {'_class': 'curvePoint', 'cornerRadius': 0, 'curveFrom': '{0.0034782608695652184, 0.99999999999999978}', 'curveMode': 1, 'curveTo': '{0.0034782608695652184, 0.99999999999999978}', 'hasCurveFrom': False, 'hasCurveTo': False, 'point': '{0.99913043478260866, 0.50000000000000022}'}], 
                # 'do_objectID': '5C6D85ED-3C55-4C54-B081-F713A7AF5CD8', 
                #'exportOptions': <SketchExportOptions>, 
                #'frame': <SketchRect x=0 y=0 w=575 h=0.5>, 
                #'isFlippedHorizontal': False, 
                #'isLocked': False, 
                #'isVisible': True, 
                #'layerListExpandedType': 0, 
                #'name': 'Path', 
                #'nameIsFixed': False, 
                #'resizing': False, 
                #'path': None

            elif isinstance(layer, SketchText):
                # https://blog.sketchapp.com/typesetting-in-sketch-dc870fc334fc
                # FIXME: Vertical positioning of text still to be finalized.
                bs = self.asBabelString(layer.attributedString)
                style = bs.runs[0].style
                font = style.get('font')
                fontSize = style.get('fontSize')
                ascender = fontSize * font.info.ascender/font.info.unitsPerEm
                yOffset = upt(style.get('leading'), base=fontSize) - ascender
                y = e.h - frame.h - frame.y - yOffset # Flip the y-axis
                fillColor = self._extractFill(sketchLayer) # Sketch color is defined in parent
                newText(bs, name=layer.name, parent=e,
                    sId=layer.do_objectID, x=frame.x, y=y+frame.h, w=frame.w, h=frame.h,
                    yAlign=ASCENDER, # Default Sketch text positioning
                    textFill=fillColor)

            elif isinstance(layer, SketchBitmap):
                # All internal Sketch file images are converted to .png
                # SketchApp2Py converts the internal names with long id's to their object
                # names and copies them into a parallel folder, indicated by self.b.sketchApi.sketchFile
                # If there are Mask elements with the same parent, then use it as clip path
                y = e.h - frame.h - frame.y # Flip the y-axis
                # We use the layer.name here, which can be tricky if the user changes it,
                # or if Sketch replaced the image by another. But we don't have another
                # way to trace the original image name, since Sketch converted it to an internal
                # unique id. So there is some responsibility of the designer here.
                path = self.b.sketchApi.sketchFile.imagesPath + layer.name + '.png'
                newImage(path=path, name=layer.name, parent=e, sId=layer.do_objectID,
                    x=frame.x, y=y, w=frame.w, h=frame.h)
                # The Image element does not have child elements.

            elif isinstance(layer, SketchSymbolInstance):
                # For now only show the Symbol name.
                y = e.h - frame.h - frame.y # Flip the y-axis
                newText('[%s]' % layer.name, name=layer.name, parent=e,
                    sId=layer.do_objectID, fill=0.9, textFill=0, font='PageBot-Regular', fontSize=12,
                    x=frame.x, y=y, w=frame.w, h=frame.h, yAligh=BASELINE)

            else:
                print('Unsupported layer type', layer.__class__.__name__)

    def readDocument(self, doc):
        """Read Page/Element instances from the SketchApi and fill the Document
        instance doc with them, interpreting SketchPages as chapters and
        Sketch Artboards as PageBot pages.

        >>> import sketchapp2py
        >>> from pagebot.toolbox.transformer import path2Dir
        >>> from pagebot.document import Document
        >>> path = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateText.sketch'
        >>> context = SketchContext(path=path) # Context now interacts with the default file.
        >>> # Create a PageBot Document instance, reading the current Sketch file data as source.
        >>> doc = Document(name='TestReadDocument')
        >>> context.readDocument(doc)
        >>> page = doc[1]
        >>> e = page.elements[0]
        >>> e
        <Text $Type & sty...$ x=137pt y=201.5pt w=518pt h=100pt>
        """
        sketchPages = self.b.pages # Collect the list of SketchPage instance
        sortedArtboards = {} # First sort the artboard by y-->x pairs

        for pIndex, sketchPage in enumerate(sketchPages):
            artboards = sketchPage.layers
            for aIndex, artboard in enumerate(artboards):
                sortedArtboards[(artboard.frame.y, artboard.frame.x)] = artboard

        page = doc[1]
        for aIndex, (yx, artboard) in enumerate(sorted(sortedArtboards.items())):
            page.w = pt(artboard.frame.w)
            page.h = pt(artboard.frame.h)
            # For the first page, also set the document
            if pIndex == 0:
                doc.w = page.w
                doc.h = page.h
            # Set the grid and margins
            layout = artboard.layout
            if layout is not None:
                # Sketch has gutter/2 centered on both sides of the column width.
                page.gw = pt(layout.gutterWidth)
                page.pl = pt(layout.horizontalOffset) + page.gw/2
                if layout.guttersOutside: # Gutter/2 + colunnWidth + gutter/2
                    page.pr = page.w - pt(layout.totalWidth) + page.gw - page.pl
                else: # -gutter/2 + columnWidth - gutter/2
                    page.pr = page.w - pt(layout.totalWidth) - page.pl
                gridX = []
                for col in range(layout.numberOfColumns):
                    gridX.append([pt(layout.columnWidth), page.gw])
                gridX[-1][1] = None
                page.gridX = gridX

                if layout.isEnabled:
                    page.showGrid = DEFAULT_GRID # Show grid as lines
                else:
                    page.showGrid = False
                """
                'isEnabled': (asBool, True),
                'columnWidth': (asNumber, 96),
                'drawHorizontal': (asBool, True),
                'drawHorizontalLines': (asBool, False),
                'drawVertical': (asBool, True),
                'gutterHeight': (asNumber, 24),
                'gutterWidth': (asNumber, 24),
                'guttersOutside': (asBool, False),
                'horizontalOffset': (asNumber, 60),
                'numberOfColumns': (asNumber, 5),
                'rowHeightMultiplication': (asNumber, 3),
                'totalWidth': (asNumber, 576),
                """
            # Recursively create all elements on the page, interpreting
            # the objects found on the artboard.
            self._createElements(artboard, page)

            # Since there is not really vertical margins defined,
            # we'll try to guess is here from the top and bottom position
            # of the elements.
            """
            topY = 0
            bottomY = page.h
            for e in page.elements:
                if e.top < page.h:
                    topY = max(topY, e.top)
                if e.bottom > 0:
                    bottomY = min(bottomY, e.bottom)
            page.pb = bottomY
            page.pt = page.h - topY
            """
            if aIndex < len(sortedArtboards)-1:
                page = page.next

    def save(self, path=None):
        """Save the current builder data into Sketch file, indicated by path.
        >>> import sketchapp2py
        >>> from sketchapp2py.sketchappcompare import sketchCompare
        >>> from pagebot.toolbox.transformer import path2Dir
        >>> readPath = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateSquare.sketch'
        >>> context = SketchContext(readPath) # Context now interacts with the reader file.
        >>> exportDir = path2Dir(sketchapp2py.__file__) + '/_export/'
        >>> if not os.path.exists(exportDir):
        ...     os.path.mkdir(exportDir)
        >>> savePath = exportDir + 'TemplateSquare.sketch'
        >>> context.save(savePath)
        >>> sketchCompare(readPath, savePath)
        []

        TODO: Read/Save should go through the creation and build of Document instance.
        """
        if path is None:
            path = self.b.sketchApi.filePath
        self.b.sketchApi.save(path)

    def newDocument(self, w, h):
        pass

    def newDrawing(self, w=None, h=None):
        pass

    def newPage(self, w, h):
        pass

    def saveDrawing(self, path, multiPage=True):
        pass

    def stroke(self, c, strokeWidth=None):
        pass

    def line(self, p1, p2):
        pass

    def getFlattenedPath(self, path=None):
        pass

    def getFlattenedContours(self, path=None):
        pass

    def getGlyphPath(self, glyph, p=None, path=None):
        pass

    def asBabelString(self, sas):
        """Convert the SketchAttributedString skText into a generic BabelString.

        * https://developer.apple.com/documentation/foundation/nsattributedstring
        * https://developer.apple.com/documentation/coretext/ctframesetter-2eg

        >>> import sketchapp2py
        >>> from sketchapp2py.sketchapi import SketchApi
        >>> from pagebot.toolbox.transformer import path2Dir
        >>> path = path2Dir(sketchapp2py.__file__) + '/Resources/TemplateText.sketch'
        >>> context = SketchContext(path)
        >>> skTextBox = context.b.artboards[0].layers[0] # Find the Sketch text box
        >>> sas = skTextBox.attributedString # SketchText inside the box
        >>> sas
        <SketchAttributedString>
        >>> len(sas.attributes)
        3
        >>> bs = context.asBabelString(sas) # Convert to generic BabelString
        >>> len(bs.runs) # We originally had 3 typographic parameter runs
        3
        >>> bs # Represented by joining text strings of all runs
        $Type & sty...$
        >>> bs.runs[0].s, bs.runs[0].style['font'], bs.runs[0].style['fontSize']
        ('Type ', <Font Proforma-Book>, 90)
        >>> bs.runs[1].s, bs.runs[1].style['font'], bs.runs[1].style['fontSize']
        ('&', <Font Proforma-Book>, 200)
        """

        """
        >>> sas2 = context.fromBabelString(bs) # New conversion
        >>> #sas == sas2 # Bi-directional conversion works
        True
        >>> # Now change the BabelString
        >>> bs.runs[0].style['font'] = 'Verdana-Bold'
        >>> bs.runs[1].style['font'] = 'Verdana-Italic'
        >>> bs.runs[1].style['textFill'] = color(1, 0, 0)
        >>> bs.runs[2].style['textFill'] = color(1, 0, 0.5)
        >>> bs.runs[2].s = ' changed' # Change text of the run
        >>> sas2 = context.fromBabelString(bs) # New conversion
        >>> skTextBox.attributedString = sas2
        >>> context.save('_export/TemplateTextChanged.sketch') # Save as other document
        >>> bs2 = context.asBabelString(sas2) # Convert back to pbs
        >>> bs == bs2 # This should be identical, after bi-directional conversion.
        True
        """
        assert isinstance(sas, SketchAttributedString), "%s.asBabelString: @sas has class %s" % (
            self.__class__.__name__, sas.__class__.__name__)
        ALIGNMENTS = {0: LEFT, 1: RIGHT, 2: CENTER, None: JUSTIFIED}
        bs = None
        for attrs in sas.attributes:
            # Font, fontSize and tracking are easy to extract.
            # More difficult is the leading, as Skype does not really keep
            # runs with styles and leading.
            fd = attrs.attributes.MSAttributedStringFontAttribute.attributes
            font = findFont(fd.name)
            if font is None: # If not found (e.g. OSX name, then keep the name)
                font = fd.name
            fontSize = fd.size
            tracking = em(attrs.attributes.kerning/fontSize) # Wrong Sketch name for tracking

            #print('----', attrs)
            # attrs = SketchStringAttribute
            #   location
            #   length
            #   attributes = SketchAttributes
            #       MSAttributedStringFontAttribute
            #       MSAttributedStringColorAttribute
            #       textStyleVerticalAlignmentKey
            #       kerning
            #       paragraphStyle = SketchParagraphStyle
            #           alignment
            #           minimumLineHeight
            #           maximumLineHeight
            #           paragraphSpacing
            #print('----', sas.string[attrs.location:attrs.location+attrs.length])
            #print('fontSize:', fd.name, fd.size)
            #print('minimumLineHeight:', attrs.attributes.paragraphStyle.minimumLineHeight)
            #print('maximumLineHeight:', attrs.attributes.paragraphStyle.maximumLineHeight)
            #print('paragraphSpacing:', attrs.attributes.paragraphStyle.paragraphSpacing)
            #print('...')

            #print('--d-d-d-', verticalAlignment)
            #paragraphStyle.maximumLineHeight)
            #print('3-3-3-', paragraphStyle.alignment)

            paragraphStyle = attrs.attributes.paragraphStyle
            leading = em(paragraphStyle.minimumLineHeight/fontSize)

            #minLeading = paragraphStyle.minimumLineHeight
            #axLeading = paragraphStyle.maximumLineHeight
            #paragraphSpacing = paragraphStyle.paragraphSpacing

            #print('vvvvvv', font, fontSize, leading, paragraphStyle, tracking)
            #print('xxxxxx', minLeading, maxLeading, paragraphSpacing)
            # Fill color of the this run.
            cc = attrs.attributes.MSAttributedStringColorAttribute
            textFill = color(r=cc.red, g=cc.green, b=cc.blue, a=cc.alpha)
            # 0 = TOP,
            verticalAlignment = attrs.attributes.textStyleVerticalAlignmentKey
            # Construct the run style from the extracted parameters.
            style = dict(font=font, fontSize=fontSize, textFill=textFill,
                tracking=tracking, yAlign=BASELINE, leading=leading,
                xAlign=ALIGNMENTS.get('alignment', LEFT)
            )
            # Get the string, using the location and length in the full string.
            s = sas.string[attrs.location:attrs.location+attrs.length]
            if bs is None:
                bs = self.newString(s, style)
            else:
                bs.add(s, style)
        return bs

    def fromBabelString(self, bs):
        """

        >>> bs = BabelString('abcd', style=dict(font='Roboto-Regular', fontSize=pt(18)))
        >>> context = SketchContext()

        """

        """
        >>> sas1 = context.fromBabelString(bs)
        >>> sas1
        <SketchAttributedString>
        >>> sas2 = context.fromBabelString(bs)
        >>> sas1 == sas2
        True
        """
        assert isinstance(bs, BabelString)
        ALIGNMENTS = {LEFT: 0, RIGHT: 1, CENTER: 2, JUSTIFIED: None}
        cIndex = 0
        sas = SketchAttributedString()
        sas.string = ''
        style = None
        attrs = sas.attributes
        for run in bs.runs:
            if style is None or run.style is not None:
                style = run.style
            ssa = SketchStringAttribute()
            ssa.location = cIndex
            ssa.length = len(run.s)
            sas.string += run.s
            cIndex += ssa.length

            ssa.attributes.MSAttributedStringFontAttribute = SketchFontDescriptor()
            fd = ssa.attributes.MSAttributedStringFontAttribute.attributes
            fd.name = run.style.get('font', 'Verdana')
            fd.size = upt(run.style.get('fontSize', 12))
            tc = run.style.get('textFill', color(0))

            # Leading is a special thing in Sketch!
            ssa.attributes = SketchAttributes()
            ssa.attributes.kerning = upt(style.get('tracking', 0), base=fd.size)
            ssa.attributes.textStyleVerticalAlignmentKey = 0 # ???
            ssa.attributes.paragraphStyle = SketchParagraphStyle()
            ssa.attributes.paragraphStyle.alignment = ALIGNMENTS.get(style.get('xAlign', JUSTIFIED))


            ssa.attributes.MSAttributedStringColorAttribute = SketchColor(red=tc.r, green=tc.g, blue=tc.b, alpha=tc.a)
            attrs.append(ssa)
        return sas


if __name__ == '__main__':
  import doctest
  import sys
  sys.exit(doctest.testmod()[0])