scorelist = []
for _ in range(5): #5번 돌린다는 뜻으로 이해
    score = input()
    scorelist.append(int(score))

total = 0
for score in scorelist:
    if score < 40:
        score = 40
    total += score

print(int(total/5))
