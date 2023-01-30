import sys

def Input():
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    return n, matrix

def FloydWarshall(n, matrix):
    for i in range(n):
        for a in range(n):
            for b in range(n):
                if matrix[a][b] == 1 or (matrix[a][i] == 1 and matrix[i][b] == 1):
                    matrix[a][b] = 1
    return matrix

def main():
    n, matrix = Input()
    matrix = FloydWarshall(n, matrix)
    for m in matrix:
        line = [str(a) for a in m]
        print(' '.join(line))

main()