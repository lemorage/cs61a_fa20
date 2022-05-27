# 1. What Would Python Display

items, n = [], 2

class Airpods:
    """
    Expression | Interactive Output
    >>> TwoAirpods.cost
    100
    >>> lost = Airpods()
    lonely
    >>> willbelost = TwoAirpods()
    pair
    pair
    >>> str(lost)
    'pair'
    >>> [item.k for item in items]
    [3, 2, 2]
    >>> u(lost, willbelost)
    pair
    pair
    [None, None]
    """ 
    cost, k = 200, 0
    f = lambda self: print(self)

    def __init__(self):
        Airpods.k += 1
        Airpods.f(self)
        items.extend([self])

    def __repr__(self):
        return (Airpods.k < 2 and "lonely") or "pair"

class TwoAirpods(Airpods):
    def __init__(self):
        self.k = 2
        Airpods.__init__(self)
        Airpods.__init__(self)

def discount(a):
    a.cost //= 2

def u(w, u):
    return [print(u) for u in [w, u]]

discount(Airpods)



# 2. Ultimate
# ...... SKIP ......



# 3. Deep lists

def in_nested(v, L):
    """
    >>> in_nested(5, [1, 2, [[3], 4]])
    False
    >>> in_nested(9, [[[1], [6, 4, [5, [9]]], 7], 7, 7])
    True
    >>> in_nested(1, 1)
    True
    """
    if type(L) != list:
        return v == L
    else:
        return any(in_nested(v, elem) for elem in L)



# 4. A data structure by any other form would smell just as sweet...

# (a)
class Link:
     empty = ()
     def __init__(self, first, rest=empty):
         self.first = first
         self.rest = rest
     def __str__(self):
         string = '<'
         while self.rest is not Link.empty:
             string += str(self.first) + ', '
             self = self.rest
         return string + str(self.first) + '>'

def link_to_dict(L):
    """
    >>> L = Link(1, Link(2, Link(3, Link(4, Link(1, Link(5))))))
    >>> print(L)
    <1, 2, 3, 4, 1, 5>
    >>> link_to_dict(L)
    {1: [2, 5], 3: [4]}
    >>> print(L)
    <1, 3, 1>
    """
    D = {}
    while L != Link.empty:
        key, value = L.first, L.rest.first
        if key in D:
            D[key] += [value]
        else:
            D[key] = [value]
        L.rest = L.rest.rest # L.rest, L = L.rest.rest, L.rest.rest
        L = L.rest
    return D

# (b)
# Answer: 𝛩(n)



# 5. I speak for the Trees

def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def print_tree_adt(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree_adt(b, indent + 1)

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        ind = []
        for b in self.branches:
            for line in b.indented(k + 1):
                ind.append('  ' + line)
        return [str(self.label)] + ind

    def is_leaf(self):
        return not self.branches
# OK
# OK
# OK
# OK
# D
# D
# OK
# OK
# OK
# OK
# OK
# E -> Function call returns an integer
# D
# D
# OK
# OK
# E -> It is an object, which cannot be passed in as an argument
# OK
# OK
# D



# 6. Trie this

# (a)
def make_trie(words):
    """ Makes a tree where every node is a letter of a word.
        All words end as a leaf of the tree.
        words is given as a list of strings.
    """
    trie = Tree('')
    for word in words:
        add_word(trie, word)
    return trie


def add_word(trie, word):
    if not word:
        return ""
    branch = None
    for b in trie.branches:
        if b.label == word[0]:
            branch = b
    if not branch:
        branch = Tree(word[0])
        trie.branches.append(branch)
    add_word(branch, word[1:])

# (b)
def get_words(trie):
    """
    >>> get_words(make_trie(['this', 'is', 'the', 'trie']))
    ['this', 'the', 'trie', 'is']
    """
    if trie.is_leaf():
        return [trie.label]
    return sum([[trie.label + word for word in get_words(b)] for b in trie.branches], [])
 