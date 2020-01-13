"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""
    # base case - when empty list
    # print zenith index
    # return call self with smaller slice of list
    if not lst:
        return
    zenith, remaining = lst[0], lst[1:]
    if isinstance(zenith, list):
        print_recursively(zenith)
    else:
        print(lst[0])
    print_recursively(remaining)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")
