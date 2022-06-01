# 1. What Would Python Display

class C:
    x = 'e'

    def f(self, y):
        self.x = self.x + y
        return self

    def __str__(self):
        return 'go'

class Big(C):
    x = 'u'

    def f(self, y):
        C.x = C.x + y
        return C.f(self, 'm')

    def __repr__(self):
        return '<bears>'

m = C().f('i')
n = Big().f('o')
"""
Expression | Interactive Output
>>> [m.x, n.x]
['ei', 'um']
>>> [C.f(n, 'a').x, C().x]
['uma', 'eo']
>>> print(m, n)
go go
>>> n
<bears>
"""

def g(y):
    def h(x):
    	nonlocal h
    	k = 2
    	if len(x) == 1:
    		h = lambda x: y
    		k = 1
    	return [-x[0]] + h(x[k:])
    	return h(y)

py = {3: {5: [7]}}
thon = {5: 6, 7: py}
thon[7][3] = thon

q = range(3, 5)
r = iter(q)
code = [next(r), next(iter(q)), list(r)]

"""
Expression | Interactive Output
>>> g([3, 4, 5])
[-3, -5, 3, 4, 5]
>>> py[3][5]
6
>>> code
[3, 3, [4]]
"""



# 3. Max Tree

# (a)
def max_tree(t, key):
	"""Return the label n of t for which key(n) returns the largest value.

	>>> t = Tree(6, [Tree(3, [Tree(5)]), Tree(2), Tree(4, [Tree(7)])])
	>>> max_tree(t, key=lambda x: x)
	7
	>>> max_tree(t, key=lambda x: -x)
	2
	>>> max_tree(t, key=lambda x: -abs(x - 4))
	4
	"""
	if t.is_leaf():
		return t.label
	x = t.label
	for b in t.branches:
		m = max_tree(b, key)
		if key(m) > key(x):
			x = m
	return x



# (b)
def max_tree(t, key):
    """Return the label n of t for which key(n) returns the largest value.
	
	>>> t = Tree(6, [Tree(3, [Tree(5)]), Tree(2), Tree(4, [Tree(7)])])
	>>> max_tree(t, key=lambda x: x)
	7
	>>> max_tree(t, key=lambda x: -x)
	2
	>>> max_tree(t, key=lambda x: -abs(x - 4))
	4
    """
    return max([t.label] + [max_tree(b, key) for b in t.branches], key=key)



# 4. Seek Once

def stable(s, k, n):
    """Return whether all pairs of elements of S within distance K differ by at most N.
    
    >>> stable([1, 2, 3, 5, 6], 1, 2)  # All adjacent values differ by at most 2.
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2)  # abs(5-2) is a difference of 3.
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2)  # abs(5-1) is a difference of 4.
    False
    """
    for i in range(len(s)):
        near = range(max(0, i-k), i) # to check elements backwards only, or forwards only
        if any([abs(s[i]-s[j]) > n for j in near]):
            return False
    return True



# 5. Do You Yield?

# (a)
def partitions(n, m):
	"""Yield all partitions of N using parts up to size M.

	>>> list(partitions(1, 1))
	['1']
	>>> list(partitions(2, 2))
	['2', '1 + 1']
	>>> list(partitions(4, 2))
	['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
	>>> for p in partitions(6, 4):
	...		print(p)
	4 + 2
	4 + 1 + 1
	3 + 3
	3 + 2 + 1
	3 + 1 + 1 + 1
	2 + 2 + 2
	2 + 2 + 1 + 1
	2 + 1 + 1 + 1 + 1
	1 + 1 + 1 + 1 + 1 + 1
	"""
	if n == m:
	  yield str(m)
	if n > 0 and m > 0:
	  for p in partitions(n-m, m):
	      yield str(m) + ' + ' + str(p)
	  yield from partitions(n, m-1)

# (b)
# Answer: Linear



# 6. Best of Both

def switch(s, t, k):
	"""Return the list with the largest sum built by switching between S and T at most K times.
	
	>>> switch([1, 2, 7], [3, 4, 5], 0)
	[1, 2, 7]
	>>> switch([1, 2, 7], [3, 4, 5], 1)
	[3, 4, 5]
	>>> switch([1, 2, 7], [3, 4, 5], 2)
	[3, 4, 7]
	>>> switch([1, 2, 7], [3, 4, 5], 3)
	[3, 4, 7]
	""" 
	if k == 0 or len(s) == 0:
		return s
	else:
	 a = switch(t, s, k-1)
	 b = s[:1] + switch(s[1:], t[1:], k)
	 return max(a, b, key=sum)



# 7. Version 2.0

class Version:
    """A version of a string after an edit.

    >>> s = Version('No power?', Delete(3, 6))
    >>> print(Version(s, Insert(3, 'class!')))
    No class!
    >>> t = Version('Beary', Insert(4, 'kele'))
    >>> print(t)
    Bearkeley
    >>> print(Version(t, Delete(2, 1)))
    Berkeley
    >>> print(Version(t, Delete(4, 5)))
    Bear
    """
    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit
    def __str__(self):
        return self.edit.apply(str(self.previous))

class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c

class Insert(Edit):
    def apply(self, t):
        """Return a new string by inserting string c into t starting at position i."""
        return t[:self.i] + self.c + t[self.i:]

class Delete(Edit):
    def apply(self, t):
        """Return a new string by deleting c characters from t starting at position i."""
        return t[:self.i] + t[self.i+self.c:]



# 8. Their Mascot is a Tree?!?

def layer(t, d):
    """Return a linked list containing all labels of Tree T at depth D.
    >>> a_tree = Tree(1, [Tree('b', [Tree('mas')]),
    ...                   Tree('a', [Tree('co')]),
    ...                   Tree('d', [Tree('t', [Tree('!')])])])
    >>> print(layer(a_tree, 0))
    <1>
    >>> print(layer(a_tree, 1))
    <b a d>
    >>> print(layer(a_tree, 2))
    <mas co t>
    >>> print(layer(a_tree, 3))
    <!>
    """
    return helper(t, d, Link.empty)

def helper(t, d, s):
	if d == 0:
		return Link(t.label, s)
	else:
		for b in reversed(t.branches):
			s = helper(b, d-1, s)
		return s


##############################
# NO FURTHER QUESTIONS BELOW #
##############################

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

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s)
    <6 7>
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
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

