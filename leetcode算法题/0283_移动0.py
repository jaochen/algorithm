'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 插入排序方法
        # index = 1
        # for index in range(1, len(nums)):
        #     if nums[index] != 0:
        #         tmp = nums[index]
        #         i = index-1
        #         while i >= 0 and nums[i] == 0:
        #             nums[i+1] = nums[i]
        #             i -= 1
        #         nums[i+1] = tmp
        
        # 双指针解法
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1
            