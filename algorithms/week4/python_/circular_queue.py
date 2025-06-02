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
        new_node = Node(data, None)
        if self.is_empty():
            new_node.next = new_node # type: ignore
        else:
            new_node.next = self.tail.next # type: ignore
            self.tail.next = new_node # type: ignore
        self.tail = new_node
        self.size += 1
    
    def rotate(self):
        if not self.is_empty():
            self.tail = self.tail.next # type: ignore