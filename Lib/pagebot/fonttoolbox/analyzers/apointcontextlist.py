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
#     vertical.py
#
from pagebot.fonttoolbox.analyzers.apointcontext import APointContext

class APointContextList(list):
    """The PointContextList us a group of related PointContext instances that can be
    queried and selected on their attributes."""
    def __repr__(self):
        return '[%s %s]' % (self.__class__.__name__, list(self))

    def append(self, pc):
        assert isinstance(pc, APointContext)
        list.append(self, pc)

class Vertical(APointContextList):
    """The Vertical class is a list of point contexts that share the same x-value
    self.append, self.x, self.y, self.alternates, self.minYPoint, self.maxYPoint

    >>> from pagebot.fonttoolbox.analyzers.apoint import APoint
    >>> from pagebot.fonttoolbox.analyzers.apointcontext import APointContext
    >>> b1 = APoint((0, 0))
    >>> b2 = APoint((0, 100))
    >>> b3 = APoint((40, 200))
    >>> p1 = APoint((100, 200))
    >>> a1 = APoint((200, 200))
    >>> a2 = APoint((140, 100))
    >>> a3 = APoint((40, 80))
    >>> pc1 = APointContext((b1, b2, b3, p1, a1, a2, a3))
    >>> b1 = APoint((100, 0))
    >>> b2 = APoint((100, 100))
    >>> b3 = APoint((140, 200))
    >>> p1 = APoint((200, 200))
    >>> a1 = APoint((300, 200))
    >>> a2 = APoint((240, 100))
    >>> a3 = APoint((140, 80))
    >>> pc2 = APointContext((b1, b2, b3, p1, a1, a2, a3))
    >>> v = Vertical()
    >>> v.append(pc1)
    >>> v.append(pc2)
    >>> v.x, v.y
    (100, None)
    >>> v.minYPoint
    pc(100,200) horizontal
    >>> v.maxYPoint
    pc(100,200) horizontal
    >>> v.alternates
    [pc(200,200) horizontal]

    """
    # self.x

    def _get_x(self):
        if self:
            return self[0].p[0]
        return None
    x = property(_get_x)

    def _get_y(self):
        # Vertical has not one defined y
        return None
    y = property(_get_y)

    def _get_minYPoint(self):
        """Answers the point context with the minimum Y of all vertical point contexts."""
        bottomPC = None
        for pc in self:
            if bottomPC is None or pc.y < bottomPC.y:
                bottomPC = pc
        return bottomPC
    minYPoint = property(_get_minYPoint)

    def _get_maxYPoint(self):
        """Answers the point context with the maximum Y of all vertical point contexts."""
        topPC = None
        for pc in self:
            if topPC is None or pc.y > topPC.y:
                topPC = pc
        return topPC
    maxYPoint = property(_get_maxYPoint)

    def _get_alternates(self):
        """Answers the list of points that are not top or bottom."""
        alternates = []
        topBottom = (self.minYPoint, self.maxYPoint)
        for pc in self:
            if not pc in topBottom:
                alternates.append(pc)
        return alternates
    alternates = property(_get_alternates)

class Horizontal(APointContextList):
    """The Horizontal class is a list of point contexts that share the same y-value
    self.append, self.x, self.y, self.alternates, self.minXPoint, self.maxXPoint.

    >>> from pagebot.fonttoolbox.analyzers.apoint import APoint
    >>> from pagebot.fonttoolbox.analyzers.apointcontext import APointContext
    >>> b1 = APoint((0, 0))
    >>> b2 = APoint((0, 100))
    >>> b3 = APoint((40, 200))
    >>> p1 = APoint((100, 200))
    >>> a1 = APoint((200, 200))
    >>> a2 = APoint((140, 100))
    >>> a3 = APoint((40, 80))
    >>> pc1 = APointContext((b1, b2, b3, p1, a1, a2, a3))
    >>> b1 = APoint((100, 0))
    >>> b2 = APoint((100, 100))
    >>> b3 = APoint((140, 200))
    >>> p1 = APoint((200, 200))
    >>> a1 = APoint((300, 200))
    >>> a2 = APoint((240, 100))
    >>> a3 = APoint((140, 80))
    >>> pc2 = APointContext((b1, b2, b3, p1, a1, a2, a3))
    >>> h = Horizontal()
    >>> h.append(pc1)
    >>> h.append(pc2)
    >>> h.x, h.y
    (None, 200)
    >>> h.minXPoint
    pc(100,200) horizontal
    >>> h.maxXPoint
    pc(200,200) horizontal
    >>> h.alternates
    []

    """

    def _get_x(self):
        # Horizontal has no defined x
        return None
    x = property(_get_x)

    def _get_y(self):
        if self:
            return self[0].p.y
        return None
    y = property(_get_y)

    def _get_minXPoint(self):
        """Answers the point context with the minimum X of all horizontal point contexts."""
        leftPC = None
        for pc in self:
            if leftPC is None or pc.x < leftPC.x:
                leftPC = pc
        return leftPC
    minXPoint = property(_get_minXPoint)

    def _get_maxXPoint(self):
        """Answers the point context with the maximum X of all horizontal point contexts."""
        rightPC = None
        for pc in self:
            if rightPC is None or pc.x > rightPC.x:
                rightPC = pc
        return rightPC
    maxXPoint = property(_get_maxXPoint)

    # self.alternates

    def _get_alternates(self):
        """Answers the list of points that are not left or right extremes."""
        alternates = []
        leftRight = (self.minXPoint, self.maxXPoint)
        for pc in self:
            if not pc in leftRight:
                alternates.append(pc)
        return alternates

    alternates = property(_get_alternates)

class Diagonal(APointContextList):
    pass

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
