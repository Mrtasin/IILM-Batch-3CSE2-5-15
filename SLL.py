class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.start = None

    def insert_at_start(self, data):
        t = Node(data)
        t.next = self.start
        self.start = t
        
    def insert_at_end(self, data):
        t = Node(data)
        if(self.start == None):
            self.start = t
        else :
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = t