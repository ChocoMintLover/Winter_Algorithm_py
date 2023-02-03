import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_distance, next_node in graph[now]:
            cost = dist + next_distance
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
        
    count = 0
    time = 0

    for i in distance:
        if i != INF:
            count += 1
            time = max(time, i)
    print(count, time)


test = int(input())

for _ in range(test):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n+1)]
    
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    
    dijkstra(c)