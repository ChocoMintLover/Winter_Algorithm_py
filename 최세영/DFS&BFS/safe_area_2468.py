from collections import deque
 
n = int(input())
graph = []
 
for i in range(n):
    graph.append(list(map(int, input().split())))

l = []
for i in range(n):
    l.append(max(graph[i]))
max_n = max(l)

def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]
 
result = 0
for i in range(max_n): 
    visited = [[0] * n for i in range(n)]
    cnt = 0
 
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0: 
                bfs(j, k, i, visited)
                cnt += 1
 
    if result < cnt:
        result = cnt
 
print(result)