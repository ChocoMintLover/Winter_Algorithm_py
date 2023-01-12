t = int(input())

def DP(floor, room):
    if floor == 0:
        return room
    sum = 0
    for i in range(1, room + 1):
        sum += DP(floor - 1, i)
    return sum

for i in range(t):
    k = int(input())
    n = int(input())
    print(DP(k, n))