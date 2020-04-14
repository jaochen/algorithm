# coding: utf-8
'''
克隆图

给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

1、节点数不超过 100 。
2、每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
3、无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
4、由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
5、图是连通图，你可以从给定节点访问到所有节点。
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        
        visit = {}
        return self.cloneNode(node, visit)
    
    def cloneNode(self, node, visit):
        new_node = Node(val=node.val)
        visit[node.val] = new_node
        
        for one in node.neighbors:
            if one.val not in visit:
                n_node = self.cloneNode(one, visit)
                new_node.neighbors.append(n_node)
            else:
                new_node.neighbors.append(visit[one.val])
                
        return new_node
        