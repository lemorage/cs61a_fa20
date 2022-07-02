# 1 Representation - A Note on Str and Repr

# 1.1
class A():
    """
    >>> A("one")
    one
    >>> print(A("one"))
    oneone
    >>> repr(A("two"))
    'two'
    """
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2

class B():
    """
    >>> b = B()
    boo!
    >>> b.add_a(A("a"))
    >>> b.add_a(A("b"))
    >>> b
    2
    aabb
    """
    def __init__(self):
        print("boo!")
        self.a = [] 

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret



# 2. Linked Lists

class Link: 
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self): 
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self): 
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# 2.1
def sum_nums(lnk): 
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if not lnk:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)

# 2.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    product = 1
    for lnk in lst_of_lnks:
        if not lnk:
            return Link.empty
        product *= lnk.first
        rest_of_lnks = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(rest_of_lnks))



# 2.3
def flip_two(lnk): 
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if not lnk or not lnk.rest:
        return
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two(lnk.rest.rest)
 
        

# 2.4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest



# 3. Trees

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

# 3.1
def make_even(t): 
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2:
        t.label += 1
    for b in t.branches:
        make_even(b)



# 3.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t
    Tree(1, [Tree(4, [Tree(9)]), Tree(16), Tree(25)])
    """
    t.label = t.label ** 2
    for b in t.branches:
        square_tree(b)



# 3.3
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths += [[t.label] + path]
    return paths



# 3.4
def combine_tree(t1, t2, combiner): 
    """
    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    # for a, b in zip(t1.branches, t2.branches):
        # combined = combine_tree(a, b, combiner)
    # return Tree(combiner(t1.label, t2.label), combined)
    combined = [combine_tree(a, b, combiner) for a, b in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)



# 3.5
def alt_tree_map(t, map_fn): 
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, depth):
        if not depth % 2:
            t.label = map_fn(t.label)
        for b in t.branches:
            helper(b, depth+1)
        return t
    return helper(t, 0)


