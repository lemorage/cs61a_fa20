test = {
  'name': 'q1',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
          [4, 3, 2, 1]
          
          >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
          True
          
          >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
          
          >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
          True
          
          >>> o.index(3) < o.index(2)                                       # and 3 before 2,
          True
          
          >>> o[4:]                                                         # and 1 at the end.
          [1]
          
          >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> b0 = Tree(2, [Tree(3, [Tree(4), Tree(5)])])
          
          >>> b1 = Tree(6, [Tree(7), Tree(8, [Tree(9)])])
          
          >>> t = Tree(1, [b0, b1])
          
          >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)
          'success!'
          
          >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)
          'success!'
          
          >>> pluck(t)(2)
          'Hey, not valid!'
          
          >>> pluck(t)(5)(9)(7)(6)
          'Hey, not valid!'
          
          >>> pluck(b0)(5)(2)
          'Hey, not valid!'
          
          >>> pluck(b0)(4)(5)(3)(2)
          'success!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
