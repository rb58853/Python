from show_graph import show
class Graph:
    def __init__(self,vertices = [], edges = [], original = False):
        self.nodes = []
        self.max_index = 0
        for weight, index in zip(vertices, range(len(vertices))):
            self.append(Node(weight, index))

        for index in range(len(edges)):
            for duple in edges[index]:
                self.nodes[index].add_adj([self.nodes[duple[0]],duple[1]])
        
    def append(self, node):
        node.active = True
        self.max_index = max(self.max_index,node.index)
        self.nodes.append(node)

    def remove(self, node):
        node.active = False
        self.nodes.remove(node)

    def calculate_total_profit(self):
        vertices_weight = 0
        edges_weight = 0

        for node in self.nodes:
            node.visited_calculate_profit = False

        for node in self.nodes:
            node.visited_calculate_profit = True
            vertices_weight+=node.weight
            for adj in node.adjacents:
                if(adj.active):
                    edge = node.adjacents[adj]
                    if(adj.visited_calculate_profit == False):
                        edges_weight += edge
        
        return edges_weight - vertices_weight

    def contains(self,node):
        return self.nodes.__contains__(node)   

class Node:
    def __init__(self, value, index):
        self.index = index
        self.weight = value
        self.adjacents = {}
        self.visited_calculate_profit = False
        self.active = False
        self.in_edge_weigth = 0

    def add_adj(self, duple):
        #duple es una dupla peso de la arista, referencia al vertice con el que se une
        if(not self.adjacents.__contains__(duple[0])):
            self.adjacents[duple[0]] = duple[1]
            self.in_edge_weigth += duple[1]     
        
        if(not duple[0].adjacents.__contains__(self)):
            duple[0].adjacents[self] = duple[1]
            duple[0].in_edge_weigth += duple[1]     