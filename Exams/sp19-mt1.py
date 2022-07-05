# 1. What Would Python Display

n = 1
f = lambda: n 
g = f
n = 2

x, y, loops = 0, 21, 0
while y:
    loops += 1
    if x <= y:
        if x % 2 == 1:
            x, y = y, x
        elif x == 0:
            x += (2 ** 2)
        else:
            x = x + 3
        y = y // 2
    else:
        y = 0

def foo(bar, z):
    def bar(w):
        z = w + 2
        return z
    print(bar(z)) # call the inner
    print(z)
    return bar

"""
>>> print(1, print(print(2), 3 or 4 // 0))
2
None 3
1 None
>>> g()
2
>>> x
10
>>> loops
4
>>> foo(lambda m: m + 1, 4)(7)
6
4
9
"""



# 3. Zip It

def make_zipper(f1, f2, sequence):
    """ Return a function of f1 and f2 composed based on sequence.
    >>> def increment(x):
    ...     return x + 1
    >>> def square(x):
    ...     return x * x
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
    2
    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 → 4 → 5 → 6
    6
    >>> sqincsqinc = make_zipper(increment, square, 2121)
    >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 → 3 → 9 → 10 → 100
    100
    """
    zipper = lambda x: x
    helper = lambda f, g: lambda x: f(g(x)) 
    while sequence:
        if sequence % 10 == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)
        sequence = sequence // 10
    return zipper