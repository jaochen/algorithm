'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1, 1]
        
        result = [1 for i in range(rowIndex+1)]
        
        for i in range(1, rowIndex):
            # 从后往前算，因为后面的值需要用到前面的
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j-1]
            print (result)
            
        return result