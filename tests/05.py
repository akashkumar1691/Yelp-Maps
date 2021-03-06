test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -3], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -2],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -2.5],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1) # Returns a pair of floats
          [0.0, -2.5]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1)
          [0.0, -3.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [0, 0],     [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, 1],     [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [101, 101], [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1)
          [34.0, 34.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1) # should be a pair of decimals
          [0.0, -3.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [0, 0],     [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, 1],     [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [101, 101], [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1) # should be a pair of decimals
          [34.0, 34.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import recommend
      >>> import tests.test_functions as test
      >>> test.swap_implementations(recommend) # don't violate abstraction!
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
