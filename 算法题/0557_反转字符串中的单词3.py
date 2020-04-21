'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        result = list(s)
        s_len = len(s)
        right = 0
        while right < s_len:
            while right < s_len and s[right] == ' ':
                right += 1
            
            left = right
            while right < s_len and s[right] != ' ':
                right += 1
            
            self.reverse(result, left, right-1)
            # print(result)
            
        return "".join(result)
    
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            
                