# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     ruler.py
#
from pagebot import setFillColor
from pagebot.elements.element import Element
from pagebot.toolbox.transformer import pointOrigin2D

class Ruler(Element):
    def __init__(self, point=None, parent=None, eId=None, style=None, **kwargs):
        Element.__init__(self, point, parent, eId, style, **kwargs)
        assert self.w is not None and self.h is not None

    def getHeight(self):
        return self.style.get('strokeWidth') or 0.5 # Force default height.

    def draw(self, origin):
        ox, oy = pointOrigin2D(self.point, origin)
        setFillColor(None)
        #setStrokeColor(self.style.get('stroke', NO_COLOR), self.style('strokeWidth'))
        sIndent = self.style.get('indent')
        sTailIndent = self.style.get('tailIndent')
        w = self.w - sIndent - sTailIndent
        line((ox + sIndent, oy), (ox + w, oy))

