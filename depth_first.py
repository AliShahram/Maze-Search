 #!/usr/bin/python


# Single Depth First Search
# Takes a 2D array and the position of the agent as input
#  and returns the biglist with a path from the agent
# to the prize marked as "#"
# It also returns a stack explored items in the path


import copy
import sys
from collections import defaultdict
from data_structures import Tra_model, Stack, Queue
from state_rep import extractParams


def single_dfs(big_list, current):
    stack = Stack()
    explored = Queue()
    pointer = current

    stack.push(pointer)
    explored.enqueue(pointer)
    tra_model = Tra_model()

    while True:

        if stack.isEmpty():
            break
        else:
            pointer = stack.peek()


        x = pointer[0]
        y = pointer[1]
        if big_list[x][y + 1] == " ": #if right is empty
            pointer = tra_model.move_right(pointer)
            stack.push(pointer)
            explored.enqueue(pointer)
            x = pointer[0]
            y = pointer[1]
            big_list[x][y] = "#"
            continue #return to the top of the loop

        if big_list[x][y + 1] == ".":
            pointer = tra_model.move_right(pointer)
            stack.push(pointer)
            explored.enqueue(pointer)
            break

        if big_list[x][y + 1] == "%" or "#":#if right is wall
            if big_list[x + 1][y] == " ":#if down is empty
                pointer = tra_model.move_down(pointer)
                stack.push(pointer)
                explored.enqueue(pointer)
                x = pointer[0]
                y = pointer[1]
                big_list[x][y] = "#"
                continue


            if big_list[x + 1][y] == ".":
                pointer = tra_model.move_down(pointer)
                stack.push(pointer)
                explored.enqueue(pointer)
                break


            if big_list[x + 1][y] == "%" or "#": # if down is wall
                if big_list[x - 1][y] == " ": # if up is empty

                    pointer = tra_model.move_up(pointer)
                    stack.push(pointer)
                    explored.enqueue(pointer)
                    x = pointer[0]
                    y = pointer[1]
                    big_list[x][y] = "#"
                    continue # return to the top of the loop

                if big_list[x - 1][y] == ".":
                    pointer = tra_model.move_up(pointer)
                    stack.push(pointer)
                    explored.enqueue(pointer)
                    break


                if big_list[x - 1][y] == "%" or "#": #if up is wall
                    if big_list[x][y - 1] == " ": #if left is empty
                        pointer = tra_model.move_left(pointer)
                        stack.push(pointer)
                        explored.enqueue(pointer)
                        x = pointer[0]
                        y = pointer[1]
                        big_list[x][y] = "#"
                        continue #return to the top

                    if big_list[x - 1][y] == ".":
                        pointer = tra_model.move_left(pointer)
                        stack.push(pointer)
                        explored.enqueue(pointer)
                        break
                    if big_list[x][y - 1] == "%" or "#":
                        big_list[x][y] = "*"
                        stack.pop()


    expanded = 0
    for i in explored.items:
        expanded += 1
        x = i[0]
        y = i[1]

        if big_list[x][y] == "*":
           big_list[x][y] = " "

    steps = 0
    for i in explored.items:
        x = i[0]
        y = i[1]

        if big_list[x][y] == "#":
            steps += 1

    return explored, big_list, steps, expanded

        

