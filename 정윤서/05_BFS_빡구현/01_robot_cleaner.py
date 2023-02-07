import sys
from collections import deque

input = sys.stdin.readline

def Input():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    area = []
    not_cleaned = 0
    for _ in range(n):
        lt = list(map(int, input().split()))
        area.append(lt)
        not_cleaned += sum(lt)
    return n, m, r, c, d, area

def BFS(n, m, r, c, d, area):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append((r, c, d))
    area[c][r] = 2
    cnt = 1
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nd = (d + i) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < m and 0 <= ny < n and area[ny][nx] == 0:
                area[ny][nx] = 2
                q.append((nx, ny, nd))
                cnt += 1
                if i == 3:
                    if area[ny - dy[nd]][nx - dx[nd]] == 1:
                        print(cnt)
                        return
                    else:
                        q.append((nx - dx[nd], ny - dy[nd], nd))
                break
    print(cnt)

n, m, r, c, d, area = Input()
BFS(n, m, r, c, d, area)