import igraph as ig
import matplotlib.pyplot as plt


def solution(vert_w, edges):
    g = ig.Graph(directed=True)
    g.add_vertices(len(vert_w),attributes={"type":'vertex'})
    g.vs.select(type='vertex')['name']= [i for i in range(len(vert_w))]

    t_vertex=g.add_vertex('t')
    s_vertex=g.add_vertex('s')


    edges_names = [[False]*len(vert_w) for _ in vert_w]
    suma_total = 0
    for index,v in enumerate(g.vs.select(type='vertex')):
        v: ig.Vertex
        g.add_edge(v, t_vertex, weight=vert_w[index],name='final_edge' )
        suma_total-=vert_w[index]
        for edge_index,(connected_vertex,weight) in enumerate(edges[index]):
            if not edges_names[index][connected_vertex]:
                suma_total+= weight

                edges_names[index][connected_vertex] = True
                edges_names[connected_vertex][index] = True

                vv= g.add_vertex(f'edge_{index}_{connected_vertex}',type='edge')
                g.add_edge(vv,v,weight=float('inf'))
                g.add_edge(vv,connected_vertex,weight=float('inf'))
                g.add_edge(s_vertex, vv, weight=weight)


    
    flow = g.maxflow(s_vertex,t_vertex, capacity=g.es['weight']).flow
    flow = [f for index,f in enumerate(flow) if g.es[index]['name'] == 'final_edge']

   #print("suma_total:", suma_total)
   #print(vert_w)
   #print(flow)

    edges_names = [[False]*len(vert_w) for _ in vert_w]
    explored_vert= [False]*len(vert_w)
    for index,(city_weight,flow_arista_final) in enumerate(zip(vert_w, flow)):
        if city_weight!=flow_arista_final and not explored_vert[index]:
            suma_total+=remove_city_dfs(index,edges_names, explored_vert,vert_w,edges)

    return max(suma_total,0)#,g


def remove_city_dfs(current_v,edges_names,explored_vert, citys_weight,edges ):
    explored_vert[current_v] = True
    sol = citys_weight[current_v]
    for (v,weight) in edges[current_v]:

        if not edges_names[current_v][v]:
            sol-=weight
        if not explored_vert[v]:

            edges_names[current_v][v]=True
            edges_names[v][current_v]=True

            value = citys_weight[v] - sum(
                [w for vv,w in edges[v] if not edges_names[v][vv]])
            if value > 0:
                sol+=remove_city_dfs(
                    v,edges_names, explored_vert,citys_weight,edges)

    return sol 


#vert_w, edges =[7, 10, 7], [[(2, 15), (1, 6)], [(0, 6)], [(0, 15)]]
#print(solution(vert_w,edges))
