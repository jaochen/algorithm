'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        first_len = len(matrix)
        second_len = len(matrix[0])
        
        visit = [[False]*second_len for x in range(first_len)]
        result = [[-1]*second_len for x in range(first_len)]
        
        # 初始化，将matrix中为0的元素，距离置成0
        queue = []
        for i in range(first_len):
            for j in range(second_len):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    visit[i][j] = True
                    queue.append((i, j))
        
        while queue:
            new_queue = []
            for point in queue:
                sr = point[0]
                sc = point[1]
                val = result[sr][sc] + 1
                # 上
                if sr-1 >= 0 and not visit[sr-1][sc]:
                    result[sr-1][sc] = val
                    visit[sr-1][sc] = True
                    new_queue.append((sr-1, sc))
                # 下
                if sr+1 < first_len and not visit[sr+1][sc]:
                    result[sr+1][sc] = val
                    visit[sr+1][sc] = True
                    new_queue.append((sr+1, sc))
                # 左
                if sc-1 >= 0 and not visit[sr][sc-1]:
                    result[sr][sc-1] = val
                    visit[sr][sc-1] = True
                    new_queue.append((sr, sc-1))
                # 右
                if sc+1 < second_len and not visit[sr][sc+1]:
                    result[sr][sc+1] = val
                    visit[sr][sc+1] = True
                    new_queue.append((sr, sc+1))
                    
            queue = new_queue
        
        return result