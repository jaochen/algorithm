'''
快速排序
'''
def quick_sort(nums, left, right):

    if left < right:
        par = partition(nums, left, right)
        # print(par)
        # print(nums)
        quick_sort(nums, left, par-1)
        quick_sort(nums, par+1, right)

    return nums

def partition(nums, left, right):
    pivot = nums[left]
    l = left
    r = right

    # print("{}, {}, {}".format(l, r, pivot))
    # 循环终止条件 -》l == r
    while l < r:
        while l < r and nums[r] > pivot:
            r -= 1
        nums[l] = nums[r]

        while l < r and nums[l] < pivot:
            l += 1
        nums[r] = nums[l]
    
    nums[l] = pivot
    return l

if __name__ == '__main__':
    nums = [3, 5, 1, 4, 6, 8, 9, 7, 12, 2]
    print(quick_sort(nums, 0, len(nums)-1))