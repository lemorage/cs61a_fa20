# 1. Evaluate This!

y = 7

def b(x):
	return lambda y: x(y)

def c(x):
  return 3

w = b(c)

def c(x):
  return x

# (a)
"""
Expression | Interactive Output
>>> (3 and abs)(-1)
1
>>> print(3) or 1/0
3
Error
>>> print
<Function>
>>> ([1, 2, 3] if y // (y+1) else [4, 5])[1]
5
>>> w(5)
3
"""

# (b)
# Interactive Output: False True



# 2. Environmental Policy
# ...... SKIP ......

# 3. Extra
# Answer: Goethe



# 4. Going Around in Cycles

def has_cycle(L, k):
	"""True iff L has a cycle of length K>=1. Assumes 0 <= L[i] < len(L)
	for 0 <= i < len(L).

	>>> L = [3, 1, 4, 5, 0, 2]
	>>> has_cycle(L, 1) # 1 -> 1
	True
	>>> has_cycle(L, 5) # 0 -> 3 -> 5 -> 2 -> 4 -> 0
	True
	>>> has_cycle(L, 2)
	False
	"""
	def cycle_at(s):
		"""L has a cycle of length K starting at S."""
		next = L[s]
		n = 1
		while n < k:
			if next == s:
				return False
			next = L[next]
			n += 1
		return next == s

	for j in range(len(L)):
		if cycle_at(j):
			return True
	return False



# 5. Your Father’s Parentheses

def count_groupings(n):
	"""For N >= 1, the number of distinct parenthesizations
	of a product of N items.
	>>> count_groupings(1)
	1
	>>> count_groupings(2)
	1
	>>> count_groupings(3)
	2
	>>> count_groupings(4)
	5
	>>> count_groupings(5)
	14
	"""
	if n == 1:
		return 1
	count = 0
	i = 1
	while i < n:
		count += count_groupings(i) * count_groupings(n-i)
		i += 1
	return count



# 6. Amazing

# (a)
def pred_maze(x0, y0, open, exit):
	"""Return a maze in which the runner is at (X0, Y0), every square
	(a, b) where a <= EXIT is an exit, and otherwise a square (a, b)
	is open iff OPEN(a, b). It is assumed that (X0, Y0) is open."""
	def maze(dir):
		x, y = (x0, y0 - 1) if dir == "south" else (x0 - 1, y0)
		if x <= exit:
			return "exit"
		elif open(x, y):
			return pred_maze(x, y, open, exit)
		else:
			return "dead end"
	return maze



# (b)
def path_out(M):
	"""Given a maze function M in which the runner is not yet out
	of the maze, returns a string of the form "D1 D2 ...", where each
	Di is either south or west, indicating a path from M to an exit,
	or None iff there is no such path."""
	for dir in ["south", "west"]:
		next = M(dir)
		if next == "exit":
			return dir + " "
		elif next != "dead end":
			rest_of_path = path_out(next)
			if rest_of_path:
				return dir + " " + rest_of_path
	return None