from time import time

from rich import print

def cascading(nums:list[int]) -> list[list[int]]:
    '''
    This is a 2^n running time algorithm for computing the power set
    :param nums: list of integers
    :return: list of list of integers
    '''
    res = [[]]
    for i in nums:
        for a in res.copy():
            res.append(a + [i])
    return res

def back_tracking(nums : list) -> list[list[int]]:
    '''
    This is a 2^n running time algorithm for computing the power set
    :param nums: list of integers
    :return: list of list of integers
    '''
    res = []
    def dfs(cur = [], i = 0):
        res.append(cur)
        for j, n in enumerate(nums[i:], i):
            dfs(cur + [n], j + 1)
    dfs()
    return res

def time_it(n: int) -> None:
    t1 = time()
    cascading(list(range(n)))
    print(f'Time to compute the power set of {n} item is {time() - t1}')
if __name__ == '__main__':
    nums = [1,2,3]
    print(cascading(nums))
    print(back_tracking(nums))

    for i in range(30): time_it(i)

