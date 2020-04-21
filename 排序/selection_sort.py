'''
选择排序
'''

def selection_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len):
        min_num = i
        for j in range(i+1, nums_len):
            if nums[j] < nums[min_num]:
                min_num = j

        # print("{}, {}".format(i, min_num))
        if i != min_num:
            nums[min_num], nums[i] = nums[i], nums[min_num]
    

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    selection_sort(nums)
    print(nums)
