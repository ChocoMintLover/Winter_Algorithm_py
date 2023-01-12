N = int(input())
time = [0]
price = [0]
total = []

def IsItPossible(day):
    if day + time[day] <= N+1:  return 1
    else:                       return 0

def FindMaxPrice(day, sum):
    while day <= N:
        tmpD = day
        tmpS = sum
        if(IsItPossible(day)):
            #상담 O
            sum += price[day]
            day += time[day]
            FindMaxPrice(day, sum)
            #상담 X
            day = tmpD
            sum = tmpS
            day += 1
        else:
            day += 1
    total.append(sum)

for i in range(N):
    tmp = list(map(int, input().split()))
    time.append(tmp[0])
    price.append(tmp[1])
FindMaxPrice(1, 0)
print(max(total))