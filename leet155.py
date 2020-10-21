155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


啥也不修改直接用list也能过，但是速度非常慢, 因为每次去取最小值是一个O（n）的操作
好的做法是用一对tuple记录每个元素放进去的时候当前的最小值。因为stack的性质决定了，他的顺序不会乱
所以每个元素的位置放进去的时候就决定了到他为止的最小值是多少

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.val) == 0:
            currMin = x
        else:
            currMin = self.getMin()
        if x < currMin:
            currMin = x
        self.val.append((x, currMin))
        

    def pop(self):
        """
        :rtype: void
        """
        self.val.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.val[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.val[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()