import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dijkstra():
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print('Problem {0}: {1}'.format(count, distance[x][y]))
            return

        for i in range(4):
            cost_x = x + dx[i]
            cost_y = y + dy[i]

            if 0 <= cost_x < n and 0 <= cost_y < n:
                cost_new = cost + graph[cost_x][cost_y]

                if cost_new < distance[cost_x][cost_y]:
                    distance[cost_x][cost_y] = cost_new
                    heapq.heappush(q, (cost_new, cost_x, cost_y))


count = 1
while 1:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for i in range(n)]
    distance = [[INF]*n for i in range(n)]
    dijkstra()

    count += 1
