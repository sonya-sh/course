from random import randint
n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
mx = m[0][0]
for i in range(n):
    for el in m[i]:
        mx = max(mx, el)

print(mx)