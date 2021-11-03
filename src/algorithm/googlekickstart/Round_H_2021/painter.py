'''
    Red + Yellow = Orange
    Red + Blue = Purple
    Yellow + Blue = Green
    Red + Yellow + Blue = Gray

    Pi will be one of {Y, B, G}.
'''


def paint(nums: list[str]) -> int:
    di = {'O': ['R', 'Y'], 'P': ['R', 'B'], 'G': ['Y', 'B'],
          'A': ['R', 'Y', 'B']}
    color = {'Y', 'B', 'G'}
    res = 1; cur = nums[0]
    for c in nums:
        if c != cur:
            res += 1
            if c in color:
                cur = c
            else:
                pass


