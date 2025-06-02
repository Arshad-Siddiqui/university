class LinkedList:
    class Node:
        """Is a private class used to store elements and pointer to next node.
        Arguments:
            Value: any
        """
        def __init__(self, value):
            self.element = value
            self.next = None
    
    def __init__(self) -> None:
        pass