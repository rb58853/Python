from graph import *
from test_cases import *
from show_graph import show, show_nodes

global_nodes = []
def start(vertices, edges):
    #El array de aristas es indesado en vertice_i, edges[i] es una lista de tuplas donde item1 es el vertice
    # al cual va, e item 2 es el peso de la arista que lo conecta con ese vertice.
    global global_nodes
    global_nodes = []
    graph = Graph(vertices, edges, original= True)
    
    for node in graph.nodes:
        global_nodes.append(node)
    for node in global_nodes:
        graph.remove(node)
        
    rec(graph,0,"")
    return rec_result

rec_result = 0
end_nodes:list
def rec(graph, index, s):
    global rec_result
    global global_nodes
    
    print(s)

    graph_weight = graph.calculate_total_profit()
    if(graph_weight>rec_result):
        rec_result = graph_weight
        update_nodes(graph)
    # rec_result = max(rec_result, graph.calculate_total_profit())
    
    for i in range(index, len(global_nodes)) :
        node = global_nodes[i]
        if(not graph.contains(node)):
            graph.append(node)
            rec(graph, i, s+ str(node.index) + " ")
            graph.remove(node)

def update_nodes(graph):
    global end_nodes
    end_nodes = []
    for node in graph.nodes:
        end_nodes.append(node)

print(start(vertices_1, edges_1))
show_nodes(end_nodes)
a = 1