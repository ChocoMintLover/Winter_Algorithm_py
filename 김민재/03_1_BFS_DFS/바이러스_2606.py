from collections import deque

def dfs(idx):
    visited[idx] = 1
    for node in mp[idx]:
        if visited[node] == 0:
            dfs(node)

n = int(input())
e = int(input())

mp = [[] * n for i in range(n + 1)]
q = deque([])
visited = [0] * (n + 1)

for i in range(e):
    a, b = map(int, input().split())
    mp[a].append(b)
    mp[b].append(a)

dfs(1)

print(sum(visited) - 1)