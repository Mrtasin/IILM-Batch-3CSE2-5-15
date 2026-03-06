class Node:
    def __init__(self, data=None):
        self.prev = None
        self.value = data
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.front = None
        self.back = None

    def insertFront(self, value: int) -> bool:
        if self.capacity == self.size:
            return False
        temp = Node(value)
        if self.front:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp
        else:
            self.front = self.back = temp
        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.capacity == self.size:
            return False
        temp = Node(value)
        if self.back:
            temp.prev = self.back
            self.back.next = temp
            self.back = temp
        else:
            self.front = self.back = temp
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:  # self.front == self.back
            self.front = self.back = None
        else:
            temp = self.front
            self.front = temp.next
            self.front.prev = None
            temp.next = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:  # self.front == self.back
            self.front = self.back = None
        else:
            temp = self.back
            self.back = temp.prev
            self.back.next = None
            temp.prev = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
