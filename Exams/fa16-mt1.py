# 3. Countizard

# (a)
def counter(d):
    """Return a function of N that returns the number of times D appears in N.

    >>> counter(8)(8018)
    2
    >>> counter(0)(2016)
    1
    >>> counter(0)(0)
    0
    """
    def count(n):
        k = 0
        while n:
            n, last = n // 10, n % 10
            if last == d:
                k += 1
        return k
    return count



# (b)
def significant(n, k):
    """Return the K most significant digits of N.

    >>> significant(12345, 3)
    123
    >>> significant(12345, 7)
    12345
    """
    if n < pow(10, k):
        return n
    return significant(n // 10, k)



# 4. Caterepeat

# (a)
def repeat_sum(f, x, n):
    """Compute the following summation of N+1 terms, where the last term
    calls F N times: x + f(x) + f(f(x)) + f(f(f(x))) + ... + f(f(...f(x)))

    >>> repeat_sum(lambda x: x*x, 3, 0) # 3
    3
    >>> repeat_sum(lambda x: x*x, 3, 1) # 3 + 9
    12
    >>> repeat_sum(lambda x: x+2, 3, 4) # 3 + 5 + 7 + 9 + 11
    35
    """
    total, k = 0, 0
    while k <= n:
        total = total + x
        x = f(x)
        k = k + 1
    return total



# (b)
def sum_squares(n):
    """Return the sum of the first N perfect squares.

    >>> sum_squares(0)
    0
    >>> sum_squares(3) # 1**2 + 2**2 + 3**2
    14
    >>> sum_squares(5) # 1**2 + 2**2 + 3**2 + 4**2 + 5**2
    55
    """
    f = lambda x: pow(round(pow(x, 0.5) + 1), 2)
    return repeat_sum(f, 0, n)



# 5. Multikarp

# (a)
def multiadder(n):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7)
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6)
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    """
    assert n > 0
    if n == 1:
        return lambda x: x
    else:
        return lambda a: lambda b: multiadder(n-1)(a+b)



# (b)
def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

compose1(multiadder(4)(1000), multiadder(3)(1000)(10))(1)(2)(3)