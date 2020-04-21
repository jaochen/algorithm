'''
计数排序
'''
def counting_sort(nums):
    nums_len = len(nums)

    # 最大值最小值确定基数区间
    min_num = nums[0]
    max_num = nums[0]
    for i in nums:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i

    count_dict = {}
    for i in range(min_num, max_num+1):
        count_dict[i] = 0

    for i in nums:
        count_dict[i] += 1
    print (count_dict)

    result = []
    for i in count_dict:
        for j in range(count_dict[i]):
            result.append(i)
    
    return result

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    print(counting_sort(nums))