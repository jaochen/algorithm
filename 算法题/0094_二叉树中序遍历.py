# coding: utf-8
'''
给定一个二叉树，返回它的中序 遍历。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 递归做法
    def DFSInorderTraversal(self, root):
        def dfs(root):
            if not root:
                return
            # 中序遍历逻辑，先访问左节点，再访问原节点，再访问右节点
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        
        result = []
        dfs(root)
        return result

    # 迭代做法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        
        node = root
        while len(stack) != 0 or node:
            # 一直找到最左边，把中间经过的节点放进栈，方便回溯
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            result.append(node.val)
            node = node.right
                
        return result