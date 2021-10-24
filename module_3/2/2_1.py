l = [1, 5, 4, 1, 'a']
m = []
for i in range(len(l)):
    if l[i] not in m:
        m.append(l[i])
print(m)
