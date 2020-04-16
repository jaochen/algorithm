'''
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

顺着输出走一遍，代码逻辑就很清晰了，如下
'''

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if not matrix:
            return result
        
        first_len = len(matrix)
        second_len = len(matrix[0])
        
        # 总共需要遍历M+N-1次
        # 从0，0开始遍历，n%2==0,方向向上，n%2==1方向向下
        i = 0
        j = 0
        for n in range(first_len+second_len-1):
            result.append(matrix[i][j])
            # 向右上角，i-1, j+1
            if n % 2 == 0:
                while i-1 >= 0 and j+1 < second_len:
                    i -= 1
                    j += 1
                    result.append(matrix[i][j])

                # 边界情况, 如果碰到了边界，就下移，否则右移
                if j+1 == second_len:
                    i += 1
                else:
                    j += 1
            
            # 向左下角，i+1, j-1
            else:
                while i+1 <first_len and j-1 >= 0:
                    i += 1
                    j -= 1
                    result.append(matrix[i][j])
                    
                # 边界情况，如果碰到了边界，就右移，否则下移
                if i+1 == first_len:
                    j += 1
                else:
                    i += 1
        
        return result
                    