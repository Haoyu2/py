# https://leetcode.com/problems/burst-balloons/
def maxCoins(nums: list[int]) -> int:
    '''

    :param nums:
    :return:
    '''
    if len(nums) > 1 and len(set(nums)) == 1:
        return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
    N = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (N + 2) for i in range(N + 2)]

    for l in range(1, N + 1):
        for i in range(1, N - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                # print(i, j, l)

                dp[i][j] = max(dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j])
    # print(dp)
    return dp[1][-2]


