class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]      

    def getMin(self) -> int:
        #const time.
        temp = []
        mini = self.stack.pop()
        temp.append(mini)
        while len(self.stack) > 0:
            item = self.stack.pop()
            if (item < mini):
                mini = item
            temp.append(item)
        temp.reverse()
        self.stack = temp
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()