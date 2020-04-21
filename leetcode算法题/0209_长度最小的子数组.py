'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

# 思路： 滑动窗口算法
'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = 0
        
        nums_sum = sum(nums)
        if nums_sum < s:
            return 0
                
        nums_len = len(nums)
        if nums_sum == s:
            return nums_len

        # l、r 为窗口左右指针
        # 如果不满足条件，窗口扩大（r+1）
        # 如果满足条件，窗口缩小（l+1）
        # 要保证l、r不越界
        l = l_r_sum = 0
        r = -1
        while l < nums_len:
            print("l: {}, r: {}, sum: {}".format(l, r, l_r_sum))
            
            if r+1 < nums_len and l_r_sum < s:
                r += 1
                l_r_sum += nums[r]
            
            else:
                l_r_sum -= nums[l]
                l += 1
            
            if l_r_sum >= s:
                if result == 0:
                    result = r-l+1
                else:
                    result = min(result, r-l+1)
        
        return result
                