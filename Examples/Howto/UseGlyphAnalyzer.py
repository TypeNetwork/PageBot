# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#     
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     UseGlyphAnalyzer.py
#
#     Implements a PageBot font classes to get info from a TTFont.
#   
from pagebot.fonttoolbox.objects.font import Font

font = Font('/Library/Fonts/Georgia.ttf')
print font.analyzer 
print font.analyzer.name 
glyphH = font['H']
gaH = glyphH.analyzer
print gaH
print 'H width:', gaH.width, gaH.glyph.width, glyphH.width
print 'H bounding box:', gaH.boundingBox
# X position of vertical lines also includes sides of serifs.
print 'x-position of verticals:', sorted(gaH.verticals.keys())
# Y position of horizontal lines
print 'y-position of horizontals:', sorted(gaH.horizontals.keys())