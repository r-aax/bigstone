# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:05:56 2020

@author: Rybakov
"""

import kivy

#---------------------------------------------------------------------------------------------------
# Area.
#---------------------------------------------------------------------------------------------------

class Area:
    """
    Area for drawing.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, x_interval, y_interval):
        """
        Constructor.

        Arguments:
            x_interval -- X interval (tupple of two values),
            y_interval -- Y interval (tupple of two values).
        """

        self.XInterval = x_interval
        self.YInterval = y_interval

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Result:
            String.
        """

        return '[%d - %d] X [%d - %d]' % (self.XInterval + self.YInterval)

#---------------------------------------------------------------------------------------------------

    def Width(self):
        """
        Get width.

        Result:
            Width.
        """

        (xl, xh) = self.XInterval

        return abs(xl - xh)

#---------------------------------------------------------------------------------------------------

    def Height(self):
        """
        Get height.

        Result:
            Height.
        """

        (yl, yh) = self.YInterval

        return abs(yl - yh)

#---------------------------------------------------------------------------------------------------

    def LoLoCorner(self):
        """
        Get lo-lo corner.

        Result:
            Corner of low coordinates.
        """

        return (self.XInterval[0], self.YInterval[0])

#---------------------------------------------------------------------------------------------------

    def HiHiCorner(self):
        """
        Get hi-hi corner.

        Result:
            Corner of high coordinates.
        """

        return (self.XInterval[1], self.YInterval[1])

#---------------------------------------------------------------------------------------------------
# Drawer class.
#---------------------------------------------------------------------------------------------------

class Drawer:
    """
    Draw master.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, phys_area, widget, paint_area):
        """
        Constructor.

        Arguments:
            phys_area -- Physical area,
            widget -- Widget,
            paint_area -- Area for paintring.
        """

        # Main data - areas, widget, canvas.
        self.PhysArea = phys_area
        self.Widget = widget
        self.Canvas = self.Widget.canvas
        self.PaintArea = paint_area

        # Colors.
        self.BackgroundColor = (0.9, 0.9, 0.9, 1.0)

#---------------------------------------------------------------------------------------------------

    def SetColor(self, components):
        """
        Set color.

        Arguments:
            components -- Color components.
        """

        (r, g, b, a) = components

        with self.Canvas:
            kivy.graphics.Color(r, g, b, a)

#---------------------------------------------------------------------------------------------------

    def Clean(self):
        """
        Clean paint area.
        """

        # First clean all in black.
        self.SetColor((0.0, 0.0, 0.0, 1.0))
        with self.Canvas:
            kivy.graphics.Rectangle(pos = (0, 50),
                                    size = (self.Widget.width, self.Widget.height - 50))

        # Set painting area inside clean function.
        self.PaintArea = Area((20, self.Widget.width - 20),
                              (50, self.Widget.height - 30))

        self.SetColor(self.BackgroundColor)

        with self.Canvas:
            kivy.graphics.Rectangle(pos = self.PaintArea.LoLoCorner(),
                                    size = (self.PaintArea.Width(), self.PaintArea.Height()))

#---------------------------------------------------------------------------------------------------

    def CoordinateTransform(f, fi, ti):
        """
        Transform coordinate.

        Arguments:
            f -- From coordinate,
            fi - From interval,
            ti - To interval.

        Result:
            Transformed coordinate.
        """

        (fl, fh) = fi
        (tl, th) = ti
        fw = fh - fl
        tw = th - tl

        return ((f - fl) / fw) * tw + tl

#---------------------------------------------------------------------------------------------------

    def To(self, p):
        """
        To transform of point.

        Arguments:
            p -- Point.

        Result:
            Point after To transform.
        """

        (x, y) = p
        t = (Drawer.CoordinateTransform(x, self.PhysArea.XInterval, self.PaintArea.XInterval),
             Drawer.CoordinateTransform(y, self.PhysArea.YInterval, self.PaintArea.YInterval))

        return t

#---------------------------------------------------------------------------------------------------

    def From(self, p):
        """
        From transform of point.

        Arguments:
            p -- Point.

        Result:
            Point after From transform.
        """

        (x, y) = p
        t = (Drawer.CoordinateTransform(x, self.PaintArea.XInterval, self.PhysArea.XInterval),
             Drawer.CoordinateTransform(y, self.PaintArea.YInterval, self.PhysArea.YInterval))

        return t

#---------------------------------------------------------------------------------------------------

    def Line(self, c):
        """
        Draw line.

        Arguments:
            c -- Coordinates of two points.
        """

        (x1, y1, x2, y2) = c
        p1 = (x1, y1)
        p2 = (x2, y2)
        t1 = self.To(p1)
        t2 = self.To(p2)

        with self.Canvas:
            kivy.graphics.Line(points = t1 + t2)

#---------------------------------------------------------------------------------------------------
