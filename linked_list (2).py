class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
    def append(self, node):
        if self.start is None:
            self.start = node
        else:
            self.end.next = node
        self.end = node
    def values(self):
        result = []
        node = self.start
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

linked_list = LinkedList()
linked_list.append(Node(1))
linked_list.append(Node(2))
linked_list.append(Node(5))
print(linked_list.values())