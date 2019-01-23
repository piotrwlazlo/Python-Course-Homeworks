from Edges import *
from Factory import *
from Graphs import *

class EdgeColor:
    
    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target: 
                raise ValueError("a loop detected")
            else:
                self.color[(edge.source, edge.target)] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def run(self):
        length = len(list(self.graph.iternodes()))
        peripheral_edges= []
        for i in range(length): # 
            edge = (i, (i+1) % length)
            if edge in self.color.keys():
                self.color[edge] = i
                peripheral_edges.append(edge)
            else:
                self.color[(edge[1], edge[0])] = i
                peripheral_edges.append((edge[1], edge[0]))
        print(peripheral_edges)
        for edge in peripheral_edges:
            start_node = edge[0]
            end_node = edge[1]
            while edge[0] != math.floor(length/2):
                pass
        

if __name__ == '__main__':
    N = 7
    G = GraphFactory(Graph)
    g1 = G.make_complete(N, directed=False)
    g1.save("graf.txt")
    c1 = EdgeColor(g1)
    c1.run()
    print(c1.color)
