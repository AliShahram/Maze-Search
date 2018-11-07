from heuristics import manDist, cartDist
from data_structures import PriorityQueue, listGraph
import copy

def aStarSP(graph, start, goal):
    '''A* search for single prize. 
    graph is a list of points. (e.g. [[1,3],[4,5],[7,5]]
    a point is a list of two integers (e.g. [1,3])
    start and goal are two points in the maze
    '''
    # convert the lists into tuple, lists are unhashble
    start_t = copy.deepcopy(start)
    start_t = tuple(start_t) 
    goal_t = copy.deepcopy(goal)
    goal_t = tuple(goal_t)
 
    explore_next = PriorityQueue()
    explore_next.push(start, 0)
    visited_w_cost = {}
    visited_w_cost[start_t] = 0 
    predecessors = {}
    predecessors[start_t] = None 

    while not explore_next.is_empty():
        # get the one with the smallest cost
        current_l = explore_next.pop()    # tuple
        current_t = copy.deepcopy(current_l)
        current_t = tuple(current_t)
        # print (current_l, goal)
        # print ("{0}".format(explore_next.show_queue()))
        if current_l == goal:
            # go home, got the prize
            print ("found the prize! {}".format(visited_w_cost[current_t]))
            break
        for next in graph.neighbors(current_l):
            next_t = copy.deepcopy(next)
            next_t = tuple(next_t)
            new_cost = visited_w_cost[current_t] + graph.cost(current_l, next)

            if next_t not in visited_w_cost or new_cost < visited_w_cost[next_t]:
                visited_w_cost[next_t] = new_cost
                priority = new_cost + manDist(next, goal)
                
                if next == goal:
                    predecessors[next_t] = current_t
                    return predecessors
                graph.set_node(next, '#')
                explore_next.push(next, priority)
                predecessors[next_t] = current_t
