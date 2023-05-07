import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph([[0,2],[1,2],[0,1], [0,3], [1,5], [2,0]])
# pos = {}
# pos[0] = 1
# levels = {}
# levels[0] = 0
# levels[1] = 1
# levels[2] = 2
# levels[3] = 3
# levels[5] = 5

# nx.draw_networkx(G,labels= levels)
# plt.show()

def show(graph):
    vertices = []
    edge_data = []

    # G = nx.Graph([])
    for node in graph.nodes:
        for adj in node.adjacents:
            vertices.append(node.weight)
            if(adj.active):
                edge_data.append((node.index,adj.index,node.adjacents[adj]))
    
    draw_graph(vertices, edge_data)    
    plt.show()

def show_nodes (nodes:list):
    vertices = []
    edge_data = []
    for node in nodes:
        for adj in node.adjacents:
            vertices.append(node.weight)
            if(nodes.__contains__(adj)):
                edge_data.append((node.index,adj.index,node.adjacents[adj]))
    
    draw_graph(vertices, edge_data)    
    plt.show()


def draw_graph(vert_weight,edge_data):
    G = nx.Graph()
    G.add_weighted_edges_from(edge_data)

    # Dibujar el grafo y las etiquetas de los nodos
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels={
        node:f'{w}' for w,node in zip(vert_weight,G.nodes)
    })


    # Crear un diccionario con los pesos de las aristas
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

    # Mostrar los pesos de las aristas en el dibujo del grafo
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el dibujo del grafo
    plt.show()   
