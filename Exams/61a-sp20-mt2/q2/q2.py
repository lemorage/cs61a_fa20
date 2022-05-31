email = 'example_key'

"""A: (3 pts) Implement is_power, which takes a positive integer base and a
non-negative integer s. It returns whether s is a power of base, meaning that there
is some non-negative integer n such that pow(base, n) equals s.

IMPORTANT: You may not call pow, use the ** operator, or import any function
(such as math.log). Your solution must be recursive.

Check the doctests with: python3 ok -q a
"""
def is_power(base, s):
    """Return whether s is a power of base.

    >>> is_power(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
    True
    >>> is_power(5, 1)    # pow(5, 0) = 1
    True
    >>> is_power(5, 5)    # pow(5, 1) = 5
    True
    >>> is_power(5, 15)   # 15 is not a power of 5 (it's a multiple)
    False
    >>> is_power(3, 9)
    True
    >>> is_power(3, 8)
    False
    >>> is_power(3, 10)
    False
    >>> is_power(1, 8)
    False
    >>> is_power(2, 0)    # 0 is not a power of any positive base.
    False

    >>> is_power(4, 16)
    True
    >>> is_power(4, 64)
    True
    >>> is_power(4, 63)
    False
    >>> is_power(4, 65)
    False
    >>> is_power(4, 32)
    False
    """
    assert base > 0 and s >= 0
    assert type(base) is int and type(s) is int
    if s == 1:
        return True
    elif base == 1 or s == 0 or s % base != 0:
        return False
    else:
        return is_power(base, s // base)


curry2 = lambda f: lambda x: lambda y: f(x, y)

"""B: (5 pts) Implement powers, a generator function which takes positive
integers n and k. It yields all integers m that are both powers of k and whose
digits appear in order in n.

Assume that is_power is implemented correctly.

Note: powers may yield its results in any order. The doctests below check what
is yielded, but not the order. The built-in sorted function used in the doctests
takes in an iterable object and returns a list containing the elements of the
iterable in non-decreasing order.

Check the doctests with: python3 ok -q b
"""
def powers(n, k):
    """Yield all powers of k whose digits appear in order in n.

    >>> sorted(powers(12345, 5))
    [1, 5, 25, 125]
    >>> sorted(powers(54321, 5))  # 25 and 125 are not in order
    [1, 5]
    >>> sorted(powers(2493, 3))
    [3, 9, 243]

    >>> sorted(powers(2493, 2))
    [2, 4]
    >>> sorted(powers(164352, 2))
    [1, 2, 4, 16, 32, 64]
    """
    def build(seed):
        """Yield all non-negative integers whose digits appear in order in seed.
        0 is yielded because 0 has no digits, so all its digits are in seed.
        """
        if seed == 0:
            yield 0
        else:
            for x in build(seed // 10):
                yield x
                yield 10 * x + seed % 10
    yield from filter(curry2(is_power)(k), build(n))

