# 5. Negative Feedback

def clear_negatives(lst):
    """
    >>> clear_negatives([1, 0, 6])
    [1, 0, 6]
    >>> clear_negatives([3, -2, 1, 6, 2])
    [3, 6, 2]
    >>> lst = [-3, -4, 5, 5]
    >>> clear_negatives(lst)
    [5]
    >>> lst
    [-3, -4, 5, 5]
    """
    if not lst:
        return []
    elif lst[0] < 0:
        return clear_negatives(lst[-lst[0]:])
    else:
        return [lst[0]] + clear_negatives(lst[1:])



# 6. Your Guess Is As Good As Mine

def make_guess(n):
    """
    >>> guesser = make_guess(10)
    >>> guess1 = guesser(6)
    >>> guess2 = guess1(7)
    >>> guess3 = guess2(8)
    >>> guess3(10)
    3
    >>> guess2(10)
    2
    >>> a = make_guess(5)(1)(2)(3)(4)(5)
    >>> a
    4
    """
    def update_guess(num_incorrect):
        def new_guess(x):
            if x == n:
                return num_incorrect
            else:
                return update_guess(num_incorrect + 1)
        return new_guess
    return update_guess(0)



# 7. Scrabbled Eggs

# (a)
def is_subseq(w1, w2):
    """ Returns True if w1 is a subsequence of w2 and False otherwise.

    >>> is_subseq("word", "word")
    True
    >>> is_subseq("compute", "computer")
    True
    >>> is_subseq("put", "computer")
    True
    >>> is_subseq("computer", "put")
    False
    >>> is_subseq("sin", "science")
    True
    >>> is_subseq("nice", "science")
    False
    >>> is_subseq("boot", "bottle")
    False
    """
    if not w1:
        return True
    elif not w2:
        return False
    else:
        with_elem = w1[0] == w2[0] and is_subseq(w1[1:], w2[1:])
        without_elem = is_subseq(w1, w2[1:])
        return with_elem or without_elem


# (b)
def scrabbler(chars, words, values):
    """ Given a list of words and point values for letters, returns a
    dictionary mapping each word that can be formed from letters in chars
    to their point value. You may not need all lines

    >>> words = ["easy", "as", "pie"]
    >>> values = {"e": 2, "a": 2, "s": 1, "p": 3, "i": 2, "y": 4}
    >>> scrabbler("heuaiosby", words, values)
    {'easy': 9, 'as': 3}
    >>> scrabbler("piayse", words, values)
    {'pie': 7, 'as': 3}
    """
    result = {}
    for word in words:
        if is_subseq(word, chars):
            result[word] = sum([values[key] for key in values if key in word])
    return result



# 8. Leaf It To Me

def tree(label, branches=[]):
    return [label] + list(branches)
def label(t):
    return t[0]
def is_leaf(t):
    return not branches(t)
def branches(t):
    return t[1:]


def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    def helper(t, k, on_path):
        if k == 0:
            return []
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(b, k - 1, True) for b in branches(t)]
        if on_path:
            return max(a, key = sum)
        else:
            b = [helper(b, k, False) for b in branches(t)]
            return max(a+b, key = sum)
    return helper(t, k, False)