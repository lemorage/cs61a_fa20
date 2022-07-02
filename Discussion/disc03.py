def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if n == 1:
		return m
	else:
		return m + multiply(m, n-1)



def multiply2(m, n):
	"""
	>>> multiply2(5, 3)
	15
	"""
	if m == 1:
		return n
	else:
		return n + multiply2(m-1, n)



def rec(x, y):
	"""This function returns x power y.

	>>> rec(3, 2)
	9
	"""
	if y > 0:
		return x * rec(x, y - 1) 
	return 1




def hailstone(n):
	"""Print out the hailstone sequence starting at n, and return the 
	number of elements in the sequence.

	>>> a = hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>> a
	7
	"""
	print(n)
	if n == 1: return n
	else:
		if n % 2 == 0: return 1 + hailstone(n // 2)
		else: return 1 + hailstone(n * 3 + 1)



def merge(n1, n2):
	""" Merges two numbers

	>>> merge(31, 42)
	4321
	>>> merge(21, 0)
	21
	>>> merge(21, 31)
	3211
	"""
	if n1 == 0: return n2
	elif n2 == 0: return n1
	elif n1 % 10 < n2 % 10: return merge(n1 // 10, n2) * 10 + n1 % 10
	else: return merge(n1, n2 // 10) * 10 + n2 % 10



def make_func_repeater(f, x): 
	"""
	>>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
	>>> incr_1(2) #same as f(f(x))
	3
	>>> incr_1(5)
	6
	>>> incr_2 = make_func_repeater(lambda x: x * 3, 5)
	>>> incr_2(4) #same as f(f(f(f(x))))
	405
	"""
	def repeat(y):
		if y == 0:
			return x
		else:
			return f(repeat(y-1))
	return repeat



def is_prime(n): 
	"""
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
	"""
	def prime_helper(i):
		if n == i:
			return True
		elif n % i == 0 or n == 1:
			return False
		else:
			return prime_helper(i+1)
	return prime_helper(2)
