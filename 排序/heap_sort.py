'''
堆排序
'''
def heap_sort(nums):
    # print(nums)
    nums_len = len(nums)
    build_max_heap(nums)
    # print(nums)
    arr_len = nums_len
    for i in range(nums_len-1, 0, -1):
        # print("arr_len: {}, swap: {}: {}, {}: {}".format(arr_len, i, nums[i], 0, nums[0]))
        nums[i], nums[0] = nums[0], nums[i]
        arr_len -= 1
        heapify(nums, 0, arr_len)

        # print("heapify result: {}".format(nums))


def build_max_heap(nums):
    '''
    构建大顶堆
    从最后一个非叶子节点开始调整
    '''
    nums_len = len(nums)
    for i in range((nums_len-1) // 2, -1, -1):
        heapify(nums, i, nums_len)

def heapify(nums, index, nums_len):
    '''
    调整堆
    '''
    # print("index: {}, nums_len: {}".format(index, nums_len))

    left = 2*index + 1
    right = 2*index + 2
    largest = index

    if left < nums_len and nums[left] > nums[largest]:
        largest = left
    
    if right < nums_len and nums[right] > nums[largest]:
        largest = right
    
    if largest != index:
        nums[largest], nums[index] = nums[index], nums[largest]
        # print(nums)
        # 继续调整交换后的叶子节点
        heapify(nums, largest, nums_len)
    

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    heap_sort(nums)
    print(nums)
