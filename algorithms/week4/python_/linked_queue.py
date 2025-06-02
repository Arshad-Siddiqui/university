from node import Node

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def enqueue(self, data):
        new_node = Node(data, None)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        if self.head == None:
            raise IndexError("doesn't exist")
        
        element = self.head.element
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None
        return element

    def first(self):
        if self.head == None:
            raise IndexError("doesn't exist")

        return self.head.element
    
    def is_empty(self):
        return self.size == 0
    
lq = LinkedQueue()
lq.enqueue("hello")
print(lq.dequeue())

items = ["hi", "my", "name", "is", "Arshad!"]

for item in items:
    lq.enqueue(item)

print(lq.first())
for _ in range(4):
    print(lq.dequeue())
