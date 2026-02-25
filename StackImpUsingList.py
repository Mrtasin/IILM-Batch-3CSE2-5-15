class Stack:
    def __init__(self):
        self.top = []

    def push(self, data):
        self.top.append(data)

    def pop(self):
        if len(self.top) == 0:
            return "Stack is Empty"
        return self.top.pop()
    
    def peek(self):
        if len(self.top) == 0:
            return "Stack is Empty"
        return self.top[-1]

    def isEmpty(self):
        return not len(self.top)
    
    def size(self):
        return len(self.top)

