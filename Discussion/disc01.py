def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining: 
        return True
    return False



def wears_jacket(temp, raining):
    return raining



def is_prime(n): 
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    temp = n - 1
    while temp != 1:
        if n % temp == 0:
            return False
        temp -= 1
    return True


