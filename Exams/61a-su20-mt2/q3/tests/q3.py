test = {
  'name': 'q3',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
