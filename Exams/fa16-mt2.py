# 1. Halloween

class Link:
    """A linked list."""
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

class Party:
    guests = Link.empty

    def __init__(self, time):
       Party.guests = Link(time+1, Party.guests)

    def attend(self):
       self.guests.rest = Link(self.guests.rest)
       return self.guests

class Costume(Party):
    """
    Expression | Interactive Output
    >>> Party(1).guests
    Link(2)
    >>> Party(3).attend() # Link(4, Link(2))
    Link(4, Link(Link(2)))
    >>> Costume(5, 6).attend() # Link(4, Link(5))
    Nice
    Link(Costume)
    >>> Party(7).attend() # Link(8, Link(4, Link(5)))
    Link(10, Link(8, Link(4, Link(5))))
    """
    def __init__(self, bow, tie):
       Party.guests.rest = Link(bow)
       self.ie = Link(self)

    def attend(self):
       print(repr(self.ie))
       Party.attend = lambda self: Party(9).guests

    def __repr__(self):
       print('Nice')
       return 'Costume'



# 2. A List with a Twist
# ...... SKIP ......



# 3. Return Policy

def quota(f, limit):
    """A decorator that limits the number of times a value can be returned.
    >>> square = lambda x: x * x
    >>> square = quota(square, 3)
    >>> square(6)                     # 1st call with return value 36
    36
    >>> [square(5) for x in range(3)] # 3 calls when the limit is 3
    [25, 25, 25]
    >>> square(5)                     # 4th call with return value 25
    'Over quota! Limit is now 2'
    >>> square(-6)                    # 2nd call with return value 36
    36
    >>> square(-6)                    # 3rd call when the limit is 2
    'Over quota! Limit is now 1'
    >>> square(7)                     # 1st call when the limit is 1
    49
    >>> square(5)                     # 5th call with return value 25
    'Over quota! Limit is now 0'
    """
    values = []
    def limited(n):
        nonlocal limit
        y = f(n)
        count = len([x for x in values if x == y])
        values.append(y)
        if count < limit:
            return y
        limit = limit - 1
        return 'Over quota! Limit is now ' + str(limit)
    return limited



# 4. A Classy Election

class VotingMachine:
    """A machine that creates and records ballots.

    >>> machine = VotingMachine(4)
    >>> a, b, c, d = machine.ballots
    >>> d.vote('Bruin')
    'Bruin is winning'
    >>> b.vote('Bruin')
    'Bruin is winning'
    >>> c.vote('Bear')
    'Bear is losing'
    >>> a.vote('Bear')
    'Bear is winning'
    >>> c.vote('Tree')
    'Fraud: multiple votes from the same ballot!'
    >>> machine.winner
    'Bear'
    """
    def __init__(self, k):
       self.ballots = [Ballot(self) for i in range(k)]
       self.votes = {}
       self.winner = None
    def record(self, ballot, choice):
        if ballot.used:
           return 'Fraud: multiple votes from the same ballot!'
        ballot.used = True
        self.votes[choice] = self.votes.get(choice, 0) + 1
        if self.votes[choice] is not max(self.votes.values()):
           return choice + ' is losing'
        else:
           self.winner = choice
           return choice + ' is winning'
class Ballot:
    used = False

    def __init__(self, machine):
       self.machine = machine

    def vote(self, x):
       return self.machine.record(self, x)



# 5. Trick or Tree

class Tree:
    """Tree abstraction."""
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

def path(s, t):
    """Return whether Link S is a path from the root to a leaf in Tree T.

    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6)])
    >>> a = Link(1, Link(3, Link(4)))  # A full path
    >>> path(a, t)
    True
    >>> b = Link(1, Link(3))           # A partial path
    >>> path(b, t)
    False
    >>> c = Link(1, Link(2, Link(7)))  # A path and an extra value
    >>> path(c, t)
    False
    >>> d = Link(3, Link(4))           # A path of a branch
    >>> path(d, t)
    False
    """
    if not s or s.first != t.label: # (s.rest is Link.empty and not t.is_leaf())
        return False
    if s.rest is Link.empty and t.is_leaf():
        return True
    return any([path(s.rest, b) for b in t.branches])



# 6. Left is Right There

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""

    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty' 
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)


# (a)
def binary(s):
    """Construct a binary search tree from S for which all paths are in order.

    >>> binary([3, 5, 1])
    BTree(3, BTree(1), BTree(5))
    >>> binary([4, 3, 7, 6, 2, 9, 8])
    BTree(4, BTree(3, BTree(2)), BTree(7, BTree(6), BTree(9, BTree(8))))
    """
    assert len(s) == len(set(s)), 'All elements of s should be unique'
    if not s:
        return BTree.empty
    root = s[0]
    left = [x for x in s if x < root]
    right = [x for x in s if x > root]
    return BTree(root, binary(left), binary(right))

# (b)
# Answer: Θ(log n)

# (b)
# Answer: Θ(n)



# 7. Summer Camp

# (a)
def sums(n, k):
    """Return the ways in which K positive integers can sum to N.

    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if n == 0 or k == 0:
        return [[]]
    y = []
    for x in range(1, n):
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y



# (b)
f = lambda x, y: (x and [[x] + z for z in y] + f(x-1, y)) or []

def sums(n, k):
    """Return the ways in which K positive integers can sum to N."""

    g = lambda w: (w and f(n, g(w-1))) or [[]]
    return [v for v in g(k) if sum(v) == n]