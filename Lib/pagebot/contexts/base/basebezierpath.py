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
#     basebezierpath.py
#

class BaseBezierPath:
    """A Bézier path object, if you want to draw the same over and over
    again."""

    #contourClass = BezierContour

    def __init__(self, path=None, glyphSet=None):
        pass

    def __repr__(self):
        return "<BezierPath>"

    # pen support

    def moveTo(self, point):
        """
        Move to a point `x`, `y`.
        """

    def lineTo(self, point):
        """
        Line to a point `x`, `y`.
        """

    def curveTo(self, *points):
        """
        Draw a cubic bezier with an arbitrary number of control points.

        The last point specified is on-curve, all others are off-curve
        (control) points.
        """

    def qCurveTo(self, *points):
        """
        Draw a whole string of quadratic curve segments.

        The last point specified is on-curve, all others are off-curve
        (control) points.
        """

    def closePath(self):
        """
        Close the path.
        """

    def beginPath(self, identifier=None):
        """
        Begin using the path as a so called point pen and start a new subpath.
        """

    def addPoint(self, point, segmentType=None, smooth=False, name=None,
            identifier=None, **kwargs):
        """
        Use the path as a point pen and add a point to the current subpath. `beginPath` must
        have been called prior to adding points with `addPoint` calls.
        """

    def endPath(self):
        """End the current subpath. Calling this method has two distinct
        meanings depending on the context:

        When the bezier path is used as a segment pen (using `moveTo`,
        `lineTo`, etc.), the current subpath will be finished as an open
        contour.

        When the bezier path is used as a point pen (using `beginPath`,
        `addPoint` and `endPath`), the path will process all the points added
        with `addPoint`, finishing the current subpath."""

    def addComponent(self, glyphName, transformation):
        """
        Add a sub glyph. The 'transformation' argument must be a 6-tuple
        containing an affine transformation, or a Transform object from the
        fontTools.misc.transform module. More precisely: it should be a
        sequence containing 6 numbers.

        A `glyphSet` is required during initialization of the BezierPath object.
        """

    def drawToPen(self, pen):
        """
        Draw the bezier path into a pen
        """

    def drawToPointPen(self, pointPen):
        """
        Draw the bezier path into a point pen.
        """

    def arc(self, center, radius, startAngle, endAngle, clockwise):
        """Arc with `center` and a given `radius`, from `startAngle` to
        `endAngle`, going clockwise if `clockwise` is True and counter
        clockwise if `clockwise` is False."""

    def arcTo(self, point1, point2, radius):
        """Arc  defined by a circle inscribed inside the angle specified by
        three points: the current point, `point1`, and `point2`. The arc is
        drawn between the two points of the circle that are tangent to the two
        legs of the angle."""

    def rect(self, x, y, w, h):
        """Add a rectangle at possition `x`, `y` with a size of `w`, `h`."""

    def oval(self, x, y, w, h):
        """Add a oval at possition `x`, `y` with a size of `w`, `h`"""

    def line(self, point1, point2):
        """Add a line between two given points."""

    def polygon(self, *points, **kwargs):
        """Draws a polygon with n-amount of points.
        Optionally a `close` argument can be provided to open or close the path.
        As default a `polygon` is a closed path.
        """

    def text(self, txt, offset=None, font=None, fontSize=10, align=None):
        """Draws a `txt` with a `font` and `fontSize` at an `offset` in the
        bezier path.  If a font path is given the font will be installed and
        used directly.

        - Optionally an alignment can be set. Possible `align` values are:
        `"left"`, `"center"` and `"right"`.
        - The default alignment is `left`.
        - Optionally `txt` can be a `FormattedString`.
        """

    def textBox(self, txt, box, font=None, fontSize=10, align=None,
            hyphenation=None):
        """
        Draws a `txt` with a `font` and `fontSize` in a `box` in the bezier path.
        If a font path is given the font will be installed and used directly.

        Optionally an alignment can be set.
        Possible `align` values are: `"left"`, `"center"` and `"right"`.

        The default alignment is `left`.

        Optionally `hyphenation` can be provided.

        Optionally `txt` can be a `FormattedString`.
        Optionally `box` can be a `BezierPath`.
        """

    def traceImage(self, path, threshold=.2, blur=None, invert=False, turd=2, tolerance=0.2, offset=None):
        """
        Convert a given image to a vector outline.

        Optionally some tracing options can be provide:

        * `threshold`: the threshold used to bitmap an image
        * `blur`: the image can be blurred
        * `invert`: invert to the image
        * `turd`: the size of small turd that can be ignored
        * `tolerance`: the precision tolerance of the vector outline
        * `offset`: add the traced vector outline with an offset to the BezierPath
        """

    def getBezierPath(self):
        """
        Return the BezierPath.
        """

    def setBezierPath(self, path):
        """
        Set a nsBezierPath.
        """

    def pointInside(self, xy):
        """Check if a point `x`, `y` is inside a path."""

    def bounds(self):
        """Return the bounding box of the path."""

    def controlPointBounds(self):
        """Return the bounding box of the path including the offcurve
        points."""

    def optimizePath(self):
        pass

    def copy(self):
        """Copy the bezier path."""

    def reverse(self):
        """Reverse the path direction."""

    def appendPath(self, otherPath):
        """Append a path."""

    def __add__(self, otherPath):
        new = self.copy()
        new.appendPath(otherPath)
        return new

    def __iadd__(self, other):
        self.appendPath(other)
        return self

    # transformations
    # NOTE: currently handled within context.

    def translate(self, x=0, y=0):
        """
        Translate the path with a given offset.
        """
        self.transform((1, 0, 0, 1, x, y))

    def rotate(self, angle, center=(0, 0)):
        """Rotate the path around the `center` point (which is the origin by
        default) with a given angle in degrees."""
        angle = math.radians(angle)
        c = math.cos(angle)
        s = math.sin(angle)
        self.transform((c, s, -s, c, 0, 0), center)

    def scale(self, x=1, y=None, center=(0, 0)):
        """Scale the path with a given `x` (horizontal scale) and `y` (vertical
        scale).

        If only 1 argument is provided a proportional scale is applied.

        The center of scaling can optionally be set via the `center` keyword
        argument. By default this is the origin."""
        if y is None:
            y = x
        self.transform((x, 0, 0, y, 0, 0), center)

    def skew(self, angle1, angle2=0, center=(0, 0)):
        """Skew the path with given `angle1` and `angle2`. If only one argument
        is provided a proportional skew is applied. The center of skewing can
        optionally be set via the `center` keyword argument. By default this is
        the origin."""
        angle1 = math.radians(angle1)
        angle2 = math.radians(angle2)
        self.transform((1, math.tan(angle2), math.tan(angle1), 1, 0, 0), center)

    def transform(self, transformMatrix, center=(0, 0)):
        """Transform a path with a transform matrix (xy, xx, yy, yx, x, y)."""

    # boolean operations

    def _contoursForBooleanOperations(self):
        # contours are very temporaly objects
        # redirect drawToPointPen to drawPoints
        contours = self.contours
        for contour in contours:
            contour.drawPoints = contour.drawToPointPen
            if contour.open:
                raise DrawBotError("open contours are not supported during boolean operations")
        return contours

    def union(self, other):
        """
        Return the union between two bezier paths.
        """
        assert isinstance(other, self.__class__)
        import booleanOperations
        contours = self._contoursForBooleanOperations() + other._contoursForBooleanOperations()
        result = self.__class__()
        booleanOperations.union(contours, result)
        return result

    def removeOverlap(self):
        """
        Remove all overlaps in a bezier path.
        """
        import booleanOperations
        contours = self._contoursForBooleanOperations()
        result = self.__class__()
        booleanOperations.union(contours, result)
        self.setBezierPath(result.getBezierPath())
        return self

    def difference(self, other):
        """
        Return the difference between two bezier paths.
        """
        assert isinstance(other, self.__class__)
        import booleanOperations
        subjectContours = self._contoursForBooleanOperations()
        clipContours = other._contoursForBooleanOperations()
        result = self.__class__()
        booleanOperations.difference(subjectContours, clipContours, result)
        return result

    def intersection(self, other):
        """
        Return the intersection between two bezier paths.
        """
        assert isinstance(other, self.__class__)
        import booleanOperations
        subjectContours = self._contoursForBooleanOperations()
        clipContours = other._contoursForBooleanOperations()
        result = self.__class__()
        booleanOperations.intersection(subjectContours, clipContours, result)
        return result

    def xor(self, other):
        """
        Return the xor between two bezier paths.
        """
        assert isinstance(other, self.__class__)
        import booleanOperations
        subjectContours = self._contoursForBooleanOperations()
        clipContours = other._contoursForBooleanOperations()
        result = self.__class__()
        booleanOperations.xor(subjectContours, clipContours, result)
        return result

    def intersectionPoints(self, other=None):
        """
        Return a list of intersection points as `x`, `y` tuples.

        Optionaly provide an other path object to find intersection points.
        """
        import booleanOperations
        contours = self._contoursForBooleanOperations()
        if other is not None:
            assert isinstance(other, self.__class__)
            contours += other._contoursForBooleanOperations()
        return booleanOperations.getIntersections(contours)

    def expandStroke(self, width, lineCap="round", lineJoin="round", miterLimit=10):
        """
        Returns a new bezier path with an expanded stroke around the original path,
        with a given `width`. Note: the new path will not contain the original path.

        The following optional arguments are available with respect to line caps and joins:
        * `lineCap`: Possible values are `"butt"`, `"square"` or `"round"`
        * `lineJoin`: Possible values are `"bevel"`, `"miter"` or `"round"`
        * `miterLimit`: The miter limit to use for `"miter"` lineJoin option
        """
        if lineJoin not in _LINEJOINSTYLESMAP:
            raise DrawBotError("lineJoin must be 'bevel', 'miter' or 'round'")
        if lineCap not in _LINECAPSTYLESMAP:
            raise DrawBotError("lineCap must be 'butt', 'square' or 'round'")

        strokedCGPath = Quartz.CGPathCreateCopyByStrokingPath(self._getCGPath(), None, width, _LINECAPSTYLESMAP[lineCap], _LINEJOINSTYLESMAP[lineJoin], miterLimit)
        result = self.__class__()
        result._setCGPath(strokedCGPath)
        return result

    def __mod__(self, other):
        return self.difference(other)

    __rmod__ = __mod__

    def __imod__(self, other):
        result = self.difference(other)
        self.setBezierPath(result.getBezierPath())
        return self

    def __or__(self, other):
        return self.union(other)

    __ror__ = __or__

    def __ior__(self, other):
        result = self.union(other)
        self.setBezierPath(result.getBezierPath())
        return self

    def __and__(self, other):
        return self.intersection(other)

    __rand__ = __and__

    def __iand__(self, other):
        result = self.intersection(other)
        self.setBezierPath(result.getBezierPath())
        return self

    def __xor__(self, other):
        return self.xor(other)

    __rxor__ = __xor__

    def __ixor__(self, other):
        result = self.xor(other)
        #self.setBezierPath(result.getBezierPath())
        return self

    def _points(self, onCurve=True, offCurve=True):
        points = []
        if not onCurve and not offCurve:
            return points
        for index in range(self._path.elementCount()):
            instruction, pts = self._path.elementAtIndex_associatedPoints_(index)
            if not onCurve:
                pts = pts[:-1]
            elif not offCurve:
                pts = pts[-1:]
            points.extend([(p.x, p.y) for p in pts])
        return points

    def _get_points(self):
        return self._points()

    points = property(_get_points, doc="Return a list of all points.")

    def _get_onCurvePoints(self):
        return self._points(offCurve=False)

    onCurvePoints = property(_get_onCurvePoints, doc="Return a list of all on curve points.")

    def _get_offCurvePoints(self):
        return self._points(onCurve=False)

    offCurvePoints = property(_get_offCurvePoints, doc="Return a list of all off curve points.")

    def _get_contours(self):
        pass

    contours = property(_get_contours, doc="Return a list of contours with all point coordinates sorted in segments. A contour object has an `open` attribute.")

    def __len__(self):
        return len(self.contours)

    def __getitem__(self, index):
        return self.contours[index]

    def __iter__(self):
        contours = self.contours
        count = len(contours)
        index = 0
        while index < count:
            contour = contours[index]
            yield contour
            index += 1
