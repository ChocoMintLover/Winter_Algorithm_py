import sys
input = sys.stdin.readline

def Input():
    m, n = map(int, input().split())
    maps = []
    for _ in range(m):
        maps.append(list(map(int, input().split())))
    return m, n, maps

def dfs(x, y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if maps[x][y] > maps[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n, maps = Input()
dp = [[-1 for _ in range(n)] for _ in range(m)]
print(dfs(0,0))