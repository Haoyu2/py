
def letter_distance_pattern(f: str)-> list[int]:
    res = [26] * 26
    idx = lambda c : ord(c) - ord('a')
    for c in f: res[idx(c)] = 0

    cur = idx(f[0]); start = 0
    for i in range(cur+1, cur + 26):
        i %= 26
        if res[i] == 0: start = 0
        else:
            start += 1; res[i] = start
    start = 0
    for i in range(cur - 1, cur - 26, -1):
        if i < 0: i += 26
        if res[i] == 0: start = 0
        else:
            start += 1
            res[i] = min(res[i],start)

    return res


def transform_the_string(s: str, f:str) -> int:
    '''

    :param s:
    :param f:
    :return:
    '''
    dp = letter_distance_pattern(f)
    res = 0
    for c in s: res += dp[ord(c) - ord('a')]
    return res

    pass
if __name__ == '__main__':
    print(letter_distance_pattern("abg"))
    print(transform_the_string('pqrst' ,'ou'))