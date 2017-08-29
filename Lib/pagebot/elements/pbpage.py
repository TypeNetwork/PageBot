# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     page.py
#
import weakref
import codecs

from pagebot.elements.element import Element
from pagebot.toolbox.transformer import pointOffset, tabs

class Page(Element):

    isPage = True
    
    def isLeft(self):
        u"""Answer the boolean flag if this is a left page. The only one who can know that is the document."""
        return self.doc.isLeftPage(self)

    def isRight(self):
        u"""Answer the boolean flag if this is a right page. The only one who can know that is the document."""
        return self.doc.isRightPage(self)

    def draw(self, origin, view):
        u"""Draw all elements this page."""
        p = pointOffset(self.oPoint, origin) # Ignoe z-axis for now.
        # If there are child elements, draw them over the text.
        self._drawElements(p, view)
        # Draw addition page info, such as crop-mark, registration crosses, etc. if parameters are set.
        view.drawPageMetaInfo(self, origin)
        # Check if we are in scaled mode. Then restore.
        #self._restoreScale()

    def build(self, view, b, htmlIndent=1, cssIndent=1):
        u"""Build the HTML/CSS code through WebBuilder (or equivalent) that is the closest representation of self. 
        If there are any child elements, then also included their code, using the
        level recursive indent."""
        if self.cssPath is not None:
            b.includeCss(self.cssPath) # Add CSS content of file, if path is not None and the file exists.
        if self.htmlPath is not None:
            b.includeHtml(self.htmlPath) # Add HTML content of file, if path is not None and the file exists.
        else:
            b.addHtml('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="utf-8">\n')
            b.addHtml('\t<title>%s</title>\n' % self.name)

            pageBotCssPath = 'pagebot.css'
            b.addHtml('\t<meta name="viewport" content="width=device-width">\n')
            b.addHtml('\t<link rel="stylesheet" href="%s">\n</head>\n<body>\n' % pageBotCssPath)

            b.addHtml('%s<div id="%s">\n' % (tabs(htmlIndent), self.eId))
            b.addHtml('<hr>')
            b.addHtml('CONTENT! Elements(%d)' % len(self.elements))
            b.addHtml('<hr>')
            for e in self.elements:
                e.build(view, b, htmlIndent+1, cssIndent+1)
            b.addHtml('%s</div> <!-- %s -->\n' % (tabs(htmlIndent), self.__class__.__name__))
            b.addHtml('<body>\n<html>\n')

class Template(Page):

    def _get_parent(self):
        u"""Answer the parent of the element, if it exists, by weakref reference. Answer None of there
        is not parent defined or if the parent not longer exists."""
        if self._parent is not None:
            return self._parent()
        return None
    def _set_parent(self, parent):
        u"""Set the parent of the template. Don't call self.appendParent here, as we don't want the 
        parent to add self to the page/element list. Just a simple reference, to connect to styles, etc."""
        if parent is not None:
            parent = weakref.ref(parent)
        self._parent = parent
    parent = property(_get_parent, _set_parent)

 
    def draw(self, origin, view):
        raise ValueError('Templates cannot draw themselves in a view. Apply the template to a page first.')