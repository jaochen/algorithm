# coding: utf-8
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

解题思路：
1、将二维数组由外向内分成一圈圈
2、每圈拆分成上（从左往右）、右（从上往下）、下（从右往左）、左（从下往上）四条线，依次遍历
3、对每个圈重复第二步骤
'''

class Solution:
    def spiralOrder(self, matrix):
        result = []
        
        if not matrix:
            return result
        
        first_len = len(matrix)
        second_len = len(matrix[0])
        total = first_len * second_len
        
        num = (min(first_len, second_len) + 1 ) // 2
        # print("num1: {}, num2: {}".format(num1, num2))
        
        n = 0
        # 外层循环，num1表示有多少圈
        while n < num:

            # 从左往右遍历 边界
            right = second_len-1-n
            # 从上往下遍历 边界
            down = first_len-1-n
            # 从右往左遍历 边界
            left = n
            # 从下往上遍历 边界
            top = n-1
            
            # 向右 从 j -》 right
            for z in range(n, right+1):
                result.append(matrix[top+1][z])
            print("right: {}".format(result))
            
            # 向下 从 i+1 -》 down
            for z in range(n+1, down+1):
                result.append(matrix[z][right])
            print("down: {}".format(result))
            
            # 如果是单行情况，已经遍历完了
            if len(result) == total:
                break
                
            # 向左 从 right-1 -》 left
            for z in range(right-1, left-1, -1):
                result.append(matrix[down][z])
            print("left: {}".format(result))
            
            # 向上 从 down+1 -》 top
            for z in range(down-1, top+1, -1):
                result.append(matrix[z][left])
            print("up: {}".format(result))
                
            # print("result: {}, i: {}, J: {}, n: {}".format(result, i, j, n))
            n += 1
            
        return result


if __name__ == '__main__':
    # l = [[1,2,3],[4,5,6],[7,8,9]]
    # print(Solution().spiralOrder(l))
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))