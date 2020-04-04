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

    name = 'origin'
    net = petri_net.Net(name)

    # Define log.
    if name == 'origin':
        log = [(['a', 'b', 'c', 'd', 'e', 'f'], 1)]
    elif name == 'second':
        log = [(['a', 'b', 'c', 'd', 'e', 'f'], 1),
               (['a', 'f'], 1)]
    elif name == 'third':
        log = [(['a', 'b', 'c', 'd', 'e', 'f'], 1),                     # common
               (['a', 'f'], 1),                                         # fast discussion
               (['a', 'b', 'd', 'c', 'e', 'f'], 1),                     # order mess
               (['a', 'b', 'c'], 1),                                    # withdraw process
               (['a', 'b', 'c', 'd', 'e', 'b', 'c', 'd', 'e', 'f'], 1)] # cycles
    else:
        raise Exception('unknown case')

    alpha_results = alpha.apply_alpha_algorithm(log)

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
        drawer.Img.save(name + '.png')

#---------------------------------------------------------------------------------------------------
