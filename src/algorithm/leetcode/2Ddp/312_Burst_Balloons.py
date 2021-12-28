# https://leetcode.com/problems/burst-balloons/
def maxCoins(nums: list[int])->int:
    '''

    :param nums:
    :return:
    '''
    N = len(nums)
    dp = [[0] * N for i in range(N)]

    for l in range(1, N + 1):
        for i in range(N):
            for j in range(i, l - i):
                # we are iterating the last burst item
                # and left and right of the last
                # burst item is certain
                left_b = 1 if i - 1 < 0 else nums[i-1]
                right_b = 1 if i + l >= N else nums[i + l]
                left_coins = 0 if i == j else dp[i][j-1]
                right_coins = 0 if i + l - 1 >= N or j + 1 == N else dp[j + 1][i + l - 1]
                dp[i][j] =  max(dp[i][j], left_coins + right_coins + left_b* right_b * nums[j])
    return dp[0][-1]


