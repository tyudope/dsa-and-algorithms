class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None



    def append(self, val):
        node = Node(val)

        # If the list is empty
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node


    def delete(self, val):
        # If the list is empty
        if not self.head:
            return
        
        # If element that needs to be deleted is head of the list.
        if self.head.val == val:
            self.head = self.head.next
            return


        curr = self.head
        prev = self.head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        return
            


        
        

    def prepend(self, val):

        node = Node(val)
        node.next = self.head
        self.head = node


    def __len__(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next

        return length

    def __str__(self) -> str:
        result = ""
        curr = self.head
        while curr is not None:
            result += str(curr.val)
            if curr.next:
                result += " -> "
            curr = curr.next

        return result
