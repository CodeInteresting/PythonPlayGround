# Quick Sort


def quick_sort(array):
    if len(array) < 2:
        return array[0:]  # don't do in place update, so copy
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    larger = [x for x in array[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(larger)


print(quick_sort([32, 1, 4, 0, 27, 11, 8]))
