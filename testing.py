import tester
import greedy
from reandom_graph_gen import gen_graph
from show_graph import show, show_nodes
from graph import Graph
from test_cases import *

vertices = vertices_9
edges = edges_9
tester_result = tester.start(vertices, edges)
greedy_result = greedy.start(vertices, edges)

def start(total):
    count_good = 0
    for i in range(total):
        test_case =  gen_graph(5,10)
        vertices = test_case[0]
        edges = test_case[1]
        tester_result = tester.start(vertices, edges)
        greedy_result = greedy.start(vertices, edges)
        is_ok = "   F"

        if(greedy_result == tester_result):
            is_ok = "   ok"
            count_good +=1
        else:    
            print( "tester: " + str(tester_result) + "    greedy:" + str(greedy_result) + is_ok)
            print( "vertices:")
            print(vertices)
            print( "edges:")
            print(edges)

        # print( "tester: " + str(tester_result) + "    greedy:" + str(greedy_result) + is_ok)

    print("accuracy = "+str(count_good*100/total)+ "%" )    

start(10000)