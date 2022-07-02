# 1 Trees

def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t): return 0
    else:
        return 1 + max(height(b) for b in branches(t))



def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> max_path_sum(t)
    9
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(b) for b in branches(t)]) + label(t)



def square_tree(t):
    """Return a tree with the square of every element in t

    >>> numbers = tree(1,
    ...             [tree(2,
    ...                 [tree(3),
    ...                  tree(4)]),
    ...             tree(5,           
    ...                 [tree(6,
    ...                     [tree(7)]),
    ...                 tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    return tree(label(t) * label(t), [square_tree(b) for b in branches(t)])



def find_path(tree, x): 
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree): # [find_path(b, x) for b in branches(tree)]
        path = find_path(b, x)
        if path: # is not None
            return [label(tree)] + path



# 2 Binary Numbers

# 2.1 Fill in the table
# 5 101
# 10 1010
# 14 1110
# 37 100101
# 2 10
# 44 101010
# 101 1100101



# 2.2
def prune(t, k):
    if k == 0:
        return tree(label(t), [])
    else:
        return tree(label(t), [prune(b, k-1) for b in branches(t)])

def prune_binary(t, nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [n[1:] for n in nums if n[0] == label(t)] 
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums) 
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch] 
        if not new_branches:
            return None
        return tree(label(t), new_branches)



# Tree ADT

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

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


