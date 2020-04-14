# coding: utf-8
'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''
class MinStack(object):
    '''
    思路：每次push都push两个数，x和最小值，这样保证每次最小值都在top位置
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.data) == 0:
            self.data.append(x)
            self.data.append(x)
        else:
            min = self.getMin()
            self.data.append(x)
            if min > x:
                min = x
            self.data.append(min)

    def pop(self):
        """
        :rtype: None
        """
        self.data.pop()
        self.data.pop()
                    
    def top(self):
        """
        :rtype: int
        """
        return self.data[-2:][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1:][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()