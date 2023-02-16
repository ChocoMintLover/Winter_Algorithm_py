from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)



def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    
    q = deque([[x,y]])
    temp = []

    visited[x][y] = 1
    while q:
        i, j = q.popleft()

        for idx in range(4):
            ni = i + dx[idx]
            nj = j + dy[idx]

            if 0 <= ni and ni < N and 0 <= nj and nj < N and visited[ni][nj] == 0:
                if space[x][y] > space[ni][nj] and space[ni][nj] != 0:
                    visited[ni][nj] =  visited[i][j] + 1
                    temp.append((visited[ni][nj] - 1, ni, nj))
                elif space[x][y] == space[ni][nj]:
                    visited[ni][nj] =  visited[i][j] + 1
                    q.append([ni,nj])
                elif space[ni][nj] == 0:
                    visited[ni][nj] =  visited[i][j] + 1
                    q.append([ni,nj])
                    
    return sorted(temp, key = lambda x: (x[0], x[1], x[2]))


cnt = 0
result = 0
size = [2, 0]
while 1:
    space[i][j] = size[0]
    shark = bfs(i,j)
    if len(shark) == 0:
        break
    step, nx,ny =shark.pop()
    
    result += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = nx, ny
print(result)