x = float(input())
y = float(input())
p = float(input())
count = 0
while x < y:
    x = x + x * (p / 100)
    count += 1
print(count)

