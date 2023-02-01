import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def Input():
    count = 0
    while True:
        count += 1
        n = int(input())
        if n == 0:
            break
        cave = []
        for _ in range(n):
            cave.append(list(map(int, input().split())))
        Dijkstra(n, cave, count)

def Dijkstra(n, cave, count):
    distance = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    distance[0][0] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        cost, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                ncost = cost + cave[nx][ny]
                if ncost < distance[nx][ny]:
                    distance[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx, ny))

Input()