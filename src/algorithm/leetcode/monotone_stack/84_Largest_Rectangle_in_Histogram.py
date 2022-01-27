#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
def max_area(heights:list[int]) -> int:
    '''
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
    复杂度分析：（同上）

    以下列出了单调栈的问题，供大家参考。

    序号	题目	题解
    1	42. 接雨水（困难）	暴力解法、优化、双指针、单调栈
    2	739. 每日温度（中等）	暴力解法 + 单调栈
    3	496. 下一个更大元素 I（简单）	暴力解法、单调栈
    4	316. 去除重复字母（困难）	栈 + 哨兵技巧（Java、C++、Python）
    5	901. 股票价格跨度（中等）	「力扣」第 901 题：股票价格跨度（单调栈）
    6	402. 移掉K位数字
    7	581. 最短无序连续子数组

    作者：liweiwei1419
    链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    :param heights:
    :return:
    '''
    if len(heights) == 1: return heights[0]
    A = [0] + heights + [0]
    ms = [0];
    res = 0
    for i, n in enumerate(A[1:], 1):
        while A[ms[-1]] > n:
            j = ms.pop()
            res = max(res, A[j] * (i - ms[-1] - 1))
        ms.append(i)
    return res