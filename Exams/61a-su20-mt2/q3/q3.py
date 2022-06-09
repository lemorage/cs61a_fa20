email = 'example_key'

"""A: (2 pts) Implement sum_link, which takes a Link instance s and a
one-argument function transform that takes an element of s and returns a number.
The sum_link function returns the sum of the results of calling transform on
each element of the linked list s.

Check the doctests with: python3 ok -q a
"""
def sum_link(s, transform):
    """Sum the result of calling transform on each element of Link s.

    >>> s = Link(3, Link(5, Link(7)))
    >>> sum_link(s, lambda x: x)       # 3 + 5 + 7
    15
    >>> double = lambda x: 2 * x
    >>> sum_link(s, double)            # double(3) + double(5) + double(7)
    30
    >>> sum_link(Link.empty, double)
    0

    >>> sum_link(Link(2, Link(6)), lambda x: x * x)
    40
    """
    if not s:
        return 0
    else:
        return transform(s.first) + sum_link(s.rest, transform)


"""B: (3 pts) Implement CreditCard, a class whose methods are described below.

Check the doctests with: python3 ok -q b
"""
class CreditCard:
    """A CreditCard.

    >>> c = CreditCard(50)
    >>> c.purchase(5)      # 45 remaining
    45
    >>> c.purchase(30)     # now only 15 remaining
    15
    >>> c.purchase(30)
    'declined'
    >>> c.pay_bill()       # current balance is 35
    35
    >>> c.purchase(30)     # 20 remaining
    20
    >>> [CreditCard(10), CreditCard(20, 5)]
    [CreditCard(10, 0), CreditCard(20, 5)]

    >>> d = CreditCard(100)
    >>> d.purchase(10)
    90
    >>> d.purchase(60)
    30
    >>> d.purchase(60)
    'declined'
    >>> d.pay_bill()
    70
    >>> d.purchase(60)
    40
    """

    def __init__(self, maximum, balance=0):
        """A CreditCard is constructed from a maximum and an optional balance,
        which defaults to 0. The maximum represents the greatest value that
        balance is allowed to take after a purchase.
        """
        assert balance <= maximum
        self.maximum = maximum
        self.balance = balance

    def purchase(self, price):
        """When the CreditCard is used to make a purchase, the purchase price
        is added to the balance unless the purchase is declined. A purchase is
        declined if the result of adding the price to the current balance would
        exceed the maximum. If the purchase is not declined, return the highest
        price of the next purchase that would not be declined.
        """
        assert price > 0
        if self.balance + price > self.maximum:
            return 'declined'
        self.balance += price
        return self.maximum - self.balance

    def pay_bill(self):
        """Reduce the balance to 0 and return the value of the balance before
        it was reset to 0.
        """
        prev = self.balance
        self.balance = 0
        return prev

    def __repr__(self):
        return 'CreditCard(' + repr(self.maximum) + ', ' + repr(self.balance) + ')'


"""C: (4 pts) Implement Wallet, a class whose methods are described below.

Check the doctests with: python3 ok -q c
"""
class Wallet:
    """A Wallet with a linked list of CreditCards.

    >>> a = Wallet(Link(CreditCard(1000), Link(CreditCard(2000))))
    >>> a.total_available
    3000
    >>> a.procure(10).procure(30).procure(1000).procure(160)
    Wallet(Link(CreditCard(1000, 200), Link(CreditCard(2000, 1000))))
    >>> a.total_available
    1800
    >>> a.procure(1500)
    'No CreditCard can purchase an item of that price.'

    >>> b = Wallet(Link(CreditCard(10), Link(CreditCard(20), Link(CreditCard(30)))))
    >>> b.total_available
    60
    >>> b.procure(20).procure(10).procure(20)
    Wallet(Link(CreditCard(10, 10), Link(CreditCard(20, 20), Link(CreditCard(30, 20)))))
    """
    def __init__(self, s):
        """A Wallet is constructed from a linked list of CreditCard instances s.
        """
        assert s is Link.empty or isinstance(s, Link)
        self.cards = s

    @property
    def total_available(self):
        """The sum of the difference between the maximum and balance for all
        CreditCards held by the Wallet.
        """
        return sum_link(self.cards, lambda card: card.maximum - card.balance)

    def procure(self, price):
        """Attempt to purchase at price using each CreditCard in order, continuing
        as long as the purchase is declined. Return the Wallet if procure resulted
        in a successful purchase for one of the CreditCards, or otherwise return
        a string describing that no CreditCard can purchase at that price.

        IMPORTANT: The price cannot be split between multiple CreditCards.
        """
        cards = self.cards
        while cards:
            if cards.first.purchase(price) != 'declined':
                return self
            cards = cards.rest
        return 'No CreditCard can purchase an item of that price.'

    def __repr__(self):
        return 'Wallet(' + repr(self.cards) + ')'

##############################
# NO FURTHER QUESTIONS BELOW #
##############################

class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

