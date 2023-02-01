import sys

def Input():
    t = int(sys.stdin.readline())
    for _ in range(t):
        testcase()

def testcase():
    n = int(sys.stdin.readline())
    home = tuple(map(int, sys.stdin.readline().split()))
    convenience_store = []
    for _ in range(n):
        convenience_store.append(tuple(map(int, sys.stdin.readline().split())))
    festival = tuple(map(int, sys.stdin.readline().split()))
    linking(n, home, convenience_store, festival)

def linking(n, home, convenience_store, festival):
    graph = [[0]*(n+2) for _ in range(n+2)]
    coordinate = []
    coordinate += [home] + convenience_store + [festival]
    """for i, c in enumerate(coordinate):
        if i == n+1:
            break
        if (abs(c[0] - coordinate[i+1][0]) + abs(c[1] - coordinate[i+1][1])) <= 1000:
            graph[i][i+1] = 1"""
    for i in range(n+2):
        if i == n+1:
            break
        if (abs(coordinate[i][0] - coordinate[i+1][0]) + abs(coordinate[i][1] - coordinate[i+1][1])) <= 1000:
            graph[i][i+1] = 1
    
    FloydWarshall(n, graph)
    
def FloydWarshall(n, graph):
    for i in range(n+2):
        for a in range(n+2):
            for b in range(n+2):
                if graph[a][b] == 1 or (graph[a][i] == 1 and graph[i][b] == 1):
                    graph[a][b] = 1
    result(n, graph)

def result(n, graph):
    if graph[0][n+1] == 1:
        print("happy")
    else:
        print("sad")

Input()