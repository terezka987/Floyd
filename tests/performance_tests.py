import sys
import timeit


from src import recursive_floyd
from src import imperative_floyd

NO_PATH = sys.maxsize

graph_2 = [[0, 7],
            [NO_PATH, 0],
            ]

graph_4 = [[0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]]

graph_8 = [
    [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8],
            [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8]
            ]

graph_10 = [
    [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8, 10, 7],
            [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8, 10, 7],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8, 10, 7]
            ]

graph_16 = [
    [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
                [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, 0, 2,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8,0, 7, NO_PATH, 8]
            ]
imperative_times = {}
recursive_times = {}

time = timeit.timeit(lambda: imperative_floyd.floyd(graph_2), number= 1)
imperative_times[2] = f'{time:.20f}'

time = timeit.timeit(lambda: imperative_floyd.floyd(graph_4), number= 1)
imperative_times[4] = f'{time:.20f}'

time = timeit.timeit(lambda: imperative_floyd.floyd(graph_8), number= 1)
imperative_times[8] = f'{time:.20f}'

time = timeit.timeit(lambda: imperative_floyd.floyd(graph_10), number= 1)
imperative_times[10] = f'{time:.20f}'

time = timeit.timeit(lambda: imperative_floyd.floyd(graph_16), number= 1)
imperative_times[16] = f'{time:.20f}'

time = timeit.timeit(lambda: recursive_floyd.recursive_floyd(graph_2), number= 1)
recursive_times[2] = f'{time:.20f}'

time = timeit.timeit(lambda: recursive_floyd.recursive_floyd(graph_4), number= 1)
recursive_times[4] = f'{time:.20f}'

time = timeit.timeit(lambda: recursive_floyd.recursive_floyd(graph_8), number= 1)
recursive_times[8] = f'{time:.20f}'

time = timeit.timeit(lambda: recursive_floyd.recursive_floyd(graph_10), number= 1)
recursive_times[10] = f'{time:.20f}'

print 'imperative_times'
print(imperative_times)
print 'recursive_times'
print(recursive_times)
