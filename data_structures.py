# Keep all the data structures we need for the program
import heapq
import copy

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Tra_model:

    def move_right(self, pointer):  #Move the pointer to the right
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[1] += 1
                return current   #Increment one to the column
                break
            except IndexError:
                print("IndexError")
                break


    def move_left(self, pointer):    #Move the pointer to the left
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[1] -= 1
                return current  #decrease one from the column
                break

            except IndexError:
                print("IndexError")
                break

    def move_up(self, pointer):         #Move the pointer up
        current = copy.deepcopy(pointer)
        while True:
            try:
                current [0] -= 1
                return current    #Add one to the row
                break

            except IndexError:
                print("IndexError")
                break

    def move_down(self, pointer):           #Move the pointer up
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[0] += 1
                return current  #subtract one from the row
                break

            except IndexError:
                print("IndexError")
                break



# graph from the 2-d list for faster navigation
class listGraph(object):
    '''listGraph object is used for better traversal of the 
        2d array for search algorithms with heuristics
    '''
    def __init__(self, list_2d):
        self.graph = list_2d
        self.wall = '%'
        self.prize = '.'
        self.empty = ' '
        self.visited = '#'
        self.start = 'P'

    def get_node(self, node):
        if self.is_valid_node(node):
            return self.graph[node[0]][node[1]]

    def set_node(self, node, value):
        if self.is_valid_node(node):
            self.graph[node[0]][node[1]] = value

    def get_graph(self):
        return self.graph

    def is_valid_node(self, point):
        try:
            x = point[0]
            y = point[1]
            if self.graph[x][y]:
                return True
        except IndexError:
            return False

    def cost(self, point_a, point_b):
        '''Is accurate only when two points are 
        neighbors. Returns the cost, or raise IndexError'''
        try:
            if self.is_valid_node(point_a):
                pass
            if self.graph[point_a[0]][point_a[1]] != self.wall:
                pass
        except IndexError:
            return IndexError

        neighbor_b = self.neighbors(point_b)
        if point_a in neighbor_b:
            return 1

        raise IndexError

    def neighbors(self, point):
        '''point is in the form of [1,3]
        Returns the neighboring cells that are traversible
        '''
        # Not sure if raising an IndexError is the best strategy
        if self.is_valid_node(point):
                pass
        else:
            raise IndexError    

        x = point[0]
        y = point[1]
        # row first, column second (opposite of cartesian)
        right = [x, y+1]
        left = [x, y-1]
        up = [x-1, y]
        down = [x+1, y]
        temp = [right, left, up, down]
        result = []
        for i, cell in enumerate (temp):
            try:
                if self.graph[cell[0]][cell[1]] != self.wall:
                    # not going to do anything with the popped value
                    result.append(temp[i])
            except IndexError:
                pass
        return result
            

# Priority Queue for A Star structure
class PriorityQueue(object):
    '''Priority queue implemented with min heap (python's
    heapq data structure.
    '''
    def __init__(self):
        self.nodes = []
    
    def is_empty(self):
        if len(self.nodes) == 0:
            return True
        else:
            return False

    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))

    def pop(self):
        return heapq.heappop(self.nodes)[1]

    def show_queue(self):
        return self.nodes

