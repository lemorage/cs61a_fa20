# 1. Down for the Count

def count(element, box):
   """Count how many times digit element appears in integer box.

   >>> count(2, 222122)
   5
   >>> count(0, -2020)
   2
   >>> count(0, 0)  # 0 has no digits
   0
   """
   assert element >= 0 and element < 10
   box = abs(box) # (a)
   total = 0
   while box > 0:
      if box % 10 == element: # (b)
         total = total + 1 # (c)
      box = box // 10
   return total



def count_nine(element, box):
   """Count how many times digit element appears in the non-negative integer
   box in a place that is not next to a 9.

   >>> count_nine(2, 222122)
   5
   >>> count_nine(1, 1911191) # Only the middle 1 is not next to a 9
   1
   >>> count_nine(9, 9)
   1
   >>> count_nine(9, 99)
   0
   >>> count_nine(3, 314159265359)
   2
   >>> count_nine(5, 314159265359)
   1
   >>> count_nine(9, 314159265359)
   2
   >>> count_nine(0, 0) # No digits are in 0
   0
   """
   assert element >= 0 and element < 10
   assert box >= 0
   nine, total = False, 0
   while box > 0:
      if box % 10 == element and not (nine or box // 10 % 10 == 9): # (a) (b)
         total = total + 1 # (c)
      nine = box % 10 == 9 # (d)
      box = box // 10
   return total



def fit(pegs, holes):
   """Return whether every digit in pegs appears at least as many times in
   holes as it does in pegs.

   >>> fit(123, 321)    # Each digit appears once in pegs and in holes.
   True
   >>> fit(1213, 33221) # 1 appears twice in pegs, but only once in holes.
   False
   >>> fit(12, 22)      # 1 appears once in pegs, but not at all in holes.
   False
   >>> fit(314159, 112233456789)
   True
   """ 
   i = 0
   while i <= 9: # (a)
      if count(i, pegs) > count(i, holes): # (b)
         return False # (c)
      i = i + 1
   return True # (d)



# 2. Mystery Function

def add_two(y):
   return y + 2

def two(y):
   return 2

def constant(k):
   def ignore(x):
      return k
   return ignore

def diff(f, g):
   return lambda z: abs(f(z) - g(z))

def mystery(n):
   return n

# (a) ... two 
# constant(2) and two are both functions with identical behavior (return 2).

# (b) ... constant(2)
# Ditto.

# (c) ... constant(0)
# Ditto.

# (d) ... lambda y: abs(mystery(y))
# After simplifying, the given function is actually lambda z: abs(mystery(z) - 0).


# 3. Please Register to Vote

def vote(vote):
   please = lambda nov: vote(nov) + third # (a)
   third = ty + 3 # (b)
   return please
ty = 1
register = vote(lambda nov: nov + ty) # (c)
ty = 3 # (d)
register(ty * 10) or register(30) # (e)



# 4. Amazing Job Growth

def growth(baseline):
   """Return a function that can be called repeatedly on numbers and prints
   the difference between its argument and the smallest argument used so far
   (including baseline).

   >>> job = growth(148)(149)(150)(130)(133)(139)(137)
   1
   2
   0
   3
   9
   7
   """
   def increase(observed):
      under = min(baseline, observed) # (a)
      print(observed - under)
      return growth(under) # (b)
   return increase



def square(x):
   return x * x

def maxer(smoke):
   """Return a repeatable function fire(y) that prints the largest smoke(y) so far.
   >>> g = maxer(square)
   >>> h = g(2)(1)(3)(2)(-4)  # print the largest square(y) so far
   4
   4
   9
   9
   16
   >>> h = maxer(abs)(2)(1)(3)(2)(-4)  # print the largest abs(y) so far
   2
   2
   3
   3
   4
   """
   def fire(y):
      print(smoke(y)) # (a)
      def haze(z):
         if smoke(y) > smoke(z): # (b)
            z = y
         return fire(z) # (c)
      return haze
   return fire



# Review cs61a-fa18-mt1 q6
####################################################
# detector works like that:
   # have_seen0 = lambda j: False
   # have_seen1 = lambda j: j == 1 or have_seen0(j)
   # have_seen2 = lambda j: j == 7 or have_seen1(j)
   # ...
####################################################

def repeat(k):
   """When called repeatedly, print each repeated argument.
   >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
   7
   1
   5
   1
   """
   return detector(lambda j: False)(k)

def detector(f):
   def g(i):
      if f(i):
         print(i)
      return detector(lambda j: j == i or f(j))
   return g
