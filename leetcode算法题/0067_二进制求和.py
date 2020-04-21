'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        
        a_index = len(a) - 1
        b_index = len(b) - 1
        
        add = False
        while a_index >=0 or b_index >= 0:
            add_flag = add
            add = False
            
            a_s = a[a_index] if a_index >= 0 else '0'
            b_s = b[b_index] if b_index >= 0 else '0'
            
            s = '0'
            # 分情况讨论
            if a_s == '0' and b_s == '0':
                if add_flag:
                    s = '1'
                    
            elif a_s == '1' and b_s == '1':
                add = True
                if add_flag:
                    s = '1'
            
            # a、b其中一个为1，一个为0
            else:
                if add_flag:
                    add = True
                else:
                    s = '1'
                    
            a_index -= 1
            b_index -= 1
            result.append(s)
        
        if add:
            result.append('1')
            
        return ''.join(result[::-1])
            