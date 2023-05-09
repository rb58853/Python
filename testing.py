import tester
import greedy
from reandom_graph_gen import gen_graph
from show_graph import show, show_nodes
from graph import Graph
from test_cases import *

#vertices = vertices_9
#edges = edges_9
#tester_result = tester.start(vertices, edges)
##greedy_result = greedy.start(vertices, edges)
#flow_result = flow.solution(vertices, edges)

def start(total, solution, vert_count = 5, edge_count=10):
    count_good = 0
    for i in range(total):
        test_case =  gen_graph(vert_count,edge_count)
        vertices = test_case[0]
        edges = test_case[1]
        tester_result = tester.start(vertices, edges)
        #greedy_result = greedy.start(vertices, edges)
        flow_result = solution(vertices, edges)
        is_ok = "   F"

        #if(greedy_result == tester_result):
        if(flow_result == tester_result):
            is_ok = "   ok"
            count_good +=1
        else:    
            #print( "tester: " + str(tester_result) + "    greedy:" + str(greedy_result) + is_ok)
            print( "tester: " + str(tester_result) + "    solution:" + str(flow_result) + is_ok)
            print( "vertices:")
            print(vertices)
            print( "edges:")
            print(edges)

        # print( "tester: " + str(tester_result) + "    greedy:" + str(greedy_result) + is_ok)

    print("accuracy = "+str(count_good*100/total)+ "%" )    

#start(100)