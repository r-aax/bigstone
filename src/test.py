# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:12:07 2020

@author: Rybakov
"""

# Own modules.
import alpha
import petri_net
import png_draw

#---------------------------------------------------------------------------------------------------
# Run.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    print('---------- test.py ---------- : ')

    case = 1

    if case == 0:
        alpha_results = alpha.apply_alpha_algorithm([(['a', 'b', 'c', 'd', 'e', 'f'], 1)])
        net = petri_net.Net('origin')
    elif case == 1:
        alpha_results = alpha.apply_alpha_algorithm([(['a', 'b', 'c', 'd', 'e', 'f'], 1),
                                                     (['a', 'f'], 1)])
        net = petri_net.Net('second')
    else:
        raise Exception('unknown case')

    print(alpha_results)
    print('y_list len = %d' % len(alpha_results[3]))

    if True:

        # Construct and print info.
        net.ConstructFromAlphaAlgorithm(alpha_results)
        net.DefineNodesCoords()
        net.DefineEdgesCoords()
        net.TuneCoords()
        net.Print()

        # Construct drawer.
        drawer = png_draw.Drawer()
        drawer.DrawPetriNet(net)
        drawer.FSS()

#---------------------------------------------------------------------------------------------------
