test = {
  'name': 'q2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_power(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
          True
          
          >>> is_power(5, 1)    # pow(5, 0) = 1
          True
          
          >>> is_power(5, 5)    # pow(5, 1) = 5
          True
          
          >>> is_power(5, 15)   # 15 is not a power of 5 (it's a multiple)
          False
          
          >>> is_power(3, 9)
          True
          
          >>> is_power(3, 8)
          False
          
          >>> is_power(3, 10)
          False
          
          >>> is_power(1, 8)
          False
          
          >>> is_power(2, 0)    # 0 is not a power of any positive base.
          False
          
          >>> is_power(4, 16)
          True
          
          >>> is_power(4, 64)
          True
          
          >>> is_power(4, 63)
          False
          
          >>> is_power(4, 65)
          False
          
          >>> is_power(4, 32)
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(powers(12345, 5))
          [1, 5, 25, 125]
          
          >>> sorted(powers(54321, 5))  # 25 and 125 are not in order
          [1, 5]
          
          >>> sorted(powers(2493, 3))
          [3, 9, 243]
          
          >>> sorted(powers(2493, 2))
          [2, 4]
          
          >>> sorted(powers(164352, 2))
          [1, 2, 4, 16, 32, 64]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
