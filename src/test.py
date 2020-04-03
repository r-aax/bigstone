# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:12:07 2020

@author: Rybakov
"""

# Outer modules.
import aggdraw
from PIL import Image, ImageDraw, ImageFont

# Own modules.
import petri_net
import png_draw

#---------------------------------------------------------------------------------------------------
# Run.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Construct net.
    net = petri_net.Net()

    # Fill net configuration.
    activities_list = ['a', 'b', 'c', 'd', 'e', 'f']
    input_activities_list = ['a']
    output_activities_list = ['f']
    y_list = [({'c'}, {'d'}), ({'a'}, {'e'}), ({'b'}, {'c', 'f'}),
              ({'e'}, {'f'}), ({'a', 'd'}, {'b'})]

    # Construct net.
    net.ConstructFromAlphaAlgorithm((activities_list, input_activities_list,
                                     output_activities_list, y_list))
    net.Print()
    net.Nodes[0].Center = (10.0, 50.0)
    net.Nodes[1].Center = (90.0, 50.0)
    net.Nodes[2].Center = (20.0, 50.0)
    net.Nodes[3].Center = (50.0, 50.50)
    net.Nodes[4].Center = (65.0, 75.0)
    net.Nodes[5].Center = (35.0, 75.0)
    net.Nodes[6].Center = (50.0, 25.0)
    net.Nodes[7].Center = (80.0, 50.0)
    net.Nodes[8].Center = (50.0, 75.0)
    net.Nodes[9].Center = (35.0, 25.0)
    net.Nodes[10].Center = (65.0, 50.0)
    net.Nodes[11].Center = (65.0, 25.0)
    net.Nodes[12].Center = (35.0, 50.0)

    # Construct drawer.
    drawer = png_draw.Drawer()
    drawer.Line((0, 0), (100, 100))
    drawer.Ellipse((30, 30), (70, 70),
                   pen = aggdraw.Pen('red', 1.5), brush = aggdraw.Brush('steelblue'))
    drawer.Point((10, 80), 5)
    drawer.Point((80, 10), 5)

    # To show type D.FSS()

#---------------------------------------------------------------------------------------------------
