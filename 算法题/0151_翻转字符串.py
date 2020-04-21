'''
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # result = s.split()
        # return " ".join(result[::-1])
        
        result = []
        
        right = len(s) - 1
        left = right
        # 从右往左找
        while left >= 0:
            # 找到右边第一个单词
            while left >= 0 and s[left] == ' ':
                left -= 1
            right = left
             
            while left >= 0 and s[left] != ' ':
                left -= 1
            
            sub_s = s[left+1:right+1]
            if sub_s:
                result.append(sub_s)
            # print(result)
            
        return " ".join(result)
       
                