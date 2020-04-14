# coding: utf-8
'''
给定步长m,每m个节点反转单链表
eg: 
    m=2, a->b->c->d->e->f => b->a->d->c->f->e
    m=3, a->b->c->d->e->f => c->b->a->e->f->d
'''

# =======================
# 链表解法
# 思路：
#     1、将k个节点的区间进行反转
#     2、将反转后的链表接上 后面反转的头节点（递归操作），所以，需要将反转后的头节点返回
# =======================

class Node(object):
    '''
    节点类
    '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def __str__(self):
        return self.data

class NodeList(object):
    '''
    链表类
    '''
    def __init__(self, array=None):
        self.length = 0

        if not array:
            self.header = None
        else:
            tmp = None
            for index in array:
                node = Node(index)
                if not tmp:
                    self.header = node
                else:
                    tmp.next_node = node

                tmp = node
                self.length += 1
    
    def series(self, node=None):
        if not self.header:
            return None
        
        tmp = node if node else self.header
        while tmp:
            print tmp,
            tmp = tmp.next_node
        print ''

    def reverse(self, k=0, log=True):

        if not self.header or k <= 1 or k > self.length:
            return None

        if log:
            print "k: ", k
            print "before: "
            self.series()

        # k反转函数返回反转后的头节点，替代掉原header
        new_header = self._k_reverse(self.header, k)
        self.header = new_header

        if log:
            print "after: "
            self.series() 

    def _k_reverse(self, header, k=0):
        '''
        反转函数
        思路：
            1、将k个节点的区间进行反转
            2、将反转后的链表接上 后面反转的头节点（递归操作），所以，需要将反转后的头节点返回

        :params k 每k个链表反转一次
        :return 反转后的头节点
        '''
        if not header or k <= 1:
            return None
    
        last = header
        for i in range(k-1):/
            last = last.next_node
            if last == None:
                return header
        
        next = last.next_node
        new_header = self._reverse(header, last)
        header.next_node = self._k_reverse(next, k)

        # 将反转后的头节点返回，作为前面反转的后驱节点
        return new_header
    
    def _reverse(self, first, last):
        '''
        反转区间链表,返回区间最后一个节点（反转后该区间的头节点）
        :return last
        '''
        if not first or not last:
            return None

        cur = first
        pre = None
        next = None

        while cur != last:
            next = cur.next_node
            cur.next_node = pre

            pre = cur
            cur = next

        cur.next_node = pre

        return cur
        
if __name__ == '__main__':

    # 链表测试
    node_list = NodeList(['a', 'b', 'c', 'd', 'e', 'f'])
    node_list.series()
    node_list.reverse(k=2)

    node_list.reverse(k=2, log=False)
    node_list.reverse(k=3)

    node_list.reverse(k=3, log=False)
    node_list.reverse(k=4)

    node_list.reverse(k=4, log=False)
    node_list.reverse(k=6)
    
