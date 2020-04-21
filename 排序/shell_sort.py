'''
希尔排序
'''

def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len // 2
    while gap > 0:
        # 插入排序
        for i in range(gap, nums_len):
            num = nums[i]
            pre = i - gap
            while pre >=0 and nums[pre] > num:
                nums[pre+gap] = nums[pre]
                pre -= gap
            
            nums[pre+gap] = num

        gap = gap // 2

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    shell_sort(nums)
    print(nums)