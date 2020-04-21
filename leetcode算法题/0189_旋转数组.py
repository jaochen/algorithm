class Solution:

    # 双重循环，O(k*n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k %= nums_len
        
        for i in range(k):
            tmp = nums[-1]
            for i in range(nums_len-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = tmp
            
            # print(nums)

    # 翻转
    def rotate2(self, nums, k):
        nums_len = len(nums)
        k %= nums_len
        
        self.reverse(nums, 0, nums_len-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, nums_len-1)
        
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1