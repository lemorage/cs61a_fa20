# 1. Buggy Quidditch
class Ball:
    points = 0
    time = lambda: 'Draco'

    def score(self, who):
        print(who, self.points)

    def __str__(self):
        return 'Magic'

class Snitch(Ball):
    points = 100
    time = lambda: 'Harry'

    def __init__(self):
        self.points = self.points + 50

    def score(self, p):
        if not time():
            print(Ball().score(p))
        else:
            Ball.score(self, p)

def chase(r):
    r.time = Snitch.time
    r.points += 1
    quaffle.points += 10
    print(r().points)

quaffle = Ball()
quaffle.points = 10
chasing = quaffle.score
time = lambda: Ball.points
malfoy = lambda: Ball.time()

"""
>>> Snitch().points
150
>>> chasing(quaffle)
Magic 10
>>> Snitch().score('Seeker')
Seeker 0
None
>>> chase(Ball)
1
>>> Snitch().score(malfoy())
Harry 150
"""



# 3. Lists

# (a)
def column(g, c):
    """Return the column of g at index c.

    >>> column([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 1)
    [4, 7, 10]
    """
    return [elem[c] for elem in g]



# (b)
def print_grid(g):
    """Print each row on a separate line with columns aligned.

    >>> print_grid([[1, 234, 50, 4, 5], [67, 8, 90, 0, 500], [3, 4, 5, -500, 7]])
    1  234 50 4    5   
    67 8   90 0    500 
    3  4   5  -500 7   
    """
    cs = range(len(g[0]))
    widths = [max([len(str(row[c])) for row in g]) for c in cs]
    for row in g:
        line = ''
        for c in cs:
            s = str(row[c])
            line = line + s + ' ' * (widths[c] - len(s) + 1)
        print(line)
    


# 4. Sequences

# (a)
def stretch(s, repeat=0):
	"""Replicate the kth element k times, for all k in s.

	>>> a = Link(3, Link(4, Link(5, Link(6))))
	>>> stretch(a)
	>>> print(a)
	<3, 4, 4, 5, 5, 5, 6, 6, 6, 6>
	"""
	if s:
		for i in range(repeat):
			s.rest = Link(s.first, s.rest)
			s = s.rest
		stretch(s.rest, repeat+1)



# (b)
def combo(a, b):
	"""Return the smallest integer with all of the digits of a and b (in order).

	>>> combo(531, 432) # 45312 contains both _531_ and 4_3_2.
	45312
	>>> combo(531, 4321) # 45321 contains both _53_1 and 4_321.
	45321
	>>> combo(1234, 9123) # 91234 contains both _1234 and 9123_.
	91234
	>>> combo(0, 321) # The number 0 has no digits, so 0 is not in the result.
	321
	"""
	if not a or not b:
		return a + b
	elif a % 10 == b % 10:
		return combo(a // 10, b // 10) * 10 + b % 10
	return min(combo(a // 10, b) * 10 + a % 10, combo(a, b // 10) * 10 + b % 10)



# 5. Trees

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

# (a)
def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.

    >>> a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
    >>> siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [b.label for b in t.branches if len(t.branches) > 1]
    for b in t.branches:
        result.extend(siblings(b))
    return result



# (b)
class Sib(Tree):
    """A tree that knows how many siblings it has.

    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        self.siblings = 0
        for b in branches:
              b.siblings += len(branches) - 1
        Tree.__init__(self, label, branches)



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