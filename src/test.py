# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:12:07 2020

@author: Rybakov
"""

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
    net.DefineNodesCoords()
    net.DefineEdgesCoords()
    net.Print()

    # Construct drawer.
    drawer = png_draw.Drawer()
    drawer.DrawPetriNet(net)
    drawer.FSS()

#---------------------------------------------------------------------------------------------------
