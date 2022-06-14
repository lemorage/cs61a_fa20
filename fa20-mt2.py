# 1. Political Environment

def v(o, t, e):
  def m(y):
      nonlocal o
      o = [o, t]
  def n(o):
      o.append([e])
      o.append(o[:]) # list(o); o + []; [o[0], o[1]]
  m(e)
  n([t]) 
  e = 2

m = [3, 4]
v(m, 5, 6)



# 2. Yield, Fibonacci!

# (a)
def fibs(f):
    """Yield all Fibonacci numbers x for which f(x) is a true value.

    >>> odds = fibs(lambda x: x % 2 == 1)
    >>> [next(odds) for i in range(10)]
    [1, 1, 3, 5, 13, 21, 55, 89, 233, 377]
    >>> bigs = fibs(lambda x: x > 20)
    >>> [next(bigs) for i in range(10)]
    [21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    >>> evens = fibs(lambda x: x % 2 == 0)
    >>> [next(evens) for i in range(10)]
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]
    """
    n, m = 0, 1
    while True:
        if f(n):
            yield n
        n, m = m, n + m



# (b)
def filter_index(f, s):
    """Return a Link containing the elements of Link s that have an index i for
    which f(i) is a true value.

    >>> powers = Link(1, Link(2, Link(4, Link(8, Link(16, Link(32))))))
    >>> filter_index(lambda x: x < 4, powers)
    Link(1, Link(2, Link(4, Link(8))))
    >>> filter_index(lambda x: x % 2 == 1, powers)
    Link(2, Link(8, Link(32)))
    """
    def helper(i, s):
        if s is Link.empty:
            return s
        filtered_rest = helper(i+1, s.rest)
        if f(i):
            return Link(s.first, filtered_rest)
        else:
            return filtered_rest
    return helper(0, s)



# 3. Sparse Lists

def most_common(s):
    """Return the most common element in non-empty list s. In case of a tie,
    return the most common element that appears first in s.

    >>> most_common([3, 1, 4, 1, 5, 9])
    1
    >>> most_common([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    5
    >>> most_common([2, 7, 1, 8, 2, 8, 1, 8, 2, 8])
    8
    >>> most_common([3, 5, 7, 7, 7, 5, 5])
    5
    >>> most_common([3, 7, 5, 5, 7, 7])
    7
    """
    return max(set(s), key=s.count)


class SparseList:
    """Represent a non-empty list as a most common value and a dictionary from
    indices to values that contains only values that are not the most common.

    >>> pi = SparseList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> pi.common
    5
    >>> pi.others
    {0: 3, 1: 1, 2: 4, 3: 1, 5: 9, 6: 2, 7: 6, 9: 3}
    >>> [pi.item(0), pi.item(1), pi.item(2), pi.item(3), pi.item(4)]
    [3, 1, 4, 1, 5]
    >>> pi.item(10)
    5
    >>> pi.item(11)
    'out of range'
    >>> pi.items()
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    """
    def __init__(self, s):
        assert s, 's cannot be empty'
        self.n = len(s)
        self.common = most_common(s)
        self.others = { i: s[i] for i in range(self.n) if s[i] != self.common }
    
    def item(self, i):
        """Return s[i] or 'out of range' if i is not smaller than the length of s."""
        assert i >= 0, 'index i must be non-negative'
        if i >= self.n:
            return 'out of range'
        elif i in self.others:
            return self.others[i]
        else:
            return self.common

    def items(self):
        """Return a list with the same elements as s in the same order as s."""
        return [self.item(i) for i in range(self.n)]



# 4. Fork It

# (a)
def max_path(t):
    """Return the largest sum of labels along any path from the root to a leaf
    of tree t, which has positive numbers as labels.

    >>> a = tree(1, [tree(2), tree(3), tree(4, [tree(5)])])
    >>> max_path(a) # 1 + 4 + 5
    10
    >>> b = tree(6, [a, a, a])
    >>> max_path(b) # 6 + 1 + 4 + 5
    16
    """
    return label(t) + max([0] + [max_path(b) for b in branches(t)])



# (b)
def is_fork(t):
    """Return whether tree t is a fork.

    >>> is_fork(tree(1, [tree(2, [tree(3), tree(4), tree(5)])]))
    True
    >>> is_fork(tree(1, [tree(2, [tree(3)]), tree(4)]))
    True
    >>> is_fork(tree(1, [tree(2), tree(3), tree(4)]))
    True
    >>> is_fork(tree(1, [tree(2, [tree(3, [tree(5)]), tree(4, [tree(6)])])]))
    True
    >>> is_fork(tree(1))
    False
    >>> is_fork(tree(1, [tree(2, [tree(3)])]))
    False
    >>> is_fork(tree(1, [tree(2, [tree(3)]), tree(4, [tree(5), tree(6)])]))
    False
    >>> is_fork(tree(1, [tree(2, [tree(3, [tree(5, [tree(7), tree(8)]), tree(6)]), tree(4)])]))
    False
    """
    neck = slide(t)
    if is_leaf(neck):
        return False
    return all([is_leaf(slide(b)) for b in branches(neck)])

def slide(t):
    """Return the deepest node within tree t whose ancestors all have exactly one child.
    Definition: The ancestors of a node include its parent and the parents of all its ancestors.
    
    >>> deepest = slide(tree(1, [tree(2, [tree(3)])]))
    >>> label(deepest)
    3
    >>> label(slide(tree(1, [tree(2, [tree(3), tree(4)])])))
    2
    """
    while len(branches(t)) == 1:
        t = [slide(b) for b in branches(t)][0]
    return t


# (c)
def max_fork(t):
    """Return the largest sum of the labels in any fork contained in tree t,
    which has positive numbers as labels. If t contains no forks, return 0.

    >>> a = tree(1, [tree(2), tree(3), tree(4, [tree(5)])])
    >>> max_fork(a) # 1 + 2 + 3 + 4 + 5
    15
    >>> b = tree(6, [a, a, a])
    >>> max_fork(b) # 6+(1+4+5)+(1+4+5)+(1+4+5)
    36
    >>> c = tree(7, [tree(8), b, tree(9)])
    >>> max_fork(c) # 7+(6+(1+4+5)+(1+4+5)+(1+4+5))
    43
    >>> d = tree(9, [c])
    >>> max_fork(d) #9+7+(6+(1+4+5)+(1+4+5)+(1+4+5))
    52
    >>> max_fork(tree(1, [tree(2, [tree(3)])])) # No forks here!
    0
    """
    n = len(branches(t))
    if n == 0:
        return 0
    elif n == 1:
        below = max_fork(branches(t)[0])
        if below > 0:
            return label(t) + below
        else:
            return 0
    else:
        here = sum([max_path(b) for b in branches(t)])
        there = max([max_fork(b) for b in branches(t)])
        return label(t) + max(here, there)


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
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
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


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)