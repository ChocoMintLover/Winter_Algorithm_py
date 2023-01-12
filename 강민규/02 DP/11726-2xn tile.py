from math import factorial as ft

n = int(input())
way = 0
col = n
row = 0

while(col >= 0):
    way += ft(row+col) / (ft(col)*ft(row)) #같은 것이 있는 순열
    print(f"col : {col} || row : {row} || sum of ways : {way} || way : {ft(row+col)/(ft(col)*ft(row))}")
    col -= 2
    row += 1

print(int(way)%10007)

# 21  -> 7704
# 22  -> 8643
# 100 -> 4955
# 777 -> 1037