INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (26) for _ in range(26)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(n):
    l = input().split()
    x = ord(l[0]) - ord('a')
    y = ord(l[2]) - ord('a')
    graph[x][y] = 1
    # print(x, y)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(26):
    for a in range(26):
        for b in range(26):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

m = int(input())
# 수행된 결과를 출력
for i in range(m):
    l = input().split()
    x = ord(l[0]) - ord('a')
    y = ord(l[2]) - ord('a')
    # 도달할 수 없는 경우,F라고 출력
    if graph[x][y] >= 1e9:
        print("F")
    # 도달할 수 있는 경우 T 출력
    else:
        print("T")