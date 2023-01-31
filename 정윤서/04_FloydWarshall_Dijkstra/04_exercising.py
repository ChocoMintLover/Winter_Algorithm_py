import sys
INF = int(1e9)

def Input():
    v, e = map(int, sys.stdin.readline().split())
    matrix = [[INF]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        matrix[a][b] = c
    return v, matrix

def FloydWarshall(v, matrix):
    for i in range(1, v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                matrix[a][b] = min(matrix[a][b], matrix[a][i] + matrix[i][b])
    return matrix

def isCycle(v, matrix):
    ans = INF
    for i in range(1, v+1):
        ans = min(ans, matrix[i][i])
    return ans

def main():
    v, matrix = Input()
    matrix = FloydWarshall(v, matrix)
    ans = isCycle(v, matrix)
    print(-1) if ans == INF else print(ans)

main()