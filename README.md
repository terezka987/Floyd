# Resursive floyd vs imperative

This project is for comparing a given imperative version of Floyd-Warshall algorithm with an implemented recursive version.

## Prerequisites
```
pip install -r requirements.txt
```

## Usage
To use the functions in your code
```
from src import recursive_floyd
from src import imperative_floyd
imperative_result = imperative_floyd.floyd(graph)
recursive_result = recursive_floyd.recursive_floyd(graph)
```
## Testing
### Unit tests
The last test is a bit slow so it can be uncommented if your machine hangs
```
python3 -m unittest tests/unit_tests.py
```
### performance testing
This outputs 2 dict with dimension of graph as key and time taken as value
```
python3 -m unittest tests/performance_tests.py
```