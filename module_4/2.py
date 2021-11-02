def insertion_sort(l):
    for i in range(1, len(l)):
        current_element = l[i]
        previous_index = i - 1
        while previous_index >= 0 and l[previous_index] > current_element:
            l[previous_index + 1] = l[previous_index]
            l[previous_index] = current_element
            previous_index -= 1
    return l


l2 = [34, 33, 666, 7]
print(insertion_sort(l2))
