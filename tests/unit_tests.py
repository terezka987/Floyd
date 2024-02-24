import unittest
import sys
import pprint
import random

from src import recursive_floyd
from src import imperative_floyd

class TestStringMethods(unittest.TestCase):
    
    def test_recursive_function_example(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]]
        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        pp.pprint(imperative_result)
        pp.pprint(recursive_result)
        self.assertEqual(imperative_result, recursive_result)

    def test_recursive_function_small(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, 3, NO_PATH],
            [0, 0, 5],
            [2, NO_PATH, 4]]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        pp.pprint(imperative_result)
        pp.pprint(recursive_result)
        self.assertEqual(imperative_result, recursive_result)

    def test_recursive_function_negative_weights(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, -4, NO_PATH],
            [0, 0, -4],
            [-2, NO_PATH, 4]]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        pp.pprint(imperative_result)
        pp.pprint(recursive_result)
        self.assertEqual(imperative_result, recursive_result)


    def test_recursive_function_big(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, 3, NO_PATH,4,4,1],
            [0, 0, 5,3,NO_PATH,4],
            [2, NO_PATH, 4,NO_PATH,NO_PATH,NO_PATH],
            [0, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,2]
            ]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        pp.pprint(imperative_result)
        pp.pprint(recursive_result)
        self.assertEqual(imperative_result, recursive_result)

    def test_recursive_function_very_big(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [
            [0, 3, NO_PATH,4,4,1,0, 3, NO_PATH,4,4,1],
            [0, 0, 5,3,NO_PATH,4,0, 0, 5,3,NO_PATH,4],
            [2, NO_PATH, 4,NO_PATH,NO_PATH,NO_PATH,0, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,4,3, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,4,0, 4, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,2,0, 0, 5,3,NO_PATH,2],
            [0, 3, NO_PATH,4,4,1,0, 3, NO_PATH,4,4,1],
            [0, 0, 5,3,NO_PATH,4,0, 0, 5,3,NO_PATH,4],
            [2, NO_PATH, 4,NO_PATH,NO_PATH,NO_PATH,0, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,4,3, 0, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,4,0, 4, 5,3,NO_PATH,4],
            [0, 0, 5,3,NO_PATH,2,0, 0, 5,3,NO_PATH,2]
            ]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        pp.pprint(imperative_result)
        pp.pprint(recursive_result)
        self.assertEqual(imperative_result, recursive_result)

    # def test_recursive_function_ge(self):
    #     pp = pprint.PrettyPrinter(indent=4)
    #     MAX_LENGTH = 4
    #     MAX_RANDOM = 9
    #     NO_PATH = sys.maxsize
    #     graph = [[None] * 4] * 4
    #     pp.pprint(graph)
    #     for start_node in range(MAX_LENGTH):
    #         for end_node in range(MAX_LENGTH):
    #             # print('a')
    #             # print(end_node)
    #             # print('b')
    #             # print(random.randint(0, 9))
    #             weight = random.randint(0, 9)
    #             if weight == 9:
    #                 weight = NO_PATH
    #             print(start_node,end_node)
    #             graph[start_node][end_node] = weight
    #     pp.pprint(graph)
    #     #imperative_result = imperative_floyd.floyd(graph)
    #     #recursive_result = recursive_floyd.recursive_floyd(graph)
    #     #pp.pprint(imperative_result)
    #     #pp.pprint(recursive_result)
    #     #self.assertEqual(imperative_result, recursive_result)

if __name__ == '__main__':
    unittest.main()