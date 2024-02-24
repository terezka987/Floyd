import sys
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance)
    print(range(MAX_LENGTH))
    for intermediate, start_node,end_node in itertools.product (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        #print (intermediate,start_node,end_node)
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node] )
    #Any value that have sys.maxsize has no path
floyd(graph)