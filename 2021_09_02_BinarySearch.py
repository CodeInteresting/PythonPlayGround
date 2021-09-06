# Binary Search

# [] intervals
def binary_search(array, target_num):
    """
    Binary Search
    return -1 if not found.
    return index if found.
    """
    left = 0
    right = len(array) - 1
    while left <= right:  # Exit when the interals become empty []
        mid = left + (right - left) // 2  # Remember to use // instead of /
        if array[mid] == target_num:
            return mid
        elif array[mid] > target_num:  # [left, mid - 1]
            right = mid - 1
        elif array[mid] < target_num:  # [mid + 1, right]
            left = mid + 1
    return -1


a = [1, 2, 2, 2, 3, 7, 9, 12]
print(binary_search(array=a, target_num=11))


# left bound search [) (half-open)
def binary_search_left(nums, target):
    left = 0
    right = len(nums)
    while left < right:  # [)
        mid = left + (right - left) // 2
        if nums[mid] == target:  # [left, mid)
            right = mid
        elif nums[mid] > target:  # [left, mid)
            right = mid
        elif nums[mid] < target:  # [mid + 1, right)
            left = mid + 1
    # Exit when left == right
    if left == len(nums):  # exceeds the right bound
        return -1
    if nums[left] != target:
        return -1
    return left


print(binary_search_left(nums=a, target=2))


# Right bound [) (half-open)
def binary_search_right(nums, target):
    left = 0
    right = len(nums)
    while left < right:  # [left, right)
        mid = left + (right - left) // 2
        if nums[mid] == target:  # [mid + 1, right)
            left = mid + 1
        elif nums[mid] > target:  # [left, mid)
            right = mid
        elif nums[mid] < target:  # [mid + 1, right)
            left = mid + 1

    # exit when left == right

    if (left - 1) < 0:
        return -1

    if nums[left - 1] != target:
        return -1
    return left - 1


print(binary_search_right(nums=a, target=2))


# left bound [ ] (full-close)
def binary_search_left2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:  # [left, mid - 1]
            right = mid - 1
        elif nums[mid] > target:  # [left, mid - 1]
            right = mid - 1
        elif nums[mid] < target:  # [mid + 1, right]
            left = mid + 1

    if (left < len(nums)) and (nums[left] == target):
        return left
    return -1


# right bound [ ] (full-close)
def binary_search_right2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:  # [mid + 1, right]
            left = mid + 1
        elif nums[mid] > target:  # [left, mid - 1]
            right = mid - 1
        elif nums[mid] < target:  # [mid + 1, right]
            left = mid + 1

    # exit when left > right

    # right >= 0 instead of right > 0
    if (right >= 0) and (nums[right] == target):
        return right
    return -1
