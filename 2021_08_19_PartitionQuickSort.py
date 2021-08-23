# Partition

def partition(array, start, end):  # inplace partition
    # no need
    # if (end - start + 1) == 1:
    #    return 0
    pivot = array[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= end:
            if array[i] > pivot:
                break
            i += 1
        while j > start:
            if array[j] < pivot:
                break
            j -= 1
        if i < j:  # i == j case never exists
            array[i], array[j] = array[j], array[i]
        else:
            break

    # swap with pivot with j
    array[start], array[j] = array[j], array[start]

    return j


def qSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        qSort(array, start, pivot - 1)
        qSort(array, pivot + 1, end)


def qSort2(array, start, end):
    if start < end:
        pivot = partition2(array, start, end)
        qSort2(array, start, pivot - 1)
        qSort2(array, pivot + 1, end)


def partition2(array, start, end):
    index = start  # check from left to right to find small
    small = start  # the position to be replaced by small
    pivot = array[end]
    while index < end:
        if array[index] < pivot:
            if small != index:
                array[small], array[index] = array[index], array[small]
            small += 1
        index += 1
    # swap small and end
    array[small], array[end] = array[end], array[small]
    return small


a = [6, 2, 3, 1, 25, 11, 77]
b = a[0:]
print(qSort(a, 0, len(a) - 1))
print(a)
print("=====")
print(b)
print(qSort2(b, 0, len(b) - 1))
print(b)
