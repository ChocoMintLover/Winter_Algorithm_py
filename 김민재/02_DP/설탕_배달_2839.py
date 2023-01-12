n = int(input())
DP = [0] * (5001)

MM = 5001

DP[1] = MM
DP[2] = MM
DP[3] = 1
DP[4] = MM
DP[5] = 1

for i in range(6, n + 1):
    DP[i] = min(DP[i - 3] + 1, DP[i - 5] + 1)

if DP[n] >= MM:
    print(-1)
else:
    print(DP[n])