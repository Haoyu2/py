def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    '''
    https://leetcode.com/problems/text-justification/
    1. pack as many words as possible in each line in sequence
    2. pad extra spaces ' ' evenly as possible
        1. the empty slots on the left will be assigned more spaces than the slots on the right.
    :param self:
    :param words:
    :param maxWidth:
    :return: list[str]
    '''

    def format_line(ws: list[str], cur_w: int, w: int = maxWidth) -> str:
        '''

        :param ws:
        :param w:
        :return:
        '''
        if len(ws) == 1:
            return ws[0] + ' ' * (w - cur_w)

        a, b = divmod(w - cur_w, len(ws) - 1)
        res = []
        for i, w in enumerate(ws[:-1]):
            if i < b:
                res.append(w + ' ' * (a + 1))
            else:
                res.append(w + ' ' * (a))
        res.append(ws[-1])
        return ' '.join(res)

    res = []
    cur = []
    cur_w = 0
    for word in words:
        if cur_w + len(word) > maxWidth:
            res.append(format_line(cur, cur_w - 1))  # subtract the last empty space
            cur = [word]
            cur_w = len(word) + 1  # empty space
        elif cur_w + len(word) == maxWidth:
            cur.append(word)
            res.append(' '.join(cur))
            cur = [];
            cur_w = 0
        else:
            cur.append(word)
            cur_w += len(word) + 1
    else:
        if cur:
            cur = ' '.join(cur)
            res.append(cur + ' ' * (maxWidth - len(cur)))
    return res


if __name__ == '__main__':
    print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
