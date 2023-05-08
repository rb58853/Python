import random

def gen_graph(total_vert, total_edges, min_weight=1, max_weight = 20):
    city_weights = [random.randint(min_weight,max_weight) for _ in range(total_vert)]  
     
    existing_edges = set()
    edges = [ [] for _ in range(total_vert)]
    for index in range(total_edges):
        x,y = random.randint(0,total_vert-1),random.randint(0,total_vert-1)
        if x==y or ((x,y) in existing_edges) or ((y,x) in existing_edges):
            continue

        existing_edges.add((x,y))
        edge_weight = random.randint(min_weight,max_weight)
        edges[x].append((y,edge_weight))
        edges[y].append((x,edge_weight))

    return city_weights, edges


# if __name__ == '__main__':
#     print(gen_graph(10,3))
