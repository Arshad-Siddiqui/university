# NOTE: You are really tired when writing this and might so this might not work. Have fun.

class LinkedStack:
    class Node:
        """Is a private class used to store elements and pointer to next node.
        Arguments:
            Value: any
            Next: pointer to node
        """
        def __init__(self, value, next):
            self.element = value
            self.next = next
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        # Don't need a tail as typically on a stack you hardly see that

    def push(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node
        self.size += 1
    
    def pop(self):
        # Head has a chance to be empty/None so we handle that
        if self.head == None:
            raise IndexError("That is empty bro")

        original_head = self.head
        self.head = self.head.next
        self.size -= 1
        return original_head.element

    def top(self):
        if self.head == None:
            raise IndexError("empty bruddah")
        return self.head.element
