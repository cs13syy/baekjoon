n = input() # str으로 입력값을 받는다
counting = [0 for _ in range(10)] # 0이 10개 들어있는 리스트를 만든다, 이후 인덱스를 이용한다
# print(counting)
# for 문에서 in 다음에 들어갈 수 있는 형태는 리스트, 튜플, 문자열
for num in n: # 숫자 n은 현재 str, n의 문자가 차례로 for 문에 들어간다
    counting[int(num)] += 1 # counting 리스트의 인덱스를 이용해, 숫자 a의 경우 a번째 요소에 1을 더한다
# 예를 들어, n의 첫번째 자리 숫자가 3이면, counting 리스트의 3번째 요소에 1이 더해진다
result = "" # 빈 문자열 생성
for i in range(9, -1, -1): # 9부터 -1까지(-1 포함X) -1씩 더해지는 반복 가능한 객체로 리턴, 내림차순 정렬
    result += str(i) * counting[i] # counting 리스트에서 i번째 요소가 0이라면 result에 포함되지 않는다
print(result)
