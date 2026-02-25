class Node:
    def __init__(self, data = None):
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(tasinCoder):
        return (tasinCoder.top == None)
    
    def size(tasinCoder):
        return tasinCoder.length
    
    def push(tasinCoder, data):
        temp = Node(data)
        temp.next = tasinCoder.top
        tasinCoder.top = temp

    def pop(tasinCoder):
        if tasinCoder.isEmpty():
            return "Stack is Empty"
        temp = tasinCoder.top
        tasinCoder.top = tasinCoder.top.next
        return temp.value
    
    def peek(tasinCoder):
        if tasinCoder.isEmpty():
            return "Stack is Empty"
        return tasinCoder.top.value



s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
while(not s1.isEmpty()):
    print(s1.pop(),end=" ")

