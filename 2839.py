s = int(input())
a = int(s//5)
k = int(s%5)
b = int(k//3)
if s % 5 == 0:
    print(int(s/5))
elif s%5 != 0 and k%3 == 0:
    print(int(a+b))
elif s%5 != 0 and s != 4 and k%3 == 1:
    print(int(a-1+b+2))
elif s%5 != 0 and s != 7 and k%3 == 2:
    print(int(a-2+b+4))
else:
    print("-1")
