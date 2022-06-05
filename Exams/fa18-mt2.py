###################
# DEFINED CLASSES #
###################

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
    <5, 7, <8, 9>>
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
            string += str(self.first) + ', '
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


# 1. A/B Test

x = [1, 2]
class A: 
    x = 3
    y = 4
    def __init__(self, y):
        self.a = y
        self.x = b
        self.__str__ = lambda: str(y)

    def __str__(self):
        return 'BB'

class B(A):
    x = [5, 6]
    def __init__(self, y):
        self.a = x[1]
        y[1] = 8

b = B(x)
a = A(6)

def dash(x):
    return print(self.x)

elastigirl = Link(7, Link(8))
elastigirl.first = elastigirl.rest

"""
Expression | Interactive Output
>>> [c.a for c in [a, b]]
[6, 2]
>>> print(a.x, b.x)
BB [5, 6]
>>> print(b.y, x)
4 [1, 8]
>>> a.__str__() # override in __init__
'6'
>>> dash(b) # no self is found
Error
>>> print(elastigirl)
<<8>, 8>
"""



# 2. Lowest

def lowest(s):
    """Return a list of the elements in s with the smallest absolute value.

    >>> lowest([3, -2, 2, -3, -4, 2, 3, 4])
    [-2, 2, 2]
    >>> lowest(range(-5, 5))
    [0]
    """
    return (lambda y: [x for x in s if abs(x) == y])(abs(min(s, key=abs)))



# 3. Hocus Pocus
# ...... SKIP ......



# 4. Nonplussed

# (a)
def plus(n):
    """Return the largest sum that results from inserting +'s into n.

    >>> plus(123456)    # 12 + 34 + 56 = 102
    102
    >>> plus(1604)    # 1 + 60 + 4 = 65
    65
    >>> plus(160450)    # 1 + 60 + 4 + 50 = 115
    115
    """
    if n:
        return max(plus(n // 10) + n % 10, plus(n // 100) + n % 100)
    return 0
    


# (b)
def plusses(n, cap):
    """Return the number of plus expressions for n with values below cap.

    >>> plusses(123, 16)  # 1+2+3=6 and 12+3=15, but 1+23=24 isn't below cap.
    2
    >>> plusses(2018, 38) # 2+0+1+8, 20+1+8, 2+0+18, and 2+01+8, but not 20+18.
    4
    >>> plusses(1, 2)
    1
    """
    if n < 10 and cap > n:
        return 1
    elif cap <= 0:
        return 0
    else:
        return plusses(n // 10, cap - n % 10) + plusses(n // 100, cap - n % 100)
    


# 5. Midterm Elections

# (a)
class Poll:
    s = []

    def __init__(self, n):
      self.name = n
      self.votes = {}
      Poll.s.append(self)

    def vote(self, choice):
      self.votes[choice] = self.votes.get(choice, 0) + 1

def tally(c):
    """Tally all votes for a choice c as a list of (poll name, vote count) pairs.

    >>> a, b, c = Poll('A'), Poll('B'), Poll('C')
    >>> c.vote('dog')
    >>> a.vote('dog')
    >>> a.vote('cat')
    >>> b.vote('cat')
    >>> a.vote('dog')
    >>> tally('dog')
    [('A', 2), ('C', 1)]
    >>> tally('cat')
    [('A', 1), ('B', 1)]
    """
    return [(p.name, p.votes[c]) for p in Poll.s if c in p.votes]



# (b)
class Crooked(Poll):
  """A poll that ignores every other call to vote.

  >>> d = Crooked('D')
  >>> for s in ['dog', 'cat', 'dog', 'cat', 'cat']:
  ...     d.vote(s)
  >>> d.votes
  {'dog': 2, 'cat': 1}
  """
  record = True
  def vote(self, choice):
      if self.record:
          Poll.vote(self, choice)
      self.record = not self.record



# 6. Dr. Frankenlink

def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.

    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        return replace(s.rest, t, i-1, j-1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
        end = t
        while end.rest != Link.empty: # find the last element in t
            end = end.rest
        s.rest, end.rest = t, s.rest # connect two parts together



# 7. Trictionary or Treat

def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    
    >>> k = Tree(5, [Tree(7, [Tree(2)]), 
    ...              Tree(8, [Tree(3), Tree(4)]),
    ...              Tree(5, [Tree(4), Tree(2)])])
    >>> v = Tree('Go', [Tree('C', [Tree('C')]),
    ...                 Tree('A', [Tree('S'), Tree(6)]),
    ...                 Tree('L', [Tree(1), Tree('A')])])
    >>> [f(v) for f in lookups(k, 2)]
    ['C', 'A']
    >>> [f(v) for f in lookups(k, 3)]
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    if k.label == key:
        yield lambda v: v.label
    for i in range(len(k.branches)):
        for lookup in lookups(k.branches[i], key):
            yield new_lookup(i, lookup)

def new_lookup(i, f): # Assuming: f is a lookup funcion for a branch of v.
    def g(v):
        return f(v.branches[i])
    return g