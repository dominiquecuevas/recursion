"""
1) A recursive algorithm must have a base case where data/parameter is exhausted.
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

def reverse_str(string):
    """
    Use recursion to reverse a string
    Other than slicing in reverse: string[-1::-1]
    """
    # base case is string length is equal to 1
    # index from end
    # make the new parameter a smaller slice of the string
    if len(string) == 1:
        return string[0]
    return string[-1] + reverse_str(string[:-1])

print("reverse_str('hello'):", reverse_str('hello'))

def is_palindrome(string):
    """
    returns True if a palindrome
    http://www.pythontutor.com/visualize.html#code=def%20is_palindrome%28string%29%3A%0A%20%20%20%20if%20len%28string%29%20%3C%3D1%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20elif%20string%5B0%5D%20!%3D%20string%5B-1%5D%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20is_palindrome%28string%5B1%3A-1%5D%29%0A%20%20%20%20%20%20%20%20%0Ais_palindrome%28'going'%29%0Ais_palindrome%28'hannah'%29&cumulative=false&curInstr=32&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
    """
    # base case is length of string is 1 or less returning True
    # check if end and beginning the same character
        # if equal, call function again recursively and return False if not
        # change state of parameter is string gets sliced at both ends

    if len(string) <= 1:
        return True

    elif string[0] != string[-1]:
        return False
    else:
    # tip: I was running into issues of the function returning None
    #       from not putting 'return' 
        return is_palindrome(string[1:-1])

print("is_palindrome('going'):", is_palindrome('going'))
print("is_palindrome('kayak'):", is_palindrome('kayak'))

def get_fibonacci_seq(length, fib=[0, 1]):
    # base case, if length is reached return
    # add numbers together, then append to sequence
    # return list, append each new sum
    if length < 1:
        return
    if length == 1:
        return [0]
    if len(fib) == length:
        return fib
    else:
        return get_fibonacci_seq(length, fib + [fib[-2] + fib[-1]])

print("get_fibonacci_seq(10):", get_fibonacci_seq(10))