import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def Input():
    n ,e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())
    return n, graph, v1, v2

def dijkstra(n, graph, start):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
    
def main():
    n, graph, v1, v2 = Input()
    distance0 = dijkstra(n, graph, 1)
    distance1 = dijkstra(n, graph, v1)
    distance2 = dijkstra(n, graph, v2)
    result = min(distance0[v1]+distance1[v2]+distance2[n],
        distance0[v2]+distance2[v1]+distance1[n])
    print(result) if result < INF else print(-1)

main()