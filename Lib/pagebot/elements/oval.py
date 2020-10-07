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
#     oval.py
#


from pagebot.constants import ORIGIN, MIDDLE, CENTER
from pagebot.elements.element import Element
from pagebot.toolbox.units import pointOffset, point2D
from pagebot.toolbox.color import noColor

class Oval(Element):

    #   G E N E R I C  C O N T E X T  S U P P O R T

    def build(self, view, origin=ORIGIN, drawElements=True, **kwargs):
        """Draws the oval in the current context canvas.

        >>> e = Oval(x=0, y=20, w=500, h=3)
        >>> e.xy
        (0pt, 20pt)
        >>> e.size
        (500pt, 3pt)
        """
        context = self.context # Get current context and builder.
        p = pointOffset(self.origin, origin)
        p = self._applyScale(view, p)
        px, py, _ = p = self._applyAlignment(p) # Ignore z-axis for now.

        self.buildFrame(view, p) # Draw optional frame or borders.

        # Let the view draw frame info for debugging, in case
        # view.showFrame == True
        view.drawElementFrame(self, p)

        if self.drawBefore is not None:
            # Call if defined
            self.drawBefore(self, view, p)

        context.fill(self.css('fill', noColor))
        context.stroke(self.css('stroke', noColor), self.css('strokeWidth'))
        context.oval(px, py, self.w, self.h)
        if drawElements:
            self.buildChildElements(view, p, **kwargs)
        if self.drawAfter is not None: # Call if defined
            self.drawAfter(self, view, p)

        self._restoreScale(view)
        self.draw(view, origin)

    def build_inds(self, view, origin, drawElements=True):
        """It is better to have a separate InDesignContext build tree, because
        we need more information than just drawing instructions. We just pass
        the PageBot Element to the InDesignContext, using it's own API."""
        context = view.context
        p = pointOffset(self.origin, origin)
        px, py = p2D = point2D(self._applyAlignment(p)) # Ignore z-axis for now.
        context.oval(px, py, e=self)
        if drawElements:
            for e in self.elements:
                e.build_inds(view, p2D)

class Circle(Oval):
    def __init__(self, r=None, x=None, y=None, w=None, h=None, xAlign=None,
            yAlign=None, **kwargs):
        """Draws the circle in the current context canvas. Default alignment
        of the circle is on its middle point (CENTER, MIDDLE). That makes it
        different from the Oval, which aligns default to bottom-left.

        >>> from pagebot.toolbox.units import pt
        >>> e = Circle(r=pt(30))
        >>> e.xy, e.size
        ((0pt, 0pt), (60pt, 60pt))
        >>> e.box, e.top, e.right, e.bottom, e.left
        ((0pt, 0pt, 60pt, 60pt), 30pt, 30pt, -30pt, -30pt)
        """
        if r is not None:
            w = h = 2*r
        if x is None:
            x = ORIGIN[0]
        if y is None:
            y = ORIGIN[1]
        Oval.__init__(self, x=x, y=y, w=w, h=h,
            xAlign=xAlign or CENTER, yAlign=yAlign or MIDDLE, **kwargs)

    def _get_h(self):
        """Answers the height of the element (same as self.w)."""
        return self.w
    def _set_h(self, r):
        self.w = r
    h = property(_get_h, _set_h)

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
