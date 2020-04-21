'''
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:
1、数组非空，且长度不会超过20。
2、初始的数组的和不会超过1000。
3、保证返回的最终结果能被32位整数存下。
'''
from functools import reduce

class Solution(object):
    def __init__(self):
        self.count = 0
            
    # 暴力列举 时间复杂度为O(2^n)
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # nums_sum = reduce(lambda x, y: x+y, nums)
        nums_sum = sum(nums)
        if nums_sum < S or (nums_sum+S) % 2 != 0:
            return 0
        
        self.DFS(nums, 0, 0, S)
        
        return self.count
    
    def DFS(self, nums, index, sum, S):
        if len(nums) == index:
            if sum == S:
                self.count += 1
                
        else:
            num = nums[index]
            self.DFS(nums, index+1, sum+num, S)
            self.DFS(nums, index+1, sum-num, S)
    # 暴力列举 end

    # 二维数组 动态规划
    # 优化，公式推导 + 动态规划
    # 公式推导：将数组分成两部分，正数部分（+）和负数部分（-）
    # sum(+) + sum(-) = sum(nums)         
    # sum(+) - sum(-) = S
    # 两条等式相加，有 2 * sum(+) = S + sum(nums)
    # 即需要满足： S+sum(nums) % 2 == 0 && sum(nums) > S
    # 
    # 问题转化为求： nums中加起来等于sum(+)的子集个数
    def opt_findTargetSumWays(self, nums, S):
        """
        :type nums: list[int]
        :type S: int
        :rtype: int
        """
        # nums_sum = reduce(lambda x, y: x+y, nums)
        nums_sum = sum(nums)
        if nums_sum < S or (nums_sum+S) % 2 != 0:
            return 0
        
        # 正数和
        positive_sum = (nums_sum + S) // 2
        opt = [([0] * (positive_sum+1)) for i in range(len(nums))]
        # print(opt)

        # 初始化opt数组
        for i in range(len(nums)):
            opt[i][0] = 1
        # print(opt)

        for i in range(len(nums)):
            # nums为非负数，所以第一行得通过计算
            for j in range(positive_sum+1):
                if nums[i] == 0:
                    opt[i][j] = opt[i-1][j] + opt[i-1][j]
                elif i == 0 and nums[i] == j:
                    opt[i][j] = 1
                elif nums[i] > j:
                    opt[i][j] = opt[i-1][j]
                else:
                    opt[i][j] = opt[i-1][j-nums[i]] + opt[i-1][j]
                    
        # print(opt)
        return opt[-1][-1]
    
    # 一维数组 动态规划
    def one_opt_findTargetSumWays(self, nums, S):
        sumup = sum(nums)
        if sumup < S or (sumup + S) % 2:
            return 0
        w = (sumup + S) / 2
        
        dp = [0] * (w+1)
        dp[0] = 1
        
        for num in nums:
            for j in range(w, num-1, -1):
                dp[j] += dp[j - num]
                
        return dp[w]

if __name__ == "__main__":
    print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
    print(Solution().opt_findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 1))
    print(Solution().opt_findTargetSumWays([1, 1, 1, 1, 1], 1))
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().opt_findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().findTargetSumWays([40,2,49,50,46,6,5,23,38,45,45,17,4,26,40,33,14,9,37,24], 7))
    print(Solution().opt_findTargetSumWays([40,2,49,50,46,6,5,23,38,45,45,17,4,26,40,33,14,9,37,24], 7))