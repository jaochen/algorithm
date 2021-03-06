# coding: utf-8
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        for i in s:
            if i in mapping:
                stack.append(i)
            elif stack and stack[-1] in mapping and i == mapping[stack[-1]] :
                stack.pop()
            else:
                return False
            
        return not stack