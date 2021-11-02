def binary_search(l, x):
    i = 0
    j = len(l)-1
    m = int(j/2)
    while l[m] != x and i < j:
        if x > l[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
    if i > j:
        return 'Нет такого'
    else:
        return m


l1 = [5, 7, 87, 7, 47, 888, 99]
print(binary_search(l1, 7))
