from data_structures import listGraph
from state_rep import parser, extractParams
from aStar import aStarSP
import sys
import copy


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

def print_graph(list_2d, path=[]):
    '''Takes two 2-D list and prints it on the terminal.
    list_2d is the whole map, path is a 2d list that has the
    path in the form of [[1,2][2,3]]
    '''
    if len(path) != 0:
        for point in path:
            [x,y] = point
            list_2d[x][y] = '>'

    for i in range(len(list_2d)):
        for j in range(i):
            if list_2d[i][j] == "#":
                list_2d[i][j] = " "

    for row in list_2d:
        for column in row:
            print(column, end='')
        print("")
    return 

def get_prize(graph, start, goal):
    [x1, y1] = start
    [x2, y2] = goal
    graph.set_node(start, 'P')
    graph.set_node(goal, '.')
    allVisited = aStarSP(graph, start, goal)
    path_t =  reconstruct_path(allVisited, (x1,y1), (x2,y2))
    path_l = []
    for point in path_t:
        (x,y) = point
        path_l.append([x,y])
    graph_in_list = graph.get_graph()
    print ("The maze with the path")
    print_graph(graph_in_list, path_l)
    
    return graph, goal

def a_star_driver(infile):
    parsed = parser(infile)
    params = extractParams(parsed)     
    graph = listGraph(parsed)

    start = params['start']
    prizes = params['loc_prizes']
    for prize in prizes:
        print("Hunting for the next prize:")
        graph, start = get_prize(graph, start, prize)
        graph_in_list = graph.get_graph()
        prizes = extractParams(graph_in_list)['loc_prizes'] 

if __name__ == '__main__':
    a_star_driver()
