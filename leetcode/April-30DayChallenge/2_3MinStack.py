"""
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
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        elif self.min[-1] >= x:
            # 因为item是一个个加的，所以在每一个时刻的min value是确定的。可以不加不是min value的item
            # 注意一定要>=，因为重复的min value都需要记录
            self.min.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            # 如果是item==min value，拿掉吧。。。
            self.min.pop()
        # return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
