def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    return s


print(area(6, 3, 5))