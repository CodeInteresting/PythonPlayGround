# Selection Sort

list_a = [44, 33, 21, 34, -1, 5, 99]


# in-place sort
def select_sort(some_list):
    length = len(some_list)
    for i in range(length - 1):
        # find smallest and swap
        # list[i] is smallest place
        min = i
        for j in range(i + 1, length):
            if some_list[j] < some_list[min]:
                min = j
        some_list[i], some_list[min] = some_list[min], some_list[i]


select_sort(list_a)
print(list_a)
