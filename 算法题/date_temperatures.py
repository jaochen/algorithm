# coding: utf-8
'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''

class Solution(object):
    # 暴力方法。事件复杂度O(n^2)
    # def dailyTemperatures(self, T):
    #     """
    #     :type T: List[int]
    #     :rtype: List[int]
    #     """
    #     result = []
    #     for i in range(len(T)):
    #         result.append(0)
        
    #     for i in range(len(T)):
    #         count = 0
    #         for j in range(i+1, len(T)):
    #             count += 1
    #             if T[j] > T[i]:
    #                 result[i] = count
    #                 break
        
    #     return result
    
    # 利用栈的特点，时间复杂度O(n)
    def dailyTemperatures(self, T):

        result = [0] * len(T)
        
        stack = []
        for index, i in enumerate(T):
            
            while stack and stack[-1][1] < i:
                num = stack.pop()[0]
                result[num] = index - num
                
            stack.append((index, i))
            
        return result
        