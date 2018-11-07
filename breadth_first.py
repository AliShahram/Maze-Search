 #!/usr/bin/python
import copy
import sys
from collections import defaultdict
from data_structures import Tra_model, Stack, Queue
from state_rep import extractParams

big_list = []




# Take a .txt file, parses out the maze, and returns a 
# 2D representation of the array

def parser(file):
    file_open = open (file, "r")
        
    for line in file_open:
        line = line.strip("\n")
        line = list(line)
        big_list.append(line)

    return big_list       	#Returns the 2d array


#-------------------------------------------------------------------

# Single Breadth First Search
# Take the 2D array, and the position of the agent as an input 
# and returns the biglist with the path from 
# the agent to the prize marked with "#"
# It also returns a stack of the explored cells


def single_bfs(big_list, current):
    queue = Queue()
    explored = Queue()
    newExplored = Stack()
    seen = set()

    pointer = current

    queue.enqueue(pointer)       #Add the our initial position to the 
    explored.enqueue(pointer)       #queue
    tra_model = Tra_model()

    
    while True:

        if queue.isEmpty():
            break 
        else:
            pointer = queue.dequeue()
            # First move to the right and check what it is 
            pointer = tra_model.move_right(pointer)#make the first move
            x = pointer[0]
            y = pointer[1]
            
            if big_list[x][y] == " ":#if it is space, add its location
                queue.enqueue(pointer)
                explored.enqueue(pointer)
                big_list[x][y] = "#"
                pointer = tra_model.move_left(pointer)
            if big_list[x][y] == "%" or "#" :#if it is hardle, move back
                pointer = tra_model.move_left(pointer)

            if big_list[x][y] == ".":#if it is goal, add its location
                queue.enqueue(pointer)
                explored.enqueue(pointer)
                break

    # second move to the bottom and check what it is 

            pointer = tra_model.move_down(pointer)

            x = pointer[0]
            y = pointer[1]


            if big_list[x][y] == " ": #if it is space, add its location
                explored.enqueue(pointer)
                queue.enqueue(pointer)
                big_list[x][y] = "#"
                pointer = tra_model.move_up(pointer)
            if big_list[x][y] == "%" or "#" : #if it is hardle, move back
                pointer = tra_model.move_up(pointer)
            if big_list[x][y] == ".": #if it is goal, add its location
                queue.enqueue(pointer)
                explored.enqueue(pointer)
                break

    # Third move to the left and check what it is 

            pointer = tra_model.move_left(pointer)
            x = pointer[0]
            y = pointer[1]

            if big_list[x][y] == " ": #if it is space, add its location
                explored.enqueue(pointer)
                queue.enqueue(pointer)
                big_list[x][y] = "#"
                pointer = tra_model.move_right(pointer)
            if big_list[x][y] == "%" or "#": #if it is hardle, move back
                pointer = tra_model.move_right(pointer)
            if big_list[x][y] == ".":#if it is goal, add its location
                queue.enqueue(pointer)
                explored.enqueue(pointer)
                break

    # Fourth move to the left and check what it is 
           
            pointer = tra_model.move_up(pointer)
            x = pointer[0]
            y = pointer[1]

            if big_list[x][y] == " ": #if it is space, add its location
                explored.enqueue(pointer)
                queue.enqueue(pointer)
                big_list[x][y] = "#"
                pointer = tra_model.move_down(pointer)
            if big_list[x][y] == "%" or "#": #if it is hardle, move back
                pointer = tra_model.move_down(pointer)
            if big_list[x][y] == ".": #if it is goal, add its location
                queue.enqueue(pointer)
                explored.enqueue(pointer)
                break
        

    expanded = 0
    for i in explored.items:
        expanded += 1 


    steps = 0
    for item in explored.items:
        t = tuple(item)
        if t not in seen:
            steps += 1
            newExplored.push(item)
            seen.add(t)
    
    return newExplored, big_list, steps, expanded