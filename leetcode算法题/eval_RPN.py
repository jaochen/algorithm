# coding: utf-8
'''
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        token = ["+", "-", "*", "/"]
        
        stack = []
        for i in tokens:
            if i in token:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                
                if i == "+":
                    result = num1 + num2
                elif i == "-":
                    result = num1 - num2
                elif i == "*":
                    result = num1 * num2
                elif i == "/":
                    # python的 b / a 会向下取整， 比如 -1 / 132 = -1。 
                    # 题目要求是取整数部分，那么负数的时候，实际应该是向上取整， 解决方法： int(b / float(a))
                    # python3 b / a 会转为小数计算，所以直接 int(b / a)， 不能 b // a
                    result = int(num1 / float(num2))
                    
                stack.append(result)
                
            else:
                stack.append(i)
            
        return int(stack[-1])
                