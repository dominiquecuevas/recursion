"""
1) A recursive algorithm must have a base case.
    condition allows algorithm to stop recursing
    problem small enough to solve directly
2) A recursive algorithm must change its state and move toward the base case.
    data or parameter gets smaller, like shortening a list
3) A recursive algorithm must call itself, recursively.
"""

def sum_nums(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def sum_nums_rec(nums):
    if len(nums) == 0:
        return 1
    return nums[0] + sum_nums_rec(nums[1:])

def get_factorial(num):
    # 1) base case to reduce to smallest data
    if num <= 1:
        return 1
    # 2) change its state, subtract 1
    # 3) call itself
    return num * get_factorial(num-1)

nums = [1, 3, 5, 7, 9]
print("sum_nums_rec(nums):", sum_nums_rec(nums))
print("get_factorial(4):", get_factorial(4))