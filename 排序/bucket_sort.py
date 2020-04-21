'''
桶排序
'''

def bucket_sort(nums, bucket_size=5):
    '''
    :param bucket_size: 桶容量
    '''
    nums_len = len(nums)

    min_num = nums[0]
    max_num = nums[0]
    for i in nums:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    
    bucket_count = (max_num-min_num) // bucket_size + 1
    buckets = [[] for i in range(bucket_count)]

    for i in nums:
        buckets[i // bucket_size].append(i)
    
    print(buckets)

    for i in range(len(buckets)):
        if buckets[i]:
            buckets[i] = sorted(buckets[i])
    
    print (buckets)

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    print(bucket_sort(nums))


