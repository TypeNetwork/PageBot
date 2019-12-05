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
#     htmlcontext.py
#

from pagebot.contexts.base.basecontext import BaseContext
from pagebot.contexts.markup.htmlbuilder import HtmlBuilder
from pagebot.contexts.markup.htmlstring import HtmlString
from pagebot.toolbox.color import noColor

class HtmlContext(BaseContext):
    """The HtmlContext builds all parts necessary for a website. Most of the
    building is done by the HtmlBuilder instance, stored as self.b.

    HtmlContext is needed, because not all drawing can be done in HTML.
    Htmlcontext will decide to include SVG or pixel images for the
    HTML-representation depending on the type of element.

    TODO: Add all methods compatible with DrawBotContext, even if empty
    functionality for HTML/CSS.
    """
    # Indication to Typesetter that by default tags should be included in
    # output.
    useTags = True

    # Used by the generic BaseContext.newString( )
    STRING_CLASS = HtmlString
    EXPORT_TYPES = ('html', 'css', 'js')

    def __init__(self):
        super().__init__()
        self.b = HtmlBuilder()
        self.name = self.__class__.__name__
        self._fill = noColor

    def newDrawing(self, w=None, h=None, doc=None):
        """PageBot function. Ignore for now in HTMLContext.

        Clear output canvas, start new export file.
        The @doc is the optional Document instance of the caller.
        """

    def endDrawing(self):
        pass

    def newPage(self, w=None, h=None, doc=None, page=None, **kwargs):
        pass

    def newPath(self):
        return None

    def frameDuration(self, value):
        pass

    #   T E X T

    def text(self, sOrBs, p):
        pass

    def textBox(self, sOrBs, r=None, clipPath=None, align=None):
        pass

    def textOverflow(self, sOrBs, box, align=None):
        pass

    def textBoxBaselines(self, txt, box, align=None):
        pass

    def textSize(self, bs, w=None, h=None, align=None):
        pass

    # String.

    def newBulletString(self, bullet, e=None, style=None):
        """Ignore by answering None, HTML creates bullets by default."""
        return None

    #   D R A W I N G

    def rect(self, x, y, w, h):
        # TODO: Implement as SVG.
        pass

    def oval(self, x, y, w, h):
        # TODO: Implement as SVG.
        pass

    def circle(self, x, y, r):
        # TODO: Implement as SVG.
        pass

    def line(self, p1, p2):
        # TODO: Implement as SVG.
        pass

    #   I M A G E

    def imagePixelColor(self, path, p):
        return 0
        #return cls.b.imagePixelColor(path, p)

    def imageSize(self, path):
        """Answers the (w, h) image size of the image file at path. As we cannot assume
        that we have DrawBotContext available, we need to use another lib, such as PIL.
        For now, we use DrawBotContext"""
        # FIXME: get size with PIL
        #from pagebot import getContext
        #return getContext().imageSize(path)

    def scaleImage(self, path, w, h, index=None, showImageLoresMarker=False,
            exportExtension=None, force=False):
        """Scales the images and save to another file. As we cannot assume
        that we have DrawBotContext available, we need to use another lib, such as PIL.
        For now, we use DrawBotContext"""
        # FIXME: scale with PIL
        #from pagebot import getContext
        #return getContext().scaleImage(path, w, h, index=index,
        #    showImageLoresMarker=showImageLoresMarker, exportExtension=exportExtension,
        #    force=force)

    def image(self, path, p=None, alpha=1, pageNumber=None, w=None, h=None):
        """Make an HTML image tag by calling the builder"""
        self.b.img(path=path) # TODO: add other attributes here, width=w, height=h)

    def saveImage(self, path):
        """Ignore for now in this context."""

    #   C O L O R

    def fill(self, c):
        self._fill = c

    setFillColor = fill # DrawBot compatible API
    cmykFill = fill

    def stroke(self, c, w=None):
        self._stroke = c
        if w is not None:
            self.strokeWidth(w)

    setStrokeColor = stroke # DrawBot compatible API
    cmykStroke = stroke

    def strokeWidth(self, w):
        self._strokeWidth = w

    def drawGlyphPath(self, glyph):
        pass

    def getFlattenedContours(self, glyph):
        return None

    def getFlattenedPath(self, glyph):
        return None

    def getGlyphPath(self, glyph):
        return None

    def numberOfImages(self):
        return 0

    def saveDocument(self, path):
        pass

    def shadow(self, eShadow, e=None):
        pass

    def linearGradient(self, startPoint=None, endPoint=None, colors=None,
            locations=None):
        pass

    cmykShadow = shadow
    cmykLinearGradient = linearGradient
    cmykRadialGradient = linearGradient

    def setStyles(self, styles):
        pass

    # System fonts listing, installation, font properties.

    def installedFonts(self, patterns=None):
        """Should Answer the list of all fonts (name or path) that are
        installed on the OS."""

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

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
