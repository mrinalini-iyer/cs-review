'''
    implement a queue using two stacks
    first in first out
'''


class Queue():
    def __init__(self):
        self.oldest_top = []
        self.newest_top = []
        
    def enqueue(self, data):
        self.newest_top.append(data)
    
    def shiftStack(self):
        if len(self.oldest_top) == 0:
            while(self.newest_top):
                self.oldest_top.append(self.newest_top.pop())
    
    def dequeue(self):
        self.shiftStack()
        return self.oldest_top.pop()
    
    def peek(self):
        self.shiftStack()
        return self.oldest_top[-1]
    
    
# Test
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
