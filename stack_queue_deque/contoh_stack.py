class Stack:
    def __init__(self):
        self.storage = []
    def is_empty(self):
        return self.storage == []

    def push(self, data):
        self.storage.append(data)

    def pop(self):
        return self.storage.pop() \
            if not self.is_empty() \
            else None

    def peek(self):
        return self.storage[-1] \
            if not self.is_empty() \
            else None
            
    def __str__(self):
        return str(self.storage)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack)
stack.is_empty()
print(stack)
# print(stack.peek())
# print(stack)
# print(stack.pop())
# print(stack)