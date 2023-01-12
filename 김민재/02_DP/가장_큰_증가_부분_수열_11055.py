n = int(input())
a = list(map(int, input().split()))
DP = [0] * n

for i in range(n):
    DP[i] = a[i]

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            DP[i] = max(DP[i], DP[j] + a[i])
print(max(DP))