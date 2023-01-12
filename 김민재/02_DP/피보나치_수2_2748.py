n = int(input())
DP = [0] * 91

def pibo(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    if DP[num] != 0:
        return DP[num]
    DP[num] = pibo(num - 1) + pibo(num - 2)
    return DP[num]


print(pibo(n))