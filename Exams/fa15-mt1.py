# 1. Evaluators Gonna Evaluate

def jazz(hands):
	if hands < out:
		return hands * 5
	else:
		return jazz(hands // 2) + 1

def twist(shout, it, out=7):
	while shout:
		shout, out = it(shout), print(shout, out)
		return lambda out: print(shout, out)

hands, out = 2, 3

"""
Expression | Interactive Output
>>> print(None, print(None))
None
None None
>>> jazz(5)
11
>>> (lambda out: jazz(8))(9)
12
>>> twist(2, lambda x: x-2)(4)
2 7
0 4 
>>> twist(5, print)(out)
5
5 7
None 3
>>> twist(6, lambda hands: hands-out, 2)(-1)
6 2
3 None
"""



# 2. Environmental Policy
# ...... SKIP ......



# 3. Digit Fidget

# (a)
def find_digit(n, d):
	"""Return the largest digit position in n for which d is the digit.

	>>> find_digit(567, 7)
	0
	>>> find_digit(567, 5)
	2
	>>> find_digit(567, 9)
	False
	>>> find_digit (568789, 8) # 8 appears at positions 1 and 3
	3
	"""
	i, k = 0, False
	while n:
		n, last = n // 10, n % 10
		if last == d:
			k = i
		i = i + 1
	return k



# (b)
def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

f = lambda x: find_digit (234567, x)
# Answer: 2, 3, 4, 5, so that compose1(f, f)(y) == y, i.e. f(f(y)) == y



# (c)
def luhn_sum(n):
	""" Return the Luhn sum of n.

	>>> luhn_sum(135) # 1 + 6 + 5
	12
	>>> luhn_sum(185) # 1 + (1+6) + 5
	13
	>>> luhn_sum(138743) # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
	30
	"""
	def luhn_digit(digit):
		x = digit * multiplier
		return (x // 10) + (x % 10)
	total, multiplier = 0, 1
	while n:
		n, last = n // 10, n % 10
		total = total + luhn_digit(last)
		multiplier = 3 - multiplier
	return total



# (d) 
def check_digit(n):
	"""Add a digit to the end of n so that the result has a valid Luhn sum.

	>>> check_digit(153) # 2 + 5 + 6 + 7 = 20
	1537
	>>> check_digit(13874)
	138743
	"""
	return 10 * n + -luhn_sum(10 * n) % 10



# 4. Zombies!

# (a)
def decompose1(f, h):
	"""Return g such that h(x) equals f(g(x)) for any non-negative integer x.

	>>> add_one = lambda x: x + 1
	>>> square_then_add_one = lambda x: x * x + 1
	>>> g = decompose1(add_one , square_then_add_one)
	>>> g(5)
	25
	>>> g(10)
	100
	"""
	def g(x):
		def r(y):
			if h(x) == f(y):
				return y
			else:
				return r(y+1)
		return r(0)
	return g



# (b)
def make_adder(n):
	def adder(k):
		return n + k
	return adder

e, square = make_adder(1), lambda x: x*x
answer = decompose1(e, compose1(square, e))(3) + 2000