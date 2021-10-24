# 45674
n = int(input())
s = 0
while n != 0:
    c = n % 10
    s += c
    n = n // 10
    n = round(n)

print(s)
