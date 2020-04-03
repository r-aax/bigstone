# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:57:13 2020

@author: Rybakov
"""

# Outer modules.
import random

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
        if lab == 'I':
            self.Color = 'silver'
            self.Width = 6.0
            self.Height = 6.0
        elif lab == 'O':
            self.Color = 'silver'
            self.Width = 6.0
            self.Height = 6.0
        elif t == 'A':
            self.Color = 'indianred'
            self.Width = 5.0
            self.Height = 5.0
        elif t == 'P':
            self.Color = 'steelblue'
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
        self.Points = ()

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
        self.AddNode(Node('P', 'I'))
        self.AddNode(Node('P', 'O'))
        for a in activities_list:
            self.AddNode(Node('A', a))
        for ia in input_activities_list:
            self.AddEdge('I', ia)
        for oa in output_activities_list:
            self.AddEdge(oa, 'O')
        for (i, (sa, sb)) in enumerate(y_list):
            lab = 'p%d' % i
            self.AddNode(Node('P', lab))
            for a in sa:
                self.AddEdge(a, lab)
            for b in sb:
                self.AddEdge(lab, b)

#---------------------------------------------------------------------------------------------------

    def DefineNodesCoords(self):
        """
        Define nodes coordinates.
        """

        self.Nodes[2].Center = (20.0, 50.0)
        self.Nodes[3].Center = (50.0, 50.0)
        self.Nodes[4].Center = (65.0, 75.0)
        self.Nodes[5].Center = (35.0, 75.0)
        self.Nodes[6].Center = (50.0, 25.0)
        self.Nodes[7].Center = (80.0, 50.0)
        self.Nodes[8].Center = (50.0, 75.0)
        self.Nodes[9].Center = (35.0, 25.0)
        self.Nodes[10].Center = (65.0, 50.0)
        self.Nodes[11].Center = (65.0, 25.0)
        self.Nodes[12].Center = (35.0, 50.0)

        #for n in self.Nodes:
        #    n.Center = (random.uniform(10.0, 90.0), random.uniform(10.0, 90.0))

        # Start and end.
        self.Nodes[0].Center = (10.0, 50.0)
        self.Nodes[1].Center = (90.0, 50.0)

#---------------------------------------------------------------------------------------------------

    def GetEdgeEndCoordInInterval(lo, hi, edges, index):
        """
        Get edge end coordinate in interval.
        Some interval is given.
        Several edges come out from it (count is 'edges').
        The given edge has index 'index'.
        It is necessary to find out value of coordinate.

        Arguments:
            lo -- Lower value of interval,
            hi -- Higher value of interval,
            edges -- Total edges count,
            index -- Index of edge comes out.
        """

        length = hi - lo
        dlength = length / (edges + 1)

        return lo + dlength * (index + 1)

#---------------------------------------------------------------------------------------------------

    def DefineEdgesCoords(self):
        """
        Define edges coordintes.
        """

        for e in self.Edges:
            a, b = e.Pred, e.Succ
            ap = (a.Center[0] + 0.5 * a.Width,
                  Net.GetEdgeEndCoordInInterval(a.Center[1] - 0.5 * a.Height,
                                                a.Center[1] + 0.5 * a.Height,
                                                len(a.OutEdges),
                                                a.OutEdges.index(e)))
            bp = (b.Center[0] - 0.5 * b.Width,
                  Net.GetEdgeEndCoordInInterval(b.Center[1] - 0.5 * b.Height,
                                                b.Center[1] + 0.5 * b.Height,
                                                len(b.InEdges),
                                                b.InEdges.index(e)))

            if ap[0] < bp[0]:
                cxf = 0.25 * (3.0 * ap[0] + bp[0])
                cxt = 0.25 * (ap[0] + 3.0 * bp[0])
                cx = random.uniform(cxf, cxt)
                ap1 = (cx, ap[1])
                bp1 = (cx, bp[1])
                e.Points = ap + ap1 + bp1 + bp
            elif abs(ap[1] - bp[1]) > a.Height:
                ap1 = (ap[0] + 0.25 * a.Width, ap[1])
                bp1 = (bp[0] - 0.25 * b.Width, bp[1])
                cyf = 0.25 * (3.0 * ap1[1] + bp1[1])
                cyt = 0.25 * (ap1[1] + 3.0 * bp1[1])
                cy = random.uniform(cyf, cyt)
                ap2 = (ap1[0], cy)
                bp2 = (bp1[0], cy)
                e.Points = ap + ap1 + ap2 + bp2 + bp1 + bp
            else:
                # Over head.
                ap1 = (ap[0] + 0.5 * a.Width, ap[1])
                bp1 = (bp[0] - 0.5 * b.Width, bp[1])
                yf = max(ap1[1] + a.Height, bp1[1] + b.Height)
                yt = yf + a.Height
                y = random.uniform(yf, yt)
                ap2 = (ap1[0], y)
                bp2 = (bp1[0], y)
                e.Points = ap + ap1 + ap2 + bp2 + bp1 + bp

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
