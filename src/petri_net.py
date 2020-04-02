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
    net.AddNode(Node('P', 'Input'))
    net.AddNode(Node('P', 'Output'))
    for a in activities_list:
        net.AddNode(Node('A', a))
    for ia in input_activities_list:
        net.AddEdge('Input', ia)
    for oa in output_activities_list:
        net.AddEdge(oa, 'Output')
    for (i, (sa, sb)) in enumerate(y_list):
        lab = 'p%d' % i
        net.AddNode(Node('P', lab))
        for a in sa:
            net.AddEdge(a, lab)
        for b in sb:
            net.AddEdge(lab, b)

    assert (len(net.Nodes) == 13) and (len(net.Edges) == 14)

#---------------------------------------------------------------------------------------------------
