fiboN = []
for i in range(91):
    fiboN.append(0)

def fibo(n):
    if n==0: return 0
    if n==1: return 1
    if fiboN[n] == 0:
        fiboN[n] = fibo(n-1) + fibo(n-2)
    return fiboN[n]

n = int(input())
print(fibo(n))
