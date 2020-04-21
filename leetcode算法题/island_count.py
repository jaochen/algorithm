# coding: utf-8
'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
示例1:
    输入:
    11110
    11010
    11000
    00000

    输出: 1
示例2:
    输入:
    11000
    11000
    00100
    00011

    输出: 3

解题思路：
    这个问题其实是广度优先遍历的问题
    1、生成一个二维数组用作节点的已访问查询
    2、遍历整个二维数组，如果节点符合条件，将访问位制成1，将其添加进队列中。
    3、循环：将节点 上下左右 中符合条件的 添加进队列中 并标记访问

更优解决方案：
    总体思路一致
    感染思想：将访问位二位数组，替换成 将当前位制成“2”，降低访问位二维数组的查询消耗
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_num = 0
        
        first_len = len(grid)
        if first_len == 0:
            return 0
        
        second_len = len(grid[0])
        
        # 初始化节点访问列表
        visit_grid = []
        for i in range(first_len):
            visit_grid.append([])
            for j in range(second_len):
                visit_grid[i].append(False)
        
        for i in range(first_len):
            for j in range(second_len):
                if grid[i][j] == "1" and not visit_grid[i][j]:
                    visit_grid[i][j] = True
                    queue = [(i, j), ]
                    while len(queue) != 0:
                        for index in range(len(queue)):
                            x = queue[index][0]
                            y = queue[index][1]

                            if x+1 < first_len and grid[x+1][y] == "1" and not visit_grid[x+1][y]:
                                visit_grid[x+1][y] = True
                                queue.append((x+1, y))
                                
                            if y+1 < second_len and grid[x][y+1] == "1" and not visit_grid[x][y+1]:
                                visit_grid[x][y+1] = True
                                queue.append((x, y+1))
                                
                            if x-1 >= 0 and grid[x-1][y] == "1" and not visit_grid[x-1][y]:
                                visit_grid[x-1][y] = True
                                queue.append((x-1, y))
                                
                            if y-1 >= 0 and grid[x][y-1] == "1" and not visit_grid[x][y-1]:
                                visit_grid[x][y-1] = True
                                queue.append((x, y-1))
                                
                        queue = queue[index+1:]
                    island_num += 1
        
        return island_num
            
            
if __name__ == "__main__":
    island_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print Solution().numIslands(island_grid)