# 1. Mutater-tot

def ready(betty): 
	print(len(betty))
	betty[0].append(betty)
	return betty [0:1]

def get_set(s):
	ready(s)
	return s.pop()

def go(on, up):
	if up:
		return go(on[0], up-1)
	else:
		return on

f = [1, [2]]
g = [[3, 4], [5], 6]
h = [g, g]

"""
Expression | Interactive Output
>>> h[1].pop()
6
>>> g[g[1][0]-g[0][1]] # g[1]
[5]
>>> len(ready(g)) # [[3, 4, [[...], [5]]]]
1
>>> g[0][2][0][1]
[5]
>>> ready(get_set(h))[0][0]
2
4
3
>>> [len(go(h, k)) for k in range(3)]
[1, 4, 3]
"""



# 2. Vulcans
#  ...... SKIP ......



# 3. Will Code for Points

# (a)
def objectify(t):
	"""Return a Tree instance equivalent to a tree represented as a list.

	>>> m = tree(2)
	>>> m
	[2]
	>>> objectify(m)
	Tree(2)
	>>> r = tree(3, [tree(4, [tree(5), tree(6)]), tree(7, [tree(8)])])
	>>> r
	[3, [4, [5], [6]], [7, [8]]]
	>>> objectify(r)
	Tree(3, [Tree(4, [Tree(5), Tree(6)]), Tree(7, [Tree(8)])])
	"""
	return Tree(label(t), [objectify(b) for b in branches(t)])

# (b)
# Answer: Θ(n)



# (c)
def closest(t):
	"""Return the smallest difference between an entry and the sum of the
	entries of its branches.

	>>> t = Tree(8, [Tree(4), Tree(3)])
	>>> closest(t) # |8 - (4 + 3)| = 1
	1
	>>> closest(Tree(5, [t])) # Same minimum as t
	1
	>>> closest(Tree(10, [Tree(2), t])) # |10 - (2 + 8)| = 0
	0
	>>> closest(Tree(3)) # |3 - 0| = 3
	3
	>>> closest(Tree(8, [Tree(3, [Tree(1, [Tree(5)])])])) # |3 - 1| = 2
	2
	>>> sum([])
	0
	"""
	diff = abs(t.label - sum([b.label for b in t.branches]))
	return min([diff] + [closest(b) for b in t.branches])



# (d)
def double_up(s):
	"""Mutate s by inserting elements so that each element is next to an equal.
	>>> s = Link(3, Link(4))
	>>> double_up(s) # Inserts 3 and 4
	2
	>>> s
	Link(3, Link(3, Link(4, Link(4))))
	>>> t = Link(3, Link(4, Link(4, Link(5))))
	>>> double_up(t) # Inserts 3 and 5
	2
	>>> t
	Link(3, Link(3, Link(4, Link(4, Link(5, Link(5))))))
	>>> u = Link(3, Link(4, Link(3)))
	>>> double_up(u) # Inserts 3, 4, and 3
	3
	>>> u
	Link(3, Link(3, Link(4, Link(4, Link(3, Link(3))))))
	"""
	if s is Link.empty:
		return 0
	elif s.rest is Link.empty:
		s.rest = Link(s.first)
		return 1
	elif s.first == s.rest.first:
		return double_up(s.rest.rest)
	else:
		s.rest = Link(s.first, s.rest)
		return 1 + double_up(s.rest.rest)



# 4. What color is it?

# (a)
class Dress:
	"""What color is the dress?
	>>> blue = Dress('blue')
	>>> blue.look()
	'blue'
	>>> gold = Dress('gold')
	>>> gold.look()
	'gold'
	>>> blue.look() # 2 does not evenly divide 3; changes to gold 
	>>> Dress('black').look()
	'black'
	>>> gold.look() # 2 does not evenly divide 5; changes to black
	>>> gold.look() # 3 evenly divides 6
	'black'
	>>> Dress('white').look()
	'white'
	>>> gold.look() # 4 evenly divides 8
	'black'
	>>> blue.look() # 3 evenly divides 9
	'gold'
	"""
	seen = 0
	color = None

	def __init__(self, color):
		self.color = color
		self.seen = 0

	def look(self):
		Dress.seen += 1
		self.seen += 1
		if not (Dress.seen % self.seen):
			Dress.color = self.color
			return self.color
		else:
			self.color = Dress.color



# (b)
def decrypt(s, d):
	"""List all possible decoded strings of s.
	>>> codes = {
	... 'alan': 'spooky',
	... 'al': 'drink',
	... 'antu': 'your',
	... 'turing': 'ghosts',
	... 'tur': 'scary',
	... 'ing': 'skeletons',
	... 'ring': 'ovaltine'
	... }
	>>> decrypt('alanturing', codes)
	['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
	"""
	if s == '':
		return []
	ms = []
	if s in d:
		ms.append(d[s])
	for k in range(1, len(s)-1): # if there're not two parts, then no work to do with it. so instead of range(0, len(s))
		first, suffix = s[:k], s[k:]
		if first in d:
			for rest in decrypt(suffix, d):
				ms.append(d[first] + " " + rest)
	return ms


##############################
# NO FURTHER QUESTIONS BELOW #
##############################

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