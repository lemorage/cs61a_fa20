# 1. The Droids You're Looking For

def x(wing):
    poe = lambda poe: wing + poe
    wing.append(droid)
    return poe

droid = [8]
b = x([1])
b([b([8])])



# 2. Stoned

# (a)
def hailstone(n, g):
    """Call g on each element of the hailstone sequence starting
    at n and return its length.

    >>> a = hailstone(10, print)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> s = []
    >>> hailstone(10, s.append)
    7
    >>> s
    [10, 5, 16, 8, 4, 2, 1]
    """
    if n == 1:
        h = lambda x, y: 1
    elif n % 2:
        h = up
    else:
        h = down
    g(n)
    return h(n, lambda n: hailstone(n, g))

def up(n, f):
    return 1 + f(3 * n + 1)

def down(n, f):
    return 1 + f(n // 2)

# (b)
def collide(m, n):
    """Return the earliest number in the hailstone sequence starting at n that
    also appears in the hailstone sequence starting at m.

    >>> collide(10, 32)  # 10, 5, 16, 8, ...  vs  32, 16, 8, ...
    16
    >>> collide(13, 11)  # 13, 40, ...  vs  11, 34, 17, 52, 26, 13, 40, ...
    13
    """
    s = []
    hailstone(m, s.append)
    found = None
    def f(k):
        nonlocal found
        if found is None and k in s:
            found = k
    hailstone(n, f)
    return found



# 3. College Party

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


class State:
    electors = {}
    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors

battleground = [State('AZ', 11), State('PA', 20), State('NV', 6),
                State('GA', 16), State('WI', 10), State('MI', 16)]

def print_all(s):
    for x in s:
        print(x)

# (a)
def wins(states, k):
    """Yield each linked list of two-letter state codes that describes a win by at least k.

    >>> print_all(wins(battleground, 50))
    <AZ PA NV GA WI MI>
    <AZ PA NV GA MI>
    <AZ PA GA WI MI>
    <PA NV GA WI MI>
    >>> print_all(wins(battleground, 75))
    <AZ PA NV GA WI MI>
    """
    if k <= 0 and not states:
        yield Link.empty
    if states:
        first = states[0].electors
        for win in wins(states[1:], k-first):
            yield Link(states[0].code, win)
            yield from wins(states[1:], k+first)



# (b)
def must_win(states, k):
    """List all states that must be won in every scenario that wins by k.

    >>> must_win(battleground, 50)
    ['PA', 'GA', 'MI']
    >>> must_win(battleground, 75)
    ['AZ', 'PA', 'NV', 'GA', 'WI', 'MI']
    """
    def contains(s, x):
        """Return whether x is a value in linked list s."""

        return (s is not Link.empty) and (x == s.first or contains(s.rest, x))
    return [s.code for s in states if all([contains(w, s.code) for w in wins(states, k)])]



# (c)
def is_minimal(state_codes, k):
    """Return whether a non-empty list of state_codes describes a minimal win by
    at least k.

    >>> is_minimal(['AZ', 'NV', 'GA', 'WI'], 0)  # Every state is necessary
    True
    >>> is_minimal(['AZ', 'GA', 'WI'], 0)        # Not a win
    False
    >>> is_minimal(['AZ', 'NV', 'PA', 'WI'], 0)  # NV is not necessary
    False
    >>> is_minimal(['AZ', 'PA', 'WI'], 0)        # Every state is necessary
    True
    """
    assert state_codes, 'state_codes must not be empty'
    votes_in_favor = [State.electors[s] for s in state_codes]
    total_possible_votes = sum(State.electors.values())
    def win_margin(n):
        """Margin of victory if n votes are in favor and the rest are against."""
        return n - (total_possible_votes - n)
    if win_margin(sum(votes_in_favor)) < k:
        return False  # Not a win
    in_favor_no_smallest = sum(votes_in_favor) - min(votes_in_favor)
    return win_margin(in_favor_no_smallest) < k



# 4. Last Lecture AMA

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
def related(a, b, offspring_trees):
    """Return whether the llamas named a and b are related.
    >>> related('Charlie', 'Max', originals)   # Grandparent
    True
    >>> related('Jules', 'Jackie', originals)  # Not related, even though they have child
    False
    >>> related('Max', 'Jules', originals)
    True
    >>> related('Max', 'Jess', originals)
    True
    """
    def family(t):
        """Return a list of the names of all llamas in Tree t."""
        result = [t.label]
        for b in t.branches:
            result.extend(family(b))
        return result
    for s in map(family, offspring_trees):
        if a in s and b in s:
            return True
        return False



# (b)
def parents(a, b, offspring_trees):
    """Return whether a and b are both parents of the same child.

    >>> parents('Jules', 'Jackie', originals)  # Parents of Alex
    True
    >>> parents('Jules', 'Finley', originals)  # Parents of Jess
    True
    >>> parents('Jules', 'Jaidyn', originals)
    False
    >>> parents('Jules', 'Sidney', originals)
    False
    """
    storage = {}
    def traverse(t):
        for b in t.branches:
            if b.label not in storage:
                storage[b.label] = []
            storage[b.label].append(t.label)
            traverse(b)
    for t in offspring_trees:
        traverse(t)
    return any([a in s and b in s for s in storage.values()])



# (c)
SELECT a.parent
    FROM family AS a, family AS b, family AS c, family AS d, family AS e
    WHERE a.child = b.parent AND b.parent != c.parent AND b.child = c.child 
        AND a.parent = d.parent AND c.parent = e.parent AND d.child = e.child;



# 5. SchemeQL

# (a)
(define (cons x s) (append (list x) s))

# (b)
(define (join s t)
    (if (null? s) nil
        (append (map (lambda (v) (append (car s) v)) t)
            (join (cdr s) t))))


# 47 points in total