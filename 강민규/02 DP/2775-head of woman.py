from collections import defaultdict
house = defaultdict(list)

def AddPeople(floor, ho): #floor층의 ho호수에 맞는 인원 추가하는 함수
    for i in range(1, ho+1):
        if house[floor-1][i] == 0:
            AddPeople(floor-1, i)
        house[floor][ho] += house[floor-1][i] #(floor-1)층의 (1~ho)호수 인원의 합을 floor층의 ho호수에 추가

N = int(input())
answer = []
for n in range(N):
    floor = int(input())
    ho = int(input())
    answer.append(0)

    for i in range(15): #0층 기본설정
        house[0].append(i)
    for i in range(1, floor): #입력 층만큼의 공간 할당
        house[i] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(1, ho+1):
        if house[floor-1][i] == 0:
            AddPeople(floor-1, i)
        answer[n] += house[floor-1][i]
        
for n in range(N):
    print(answer[n])
