import sys

input = sys.stdin.readline

def Input():
    n, m = map(int, input().split())
    state = []
    for _ in range(n):
        lt = list(input().rstrip())
        lt2 = [ord(a) - 65 for a in lt]
        state.append(lt2)
    return n, m, state

def dfs(x, y, dots, visited):
    global state

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and state[y][x] == state[ny][nx]:
            if dots < 3:
                if not (nx,ny) in visited:
                    dfs(nx, ny, dots+1, visited + [(nx,ny)])
            else:
                if not (nx,ny) in visited:
                    dfs(nx, ny, dots+1, visited + [(nx,ny)])
                else:
                    if visited[0] == (nx,ny):
                        print("Yes")
                        sys.exit()

n, m, state = Input()
for i in range(n):
    for j in range(m):
        dfs(j, i, 1, [(j,i)])
print('No')