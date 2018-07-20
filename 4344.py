N = int(input())                   #입력값을 정수로 받는다
for k in range(N):                 #N의 각 행에 대한 반복문
    T = input().split()             #T에 대한 정의. 입력값을 리스트화
    nT = []                         #nT는 빈 리스트임을 선언
    for x in T:                    #T의 인덱스 x에 대한 반복문
        nT.append(int(x))           #T의 인덱스 x를 정수화 시켜 리스트에 넣어라
    nT.pop(0)                       #nT에서 학생 수 버리고 성적만 남긴 리스트
    m = sum(nT) / len(nT)           #성적 다 더해서 학생 수로 나눈 게 평균
    count = 0                       #count 정의 (평균 보다 점수 높은 학생 수 구하기 위해)
    for i in nT:                    #nT의 인덱스 i에 대한 반복문
        if i > m:                   #인덱스 i가 평균 m보다 클 경우에 대한 조건문
            count += 1              #리스트에 있는 인덱스가 평균보다 높으면 count
    rate = count / len(nT) * 100    #비율은 평균 초과 학생수 / 전체 학생 수 * 100
    print("%0.3f" % rate + "%")    #소수점 넷째자리에서 반올림하여 출력
