N = int(input())
count = 0
for k in range(1, N+1):
    a = k // 100
    b = (k % 100) // 10
    c = (k % 100) % 10
    if 1 <= k < 100 or a - b == b - c:
        count += 1
print(count)
