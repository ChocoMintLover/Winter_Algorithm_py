n = int(input())
t = [0] * n
p = [0] * n
DP = [0] * (n + 1)

for i in range(n):
    t[i], p[i] = map(int, input().split())

DP[n] = 0
if t[n - 1] == 1:
    DP[n - 1] = p[n - 1]
else:
    DP[n - 1] = 0

for i in range(n - 2, -1, -1):
    if i + t[i] <= n:
        DP[i] = max(DP[i + 1], p[i] + DP[i + t[i]])
    else:
        DP[i] = DP[i + 1]

print(DP[0])