'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''

class Solution:
    # 递归解法
    def plusOne(self, digits: List[int]) -> List[int]:
        def addOne(index):
            nonlocal digits
            # 两种情况，一种是9，需要进位，另一种加就完事了
            if digits[index] == 9:
                digits[index] = 0
                if index != 0:
                    addOne(index-1)
                else:
                    digits = [1] + digits
            else:
                digits[index] += 1
            
        addOne(len(digits)-1)
        
        return digits
    
    # 迭代解法
    def plusOne2(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        while n >= 0:
            digits[n] += 1
            digits[n] %= 10
            if digits[n] != 0:
                return digits
            n -= 1
        return [1] + digits
    