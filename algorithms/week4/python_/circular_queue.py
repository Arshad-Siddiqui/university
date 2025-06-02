from node import Node

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        new = Node(data, None)
        if self.is_empty():
            self.tail = new
            self.tail.next = self.tail # type: ignore
        else:
            head = self.tail.next # type: ignore
            new.next = head
            self.tail.next = new # type: ignore
            self.tail = new

        self.size += 1