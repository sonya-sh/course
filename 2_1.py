a = int(input())
b = int(input())
c = int(input())
r = (a == b) + (a == c) + (b == c)
if r == 1:
    print('2')
else:
    print(r)

