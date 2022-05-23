# 1. If (s)he can wield the Hammer...

from operator import add

avengers = 6

def vision(avengers):
	print(avengers)
	return avengers + 1

def hawkeye(thor, hulk):
	love = lambda black_widow: add(black_widow, hulk)
	return thor(love)

def hammer(worthy, stone):
	if worthy(stone) < stone:
		return stone
	elif worthy(stone) > stone:
		return -stone
	return 0

capt = lambda iron_man: iron_man(avengers)

"""
Expression | Interactive Output
>>> capt(vision) 
6
7
>>> print(print(1), vision(2))
1
2
None
3
>>> hawkeye(hammer, 3)
Error
>>> hawkeye(capt, 3)
9
>>> hammer(lambda ultron: ultron, -1)
0
>>> hammer(vision, avengers)
6
6
-6
"""


# 2. “You’ll get lost in there.” “C’mon! Think positive!”
# ...... SKIP ......



# 3. “After a long day of Turing tests, you gotta unwind.”

# (a)
def make_direction(secret):
	"""Returns a function that compares the guess to the secret.

	>>> direction = make_direction(40)
	>>> direction(50) # 40 is lower than 50
	-1
	>>> direction(13) # 40 is higher than 13
	1
	>>> direction(40) # 40 is equal to 40
	0
	"""
	def direction(attempt):
		if secret < attempt:
			return -1
		elif secret > attempt:
			return 1
		else:
			return 0
	return direction



# (b)
def naive_search(low, high, direction):
	"""Guess the secret number, as specified by direction, in a naive way;
	returns the number of guesses made. Starts with an initial guess and
	moves up or down one number at a time.
	>>> count1 = naive_search(0, 100, make_direction(50))
	50
	>>> count1
	1
	>>> count2 = naive_search(0, 20, make_direction(14))
	10
	11
	12
	13
	14
	>>> count2
	5
	"""
	guess, count = (low + high) // 2, 1
	print(guess)
	sign = direction(guess)
	while sign != 0:
		guess = guess + sign
		count = count + 1
		sign = direction(guess)
		print(guess)
	return count

# (c)
# O(n) -> increment through only one direction until target



# (d)
def binary_search(low, high, direction):
	"""Guesses the secret number, as specified by direction, using binary
	search; returns the number of guesses made.

	>>> count1 = binary_search(0, 100, make_direction(50))
	50
	>>> count1
	1
	>>> count2 = binary_search(0, 100, make_direction(40))
	50
	25
	37
	43
	40
	>>> count2
	5
	"""
	guess = (low + high) // 2 # midpoint
	print(guess)
	sign = direction(guess)
	if sign == 0:
		return 1
	elif sign < 0:
		return 1 + binary_search(low, guess, direction)
	else:
		return 1 + binary_search(guess, high, direction)

# (e)
# O(log n)



# 4. “A highly intelligent animal.”

# (a)
def subset_sum(target, lst):
	"""Returns True if it is possible to add some of the integers in lst
	to get target.

	>>> subset_sum(10, [-1, 5, 4, 6])
	True
	>>> subset_sum(4, [5, -2, 12])
	False
	>>> subset_sum(-3, [5, -2, 2, -2, 1])
	True
	>>> subset_sum(0, [-1, -3, 15]) # Sum up no numbers to get 0
	True
	"""
	if target == 0:
		return True
	elif not lst:
		return False
	else:
		a = subset_sum(target-lst[0], lst[1:])
		b = subset_sum(target, lst[1:])
		return a or b 



# (b)
def intersection(lst_of_lsts):
	"""Returns a list of elements that appear in every list in
	lst_of_lsts.
	>>> lsts1 = [[1, 2, 3], [1, 3, 5]]
	>>> intersection(lsts1)
	[1, 3]
	>>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
	>>> intersection(lsts2)
	[4]
	>>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
	>>> intersection(lsts3) # No number appears in all lists
	[]
	"""
	elements = []
	for ele in lst_of_lsts[0]:
		condition = True
		for lst in lst_of_lsts[1:]:
			if ele not in lst:
				condition = False
		if condition:
			elements = elements + [ele]
	return elements



# (c)
def sandwich(n):
	"""Return True if n contains a sandwich and False otherwise
	
	>>> sandwich(416263) # 626
	True
	>>> sandwich(5050) # 505 or 050
	True
	>>> sandwich(4441) # 444
	True
	>>> sandwich(1231)
	False
	>>> sandwich(55)
	False
	>>> sandwich(4456)
	False
	"""
	tens, ones = n // 10 % 10, n % 10
	n = n // 100
	while n != 0:
		if ones == n % 10:
			return True
		else:
			tens, ones = n % 10, tens
			n = n // 10
	return False