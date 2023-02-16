from math import inf

N, R = map(int, input().split())
cities = set(input().split())
N = len(cities)
ctoi = {city: i for i, city in enumerate(cities)}
M = int(input())
root = list(map(lambda x: ctoi[x], input().split()))

free = ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun']
half = ['S-Train', 'V-Train']

graph = [[inf] * N for _ in range(N)]
graph_t = [[inf] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    typee, s, e, cost = input().split()
    s_index = ctoi[s]
    e_index = ctoi[e]
    cost = int(cost)

    # 티켓 X
    graph[s_index][e_index] = min(graph[s_index][e_index], cost)
    graph[e_index][s_index] = min(graph[e_index][s_index], cost) 
        
    # 티켓 O
    if typee in free:
      cost = 0
    elif typee in half:
      cost /= 2
    graph_t[s_index][e_index] = min(graph_t[s_index][e_index], cost)
    graph_t[e_index][s_index] = min(graph_t[e_index][s_index], cost)


for k in range(N):
    graph[k][k] = 0
    graph_t[k][k] = 0
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            graph_t[i][j] = min(graph_t[i][j], graph_t[i][k] + graph_t[k][j])


graph_Cost = graph_t_Cost = 0
for i in range(M - 1):
    graph_Cost += graph[root[i]][root[i+1]]
    graph_t_Cost += graph_t[root[i]][root[i+1]]


if graph_Cost > graph_t_Cost + R:
    print('Yes') 
else: print('No')
