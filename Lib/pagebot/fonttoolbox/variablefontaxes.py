#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#       from https://github.com/fonttools/fonttools/blob/master/Lib/fontTools/varLib/mutator.py
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     variablefontaxes.py
#
from sys import maxsize

# Types of axes
PRIMARY_AXIS = 'Primary'
TREATMENT_AXIS = 'Treatment'
CJK_AXIS = 'Non-latin' # ??? CJK
MOTION_AXIS = 'Motion'
GLYPH_AXIS = 'Glyph'
UNDEFINED_AXIS = 'Undefined'
CUSTOM_AXIS = 'Custom'

axisDefinitions = {
    # https://www.typenetwork.com/brochure/opentype-variable-fonts-moving-right-along/
    # Registered axes
    'wght': dict(name='Weight', tag='wght', description='Used to vary stroke thicknesses to give variation from lighter to blacker.',
        minValue=0, maxValue=1000, defaultValue=500,
        scale=u"Values must be in the range 1 to 1000. Values can be interpreted in direct comparison to values for usWeightClass (in the 'OS/2' table), or the CSS font-weight property — see the note below.",
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['wdth'],
        type=PRIMARY_AXIS,
        images=[]),
    'wdth': dict(name='Width', tag='wdth', description='Used to vary width of text from narrower to wider.',
        minValue=0, maxValue=1000, defaultValue=100,
        scale='Values can be interpreted as a percentage of whatever the font designer considers “normal” for that font design. Values must be strictly greater than zero.',
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['wght'],
        type=PRIMARY_AXIS,
        images=[]),
    'slnt': dict(name='Slant', tag='slnt', description='Used to vary between upright and slanted text.',
        minValue=0, maxValue=1000, defaultValue=0,
        scale=u'Values can be interpreted as the angle, in counter-clockwise degrees, of oblique slant from whatever the designer considers to be upright for that font design. Values must be greater than -90 and less than +90.',
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['ital'],
        type=PRIMARY_AXIS,
        images=[]),
    'opsz': dict(name='Optical size', tag='opsz', description='Used to vary design to suit different text sizes.',
        minValue=8, maxValue=72, defaultValue=12,
        scale='Values can be interpreted as text size, in points. (Text size can be as determined in an application and is not necessarily physical size on a display surface.) Values must be strictly greater than zero.',
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=[]),
    'ital': dict(name='Italic', tag='ital', description='Used to vary between non-italic and italic.',
        minValue=0, maxValue=1, defaultValue=0,
        scale='Values must be in the range 0 to 1. A value of 0 can be interpreted as “Roman” (non-italic); a value of 1 can be interpreted as (fully) italic.',
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['slnt'],
        type=PRIMARY_AXIS,
        images=[]),

    # PageBot defined axes.
    'YOPQ': dict(name='????', tag='YOPQ', description='Description of YOPQ here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'YTSE': dict(name='????', tag='YTSE', description='Description of YTSE here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'YTLC': dict(name='????', tag='YTLC', description='Description of YTLC here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'XTRA': dict(name='????', tag='XTRA', description='Description of XTRA here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'XOPQ': dict(name='????', tag='XOPQ', description='Description of XOPQ here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'GRAD': dict(name='????', tag='GRAD', description='Description of GRAD here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),

    # Decovar (temp names?)
    'wmx2': dict(name='????', tag='wmx2', description='Description of wmx2 here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=[],
        type=CUSTOM_AXIS,
        images=[]),
    'bldB': dict(name='????', tag='bldB', description='Description of bldB here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['bldA'],
        type=CUSTOM_AXIS,
        images=[]),
    'bldA': dict(name='????', tag='bldA', description='Description of bldA here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['bldB'],
        type=CUSTOM_AXIS,
        images=[]),
    'sklA': dict(name='Skeleton A', tag='sklA', description='Description of sklA here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['sklB', 'sklD'],
        type=CUSTOM_AXIS,
        images=[]),
    'sklB': dict(name='Skeleton B', tag='sklB', description='Description of sklB here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['sklA', 'sklD'],
        type=CUSTOM_AXIS,
        images=[]),
    'sklD': dict(name='Skeleton D', tag='sklD', description='Description of sklD here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['sklB', 'sklB'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmA': dict(name='Terminal A', tag='trmA', description='Description of trmA here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmB': dict(name='Terminal B', tag='trmB', description='Description of trmB here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmC': dict(name='Terminal C', tag='trmC', description='Description of trmC here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmD': dict(name='Terminal D', tag='trmD', description='Description of trmD here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmE': dict(name='Terminal E', tag='trmE', description='Description of trmE here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmF': dict(name='Terminal F', tag='trmF', description='Description of trmF here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmG': dict(name='Terminal G', tag='trmG', description='Description of trmG here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmK': dict(name='Terminal K', tag='trmK', description='Description of trmK here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),
    'trmL': dict(name='Terminal L', tag='trmL', description='Description of trmL here',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='',
        userInteractions='',
        relatedAxesDescription='',
        relatedAxes=['trmA', 'trmB', 'trmC', 'trmD', 'trmE', 'trmF', 'trmG', 'trmK'],
        type=CUSTOM_AXIS,
        images=[]),

    # Poposed registered axes
    'xtra': dict(name='X transparent', tag='xtra', description='Assigns a “white” per mille value to each instance of the design space',
        minValue=-1000, maxValue=2000, scale='per-mille-of-em', defaultValue=400,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-xtra.gif']
    ),
    'xopq': dict(name='X opaque', tag='xopq', description='Assigns a “black” per mille value to each instance of the design space',
        minValue=-1000, maxValue=2000, scale='per-mille-of-em', defaultValue=400,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-xopq.gif']
    ),
    'ytra': dict(name='Y transparent', tag='ytra', description='Assigns an overall “white” per mille value to each instance',
        minValue=0, maxValue=2000, scale='per-mille-of-em', defaultValue=884,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-ytra.gif']
    ),
    'yopq': dict(name='Y transparent', tag='yopq', description='Assigns a “black” per mille value to each instance of the design space',
        minValue=-1000, maxValue=2000, scale='per-mille-of-em', defaultValue=884,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-yopq.gif']
    ),
    'ytlc': dict(name='Y transparent lowercase', tag='ytlc', description='Assigns a “white” per mille value to each instance of the design space',
        minValue=-1000, maxValue=2000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-ytlc.gif']
    ),
    'ytuc': dict(name='Y transparent uppercase', tag='ytuc', description='Assigns a “white” per mille value to each instance of the design space',
        minValue=-1000, maxValue=2000, scale='per-mille-of-em', defaultValue=725,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-ytuc.gif']
    ),
    'ytde': dict(name='Y transparent descender', tag='ytde', description='Assigns a “white” per mille value to each instance of the design space',
        minValue=-1000, maxValue=0, scale='per-mille-of-em', defaultValue=-250,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-ytde.gif']
    ),
    'ytas': dict(name='Y transparent descender', tag='ytas', description='Assigns a “white” per mille value to each instance of the design space',
        minValue=0, maxValue=1000, scale='per-mille-of-em', defaultValue=750,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-ytas.gif']
    ),
    'xtab': dict(name='Tabular width', tag='xtab', description='Axis contains a per mille value to each monospace or tabular instance',
        minValue=1, maxValue=4000, scale='per-mille-of-em', defaultValue=500,
        programInteractions='Applications may choose to select a variant in connection to an input, or it might be programmatically used',
        userInteractions='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-xtab.gif']
    ),
    'vrot': dict(name='Tabular width', tag='vrot', description='Assigns a value to each instance of the axis',
        minValue=-360.00, maxValue=360, scale='Values can be interpreted as degrees of rotation from the default, which is zero', defaultValue=500,
        programInteractions='Applications may choose to select a variant in connection to an input for ccw or cw vrot, or it might be programmatically used.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=PRIMARY_AXIS,
        images=['animation-vrot.gif']
    ),
    'udln': dict(name='Underline', tag='udln', description='Assigns a value to each instance of the axis',
        minValue=-360.00, maxValue=360, scale='Sample value for a Sans regular Latin would be 120.', defaultValue=120,
        programInteractions='Applications may use the underline axis, or it may inform instance-making software of underline value and location.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-udln.gif']
    ),
    'shdw': dict(name='Shadow depth', tag='shdw', description='Assigns a value to each instance of the axis',
        minValue=1, maxValue=1000, scale='Values can be interpreted as per-mille-of-em.', defaultValue=30,
        programInteractions='Applications allow the user to select the drop shadow treatment for text, raising need for a value for every instance in a design space that affects a shadow.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-shdw.gif', 'animation-shdw-2.png', 'animation-shdw-38.png'],
    ),
    'refl': dict(name='Y reflection', tag='shdw', description='Assigns a value to each instance of the axis',
        minValue=1, maxValue=1000, scale='Values can be interpreted as per-mille-of-em.', defaultValue=-350,
        programInteractions='Applications may allow the user to select the reflection of text.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-refl.gif', 'animation-refl.jpg'],
    ),
    'otln': dict(name='Outline value', tag='otln', description='Values for the weight of an outlined font.',
        minValue=1, maxValue=1000, scale='Values can be interpreted as per-mille-of-em.', defaultValue=-350,
        programInteractions='Applications may allow the user to select the embossing of text and a depth if the axis exists.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-otln.gif', 'animation-otln-2.png', 'animation-otln-25.png'],
    ),
    'engr': dict(name='Engraving value', tag='engr', description='Values for the width of the engrave.',
        minValue=1, maxValue=1000, scale='Sample value for a Sans regular Latin engraving would be 33.', defaultValue=33,
        programInteractions='Applications may allow the user to select the embossing of text, and a depth if the axis exists.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-engr.gif', 'image-engr.jpeg'],
    ),
    'embo': dict(name='Emboss depth', tag='engr', description='Values for embossment depth.',
        minValue=1, maxValue=1000, scale='Sample value for Sans 60 point emboss would be 24.', defaultValue=24,
        programInteractions='Applications may allow the user to select the embossing of text, and a depth if the axis exists.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=TREATMENT_AXIS,
        images=['animation-embo.gif', 'image-embo.jpeg'],
    ),
    'ytch': dict(name='Y transparent Chinese', tag='ytch', description='Values represent the height of Chinese glyphs.', # CJK?
        minValue=1, maxValue=2400, scale='Sample value for Sans 60 point emboss would be 24.', defaultValue=24,
        programInteractions='Values can be interpreted as per-mille-of-em changes, between any instances in the axis.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=CJK_AXIS,
        images=['animation-ytch.gif'],
    ),
    'xtch': dict(name='X transparent Chinese', tag='ytch', description='Values represent the width of Chinese glyphs.', # CJK?
        minValue=1, maxValue=2400, scale='Sample value 950.', defaultValue=950,
        programInteractions='Values can be interpreted as per-mille-of-em changes, between any instances in the axis.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=CJK_AXIS,
        images=['animation-xtch.gif'],
    ),
    'rxad': dict(name='Relative x advance', tag='rxad', description='Assigns a distance value per mille to the motion of a glyph',
        minValue=-1000, maxValue=1000, scale='Normal value 0', defaultValue=0,
        programInteractions='Applications may enable plotting the number of loops of an animation required for the time and distance defined by the user.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=MOTION_AXIS,
        images=['animation-rxad.gif'],
    ),
    'ryad': dict(name='Relative y advance', tag='ryad', description='Assigns a distance value per mille to the motion of a glyph',
        minValue=-1000, maxValue=1000, scale='Normal value 0', defaultValue=0,
        programInteractions='Applications may enable plotting the number of loops of an animation required for the time and distance defined by the user',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=MOTION_AXIS,
        images=['animation-ryad.gif'],
    ),
    'rsec': dict(name='Relative second', tag='rsec', description='Value can be interpreted as a recommendation for one second of animation time',
        minValue=-1000, maxValue=1000, scale='Normal value 1', defaultValue=1,
        programInteractions='Applications may plot the relative time of a glyph, or a glyph to other glyphs, and play them in relative or absolute time',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection. ',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=MOTION_AXIS,
        images=['animation-rsec.gif'],
    ),
    'vuid': dict(name='Unicode variation axis', tag='vuid', description='Value can be interpreted as a recommendation for one second of animation time',
        minValue=-1000, maxValue=maxsize, scale='Any Unicode value can be used', defaultValue=1,
        programInteractions='Applications may choose to present a variation in connection to an input Unicode id',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection.',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=GLYPH_AXIS,
        images=['animation-vuid.gif'],
    ),
    'votf': dict(name='Feature variation axis', tag='votf', description=u'Instances represent changes to a glyph’s feature',
        minValue=-0, maxValue=1000, scale='Any common feature', defaultValue=0,
        programInteractions='Applications may choose to select a variation in connection to an input feature tag id.',
        userInteractions='Users may choose to program a variant for direct input, or via a user interface connection.',
        relatedAxesDescription='Users may choose to program a variant in connection to direct or conjunctive input for a page description language, or via a user interface',
        relatedAxes=[],
        type=GLYPH_AXIS,
        images=['animation-votf.gif'],
    ),
}
