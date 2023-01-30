import sys
INF = int(1e9)

def Input():
    n = int(sys.stdin.readline())
    premise = []
    for _ in range(n):
        a, b = sys.stdin.readline().rstrip().split(' is ')
        premise.append([ord(a)-97, ord(b)-97])
    m = int(sys.stdin.readline())
    conclusion = []
    for _ in range(m):
        a, b = sys.stdin.readline().rstrip().split(' is ')
        conclusion.append([ord(a)-97, ord(b)-97])
    return premise, conclusion

def linking(premise):
    graph = [[INF]*(26) for _ in range(26)]
    for i in range(26):
        for j in range(26):
            if i == j:
                graph[i][j] = 0
    for k in premise:
        graph[k[0]][k[1]] = 1
    return graph

def FloydWarshall(graph):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    return graph

def TrueOrFalse(conclusion, graph):
    for i in conclusion:
        if graph[i[0]][i[1]] != INF:
            print('T')
        else:
            print('F')

def main():
    premise, conclusion = Input()
    graph = linking(premise)
    graph = FloydWarshall(graph)
    TrueOrFalse(conclusion, graph)
main()