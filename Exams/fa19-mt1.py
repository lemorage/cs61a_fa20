# 3. You Again

def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)

def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)

def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola)  # parabola(4) == parabola(5)
    5
    >>> again(vee)       # vee(1) == vee(3)
    3
    """
    n = 1
    while n:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m = m + 1
        n = n + 1



# 4. Ups and Downs

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# (a)
def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.

    >>> ramp(123)   # 2 increases (1 -> 2, 2 -> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1 -> 3, 1 -> 5) and 1 decrease (3 -> 1)
    True
    >>> ramp(176)   # 1 increases (1 -> 7) and 1 decrease (7 -> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decrease
    False
    """
    n, last, tally = n // 10, n % 10, 0
    while n:
        n, last, tally = n // 10, n % 10, tally + sign(n%10 - last)
    return True if tally else False


# (b)
def over_under(y):
    """Return a function that takes X and returns:
        -1 if X is less than Y
        0 if X is equal to Y
        1 if X is greater than Y
    >>> over_under(5)(3)  # 3 < 5
    -1
    >>> over_under(5)(5)  # 5 == 5
    0
    >>> over_under(5)(7)  # 7 > 5
    1
    """
    return lambda x: sign(x-y)


def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT."""
    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()


# (c)
def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.
    >>> f, g = ups(3)
    >>> process(1200849, f, g)    # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)      # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)  # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)          # 0 increases
    False
    """
    def f(left, right):
       return ups(min(k, k + sign(left - right)))
    return f, lambda: k == 0


# (d)
def at_most(n, k):
    """Return whether non-negative integer N has at most K increases.
    >>> at_most(567, 3)
    True
    >>> at_most(567, 2)
    True
    >>> at_most(567, 1)
    False
    """
    result = False
    while k >= 0:
       a, b = ups(k)
       k, result = k - 1, result or process(n, a, b)
    return result