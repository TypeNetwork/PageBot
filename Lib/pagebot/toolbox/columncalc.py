#!/usr/bin/env python3
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
#     columncalc.py
#
#     Column --> measure transformers.

def x2cx(x, e):
    """Transform from *x* value to column *x* index value, using the
    *e.css('cw')* (column width) as column measure."""
    # Gutter
    gw = e.gw
    cw = e.css('cw', 0)
    # Check on division by 0
    if cw + gw:
        return (x - e.parent.pl) / (cw + gw)
    return 0

def cx2x(cx, e):
    """Transform from *x* index value to *x* index value, using the
    *e.css('cw')* (column width) as column measure."""
    if cx is None:
        x = 0
    else:
        x = e.parent.pl + cx * (e.css('cw', 0) + e.gw)
    return x

def y2cy(y, e):
    """Transform from *y* value to column *y* index value, using the
    *e.css('ch')* (column height) as column measure."""
    # Gutter
    gh = e.gh
    ch = e.css('ch', 0)
    cy = 0
    # Check on division by 0
    if ch + gh:
        paddingY = e.pb
        cy = (y - paddingY) / (ch + gh)
    return cy

def cy2y(cy, e):
    """Transform from *y* index value to *y* index value, using the
    *e.css('ch')* (column height) as column measure."""
    if cy is None:
        y = 0
    else:
        paddingY = e.pb
        y = paddingY + cy * (e.css('ch', 0) + e.gh)
    return y

def z2cz(z, e):
    """Transform from *z* value to column *z* index value, using the
    *e.css('cd')* (column depth) as column measure."""
    # Column width
    cd = e.css('cd', 0)
    cz = 0
    # Check on division by 0
    if cd + e.gd:
        cz = (z - e.parent.pzf) / (cd + e.gd)
    return cz

def cz2z(cz, e):
    """Transform from *z* index value to *z* index value, using the
    *e.css('cd')* (column depth) as column measure."""
    if cz is None:
        z = 0
    else:
        z = e.parent.pzf + cz * (e.css('cd', 0) + e.gd)
    return z

# Number of cols, rows, lanes
# TODO Make this work
"""
def w2cols(w, e): # Answer the rounded amount of columns that fit in the given width.
    gw = e.gw
    cw = e.css('cw', 0)
    if cw + gw:
        return int((e.w - e.pl - e.pr + gw) / (cw + gw))

def cols2w(w, e): # Answer the col width for the give amount of colums
    gw = e.gw
    cw = e.css('cw', 0)
    if cw + gw:
        return int((e.w - e.pl - e.pr + gw) / (cw + gw))

def w2rows(w, e): # Answer the rounded amount of rows that fit in the given width.
    gh = e.gh
    ch = e.css('ch', 0)
    if ch + gh:
        return int((e.h - e.pt - e.pb + gh) / (ch + gh))

def rows2w(w, e): # Answer the row width for the give amount of colums
    gh = e.gh
    ch = e.css('ch', 0)
    if ch + gh:
        return int((e.h - e.pt - e.pr + e.gw) / (cw + gw))

def w2cols(w, e): # Answer the rounded amount of columns that fit in the given width.
    gw = e.gw
    cw = e.css('cw', 0)
    if cw + gw:
        return int((e.w - e.pl - e.pr + e.gw) / (cw + gw))

def cols2w(w, e): # Answer the col with for the give amount of colums
    gw = e.gw
    cw = e.css('cw', 0)
    if cw + gw:
        return int((e.w - e.pl - e.pr + e.gw) / (cw + gw))
"""

# Size

def w2cw(w, e):
    """Transform from *w* value to column *w* count value, using the
    *e.css('cw')* (column width) as column measure."""
    gw = e.gw
    cw = e.css('cw', 0)
    # Test for division by 0
    if cw + gw:
        return (w + gw) / (cw + gw)
    # Undefined, not info about column width and gutter or zero division
    return 0

def cw2w(cw, e):
    """Transform from *w* index value to *w* count value, using the
    *e.css('cd')* (column width) as column measure."""
    if cw is None:
        w = 0
    else:
        gw = e.gw
        # Overwrite style from here.
        w = cw * (e.css('cw', 0) + gw) - gw
    return w

def h2ch(h, e):
    """Transform from *h* value to column *w* count value, using the
    *e.css('ch')* (column height) as column measure."""
    gh = e.gh
    ch = e.css('ch', 0)
    # Test for division by 0
    if ch + gh:
        return (h + gh) / (ch + gh)
    # Undefined, no info about column height and gutter or zero division
    return 0

def ch2h(ch, e):
    """Transform from *h* index value to *w* count value, using the
    *e.css('ch')* (column height) as column measure."""
    if ch is None:
        h = 0
    else:
        gh = e.gh
        # Overwrite style from here.
        h = ch * (e.css('ch', 0) + gh) - gh
    return h

def d2cd(d, e):
    """Transform from *d* value to column *cd* count value, using the
    *e.css('cd')* (column depth) as column measure."""
    cd = e.css('cd', 0)
    # Test for division by 0
    if cd + e.gd:
        return (d + e.gd) / (cd + e.gd)
    # Undefined, no info about column depth and gutter or zero division.
    return 0

def cd2d(cd, e):
    """Transform from *cd* index value to *d* count value, using the
    *e.css('ch')* (column depth) as column measure."""
    if cd is None:
        d = 0
    else:
        # Overwrite style from here.
        d = cd * (e.css('cd', 0) + e.gd) - e.gd
    return d

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
