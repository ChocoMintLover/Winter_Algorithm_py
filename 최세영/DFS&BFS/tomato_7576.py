from collections import deque

m, n = map(int, input().split())
graph = []
 
for i in range(n):
    graph.append(list(map(int, input().split())))

print(graph)
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

dy = [0 ,0, 1, -1]
dx = [1, -1, 0 ,0]


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
    ans = max(ans, max(line))
print(ans-1)