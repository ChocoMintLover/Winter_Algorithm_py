import sys

def Input():
    n, k = map(int, sys.stdin.readline().split())
    history = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        history[a][b] = 1
    s = int(sys.stdin.readline())
    events = []
    for _ in range(s):
        c, d = map(int, sys.stdin.readline().split())
        events.append((c, d))
    return n, history, events

def FloydWarshall(n, history):
    for i in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if history[a][i] == 1 and history[i][b] == 1:
                    history[a][b] = 1
    return history

def verification(history, events):
    for e in events:
        if history[e[0]][e[1]] == 1:
            print(-1)
        elif history[e[1]][e[0]] == 1:
            print(1)
        else:
            print(0)

def main():
    n, history, events = Input()
    history = FloydWarshall(n, history)
    verification(history, events)

main()