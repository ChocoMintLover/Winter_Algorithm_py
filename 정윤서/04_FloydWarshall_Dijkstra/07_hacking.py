import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def Input():
    testcases = int(input())
    for _ in range(testcases):
        n, d, c = map(int, input().split())
        cps = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            cps[b].append((a, s))
        dijkstra(n, c, cps)
        
def dijkstra(n, start, cps):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in cps[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    result(distance)

def result(distance):
    last = 0
    count = 0
    for d in distance:
        if d != INF:
            count += 1
            last = max(last, d)
    print(count, last)

Input()