from graph import *
from test_cases import *
from show_graph import show

change = True
def start(vertices, edges):
    global change
    graph = Graph(vertices, edges, original= True)
    max_CC_from_node = {}
    max_of_this = [[],-1000000]
    
    # reduce_graph(graph)

    change = True
    count_while = 0
    sh = True
    while(change):
        if(len(graph.nodes)==1):
            break
        
        reduce_graph(graph)
        count_graph = len(graph.nodes)
        change = False
        calculate_max(graph)
        
        if(count_graph == len(graph.nodes)):
            #no hubo cambios
            break
    
    return max(0, graph.calculate_total_profit())
        
        
def calculate_max(graph):
    global change
    max_CC_from_node = {}
    max_of_this = [[],-10000]
    positive_min_len = [[0]*10000,0]
    positive_min_len_change = False

    for node in graph.nodes:
        temp = calculate_delete_node(graph, node)
        max_CC_from_node[node] = temp
        
        if (temp[1]>= max_of_this[1]):
            max_of_this = temp

        if(len(temp[0]) == len(positive_min_len[0]) and temp[1]>positive_min_len[1]):
            positive_min_len = temp

        if(len(temp[0]) < len(positive_min_len[0]) and temp[1]>0): 
            positive_min_len_change = True
            positive_min_len = temp

    CC = max_of_this[0]
    weight = max_of_this[1]
    
    if(positive_min_len_change):
        CC = positive_min_len[0]
        weight = positive_min_len[1]

    if(len(CC)>0):
        new_node = Node(weight, CC[0].index)
    else:
        #no encontro nada para resumir
        change = False
        return

    for node in max_of_this[0]:
        graph.remove(node)
        node.active = False
        for adj in node.adjacents:
            if(not CC.__contains__(adj)):
                adj.remove_adj(node)
                if(weight < 0):
                    new_node.add_adj([adj,0])
                    adj.add_adj([new_node,0])
    
    if(weight <= 0):
        graph.append(new_node)
    
def calculate_delete_node(graph, in_node):
    #O(n) peor caso
    global change
    CC = []
    q = [in_node]
    count = 0
    
    # if(in_node.weight> in_node.in_edge_weigth):
    #     return [[in_node],in_node.weight-in_node.in_edge_weigth]

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
                    change = True
                    # count -= new_weight
   
    return (CC, count)         

def reduce_graph(graph):
    change = True
    while(change):
        change = False

        temp_nodes = []
        for node in graph.nodes:
            temp_nodes.append(node)

        for node in temp_nodes:
            if(node.in_edge_weigth < node.weight):
                change = True
                node.active = False
                graph.remove(node)
                for adj in node.adjacents:
                    adj.remove_adj(node)
    
    change = True
    while(change):
        change = False
        temp_nodes = []
        for node in graph.nodes:
            temp_nodes.append(node)

        change_node = False
        for node in temp_nodes:
            if(change_node):
                    break
            change_node = False
                
            for adj in node.adjacents:
                if(change_node):
                    break
                if(graph.contains(adj)):
                    if(adj.weight <= node.adjacents[adj] and node.weight <= node.adjacents[adj]):
                        change = True
                        change_node = True
                        new_node = Node((node.weight + adj.weight)-node.adjacents[adj], node.index)
                        graph.remove(node)
                        graph.remove(adj)
                        node.active = False
                        adj.active = False
                        for adj_adj in adj.adjacents:
                            if(adj_adj != node):
                                adj_adj.remove_adj(adj)
                                # adj.remove_adj(adj_adj)
                                new_node.add_adj([adj_adj,adj.adjacents[adj_adj]])
                        for node_adj in node.adjacents:
                            if(node_adj != adj):
                                node_adj.remove_adj(node)
                                # adj.remove_adj(adj_adj)
                                if(not new_node.adjacents.__contains__(node_adj)):
                                    new_node.add_adj([node_adj,node.adjacents[node_adj]])
                                else:
                                    new_node.adjacents[node_adj] += node.adjacents[node_adj]
                                    new_node.in_edge_weigth += node.adjacents[node_adj]

                                    node_adj.adjacents[new_node] +=node.adjacents[node_adj]
                                    node_adj.in_edge_weigth += node.adjacents[node_adj]

                        graph.append(new_node)        
            

# print("profit: " + str(start(vertices_3, edges_3)))
