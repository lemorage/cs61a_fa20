# 1. Tree Recursion

def count_stair_ways(n):
    if n <= 2: return n
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0: return 1
    elif n < 0: 
        return 0
    else:
        # count_k(n-1, k) + count_k(n-2, k) + ... + count_k(n, k)
        i, total = 1, 0
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total

def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m) # count_partitions(n-m, min(m, n-m))
        without_m = count_partitions(n, m-1)
        return with_m + without_m


# 2. Lists

# 2.1
# >>> print(a[0], a[-1]) 
    # 1 3
# >>> len(a) 
    # 5
# >>> 2 in a 
    # False
# >>> 4 in a
    # True
# >>> a[3][0]
    # 2

# 2.2
def even_weighted(s): 
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(0, len(s)) if i % 2 == 0]

# 2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []: return 1
    else:
        return max(max_product(s[1:]), s[0]*max_product(s[2:]))


