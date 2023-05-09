import igraph as ig
import matplotlib.pyplot as plt

def draw_flow(g):
    #ig.plot(g)
    fig, ax = plt.subplots()
    g.vs['label'] =g.vs['name']  
    g.es['edge_label'] = g.es['weight']
    g.es['label'] = g.es['weight']
    ig.plot(g, target=ax,layout='sugiyama', edge_label=g.es['weight'])
    plt.show()

def draw_graph(vertices, edges):
    g = ig.Graph()   
    g.add_vertices(len(vertices))
    g.vs['label'] = list(f"{i}[{w}]"for i,w in zip(range(0,len(vertices)),vertices))


    edges_names = [[False]*len(vertices) for _ in vertices]
    for i, edgs in enumerate(edges):  
        for v,weight in edgs: 
            if not edges_names[i][v]:
                g.add_edge(i,v, weight=weight)
                edges_names[i][v]=True
                edges_names[v][i]=True

    fig, ax = plt.subplots()
    ig.plot(g, target=ax, edge_label=g.es['weight'])
    plt.show()



#v = [12, 5, 20]
#edg=[[(2, 5)], [(2, 20)], [(0, 5), (1, 20)]]

#draw_graph(v,edg)