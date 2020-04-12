# coding: utf-8
'''
循环列表
'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.max_length = k
        self.length = 0   # 用于记录当前链表的长度
        self.front = 0
        self.rear = -1
        
        self.queue = []
        for i in range(k):
            self.queue.append(None)

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
            
        self.rear = (self.rear+1) % self.max_length   
        self.queue[self.rear] = value
        
        self.length += 1
            
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.front = (self.front+1) % self.max_length
        self.length -= 1
            
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return True if self.length == 0 else False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return True if self.length == self.max_length else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()