# 剑指 offer: 面试题 51: 数字中的重复的数字
# 题目：在一个长度为n的数组的所有数字都在0到n-1的范围内。
# 数组中的某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复数字。
# 例如，如果输入长度为7的数组{2，3，1，0，2，5，3}，那么对应的输出是重复的数字2或者3


# 利用hashtable
def return_any_duplicate_num(nums):
    nums_occurs = {}
    dup_nums = []
    is_Dup_Exist = False
    for num in nums:
        nums_occurs[num] = nums_occurs.get(num, 0) + 1

    for num, occurs in nums_occurs.items():
        if occurs > 1:
            dup_nums.append((num, occurs))

    is_Dup_Exist = True if len(dup_nums) > 0 else False

    return is_Dup_Exist, dup_nums


print(return_any_duplicate_num([2, 3, 1, 0, 2, 5, 3]))


# return the first found duplicate
# in place change
def return_first_duplicate_num(nums):
    for i in range(len(nums)):
        m = nums[i]
        while i != m:  # m is not in right position
            if m == nums[m]:  # try to place m to right position
                return True, m  # The place is already occupied
            else:
                tmp = nums[m]
                nums[m] = m
                m = tmp
        nums[i] = m
    return False, None


print(return_first_duplicate_num([2, 3, 1, 0, 2, 5, 3]))
