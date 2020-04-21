# coding: utf-8
'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

# 两个队列（先进先出）可实现栈（后进先出）
'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1 = []
        self.list2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.list1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = None
        for index, x in enumerate(self.list1):
            if index == len(self.list1)-1:
                result = x
            else:
                self.list2.append(x)
                
        self.list1, self.list2 = self.list2, []
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        for index, x in enumerate(self.list1):
            if index == len(self.list1)-1:
                return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.list1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()