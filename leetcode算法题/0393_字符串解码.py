# coding: utf-8
'''
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

# 遍历字符
# if not ']':
#     放进栈
# else:
#     将字母出栈
#     将数字出栈
#     将 字母*数字 进栈 
'''
class Solution:
    def decodeString(self, s: str) -> str:
        nums = set([str(x) for x in range(10)])
        
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # 字母出栈
                char = ""
                n = stack.pop()
                while n != "[":
                    char = n + char
                    n = stack.pop()
                
                # 数字出栈
                num = ""
                while stack:
                    n = stack[-1]
                    if n not in nums:
                        break
                        
                    num = n + num
                    stack.pop()
                
                stack.append(int(num)*char)
                
        return "".join(stack)