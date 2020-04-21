# coding: utf-8
'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sequares = self.getSquares(n)
        print sequares
        queue = [n]
        count = 0
        while len(queue) != 0:
            add_flag = False
            for i in range(len(queue)):
                num = queue[i]

                for sequare in sequares:
                    if num == sequare:
                        return count + 1

                    if num > sequare:
                        queue.append(num-sequare)
                        add_flag = True
            
            if add_flag:
                count += 1
            queue = queue[i+1:]
        
        return count

    def getSquares(self, n):
        sequares = []
        num = 1
        while num*num <= n:
            sequares.append(num*num)
            num += 1
        return sequares[::-1]       # 算最小步数，所以需要将数组反转，先减去大的数，步数最少


if __name__ == '__main__':
    solution = Solution()
    print solution.numSquares(7)
    print solution.numSquares(31)
