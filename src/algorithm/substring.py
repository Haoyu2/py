def right_rotate_by_k_in_place(nums:list[int], k) ->None:
    '''

    :param nums:
    :return:
    '''
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def all_rotations(s: str) -> list[str]:
    '''

    :param s:
    :return:

    :: eg
    >>> print(all_rotations('abc'))
    ['abc', 'bca', 'cab']
    '''
    l, s = len(s), s*2
    return [s[i: l + i] for i in range(l)]


def repeatedSubstringPattern_qudratic(s: str) -> bool:
    '''

    :param s:
    :return: True or False
    eg::
        s = "abab" is "0123"
        so s + s = "abababab" = "01230123".
        Removing the first and the last element, we have ss = "bababa" = "123012".
        If you notice that, ss contains all of the rotation of s for 0 < k < len(s)
            "baba" = "1230" = rotateLeft(s, 1)
            "abab" = "2301" = rotateLeft(s,2)
            "baba" = "3012" = rotateLeft(s,3 )
        If any of the above rotation is equal to s, we found our smallest k rotation
        which equals the old string

    '''
    if not s: return False
    for j in range(1, len(s) // 2 + 1):
        if s[:j] * (len(s) // j) == s: return True
    else:
        return False


def repeatedSubstringPattern(s: str) -> bool:
    '''
    If these is a repeated substring pattern, suppose the length is k
    then after a k rotation, the new string should equal to the old string
    if not, there is not this repeated substring pattern.

    And this k is smaller than half of the length

    :param s:
    :return:
    .. _target to  repeatedSubstringPattern

    repeatedSubstringPattern
    ~~~~~~~~~~~~~~~~~~~~~~~~
    This is a O(n) function for computer repeat substring componet
    eg::
    >>> repeatedSubstringPattern('abab')
    True
    >>> repeatedSubstringPattern('aba')
    False
    >>> repeatedSubstringPattern('abcabcabcabc')
    True

    '''
    if not s:        return False
    ss = (s + s)[1:-1]
    return ss.find(str) != -1

def reverse_words_in_place(s:str) ->None:
    '''
    Reverse the whole string and then reverse each word
    :param s:
    :return:
    :: eg:
    >>> print(reverse_words_in_place(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
    ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    '''
    s[:] = s[::-1]
    i = 0
    for j, c in enumerate(s):
        if c == ' ':
            s[i: j] = s[i: j][::-1]  # j is ' '
            i = j + 1
    else:
        s[i: j + 1] = s[i: j + 1][::-1]  # j is length

if __name__ == '__main__':
    print(all_rotations('abc'))
