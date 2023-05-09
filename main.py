import flow_igraph
import tester
import draw_igraph

def load_raul():
    vertices_1 = [7,7,7,7,7,7,7,7,7,7,2,31,31]
    edges_1 = []

    edges_1.append([(1,6),(2,6),(10,1)])
    edges_1.append([(0,6),(2,6)])
    edges_1.append([(0,6),(1,6),(9,4)])

    edges_1.append([(4,6),(5,6),(9,4)])
    edges_1.append([(3,6),(5,6)])
    edges_1.append([(3,6),(4,6)])

    edges_1.append([(7,6),(8,6),(9,4)])
    edges_1.append([(6,6),(8,6)])
    edges_1.append([(6,6),(7,6)])


    edges_1.append([(2,4),(3,4),(6,4)])

    edges_1.append([(0,6),(11,30),(12,30)])
    edges_1.append([(12,30),(10,30)])
    edges_1.append([(11,30),(10,30)])
    return vertices_1, edges_1


def load_graph1():
    return [4,3,4,10,4,12],[
    #return [4,3,4,10],[
        [(1,2),(2,9)],
        [(0,2),(2,2)],
        [(0,9),(1,2),(3,3)],
       #   [(2,3)],
       [(2,3),(4,5),(5,9)],
       [(3,5),(5,6)],
       [(3,9),(4,6)],
    ]


def main():
    #vert_w, edges = load_raul()
    #vert_w, edges = load_graph1()
    #vert_w, edges=random_graph_gen.gen_graph(4, 6)

    #print(flow.solution(vert_w, edges))

    #draw_graph.from_usual_format(vert_w, edges)

    from testing import start

    start(10000,flow_igraph.solution, vert_count=10, edge_count=4)

   #vert_w, edges = [9, 3, 10, 13, 16],[[(4, 19), (1, 4)], [(0, 4)], [(3, 16)], [(2, 16), (4, 14)], [(3, 14), (0, 19)]]
   #print(flow.solution(vert_w,edges))
   #print('tester_solution:',tester.start(vert_w,edges))
   #draw_graph.from_usual_format(vert_w, edges)


    #vert_w, edges = [3, 12, 15, 17, 19],[[(1, 18)], [(0, 18)], [(3, 7), (4, 10)], [(2, 7), (4, 15)], [(2, 10), (3, 15)]]
    #sol,g = flow_igraph.solution(vert_w,edges)
    #print(sol)
    #print('tester_solution:',tester.start(vert_w,edges))
    ##draw_igraph.draw_graph(vert_w,edges)
    #draw_igraph.draw_flow(g)

main()
