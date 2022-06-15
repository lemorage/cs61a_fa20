# 3. High Scores

"""
>>> lst = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> lst[2][0] # OR len(lst)
5
>>> [[11-x, 11-y] for x, y in lst]
[[10, 9], [8, 7], [6, 5], [4, 3], [2, 1]]
>>> [x[1] for x in lst[:2]]
[2, 4]
"""



# 4. Kerbal Space Program

def is_sorted(n):
    """Returns whether the digits in n are in non-increasing order
    from left to right.

    >>> is_sorted(4)
    True
    >>> is_sorted(55555)
    True
    >>> is_sorted(9876543210) # blastoff !
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    elif n // 10 % 10 < n % 10:
        return False
    else:
        return is_sorted(n // 10)



# 5. Katamari

# (a)
def aggregate(fn, seq, pred):
    """Aggregates using fn the elements in seq that satisfy pred.

    >>> def is_even(x):
    ...     return x % 2 == 0 
    >>> def sum_plus_one(x, y):
    ...     return x + y + 1
    >>> aggregate(sum_plus_one, [2, 4, 6], is_even) # (2 + 4 + 1) + 6 + 1
    14
    >>> # If no elements satisfy pred, return None
    >>> aggregate(sum_plus_one, [1, 3, 5, 7, 9], is_even)
    >>> # If only one element satisfies pred, return that element
    >>> aggregate(sum_plus_one , [1, 2, 3], is_even)
    2
    """
    result = None
    for elem in seq:
        if pred(elem):
            if not result:
                result = elem
            else:
                result = fn(result, elem)
    return result



# (b)
from operator import add, mul
"""
>>> fact(0)
1
>>> fact(5)
120
"""
fact = lambda n: 1 if n <= 1 else aggregate(mul, [n, fact(n-1)], lambda x: x > 1)



# 6. Legend of Zelda

def linked_sum(lnk, total):
    """Return the number of combinations of elements in lnk that
    sum up to total.
    >>> # Four combinations: 1 1 1 1 , 1 1 2 , 1 3 , 2 2
    >>> linked_sum(Link(1, Link(2, Link(3, Link(5)))), 4)
    4
    >>> linked_sum(Link(2, Link(3, Link(5))), 1)
    0
    >>> # One combination: 2 3
    >>> linked_sum(Link(2, Link(4, Link(3))), 5)
    1
    """
    if not total:
        return 1
    elif not lnk or total < 0:
        return 0
    else:
        with_first = linked_sum(lnk, total-lnk.first)
        without_first = linked_sum(lnk.rest, total)
        return with_first + without_first



# 7. Game of Thrones

# (a)
def track_lineage(family_tree, name):
    """Return the entries of the parent and grandparent of
    the node with entry name in family_tree.

    >>> t = tree('Tytos', [
    ...         tree('Tywin', [
    ...             tree('Cersei'), tree('Jaime'), tree('Tyrion'),
    ...         ]),
    ...         tree('Kevan', [
    ...             tree('Lancel'), tree('Martyn'), tree('Willem')
    ...         ])])
    >>> track_lineage(t, 'Cersei')
    ['Tywin', 'Tytos']
    >>> track_lineage(t, 'Tywin')
    ['Tytos', None]
    >>> track_lineage(t, 'Tytos')
    [None, None]
    """
    def tracker(t, p, gp):
        if name == entry(t):
            return [p, gp]
        for c in children(t):
            res = tracker(c, entry(t), p)
            if res:
                return res
    return tracker(family_tree, None, None)



# (b)
def are_cousins(family_tree, name1, name2):
    """Return True if a node with entry name1 is a cousin of a node with
    entry name2 in family_tree.

    >>> t = tree('Tytos', [
    ...         tree('Tywin', [
    ...             tree('Cersei'), tree('Jaime'), tree('Tyrion'),
    ...         ]),
    ...         tree('Kevan', [
    ...             tree('Lancel'), tree('Martyn'), tree('Willem')
    ...         ])])
    >>> are_cousins(t, 'Kevan', 'Tytos') # same tree as before
    False
    >>> are_cousins(t, 'Cersei', 'Lancel')
    True
    >>> are_cousins(t, 'Jaime', 'Lancel')
    True
    >>> are_cousins(t, 'Jaime', 'Tyrion')
    False
    """
    l1 = track_lineage(family_tree, name1)
    l2 = track_lineage(family_tree, name2)
    p1, p2, gp1, gp2 = l1[0], l2[0], l1[1], l2[1]
    return True if p1 != p2 and gp1 == gp2 != None else False



# (8) 
# Number: 39


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


def tree(entry, children=[]):
    return [entry, children]

def entry(tree):
    return tree[0]

def children(tree):
    return tree[1]