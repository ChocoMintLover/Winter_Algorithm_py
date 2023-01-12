N = int(input())
cnt = 0
wrong = [1, 2, 4, 7]
now3 = [3, 6, 9, 12]

while(N != 0):
    if N in wrong:
        cnt = -1
        break
    if N in now3:
        N -= 3
    else:
        N -= 5
    cnt += 1
print(cnt)