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
            self.BorderColor = 'silver'
            self.FontColor = 'black'
            self.Width = 4.0
            self.Height = 4.0
        elif lab == 'O':
            self.Color = 'silver'
            self.BorderColor = 'silver'
            self.FontColor = 'black'
            self.Width = 4.0
            self.Height = 4.0
        elif t == 'A':
            self.Color = 'black'
            self.BorderColor = 'black'
            self.FontColor = 'white'
            self.Width = 5.0
            self.Height = 5.0
        elif t == 'P':
            self.Color = 'white'
            self.BorderColor = 'black'
            self.FontColor = 'black'
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
        self.APoint = None
        self.BPoint = None
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

    def __init__(self, name):
        """
        Constructor.

        Arguments:
            name -- Name of net.
        """

        self.Nodes = []
        self.Edges = []
        self.Name = name

#---------------------------------------------------------------------------------------------------

    def Print(self):
        """
        Print information.
        """

        print('Net %s : %d nodes, %d edges' % (self.Name, len(self.Nodes), len(self.Edges)))
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

    def FindEdge(self, laba, labb):
        """
        Find edge by nodes labels.

        Arguments:
            laba -- Node A label,
            labb -- Node B label.

        Result:
            Edge or None.
        """

        for e in self.Edges:
            if (e.Pred.Label == laba) and (e.Succ.Label == labb):
                return e

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

    def DefineNodeCoords(self, lab, coords):
        """
        Define coordinates of node.

        Arguments:
            lab -- Node label,
            coords -- Coordinares.
        """

        self.FindNode(lab).Center = coords

#---------------------------------------------------------------------------------------------------

    def DefineNodesCoords(self):
        """
        Define nodes coordinates.
        """

        # Start and end.
        self.DefineNodeCoords('I', (10.0, 50.0))
        self.DefineNodeCoords('O', (90.0, 50.0))

        if self.Name == 'origin':
            self.DefineNodeCoords('a',  (20.0, 50.0))
            self.DefineNodeCoords('p2', (26.0, 50.0))
            self.DefineNodeCoords('b',  (32.0, 50.0))
            self.DefineNodeCoords('p3', (38.0, 50.0))
            self.DefineNodeCoords('c',  (44.0, 50.0))
            self.DefineNodeCoords('p0', (50.0, 50.0))
            self.DefineNodeCoords('d',  (56.0, 50.0))
            self.DefineNodeCoords('p1', (62.0, 50.0))
            self.DefineNodeCoords('e',  (68.0, 50.0))
            self.DefineNodeCoords('p4', (74.0, 50.0))
            self.DefineNodeCoords('f',  (80.0, 50.0))
        elif self.Name == 'second':
            self.DefineNodeCoords('a',  (20.0, 50.0))
            self.DefineNodeCoords('p2', (26.0, 45.0))
            self.DefineNodeCoords('b',  (32.0, 50.0))
            self.DefineNodeCoords('p3', (38.0, 50.0))
            self.DefineNodeCoords('c',  (44.0, 50.0))
            self.DefineNodeCoords('p0', (50.0, 50.0))
            self.DefineNodeCoords('d',  (56.0, 50.0))
            self.DefineNodeCoords('p1', (62.0, 50.0))
            self.DefineNodeCoords('e',  (68.0, 50.0))
            self.DefineNodeCoords('p4', (74.0, 55.0))
            self.DefineNodeCoords('f',  (80.0, 50.0))
        else:
            raise Exception('unexpected neet name')

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

    def SetEdgeCoordsTypeHorizontal(e):
        """
        Define edge coordinates type 'horizontal'.

        Arguments:
            e -- Edge.
        """

        ap, bp = e.APoint, e.BPoint
        cxf = 0.25 * (3.0 * ap[0] + bp[0])
        cxt = 0.25 * (ap[0] + 3.0 * bp[0])
        cx = random.uniform(cxf, cxt)
        ap1 = (cx, ap[1])
        bp1 = (cx, bp[1])
        e.Points = ap + ap1 + bp1 + bp

#---------------------------------------------------------------------------------------------------

    def SetEdgeCoordsTypeVertical(e):
        """
        Define edge coordinates type 'vertical'.

        Arguments:
            e -- Edge.
        """

        a, b, = e.Pred, e.Succ
        ap, bp = e.APoint, e.BPoint
        ap1 = (ap[0] + 0.25 * a.Width, ap[1])
        bp1 = (bp[0] - 0.25 * b.Width, bp[1])
        cyf = 0.25 * (3.0 * ap1[1] + bp1[1])
        cyt = 0.25 * (ap1[1] + 3.0 * bp1[1])
        cy = random.uniform(cyf, cyt)
        ap2 = (ap1[0], cy)
        bp2 = (bp1[0], cy)
        e.Points = ap + ap1 + ap2 + bp2 + bp1 + bp

#---------------------------------------------------------------------------------------------------

    def SetEdgeCoordsTypeOverHead(e):
        """
        Define edge coordinates type 'over head'.

        Arguments:
            e -- Edge.
        """

        a, b, = e.Pred, e.Succ
        ap, bp = e.APoint, e.BPoint
        ap1 = (ap[0] + 0.5 * a.Width, ap[1])
        bp1 = (bp[0] - 0.5 * b.Width, bp[1])
        yf = max(ap1[1] + a.Height, bp1[1] + b.Height)
        yt = yf + a.Height
        y = random.uniform(yf, yt)
        ap2 = (ap1[0], y)
        bp2 = (bp1[0], y)
        e.Points = ap + ap1 + ap2 + bp2 + bp1 + bp

#---------------------------------------------------------------------------------------------------

    def SetEdgeCoordsTypeOverBottom(e):
        """
        Define edge coordinates type 'over bottom'.

        Arguments:
            e -- Edge.
        """

        a, b, = e.Pred, e.Succ
        ap, bp = e.APoint, e.BPoint
        ap1 = (ap[0] + 0.5 * a.Width, ap[1])
        bp1 = (bp[0] - 0.5 * b.Width, bp[1])
        yt = max(ap1[1] - a.Height, bp1[1] - b.Height)
        yf = yt - a.Height
        y = random.uniform(yf, yt)
        ap2 = (ap1[0], y)
        bp2 = (bp1[0], y)
        e.Points = ap + ap1 + ap2 + bp2 + bp1 + bp

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
            e.APoint = ap
            e.BPoint = bp

            if ap[0] < bp[0]:
                Net.SetEdgeCoordsTypeHorizontal(e)
            elif abs(ap[1] - bp[1]) > a.Height:
                Net.SetEdgeCoordsTypeVertical(e)
            else:
                Net.SetEdgeCoordsTypeOverHead(e)

#---------------------------------------------------------------------------------------------------

    def TuneCoords(self):
        """
        Tune coords.
        """

        if self.Name == 'origin':
            pass
        elif self.Name == 'second':
            Net.SetEdgeCoordsTypeOverHead(self.FindEdge('a', 'p4'))
            Net.SetEdgeCoordsTypeOverBottom(self.FindEdge('p2', 'f'))
        else:
            raise Exception('unexpected neet name')

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
