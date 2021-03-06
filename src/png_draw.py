# -*- coding: utf-8 -*-
"""
Drawing examples.

Created on Tue May  7 09:58:45 2019

@author: Rybakov
"""

# Outer modules.
import aggdraw
from PIL import Image, ImageDraw, ImageFont

# Own modules.
import petri_net

#---------------------------------------------------------------------------------------------------
# Variables.
#---------------------------------------------------------------------------------------------------

BlackPen = aggdraw.Pen('black', 1.0)
BlackBrush = aggdraw.Brush('black')
WhiteBrush = aggdraw.Brush('white')

#---------------------------------------------------------------------------------------------------
# Class drawer.
#---------------------------------------------------------------------------------------------------

class Drawer:
    """
    Drawer based on aggdraw.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self,
                 draw_area = (0.0, 0.0, 100.0, 100.0),
                 pic_size = (1600, 1200),
                 margins = (10, 10),
                 invert = (False, True),
                 backcolor = (255, 255, 255)):
        """
        Constructor.

        Arguments:
            draw_size -- Drawing area size,
            margins -- Margins,
            pic_size -- Picture size.
        """

        # Create image and drawer.
        self.Img = Image.new('RGB', pic_size, color = backcolor)
        self.Backcolor = backcolor
        self.Canvas = aggdraw.Draw(self.Img)
        self.Canvas.setantialias(True)

        # Data for transform.
        self.DrawArea = draw_area
        (dxl, dyl, dxh, dyh) = draw_area
        (px, py) = pic_size
        (mx, my) = margins
        self.FXI = (dxl, dxh)
        self.FYI = (dyl, dyh)
        self.TXI = (mx, px - mx)
        self.TYI = (my, py - my)
        (inv_x, inv_y) = invert
        self.InvKX = -1.0 if inv_x else 1.0
        self.InvKY = -1.0 if inv_y else 1.0

#---------------------------------------------------------------------------------------------------

    def FSS(self,
            filename = 'test.png'):
        """
        Flush, Save, Show.

        Arguments:
            filename -- Name of file.
        """

        # Flush
        #self.Canvas.flush()
        if filename != None:
            self.Img.save(filename)
        self.Img.show()

#---------------------------------------------------------------------------------------------------

    def TransformCoord(self, x, f, t, inv_k):
        """
        Transform coordinate.

        Arguments:
            x -- Coordinate,
            f -- From interval,
            t -- To interval,
            inv_k -- Invert coefficient.

        Result:
            New coordinate.
        """

        (fl, fh) = f
        (tl, th) = t

        if inv_k > 0.0:
            a = (tl - th) / (fl - fh)
            b = tl - a * fl
        else:
            a = (th - tl) / (fl - fh)
            b = tl - a * fh

        return a * x + b

#---------------------------------------------------------------------------------------------------

    def To(self, p):
        """
        Transform point TO.

        Arguments:
            p -- Point from drawing area.

        Result:
            Point from picture area.
        """

        (px, py) = p

        return (self.TransformCoord(px, self.FXI, self.TXI, self.InvKX),
                self.TransformCoord(py, self.FYI, self.TYI, self.InvKY))

#---------------------------------------------------------------------------------------------------

    def From(self, p):
        """
        Transfrom point FROM.

        Arguments:
            p -- Point from picture area.

        Result:
            Point from drawing area.
        """

        (px, py) = p

        return (self.TransformCoord(px, self.TXI, self.FXI, self.InvKX),
                self.TransformCoord(py, self.TYI, self.FYI, self.InvKY))

#---------------------------------------------------------------------------------------------------

    def Line(self, p1, p2, pen = BlackPen):
        """
        Line.

        Arguments:
            p1 -- From point,
            p2 -- To point,
            pen -- Pen.
        """

        self.Canvas.line(self.To(p1) + self.To(p2), pen)

#---------------------------------------------------------------------------------------------------

    def Lines(self, ps, pen = BlackPen):
        """
        Lines.

        Arguments:
            ps -- Points,
            pen -- Pen.
        """

        ts = ()
        i = 0
        while i < len(ps):
            ts = ts + self.To((ps[i], ps[i + 1]))
            i = i + 2

        self.Canvas.line(ts, pen)

#---------------------------------------------------------------------------------------------------

    def Polygon(self, ps, pen = BlackPen, brush = BlackBrush):
        """
        Lines.

        Arguments:
            ps -- Points,
            pen -- Pen,
            brush -- Brush.
        """

        ts = ()
        i = 0
        while i < len(ps):
            ts = ts + self.To((ps[i], ps[i + 1]))
            i = i + 2

        self.Canvas.polygon(ts, pen, brush)

#---------------------------------------------------------------------------------------------------

    def FixLine(self, p, dp, pen = BlackPen):
        """
        Fix line.

        Arguments:
            p -- From point,
            dp -- Fixed displacement.
        """

        (cx, cy) = self.To(p)
        (dpx, dpy) = dp
        c = (cx, cy, cx + dpx, cy + dpy)
        self.Canvas.line(c, pen)

#---------------------------------------------------------------------------------------------------

    def Ellipse(self, p1, p2, pen = BlackPen, brush = None):
        """
        Ellipse.

        Arguments:
            p1 -- First point,
            p2 -- Second point,
            pen -- Pen,
            brush -- Brush.
        """

        c = self.To(p1) + self.To(p2)
        if brush == None:
            self.Canvas.ellipse(c, pen)
        else:
            self.Canvas.ellipse(c, pen, brush)

#---------------------------------------------------------------------------------------------------

    def Point(self, p, r, pen = BlackPen, brush = None):
        """
        Point.

        Arguments:
            p -- Center of point,
            r -- Radius,
            pen -- Pen,
            brush -- Brush.
        """

        (cx, cy) = self.To(p)
        c = (cx - r, cy - r, cx + r, cy + r)
        if brush == None:
            self.Canvas.ellipse(c, pen)
        else:
            self.Canvas.ellipse(c, pen, brush)

#---------------------------------------------------------------------------------------------------

    def Axis(self,
             h = 12, w = 4,
             pen = aggdraw.Pen('silver', 2.0)):
        """
        Draw axis.

        Arguments:
            h -- Arrow height,
            w -- Arrow width,
            pen -- Pen.
        """

        (min_x, min_y, max_x, max_y) = self.DrawArea

        # OX
        if (min_y <= 0) and (max_y >= 0):
            self.Line((min_x, 0), (max_x, 0), pen = pen)
            self.FixLine((max_x, 0), (-h * self.InvKX, w), pen = pen)
            self.FixLine((max_x, 0), (-h * self.InvKX, -w), pen = pen)

        # OY
        if (min_x <= 0) and (max_x >= 0):
            self.Line((0, min_y), (0, max_y), pen = pen)
            self.FixLine((0, max_y), (w, -h * self.InvKY), pen = pen)
            self.FixLine((0, max_y), (-w, -h * self.InvKY), pen = pen)

#---------------------------------------------------------------------------------------------------

    def Grid(self,
             deltas,
             pen = aggdraw.Pen('silver', 1.0)):
        """
        Draw grid.

        Arguments:
            deltas -- Distances between adjacent lines,
            pen -- Pen.
        """

        (min_x, min_y, max_x, max_y) = self.DrawArea

        (gx, gy) = deltas
        gx_cur = gx
        while gx_cur <= max_x:
            if gx_cur >= min_x:
                self.Line((gx_cur, min_y), (gx_cur, max_y), pen = pen)
            gx_cur = gx_cur + gx
        gx_cur = -gx
        while gx_cur >= min_x:
            if gx_cur <= max_x:
                self.Line((gx_cur, min_y), (gx_cur, max_y), pen = pen)
            gx_cur = gx_cur - gx
        gy_cur = gy
        while gy_cur <= max_y:
            if gy_cur >= min_y:
                self.Line((min_x, gy_cur), (max_x, gy_cur), pen = pen)
            gy_cur = gy_cur + gy
        gy_cur = -gy
        while gy_cur >= min_y:
            if gy_cur <= max_y:
                self.Line((min_x, gy_cur), (max_x, gy_cur), pen = pen)
            gy_cur = gy_cur - gy

#---------------------------------------------------------------------------------------------------

    def Rect(self, p1, p2, pen = BlackPen, brush = None):
        """
        Rectangle.

        Arguments:
            p1 -- First point,
            p2 -- Second point,
            pen -- Pen,
            brish -- Brush.
        """

        if brush == None:
            self.Canvas.rectangle(self.To(p1) + self.To(p2), pen)
        else:
            self.Canvas.rectangle(self.To(p1) + self.To(p2), pen, brush)

#---------------------------------------------------------------------------------------------------

    def RectWithCenterPoint(self, p1, p2, r, pen = BlackPen, brush = None):
        """
        Rectangle with point in its center.

        Argements:
            p1 -- First point,
            p2 -- Second point,
            r -- Point radius,
            pen -- Pen,
            brush -- Brush.
        """

        (p1x, p1y) = p1
        (p2x, p2y) = p2

        self.Rect(p1, p2, pen, brush)
        self.Point((0.5 * (p1x + p2x), 0.5 * (p1y + p2y)), r, pen, brush)

#---------------------------------------------------------------------------------------------------

    def FullGraph(self, ps, pen = BlackPen):
        """
        Draw full graph.

        Arguments:
            ps -- Point list,
            pen -- Pen.
        """

        n = len(ps)
        for i in range(n):
            for j in range(i + 1, n):
                self.Line(ps[i], ps[j], pen)

#---------------------------------------------------------------------------------------------------

    def DrawPetriNet(self, net):
        """
        Draw Petri net.

        Arguments:
            net - Petri net.
        """

        # Draw nodes.
        for n in net.Nodes:
            self.Rect(n.LoLoCorner(),
                      n.HiHiCorner(),
                      pen = aggdraw.Pen(n.BorderColor, 1.0),
                      brush = aggdraw.Brush(n.Color))

        # Draw edges.
        for e in net.Edges:
            pen = aggdraw.Pen(e.Color, 1.0)
            ps = e.Points
            self.Lines(ps, pen = pen)

            if len(ps) > 1:
                self.Point((ps[0], ps[1]), 4, pen = pen, brush = WhiteBrush)
                x, y = ps[-2], ps[-1]
                (tx, ty)= self.To((x, y))
                self.Canvas.polygon((tx + 4, ty, tx - 4, ty + 5, tx - 4, ty - 5),
                                     pen, WhiteBrush)

        self.Canvas.flush()

        # Labels.
        dr = ImageDraw.Draw(self.Img)
        font = ImageFont.truetype('C:\Windows\Fonts\lucon.ttf', 24)
        for n in net.Nodes:
            (x, y) = self.To(n.Center)
            l = len(n.Label)
            dr.text((x - l * 7.0, y - 10.0), n.Label, font = font, fill = n.FontColor)

#---------------------------------------------------------------------------------------------------
# Other functions.
#---------------------------------------------------------------------------------------------------

def test_pil():
    """
    PIL test.
    """

    # Create image and drawer.
    img = Image.new('RGB', (600, 300), color = (73, 109, 137))
    c = ImageDraw.Draw(img)

    # Draw text.
    fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 15)
    c.text((10, 10), "Arial", font = fnt, fill = (255, 255, 0))
    #
    fnt = ImageFont.truetype('C:\Windows\Fonts\lucon.ttf', 18)
    c.text((200, 80), "Lucida Console", font = fnt, fill = (0, 255, 255))
    #
    fnt = ImageFont.truetype('C:\Windows\Fonts\COLONNA.ttf', 20)
    c.text((400, 170), "Colonna MT", font = fnt, fill = (255, 0, 0))
    #
    fnt = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.ttf', 14)
    c.text((350, 250), "Old English Text", font = fnt, fill = (60, 70, 80))

    # Draw primitives.
    c.ellipse((50, 50, 200, 100), fill = 'red', outline = 'blue')
    c.line((10, 10, 590, 290))

    # Save and show.
    img.save('test.png')
    img.show()

#---------------------------------------------------------------------------------------------------

def test_aggdraw():
    """
    aggdraw test.
    """

    # Create image and drawer.
    img = Image.new('RGB', (2000, 1000), color = (73, 109, 137))
    c = aggdraw.Draw(img)

    c.setantialias(True)

    # Draw aggdraw primitives.
    c.arc((500, 200, 550, 280), 85, 320, aggdraw.Pen('red', 2.1))
    c.chord((400, 200, 450, 290), 10, 290, aggdraw.Pen('orange', 2.5), aggdraw.Brush('blue'))
    c.ellipse((50, 50, 200, 100), aggdraw.Pen('orange', 3.5), aggdraw.Brush('green'))
    c.line((10, 10, 590, 290), aggdraw.Pen('blue', 2.9))
    c.line((5, 5, 100, 20, 30, 40, 400, 250, 550, 250, 300, 100), aggdraw.Pen('red', 0.5))
    #
    path = aggdraw.Path()
    path.moveto(0, 0)
    path.curveto(200, 250, 500, 50, 400, 250)
    path.curveto(0, 60, 40, 100, 100, 100)
    c.path(path, aggdraw.Pen('pink', 5.0))
    #
    c.pieslice((100, 100, 300, 250), 50, 350,
               aggdraw.Pen('green', 2.5), aggdraw.Brush('yellow'))
    c.polygon((590, 10, 590, 290, 580, 290, 580, 20, 500, 10),
              aggdraw.Pen('blue', 1.0), aggdraw.Brush('pink'))
    c.rectangle((400, 200, 500, 300), aggdraw.Pen('black', 2.8), aggdraw.Brush('orange'))

    # Flush
    c.flush()

    # Save and show.
    img.save('test.png')
    img.show()

#---------------------------------------------------------------------------------------------------

def test_drawer():
    """
    Drawer test.
    """

    D = Drawer()
    D.Line((0, 0), (100, 100))
    D.Ellipse((30, 30), (70, 70), pen = aggdraw.Pen('red', 1.5), brush = aggdraw.Brush('steelblue'))
    D.Point((10, 80), 5)
    D.Point((80, 10), 5)
    D.FSS()

#---------------------------------------------------------------------------------------------------
# Tests.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test_pil()
    #test_aggdraw()
    #test_drawer()

#---------------------------------------------------------------------------------------------------
