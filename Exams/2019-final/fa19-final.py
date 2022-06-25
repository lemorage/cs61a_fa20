# 1. What Would Python Display

def again(x):
    def again(y):
        nonlocal x
        x = x - y
        return x
    return again(x) + x

n = sum([again(z) for z in range(9)])
s = [[i] for i in range(3)]
s.append(s)

for t in list(s):
    t.extend(range(3, 5))

class A:
    b = 'one'
    def __init__(self, a):
        f = self.a
        self.a = a[1:]
        self.b = 'two'
        f(a)

    def a(self, b):
        print([b, type(self).b])

    def __repr__(self):
        return str(self.a)

class B(A):
    b = 'three'
    def a(self, c):
        A.a(self, self.b)

f = lambda g, h: lambda p, q: h(g(q), p)
g = f(lambda half: half // 2, pow)
"""
>>> print([1].append(2))
None
>>> n
0
>>> len(s)
6
>>> s[1]
[1, 3, 4]
>>> A('four')
['four', 'one']
our
>>> B('five')
['two', 'three']
ive
>>> g(3, 5) # pow(5 // 2, 3)
8
"""



# 3. The Price is Right

def winner(price):
    """Return a function that takes a list and returns the largest element not above price.
    
    >>> ipad = winner(499)                  # the iPad actual price is $499
    >>> ipad([500, 600, 200, 1, 350, 299])  # the closest guess that doesn't go over is $350
    350
    """
    return lambda guesses: max(filter(lambda g: g <= price, guesses))



# 4. Big Leaf

def tops(t):
    """Yield the leaf labels of Tree t at the end of increasing paths.

    >>> ex = Tree(1, [Tree(2), Tree(5, [Tree(1, [Tree(3)])]), Tree(3, [Tree(4), Tree(1)])])
    >>> list(tops(ex))
    [2, 4]
    >>> list(tops(Tree(1)))
    [1]
    >>> list(tops(Tree(1, [Tree(3, [Tree(2)])])))
    []
    """
    if t.is_leaf():
       yield t.label
    else:
        for b in t.branches:
            if b.label > t.label:
                yield from tops(b)



# 5. To-Do Lists

class TodoList:
    """A to-do list that tracks the number of completed items in the list and overall.

    >>> a, b = TodoList(), TodoList()
    >>> a.add(Todo('Laundry'))
    >>> t = Todo('Shopping')
    >>> a.add(t)
    >>> b.add(t)
    >>> print(a)
    Remaining: ['Laundry', 'Shopping'] ; Completed in list: 0 ; Completed overall: 0
    >>> print(b)
    Remaining: ['Shopping'] ; Completed in list: 0 ; Completed overall: 0
    >>> t.complete()
    >>> print(a)
    Remaining: ['Laundry'] ; Completed in list: 1 ; Completed overall: 1
    >>> print(b)
    Remaining: [] ; Completed in list: 1 ; Completed overall: 1
    >>> Todo('Homework').complete()
    >>> print(a)
    Remaining: ['Laundry'] ; Completed in list: 1 ; Completed overall: 2
    """
    def __init__(self):
        self.items, self.complete = [], 0
    def add(self, item):
        self.items.append(item)
        item.lists.append(self)
    def remove(self, item):
        self.complete += 1
        self.items.remove(item)
    def __str__(self):
        return ('Remaining: ' + str([item.task for item in self.items]) +
                ' ; Completed in list: ' + str(self.complete) +
                ' ; Completed overall: ' + str(Todo.done))
class Todo:
    done = 0
    def __init__(self, task):
        self.task, self.lists = task, []
    def complete(self):
        Todo.done += 1
        for t in self.lists:
            t.remove(self)



# 6. Palindromes

# (a)
def pal(n):
    """Return a palindrome starting with n.

    >>> pal(12430)
    1243003421
    """
    m = n
    while m:
        n, m = n * 10 + m % 10 , m // 10
    return n

# (b)
def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.

    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)

# (c)
def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.

    >>> biggest_palindrome(3425534)
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    return big(n, 0)

def big(n, k):
    """A helper function for biggest_palindrome."""
    if n == 0:
        return 0
    choices = [big(n // 10, k), big(n // 10, 10 * k + n % 10)]
    if contains(k, n):
       choices.append(pal(k))
    return max(choices)

# (d)
# Answer: Linear

# (e)
def palinkdrome(n):
    """Return a function that returns a palindrome starting with the args of n repeated calls.
    >>> print(palinkdrome(3)(5)(6)(7))
    <5 6 7 7 6 5>
    >>> print(palinkdrome(1)(4))
    <4 4>
    """
    return outer(Link.empty, n)

def outer(r, n):
    def inner(k):
        s = Link(k, r)
        if n == 1:
            t = s
            while s is not Link.empty:
                t, s = Link(s.first, t), s.rest
            return t
        else:
            return outer(s, n-1)
    return inner


##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Link:
    """A linked list.
    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
        

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches