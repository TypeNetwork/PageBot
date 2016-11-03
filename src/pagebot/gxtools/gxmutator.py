# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#       from https://github.com/fonttools/fonttools/blob/master/Lib/fontTools/varLib/mutator.py
#     Licensed under MIT conditions
#     Made for usage in Drawbot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     gxmutator.py
#
import os
from fontTools.misc.py23 import *
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
from fontTools.varLib import _GetCoordinates, _SetCoordinates
from fontTools.varLib.models import VariationModel, supportScalar, normalizeLocation

from drawBot import installFont

def generateInstance(varFileName, location, targetDirectory):
    u"""
    Instantiate an instance of a variation font at the specified location.
    Keyword arguments:
        varfilename -- a variation font file path
        location -- a dictionary of axis tag and value {"wght": 0.75, "wdth": -0.5}
    """
    # make a custom file name from the location e.g. VariationFont-wghtXXX-wdthXXX.ttf
    instanceName = ""

    normalizedLoc = {}
    for k, v in location.items():
        # TODO better way to normalize the location name to (0, 1000)
        v = min(v, 1000)
        v = max(v, 0)
        instanceName += "-%s%s" % (k, v)
        normalizedLoc[k] = (v / 500.0) - 1
    targetFileName = '.'.join(varFileName.split('/')[-1].split('.')[:-1]) + instanceName + '.ttf'

    if not targetDirectory.endswith('/'):
        targetDirectory += '/'
    if not os.path.exists(targetDirectory):
        os.makedirs(targetDirectory)
    outFile = targetDirectory + targetFileName

    # print("Loading GX font")
    varfont = TTFont(varFileName)

    # Set the instance name IDs in the name table
    familyName = varfont['name'].getName(1, platformID=3, platEncID=1, langID=0x409) # 1 Font Family name
    familyName = unicode(familyName) # ensure it's correctly encoded
    styleName = unicode(instanceName) # ensure it's correctly encoded
    fullFontName = " ".join([familyName, styleName])
    postscriptName = fullFontName.replace(" ", "-")
    varfont['name'].setName(styleName, nameID=2, platformID=3, platEncID=1, langID=0x409) # 2 Font Subfamily name
    varfont['name'].setName(fullFontName, nameID=4, platformID=3, platEncID=1, langID=0x409) # 4 Full font name
    varfont['name'].setName(postscriptName, nameID=6, platformID=3, platEncID=1, langID=0x409) # 6 Postscript name for the font
    # Other important name IDs
    # 3 Unique font identifier (e.g. Version 0.000;NONE;Promise Bold Regular)
    # 25 Variations PostScript Name Prefix

    fvar = varfont['fvar']
    axes = {a.axisTag: (a.minValue, a.defaultValue, a.maxValue) for a in fvar.axes}
    # TODO Round to F2Dot14?
    normalizedLoc = normalizeLocation(normalizedLoc, axes)
    # Location is normalized now
    print("Normalized location:", varFileName, normalizedLoc)

    gvar = varfont['gvar']
    for glyphname, variations in gvar.variations.items():
        coordinates, _ = _GetCoordinates(varfont, glyphname)
        for var in variations:
            scalar = supportScalar(normalizedLoc, var.axes)
            if not scalar: continue
            # TODO Do IUP / handle None items
            varcoords = []
            for coord in var.coordinates:
                # TODO temp hack to avoid NoneType
                if coord is None:
                    varcoords.append((0, 0))
                else:
                    varcoords.append(coord)
            coordinates += GlyphCoordinates(varcoords) * scalar
            # coordinates += GlyphCoordinates(var.coordinates) * scalar
        _SetCoordinates(varfont, glyphname, coordinates)

    # print("Removing GX tables")
    for tag in ('fvar', 'avar', 'gvar'):
        if tag in varfont:
            del varfont[tag]

    print("Saving instance font", outFile)
    varfont.save(outFile)
    # Installing the font in Drawbot
    print outFile
    fontName = installFont(outFile)
    print fontName
    return fontName
