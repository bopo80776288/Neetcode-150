class MinStack:
    def __init__(self):
        # create two stack one for tracking the added value and one to track the current min of the corresponding value
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # for the num stack just append the value by push 
        self.stack.append(val)
        # we need to modify the value before we add it to min stack
        # if min stack is empty just add the val to it, but if it already has value in it we need to do a compare and record the min
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        # just use python pop()
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        # return the top value (last value) of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the top value (last value) of the min stack 
        return self.minStack[-1]
    

# Test Case 1: Creating the MinStack object and testing push and getMin
obj = MinStack()
obj.push(3)
print(obj.getMin())  # Expected: 3
obj.push(5)
print(obj.getMin())  # Expected: 3
obj.push(2)
print(obj.getMin())  # Expected: 2
obj.pop()
print(obj.getMin())  # Expected: 3

