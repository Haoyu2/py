import collections
import heapq


class Solution:
    def maxRunTime(self, n: int, batteries) -> int:

        if n == 1: return sum(batteries)
        M = len(batteries)
        if M == n: return min(batteries)
        
        batteries = [-i for i in batteries]
        batteries.sort()
        res = 0
        while len(batteries) >= n:

            for i in range(n):
                cur = heapq.heappop(batteries) + 1
                if cur < 0: heapq.heappush(batteries, cur)
            res += 1

            print(batteries)

        return res

        # batteries = [-i for i in batteries]
        # batteries.sort()
        # res = 0
        # while len(batteries) >= n:
        #     print(batteries)
        #     cur = []; ma = 0
        #     for i in range(n):
        #         cur.append(heapq.heappop(batteries))
        #         ma = max(ma, cur[-1])
        #     res -= ma
        #     for j in cur:
        #         j += ma
        #         if j < 0: heapq.heappush(batteries, j)
        #
        # return res


solution = Solution()
a =  [3,3,3] # 157
b = [10,10,3,5] # 3， 8
c = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(solution.maxRunTime(3, b))
print(solution.maxRunTime(2, a))