class Queue:
    def __init__(self):
        self.storage = []
    def is_empty(self):
        return self.storage == []
    def enqueue(self, data):
        self.storage.append(data)
    def dequeue(self):
        return self.storage.pop(0) \
            if not self.is_empty() \
            else None
    def peek(self):
        return self.storage[0] \
            if not self.is_empty() \
            else None
    def __str__(self):
        return str(self.storage)

queue = Queue()
queue.enqueue(34)
queue.enqueue(25)
queue.enqueue(76)
print(queue)
print(queue.peek())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)