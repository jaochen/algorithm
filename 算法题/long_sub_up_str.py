# coding: utf-8
'''
最长升序子序列
'''

def LIS(str_list):
    list_len = len(str_list)

    dp = [1, ]
    max_len = 1

    for index in range(1, list_len):
        dp.append(0)
        max = 1
        change_flag = False

        for i in range(index):
            if(str_list[index] >= str_list[i] and dp[i] >= max):
                change_flag = True
                max = dp[i]

        if change_flag:
            dp[index] = max + 1

            if dp[index] > max_len:
                max_len = dp[index]

        else:
            dp[index] = 1

    print max_len

if __name__ == '__main__':

    # 5
    LIS([2, 4, 6, 3, 5, 7, 9, 8])
    # 8
    LIS([1, 2, 3, 4, 5, 4, 3, 2, 5, 6, 7])
    # 4
    LIS([1, 2, 3, 4])
    # 4
    LIS([1, 1, 1, 1])
    # 7
    LIS([9, 8, 1, 2, 3, 4, 5, 6, 7])
