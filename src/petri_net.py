# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:57:13 2020

@author: Rybakov
"""

#---------------------------------------------------------------------------------------------------
# Class node.
#---------------------------------------------------------------------------------------------------

class Node:
    """
    Node.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, t, lab):
        """
        Constructor.

        Arguments:
            t -- Type ('A' or 'P'),
            lab -- Label.
        """

        assert (t == 'A') or (t == 'P')

        self.Type = t
        self.Label = lab
        self.InEdges = []
        self.OutEdges = []
        self.Center = (50.0, 50.0)

        # Color.
        if t == 'A':
            self.Color = (255, 0, 0, 255)
            self.Width = 5.0
            self.Height = 5.0
        elif t == 'P':
            self.Color = (0, 0, 255, 255)
            self.Width = 4.0
            self.Height = 4.0

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        Convert to string.

        Result:
            String.
        """

        return 'node : %s (%s)' % (self.Label, self.Type)

#---------------------------------------------------------------------------------------------------

    def IsActivity(self):
        """
        Check if node is activity.

        Result:
            True -- If node is activity,
            False -- If node is not activity.
        """

        return self.Type == 'A'

#---------------------------------------------------------------------------------------------------

    def IsPlace(self):
        """
        Check if node is place.

        Result:
            True -- If node is place,
            False -- If node is not place.
        """

        return self.Type == 'P'

#---------------------------------------------------------------------------------------------------

    def LoLoCorner(self):
        """
        Get lo-lo corner.

        Result:
            Lo-lo corner.
        """

        return (self.Center[0] - 0.5 * self.Width, self.Center[1] - 0.5 * self.Height)

#---------------------------------------------------------------------------------------------------

    def HiHiCorner(self):
        """
        Get hi-hi corner.

        Result:
            Hi-hi corner.
        """

        return (self.Center[0] + 0.5 * self.Width, self.Center[1] + 0.5 * self.Height)

#---------------------------------------------------------------------------------------------------
# Class edge.
#---------------------------------------------------------------------------------------------------

class Edge:
    """
    Edge.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, pred, succ):
        """
        Constructor.

        Arguments:
            pred -- Predecessor,
            succ -- Successor.
        """

        self.Pred = pred
        self.Succ = succ
        self.Color = (0, 0, 0, 255, 255)

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        Convert to string.

        Result:
            String.
        """

        return 'edge : %s - %s' % (str(self.Pred), str(self.Succ))

#---------------------------------------------------------------------------------------------------
# Class net.
#---------------------------------------------------------------------------------------------------

class Net:
    """
    Net.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor.
        """

        self.Nodes = []
        self.Edges = []

#---------------------------------------------------------------------------------------------------

    def Print(self):
        """
        Print information.
        """

        print('Net : %d nodes, %d edges' % (len(self.Nodes), len(self.Edges)))
        for n in self.Nodes:
            print(str(n))
        for e in self.Edges:
            print(str(e))

#---------------------------------------------------------------------------------------------------

    def FindNode(self, lab):
        """
        Find node by label.

        Arguments:
            lab -- Label.

        Result:
            Node or None.
        """

        for n in self.Nodes:
            if n.Label == lab:
                return n

        return None

#---------------------------------------------------------------------------------------------------

    def AddNode(self, node):
        """
        Add node.

        Arguments:
            node -- Node.
        """

        self.Nodes.append(node)

#---------------------------------------------------------------------------------------------------

    def AddEdge(self, pred_lab, succ_lab):
        """
        Add edge.

        Arguments:
            pred_lab -- Predecessor label,
            succ_lab -- Successor label.

        Result:
            New edge.
        """

        pred = self.FindNode(pred_lab)
        succ = self.FindNode(succ_lab)

        assert (pred != None) and (succ != None)

        edge = Edge(pred, succ)
        self.Edges.append(edge)
        pred.OutEdges.append(edge)
        succ.InEdges.append(edge)

#---------------------------------------------------------------------------------------------------

    def ConstructFromAlphaAlgorithm(self, alpha_algorithm_results):
        """
        Construct net from results of alpha algorithm.

        Arguments:
            alpha_algorithm_results -- Results of alpha algorithm.
        """

        (activities_list, input_activities_list,
         output_activities_list, y_list) = alpha_algorithm_results

        # Construct net.
        self.AddNode(Node('P', 'Input'))
        self.AddNode(Node('P', 'Output'))
        for a in activities_list:
            self.AddNode(Node('A', a))
        for ia in input_activities_list:
            self.AddEdge('Input', ia)
        for oa in output_activities_list:
            self.AddEdge(oa, 'Output')
        for (i, (sa, sb)) in enumerate(y_list):
            lab = 'p%d' % i
            self.AddNode(Node('P', lab))
            for a in sa:
                self.AddEdge(a, lab)
            for b in sb:
                self.AddEdge(lab, b)

#---------------------------------------------------------------------------------------------------
# Test.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Create test net.
    net = Net()

    # Fill net configuration.
    activities_list = ['a', 'b', 'c', 'd', 'e', 'f']
    input_activities_list = ['a']
    output_activities_list = ['f']
    y_list = [({'c'}, {'d'}), ({'a'}, {'e'}), ({'b'}, {'c', 'f'}),
              ({'e'}, {'f'}), ({'a', 'd'}, {'b'})]

    # Construct net.
    net.ConstructFromAlphaAlgorithm((activities_list, input_activities_list,
                                     output_activities_list, y_list))

    assert (len(net.Nodes) == 13) and (len(net.Edges) == 14)

#---------------------------------------------------------------------------------------------------
