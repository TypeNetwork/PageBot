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
#     specimen.py
#
#     Implement base specimen elements.
#
from pagebot.elements.element import Element
from pagebot.elements.pbgroup import Group
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.units import pointOffset, pt, em, upt, px
from pagebot.conditions import *

FONT_DOWNLOAD_URL = 'download' # Url to download the font: font/Upgrade_Try.zip
FONT_SEEALSO = 'seeAlso' # Url to alternative website: https://upgrade.typenetwork.com
FONT_ADOBE_URL = 'adobe' # Url to adobe page of the font: https://fonts.adobe.com/fonts/upgrade
FONT_GOOGLE_URL = 'google' # Url to Google fonts page of the font: https://fonts.google.com/specimen/Roboto
FONT_TYPENETWORK_URL = 'typenetwork' # Url to typeNetWork: https://store.typenetwork.com/foundry/typetr/fonts/upgrade
FONT_DESCRIPTION = 'description' # Description of this style, status, usage, glyph set', 
FONT_CAPTION = 'caption' # Optional caption with the image'

FONT_DATA_KEYS = (
    (FONT_DOWNLOAD_URL, '[F] TRY Download'), # Adding icon string once implemented in PageBot font.
    (FONT_SEEALSO, '[?] More about'),
    (FONT_TYPENETWORK_URL, '[TN] Type Network Library'), 
    (FONT_ADOBE_URL, '[A] Adobe Fonts Library'), 
    (FONT_GOOGLE_URL, '[G] Google Fonts Library'),
)
class TypeListLine(Element):

    LABEL_FONT_NAME = 'PageBot-Regular'
    CSS_ID = 'TypeListLine'
    CSS_CLASS = None

    def __init__(self, font, fontData=None, sampleText=None, fontName=None, 
            fontSize=None, labelFont=None, labelFontSize=None, **kwargs):
        """Make a sample line with font (can be None)"""
        Element.__init__(self, **kwargs)
        self.cssClass = self.CSS_CLASS or self.__class__.__name__.lower()

        # Fonts
        assert font is not None
        self.font = font
        if labelFont is None:
            labelFont = findFont(self.LABEL_FONT_NAME)
        elif not hasattr(labelFont, 'path'):
            labelFont = findFont(labelFont)
        assert labelFont is not None
        self.labelFont = labelFont

        # Font sizes
        if fontSize is not None:
            self.fontSize = fontSize
        if labelFontSize is None:
            labelFontSize = max(pt(12), self.fontSize/4)
        self.labelFontSize = labelFontSize

        if fontData is None: # No extra information available about this font
            fontData = {}
        self.fontData = fontData

        if sampleText is None:
            sampleText = fontData.get('sample')
        if sampleText is None:
            if font is None:
                sampleText = 'Missing font "%s"' % fontName
            else:
                sampleText = font.info.fullName
        self.sampleText = sampleText

        # Auto position in the TypeList parent frame
        if not self.conditions:
            self.conditions = Fit2Width(), Float2Top()

    def getLabelString(self):
        return 'Family: %s | Style: %s | Font size: %d | Glyphs: %d' % (self.font.info.familyName, self.font.info.styleName, self.fontSize, len(self.font))

    def build_html(self, view, path, drawElements=True, **kwargs):
        b = self.context.b
        b.div(cssClass=self.cssClass, style="width:100%%")

        sampleCss = """font-family:'%s';font-size:%s;line-height:%s;letter-spacing:%s""" % (
            self.font.info.cssName, px(self.fontSize), self.leading, px(self.tracking or 0))
        labelCss = """font-family:'%s';font-size:%s;line-height:%s;letter-spacing:%s""" % (
            self.labelFont.info.cssName, px(self.labelFontSize), self.leading, px(self.tracking or 0))

        b.div(cssClass='sample', style=sampleCss)
        b.addHtml(self.sampleText)
        b._div()

        b.div(cssClass='label', style=labelCss)
        #labelString = self.getLabelString()
        #if labelString:
        #    b.addHtml(labelString)

        # If Urls provided, then add then as links. 
        hasLine = False
        for k, label in FONT_DATA_KEYS:
            if k in self.fontData:
                b.a(href=self.fontData[k], target='external') # Always jump out on new window
                b.addHtml(' | ' + label)
                b._a()
                hasLine = True
        if hasLine:
            b.addHtml(' |')
        b._div()
        b._div()

    def build_css(self, view, cssList=None):
        """Build the scss variables for this element and pass the request on
        to the child elements. This should harvest the CSS that is specific
        for a single page."""
        if cssList is None:
            cssList = []

        # cssName = Upgrade-RegularItalic
        # eotName = Upgrade-Book_Italic.eot
        # woff2Name = Upgrade-Book_Italic.woff2
        # woffName = Upgrade-Book_Italic.woff
        # ttfName = Upgrade-Book_Italic.ttf --> Currently not including TTF for safety.
        css = """@font-face {
            font-family: "%s";
            src: url("%s") format("eot"),
            url("%s") format("woff2"),
            url("%s") format("woff");
        }\n""" % (self.font.info.cssName, self.font.info.eotName, 
            self.font.info.woff2Name, self.font.info.woffName)
        if css not in cssList:
            cssList.append(css)
        return cssList

    def buildElement(self, view, p, drawElements, **kwargs):
        """Draw the specimen line, assuming context to be of a drawing type.
        """
        c = self.context
        labelFont = findFont(self.LABEL_FONT_NAME)
        sampleStyle = dict(font=self.font, fontSize=self.fontSize, textFill=self.textFill)
        labelStyle = dict(font=labelFont, fontSize=self.labelFontSize or self.fontSize/4, textFill=self.textFill)
        bs = c.newString(self.sampleText, style=sampleStyle)
        bs += c.newString('\n'+self.getLabelString(), style=labelStyle)

        c.textBox(bs, (p[0], p[1], self.w, self.h))
        #print(self, self.font)

class TypeList(Group):
    """Shows a list of type styles in their style.
    Add information as it is available in the font.

    >>> from pagebot.document import Document
    >>> from pagebot.constants import A4Rounded
    >>> from pagebot.contexts import getDrawBotContext, getHtmlContext
    >>> from pagebot.toolbox.units import pt
    >>> context = getDrawBotContext()
    >>> context
    <DrawBotContext>
    >>> W, H = A4Rounded
    >>> fontSize = pt(32) # Size of main sample
    >>> adobeUrl = 'https://fonts.adobe.com/fonts/upgrade'
    >>> #adobeUrl = 'https://fonts.adobe.com/fonts/bitcount-mono-double'
    >>> downloadFontUrl = 'font/Upgrade_Try.zip'
    >>> typeNetWorkUrl = 'https://store.typenetwork.com/foundry/typetr/fonts/upgrade'
    >>> seeAlsoUrl = 'https://upgrade.typenetwork.com'
    >>> fdl = [('PageBot-Book', dict(description=None, caption=None, adobe=adobeUrl, download=downloadFontUrl, typenetwork=typeNetWorkUrl, seeAlso=seeAlsoUrl))]
    >>> fdl.append(('PageBot-Bold', dict(description=None, caption=None, adobe=adobeUrl, download=downloadFontUrl, typenetwork=typeNetWorkUrl, seeAlso=seeAlsoUrl)))
    >>> doc = Document(w=W, h=H, context=context)
    >>> view = doc.view
    >>> view.showPadding = True
    >>> page = doc[1]
    >>> page.padding = pt(50) 
    >>> typeList = TypeList(fdl, sampleText=None, fontSize=fontSize, parent=page, x=page.pl, y=page.pb, w=page.pw, h=page.ph)
    >>> typeList.size
    (495pt, 742pt)
    >>> score = page.solve()
    >>> typeList.fontSize, typeList.elements[0].box
    (32pt, (0pt, 697.2pt, 495pt, 44.8pt))
    >>> len(typeList.fonts)
    2
    >>> typeList.elements[0].size # TypeListLine expanded the width inside the typeList
    (495pt, 44.8pt)
    >>> doc.export('_export/TypeList.pdf')
    >>> view = doc.newView('Site')
    >>> doc.export('_export/TypeList')

    """
    CSS_ID = 'TypeList'

    def __init__(self, fontDataList, parent=None, h=None, fontSize=None, 
            labelFont=None, labelFontSize=None, **kwargs):
        """
        @fontNames is order and list of findFont(fontName)
        @fontData has format {
            'PageBot-Book': dict(
                description='Description of this style, status, usage, glyph set', 
                caption='Optional caption with the image'
                adobe=adobeUrl, # https://fonts.adobe.com/fonts/upgrade
                download=downloadFontUrl, # font/Upgrade_Try.zip
                typenetwork=typeNetWorkUrl, # https://store.typenetwork.com/foundry/typetr/fonts/upgrade
                seeAlso=seeAlsoUrl # https://upgrade.typenetwork.com
            )
        }
        """
        Element.__init__(self, parent=parent, h=h, fontSize=fontSize, **kwargs)
        self.fonts = []
        self.fontSize = fontSize
        for fontName, fontData in fontDataList:
            font = findFont(fontName)
            if font is not None:
                self.fonts.append(font)
            h = self.leading * pt(self.fontSize)
            TypeListLine(font, fontData=fontData, fontName=fontName, 
                fontSize=self.fontSize, labelFont=labelFont, 
                labelFontSize=labelFontSize, parent=self, h=h, **kwargs)

    def build_html(self, view, path, drawElements=True, **kwargs):
        b = self.context.b
        b.comment('Start %s.%s\n' % (self.cssId, self.cssClass))
        b.div(cssId=self.cssId, cssClass=self.cssClass)
        for e in self.elements:
            e.build_html(view, path, **kwargs)
        b._div()
        b.comment('End %s.%s\n' % (self.cssId, self.cssClass))

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])