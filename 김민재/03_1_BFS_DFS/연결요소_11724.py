from collections import deque

def dfs(idx):
    visited[idx] = 1
    for node in mp[idx]:
        if visited[node] == 0:
            dfs(node)

n, e = map(int, input().split())

mp = [[] * n for i in range(n + 1)]
q = deque([])
visited = [0] * (n + 1)

for i in range(e):
    a, b = map(int, input().split())
    mp[a].append(b)
    mp[b].append(a)

c_cnt = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        c_cnt += 1
print(c_cnt)