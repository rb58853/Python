from graph import *
from test_cases import *


def start(vertices, edges):
    graph = Graph(vertices, edges, original= True)
    max_CC_from_node = {}
    max_of_this = [[],-1000000]
    while(len(graph.nodes)>1):
        calculate_max(graph)    
    show(graph)
        
        
def calculate_max(graph):
    max_CC_from_node = {}
    max_of_this = [[],-10000]

    for node in graph.nodes:
        temp = calculate_delete_node(graph, node)
        max_CC_from_node[node] = temp
    
        if (temp[1]>= max_of_this[1]):
            max_of_this = temp

    CC = max_of_this[0]
    weight = max_of_this[1]

    new_node = Node(0, CC[0].index)

    for node in max_of_this[0]:
        graph.remove(node)
        node.active = False
        for adj in node.adjacents:
            if(not CC.__contains__(adj)):
                adj.in_edge_weigth -= node.adjacents[adj]
                adj.adjacents.pop(node)
                if(weight < 0):
                    new_node.add_adj([adj,-weight])
                    adj.add_adj([new_node,-weight])
    
    if(weight < 0):
        graph.append(new_node)
    
    if (len(graph.nodes)==1):
       graph.nodes[0].weight = weight

def calculate_delete_node(graph, in_node):
    #O(n) peor caso
    CC = []
    q = [in_node]
    count = 0
    
    while(len(q)>0):
        node = q.pop()
        CC.append(node)
        count += node.weight
        
        new_weight = node.in_edge_weigth
        for n in CC:
            if(node.adjacents.__contains__(n)):
                new_weight -= node.adjacents[n]
        count-= new_weight

        for adj in node.adjacents:
            if(not CC.__contains__(adj) and not q.__contains__(adj)):
                new_weight = adj.in_edge_weigth
                for n in CC:
                    if(adj.adjacents.__contains__(n)):
                        new_weight -= adj.adjacents[n]
                if( new_weight <= adj.weight):
                    q.insert(0, adj)
                    # count -= new_weight
   
    return (CC, count)         

start(vertices_1, edges_1)
