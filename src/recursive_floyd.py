import sys
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

# MAX_LENGTH = len(graph)
def recursive_floyd(distance):
    """
    Recursive implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance)
    def return_min(start_node, end_node, intermediate):
        if intermediate < 0:
            return distance[start_node][end_node]
        return min(
            return_min(start_node, end_node, intermediate - 1),
            return_min(start_node, intermediate, intermediate - 1) + return_min(intermediate, end_node, intermediate - 1)
        )
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            for intermediate in range(MAX_LENGTH):
                distance[start_node][end_node] = return_min(start_node, end_node, intermediate)
recursive_floyd(graph)