# 1. In-N-Out

############################################################
# Expression 			   | Interactive Output	   #
############################################################
# print(re(1+2), print(4)) 	   | 3 3\n 4\n None\n None #
# cheap(3)			   | 3 3\n None\n 6 	   #
# cheap(seat(2))		   | 4 4\n None\n 8	   #
# car(1)(double)(pow)	 	   | 25 		   #
# double(print(1))		   | 1\n None\n 5 None\n 6 #
# car(0)(seat)(add)		   | 0\n 5 None\n 11 	   #
############################################################



# 2. Supernatural
# ...... SKIP ......



# 3. You Complete Me

# (a)
def longest_increasing_suffix(n):
	"""Return the longest increasing suffix of a positive integer n.

	>>> longest_increasing_suffix(63134)
	134
	>>> longest_increasing_suffix(233)
	3
	>>> longest_increasing_suffix(5689)
	5689
	>>> longest_increasing_suffix(568901) # 01 is the suffix, displayed as 1
	1
	"""
	m, suffix, k = 10, 0, 1
	while n:
		n, last = n // 10, n % 10
		if last < m:
			m, suffix, k = last, last * k + suffix, 10 * k
		else:
			return suffix
	return suffix



# (b)
lamb = lambda lamb: lambda: lamb + lamb
lamb(1000)() + (lambda b, c: b() * b() - c)(lamb(2), 1)



# (c)
from operator import add , mul

def combine(n, f, result):
	"""Combine the digits in non-negative integer n using f.

	>>> combine(3, mul, 2) # mul(3, 2)
	6
	>>> combine(43, mul, 2) # mul(4, mul(3, 2))
	24
	>>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)))
	16
	>>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0)))
	8
	"""
	if n == 0:
		return result
	else:
		return combine(n // 10, f, f(n % 10, result))



# (d)
square = lambda x: x * x
double = lambda x: 2 * x

def memory(x, f):
	"""Return a higher-order function that prints its memories.

	>>> f = memory(3, lambda x: x)
	>>> f = f(square)
	3
	>>> f = f(double)
	9
	>>> f = f(print)
	6
	>>> f = f(square)
	3
	None
	"""
	def g(h):
		print(f(x))
		return memory(x, h)
	return g
