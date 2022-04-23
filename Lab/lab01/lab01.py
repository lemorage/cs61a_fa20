def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    times = k - 1
    return compute_falling(n, times)

def compute_falling(n, times):
    result = 1
    if times < 0: return 1
    elif times == 0: return n
    else:
        while times >= 0:
            result *= n
            times -= 1
            n -= 1
    return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    current, sum = 0, y % 10
    while y:
        sum += current
        y //= 10
        current = y % 10
    return sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    last, second_to_last = n % 10, n // 10 % 10
    while n:
        if last == second_to_last:
            return True
        n //= 10
        last, second_to_last = n % 10, n // 10 % 10
    return False


