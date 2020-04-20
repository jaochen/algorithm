'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        
        if not strs:
            return ""
        
        length = min([len(s) for s in strs])
        print(length)
        
        for i in range(length):
            c = strs[0][i]
            
            same = True
            for s in strs:
                if s[i] != c:
                    same = False
                    break
            
            print(same)
            if same:
                result.append(c)
            else:
                break
        
        return "".join(result)
            