'''
冒泡排序
'''
def bubble_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len - 1):
        for j in range(0, nums_len-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            # print(nums)


if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8,9, 7, 12]
    bubble_sort(nums)
    print(nums)