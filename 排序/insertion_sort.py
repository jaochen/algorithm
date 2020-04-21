'''
插入排序
'''

def insertion_sort(nums):
    for i in range(1, len(nums)):
        num = nums[i]
        pre = i-1
        while pre >= 0 and nums[pre] > num:
            nums[pre+1] = nums[pre]
            pre -= 1
        
        nums[pre+1] = num


if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    insertion_sort(nums)
    print(nums)