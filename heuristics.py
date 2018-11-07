import math

def cartDist(a, b):
    '''Returns the cartesian distance between point a and b.
    points are a list of two integers, e.g, [1,3]'''
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    x = (x1 - x2) * (x1 - x2)
    y = (y1 - y2) * (y1 - y2)

    result = math.sqrt(x + y)
    return result

def manDist(a, b):
    '''Returns the manhattan distance between point a and b.
    points are a list of two integers, e.g, [1,3]'''
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    x = abs(x1 - x2)
    y = abs(y1 - y2)

    result = x + y
    return result 
