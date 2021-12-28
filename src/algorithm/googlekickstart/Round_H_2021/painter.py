'''
    Red + Yellow = Orange
    Red + Blue = Purple
    Yellow + Blue = Green
    Red + Yellow + Blue = Gray

    Pi will be one of {Y, B, G}.

    U = Uncolored
    R = Red
    Y = Yellow
    B = Blue
    O = Orange
    P = Purple
    G = Green
    A = Gray

'''


def paint(paints: list[str]) -> int:
    di = {'O': ['R', 'Y'], 'P': ['R', 'B'], 'G': ['Y', 'B'],
          'A': ['R', 'Y', 'B'], 'Y': ['Y'], 'B': ['B'], 'R': ['R']}
    colors = {'Y', 'B', 'R'}
    res = 0;
    A = [paints[0]]

    for p in paints:
        if p != A[-1]: A.append(p)
    for c in colors:
        unseen = True
        for p in A:
            if p == 'U':
                unseen = True
                continue
            if p == c or c in di[p]:
                if unseen:
                    res += 1
                    # print(c)
                    unseen = False
            else:
                unseen = True
    return res


def solve():
    n = int(input().strip())
    print(n)
    res = []
    for i in range(1, n+1):
        input();
        s = input().strip();
        n = paint(s)
        cur = f'Case #{i}: {n}'
        # print(cur)
        res.append(cur)
    i = 0
    print(len(res))
    with open('./test_data_painter/test_set_2/ts2_output.txt', 'r') as out:
        for line in out:
            # print(i)
            if line.strip() == '': continue
            if line.strip() != res[i%100]:  print(f'{line}  get:{res[i]}')
            i += 1


if __name__ == '__main__':
    # print(paint('YYYBBBYYY'))
    # print(paint('YYGGBB'))
    # print(paint('ROAOR'))
    print(paint('RRRRRRRRRR'))
    solve()
