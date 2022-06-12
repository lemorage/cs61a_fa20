# 1. By Any Other Name

class Plant:
    k = 1
    kind = "green"

    def __init__(self):
        self.k = Plant.k
        Plant.k = self.k + 1
        if self.k > 3:
            Plant.name = lambda t: "tree"
            Plant.k = 6
    
    def name(self):
        return kind # no self here

    def __repr__(self):
        s = self.name() + " "
        return s + str(self.k)

class Flower(Plant):
    """
    >>> f1 = Flower() # self.k = 1
    >>> f2 = Flower() # self.k = 2

    # --- Questions ---
    >>> f1.name()
    Traceback (most recent call last):
    ...
    NameError: name 'kind' is not defined
    >>> f1.k # Plant.k = 3
    1
    >>> Plant().k
    3
    >>> Rose.k
    4
    >>> Plant()
    tree 4
    >>> Rose()
    nice rose 6
    >>> Garden(Flower).smell()
    'bad'
    >>> Garden(Flower).name()
    bad tree 6
    """
    kind = "pretty"

    def __repr__(self):
        s = self.smell() + " "
        return s + Plant.__repr__(self)
    
    def smell(self):
        return "bad"

class Rose(Flower):

    def name(self):
        return "rose"

    def smell(self):
        return "nice"

class Garden:

    def __init__(self, kind):
        self.name = kind
        self.smell = kind().smell

    def smell(self):
        return self.name.kind



# 3. Pumpkin Splice Latte

# (a)
def splice(a, b, k):
    """Return a list of the first k elements of a, then all of b, then the rest of a.

    >>> splice([2, 3, 4, 5], [6, 7], 2)
    [2, 3, 6, 7, 4, 5]
    """
    return a[:k] + b + a[k:]



# (b)
def all_splice(a, b, c):
    """Return a list of all k such that splicing b into a at position k gives c.

    >>> all_splice([1, 2], [3, 4], [1, 3, 4, 2])
    [1]
    >>> all_splice([1, 2, 1, 2], [1, 2], [1, 2, 1, 2, 1, 2])
    [0, 2, 4]
    """
    return [i for i in range(len(a)+1) if splice(a, b, i) == c]



# (c)
def splink(a, b, k):
    """Return a Link containing the first k elements of a, then all of b, then the rest of a.

    >>> splink(Link(2, Link(3, Link(4, Link(5)))), Link(6, Link(7)), 2)
    Link(2, Link(3, Link(6, Link(7, Link(4, Link(5))))))
    """
    if not b:
        return a
    elif k == 0:
        return Link(b.first, splink(a, b.rest, k))
    return Link(a.first, splink(a.rest, b, k-1))



# 4. Both Ways

# (a)
def both(a, b):
    """Return whether there is any value that appears in both a and b, two sorted Link instances.

    >>> both(Link(1, Link(3, Link(5, Link(7)))), Link(2, Link(4, Link(6))))
    False
    >>> both(Link(1, Link(3, Link(5, Link(7)))), Link(2, Link(7, Link(9)))) # both have 7
    True
    >>> both(Link(1, Link(4, Link(5, Link(7)))), Link(2, Link(4, Link(5)))) # both have 4 and 5
    True
    """
    if not a or not b:
        return False
    if a.first > b.first:
        a, b = b, a
    return a.first == b.first or both(a.rest, b)

# (b)
# Answer: Θ(n)



# (c)
def ways(start, end, k, actions):
    """Return the number of ways of reaching end from start by taking up to k actions.

    >>> ways(-1, 1, 5, [abs, lambda x: x+2]) # abs(-1) or -1+2, but not abs(abs(-1))
    2
    >>> ways(1, 10, 5, [lambda x: x+1, lambda x: x+4]) # 1+1+4+4, 1+4+4+1, or 1+4+1+4
    3
    >>> ways(1, 20, 5, [lambda x: x+1, lambda x: x+4])
    0
    >>> ways([3], [2, 3, 2, 3], 4, [lambda x: [2]+x, lambda x: 2*x, lambda x: x[:-1]])
    3
    """
    if start == end:
        return 1
    elif k == 0:
        return 0
    return sum([ways(f(start), end, k-1, actions) for f in actions])



# 5. Autumn Leaves

# (a)
def pile(t):
    """Return a dict that contains every path from a leaf to the root of tree t.

    >>> pile(tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])]))
    {1: (3, (5, ())), 2: (3, (5, ())), 7: (6, (5, ()))}
    """
    p = {}
    def gather(u, parent):
        if is_leaf(u):
            p[label(u)] = parent
        for b in branches(u):
            gather(b, (label(u), parent))
    gather(t, ())
    return p



# (b)
class Path:
    """A path through a tree from the root to a leaf, identified by its leaf label.
    
    >>> a = tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])])
    >>> print(Path(a, 7), Path(a, 2))
    5-6-7 5-3-2
    """
    def __init__(self, t, leaf_label):
        self.pile, self.end = pile(t), leaf_label

    def __str__(self):
        path, s = self.pile[self.end], str(self.end)
        while path:
            path, s = path[1], str(path[0]) + '-' + s
        return s


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