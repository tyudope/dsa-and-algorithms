class Stack:
    
    
    def __init__(self):
        self.stack = []


    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not self.stack

    def __len__(self) -> int:
        return len(self.stack)
