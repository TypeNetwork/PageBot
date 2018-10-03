#!/usr/bin/env python
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#

print('\nChecking installation paths... \n')

import sys, os, shutil
print('System: %s, %s' % (os.name, sys.platform))
print('Python version is:')
print(sys.version)
print('Which Python?')
print(sys.executable)
from pagebot import getResourcesPath

CLEAN = True

try:
    import site
    print('Found site at %s' % site.__file__)
    packages = site.getsitepackages()
    for p in packages:
        print(' - %s' % p)
except:
    print('x Could not read site packages :S')

# TODO: add svgwrite, flat, markdown etc?
# TODO automate, eval()?
# TODO: make OS dependent.

libs = ['pagebot', 'fontTools', 'objc', 'AppKit', 'vanilla', 'drawBot', 'sass']
missing = []

for l in libs:
    try:
        __import__(l)
        print('%s installed at %s' % (l, __import__(l).__file__))
    except:
        print('x %s not installed' % l)
        missing.append(l)
        CLEAN = False

if not CLEAN:
    print('Not all dependencies are installed, please install missing ones:')
    print(', '.join(missing))
else:
    print('Found all dependencies, running some test...')
    # Testing PageBot.
    from pagebot import getContext
    context = getContext()
    print(context)
    print(context.b)
    import sass

    # Testing Sass.
    css = sass.compile(string='a { b { color: blue; } }')
    print(css)
    path = getResourcesPath() + '/templates/test.scss'
    import os.path
    print(os.path.exists(path))
    css = sass.compile(filename=path)
    print(css)

    #test_scss = open('test.scss', 'w')
    import os, os.path

    for f in ('css', 'sass'):
        if not os.path.exists(f):
            os.mkdir(f)
    shutil.copy(path, 'sass')
    sass.compile(dirname=('sass', 'css'), output_style='compressed')
    with open('css/test.css') as example_css:
        print(example_css)

    # Export with HtmlBuilder.
    from pagebot.contexts.builders.htmlbuilder import HtmlBuilder
    hb = HtmlBuilder()
    print(hb)
    hb.compileScss(path, cssPath = 'css/testHtmlBuilder.css')
