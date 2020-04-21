'''
归并排序
'''

def merge_sort(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums
    
    middle = nums_len // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    
    return merge(left, right)

def merge(left, right):
    result = []

    left_len = len(left)
    right_len = len(right)
    l_num = r_num = 0

    while l_num < left_len and r_num < right_len:
        if left[l_num] < right[r_num]:
            result.append(left[l_num])
            l_num += 1
        
        else:
            result.append(right[r_num])
            r_num += 1
    
    while l_num < left_len:
        result.append(left[l_num])
        l_num += 1
    while r_num < right_len:
        result.append(right[r_num])
        r_num += 1
    
    return result

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    print(merge_sort(nums))