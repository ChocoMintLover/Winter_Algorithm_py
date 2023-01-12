n = int(input())
t = [0] * n
p = [0] * n
DP = [0] * (n + 1)

for i in range(n):
    t[i], p[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(i):
        if j + t[j] <= i:
            DP[i] = max(DP[i], DP[j] + p[j])
print(DP[n])