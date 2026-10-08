class LinkedList:


    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        current = self.head.next

        for _ in range(index):
            if current is None:
                return-1
            current = current.next

        return current.val if current is not None else -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val,self.head.next)
        self.head.next = node

        if self.tail is self.head:
            self.tail = node

        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if index < 0:
            return False

        previous = self.head

        for _ in range(index):
            if previous.next is None:
                return False
            previous = previous.next

        node = previous.next
        if node is None:
            return False

        previous.next = node.next

        if node is self.tail:
            self.tail = previous

        return True
        

    def getValues(self) -> List[int]:
        values = []
        current = self.head.next

        while current is not None:
            values.append(current.val)
            current = current.next

        return values

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next
