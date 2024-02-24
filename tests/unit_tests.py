import unittest
import sys
import pprint

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
        self.assertEqual(imperative_result, recursive_result)

    def test_recursive_function_small(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, 3, NO_PATH],
            [0, 0, 5],
            [2, NO_PATH, 4]]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
        self.assertEqual(imperative_result, recursive_result)

    def test_recursive_function_negative_weights(self):
        pp = pprint.PrettyPrinter(indent=4)

        NO_PATH = sys.maxsize
        graph = [[0, -4, NO_PATH],
            [0, 0, -4],
            [-2, NO_PATH, 4]]

        imperative_result = imperative_floyd.floyd(graph)
        recursive_result = recursive_floyd.recursive_floyd(graph)
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
        self.assertEqual(imperative_result, recursive_result)

if __name__ == '__main__':
    unittest.main()