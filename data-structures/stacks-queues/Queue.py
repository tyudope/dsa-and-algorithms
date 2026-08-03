from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()


    def enqueue(self, val):
        """Adds value to the right/back end of the queue. """
        self.queue.append(val) 


    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft() # .popleft() removes and returns the leftmost(front) element in O(1). 

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]


    def is_empty(self) -> bool:
        return not self.queue


    def __len__(self) -> int:
        return len(self.queue)


"""
Queue — FIFO, backed by collections.deque.

enqueue: append (back)      — O(1)
dequeue: popleft (front)    — O(1)
peek:    index [0] (front)  — O(1)

deque gives O(1) at BOTH ends. A plain list would make dequeue O(n),
because list.pop(0) shifts every remaining element left.
"""