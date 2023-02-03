INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

# 수행된 결과를 출력
for a in graph:
    print(*a)