#!/usr/bin/python

import sys
import collections as c

def eq_orderfree(list1, list2):
    """Check whether two lists contains the same elements regardless of the
       order. We convert the lists into tuple and then to set.
       use collections.Counter function
    """
    set1 = set(map(tuple, list1))
    set2 = set(map(tuple, list2))

    if c.Counter(set1) == c.Counter(set2):
        return True
    else:
        return False

def parser(file):
    """Parse the file containing the maze, return a 2D list that represents
       the maze. 
       #TODO: add error handling         
    """
    file_open = open (file, "r")
    big_list = []

    for line in file_open:
        line = line.strip("\n")
        line = list(line)
        big_list.append(line)

    return big_list

def extractParams (array_2d):
    '''Given an array, this function extract
       the environment variables to make a representation of the world
    
       - # of prizes    
       - starting point (P)
       - prize locations (.)
    '''
    # do some checking (try?)
    number_prizes = 0
    prize_locations = []
    # starting point not found yet (default =  (-inf, -inf))
    # first index refers to line number
    # second index refers to char in the line
    starting_point = [[-99999,-99999]]

    for (line_idx, line) in enumerate (array_2d):
        for (point_idx, point) in enumerate(line):
            if point == '.':
                number_prizes += 1 
                prize_locations.append([line_idx, point_idx])
            elif point == 'P':
                starting_point[0][0] = array_2d.index(line)
                starting_point[0][1] = line.index(point)
            else:
                pass
    return {
            'prizes': number_prizes,
            # starting point is a 1-d list
            'start': starting_point[0],
            'loc_prizes': prize_locations
    }
  
def goalTest(sample, ideal):
    """
    sample is the state we are wanting to examine. ideal is the goal state.
    """
    for goal in ideal:
        print ("goal in question is {}".format(goal))
        if isinstance (ideal[goal], int):
            print ("Within the try block")
            # for comparing integer
            if ideal[goal] != sample[goal]:
                print ("they int/single arrays are not matching")
                print (ideal[goal], sample[goal])
                return False
            else:
                print ("The int/list matched")
                pass
            # for comparing 2-d lists
        elif isinstance(ideal[goal], list):
            print ("There is a typeerror, mean it's a 2d list")
            print (ideal[goal], sample[goal])
            if eq_orderfree(ideal[goal], sample[goal]) != True:
                print ("Equality function returned false")
                print (ideal[goal], sample[goal])
                return False
            else:
                pass
                print ("Equality function returned true")
    print ("All things traversed. All goals are matched")
    return True

def main():
    try:
        in_file = sys.argv[1]
        parsed = parser(in_file)
        ideal = extractParams(parsed)
        goalTest (ideal, ideal)
    except IndexError as e:
        print ("python state_rep.py MAZE_FILENAME\n")
        exit
            
if __name__ == "__main__":
    main()
