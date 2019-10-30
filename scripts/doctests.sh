#!/bin/bash
set -ev
export PWD="Lib/pagebot"
python3 $PWD/__init__.py
python3 $PWD/article.py
python3 $PWD/composer.py
python3 $PWD/conditions/__init__.py
python3 $PWD/conditions/align.py
python3 $PWD/conditions/columns.py
python3 $PWD/conditions/condition.py
python3 $PWD/conditions/floating.py
python3 $PWD/conditions/flow.py
python3 $PWD/conditions/score.py
python3 $PWD/conditions/text.py
python3 $PWD/constants.py
python3 $PWD/contexts/__init__.py
python3 $PWD/contexts/base/abstractcontext.py
python3 $PWD/contexts/base/babelstring.py
python3 $PWD/contexts/base/basebezierpath.py
python3 $PWD/contexts/base/basebuilder.py
python3 $PWD/contexts/base/basecontext.py
python3 $PWD/contexts/base/basecontour.py
python3 $PWD/contexts/base/baseimageobject.py
python3 $PWD/contexts/base/basepoint.py
python3 $PWD/contexts/flatcontext/flatbuilder.py
python3 $PWD/contexts/flatcontext/flatbezierpath.py
python3 $PWD/contexts/flatcontext/flatcontext.py
python3 $PWD/contexts/flatcontext/flatstring.py
python3 $PWD/contexts/markup/htmlbuilder.py
python3 $PWD/contexts/markup/svgbuilder.py
python3 $PWD/contexts/markup/sitebuilder.py
python3 $PWD/contexts/markup/xmlbuilder.py
python3 $PWD/contexts/markup/htmlcontext.py
python3 $PWD/contexts/markup/htmlstring.py
python3 $PWD/contexts/markup/svgcontext.py
#TODO: add rest of contributions.
python3 $PWD/contributions/filibuster/blurb.py
python3 $PWD/contributions/filibuster/blurbwriter.py
python3 $PWD/document.py
python3 $PWD/elements/element.py
python3 $PWD/elements/paths/glyphpath.py
python3 $PWD/elements/pbcodeblock.py
python3 $PWD/elements/pbgalley.py
python3 $PWD/elements/pbgroup.py
python3 $PWD/elements/pbimage.py
python3 $PWD/elements/pbline.py
python3 $PWD/elements/pboval.py
python3 $PWD/elements/pbpage.py
python3 $PWD/elements/pbplacer.py
python3 $PWD/elements/pbpolygon.py
python3 $PWD/elements/pbquire.py
python3 $PWD/elements/pbrect.py
python3 $PWD/elements/pbruler.py
python3 $PWD/elements/pbtable.py
python3 $PWD/elements/pbtext.py
python3 $PWD/elements/pbtextbox.py
python3 $PWD/elements/variablefonts/variablecircle.py
python3 $PWD/elements/variablefonts/variablecube.py
python3 $PWD/elements/variablefonts/variablecube2.py
python3 $PWD/elements/variablefonts/variableglyphs.py
python3 $PWD/elements/variablefonts/variablescatter.py
python3 $PWD/elements/views/__init__.py
python3 $PWD/elements/views/baseview.py
python3 $PWD/elements/views/gitview.py
python3 $PWD/elements/views/googleappsview.py
python3 $PWD/elements/views/googlecloudview.py
python3 $PWD/elements/views/htmlview.py
python3 $PWD/elements/views/mampview.py
python3 $PWD/elements/views/pageview.py
python3 $PWD/elements/views/pagemapview.py
python3 $PWD/elements/views/siteview.py
python3 $PWD/errors.py
python3 $PWD/fonttoolbox/objects/family.py
python3 $PWD/fonttoolbox/objects/font.py
python3 $PWD/fonttoolbox/objects/fontinfo.py
python3 $PWD/fonttoolbox/objects/glyph.py
python3 $PWD/fonttoolbox/objects/prevarfamily.py
python3 $PWD/fonttoolbox/otlTools.py
python3 $PWD/fonttoolbox/ttftools.py
python3 $PWD/fonttoolbox/unicodes/unicoderanges.py
python3 $PWD/gradient.py
python3 $PWD/mathematics/__init__.py
python3 $PWD/mathematics/transform3d.py
python3 $PWD/mathematics/numpytransform.py
python3 $PWD/filepaths.py
python3 $PWD/publications/typespecimens/__init__.py
python3 $PWD/publications/typespecimens/basetypespecimen.py
python3 $PWD/publications/typespecimens/simplespecimen.py
python3 $PWD/publications/typespecimens/specimens.py
python3 $PWD/publications/typespecimens/typespecimen.py
python3 $PWD/publications/typespecimens/proofing/__init__.py
python3 $PWD/publications/typespecimens/proofing/pagewide.py
python3 $PWD/publications/typespecimens/proofing/proof.py
python3 $PWD/publications/typespecimens/proofing/tx.py
python3 $PWD/publications/websites/nanosite/nanosite.py
python3 $PWD/publications/newspapers/basenewspaper.py
# TODO: add rest of publications...
# ...
python3 $PWD/publications/calendars/basecalendar.py
python3 $PWD/readers/__init__.py
python3 $PWD/readers/mdreader.py
python3 $PWD/readers/rereader.py
python3 $PWD/readers/xmlreader.py
python3 $PWD/server/__init__.py
# Hangs on server process.
# python3 $PWD/server/baseserver.py
python3 $PWD/style.py
python3 $PWD/stylelib.py
python3 $PWD/templates/__init__.py
# ...
python3 $PWD/themes/__init__.py
python3 $PWD/themes/backtothecity.py
python3 $PWD/themes/basetheme.py
python3 $PWD/themes/businessasusual.py
python3 $PWD/themes/fairytales.py
python3 $PWD/themes/freshandshiny.py
python3 $PWD/themes/happyholidays.py
python3 $PWD/themes/intothewoods.py
python3 $PWD/themes/seasoningthedish.py
python3 $PWD/themes/somethingintheair.py
python3 $PWD/themes/wordlywise.py
python3 $PWD/toolbox/color.py
python3 $PWD/toolbox/columncalc.py
python3 $PWD/toolbox/dating.py
python3 $PWD/toolbox/hyphenation.py
python3 $PWD/toolbox/markers.py
python3 $PWD/toolbox/timemark.py
python3 $PWD/toolbox/units.py
python3 $PWD/typesetter.py
