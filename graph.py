from show_graph import show
class Graph:
    def __init__(self,vertices = [], edges = [], original = False):
        self.nodes = []
        for weight, index in zip(vertices, range(len(vertices))):
            self.append(Node(weight, index))

        for index in range(len(edges)):
            for duple in edges[index]:
                self.nodes[index].add_adj([self.nodes[duple[0]],duple[1]])
        
    def append(self, node):
        node.active = True
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

    def add_adj(self, duple):
        #duple es una dupla peso de la arista, referencia al vertice con el que se une
        self.adjacents[duple[0]] = duple[1]    