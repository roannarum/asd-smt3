from collections import deque


class Deque(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0,item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)


def palindrom(characters):
    character_deque = Deque()
    for i in characters:
        character_deque.add_rear(i)
    equal = True
    while character_deque.size() > 1 and equal:
        first = character_deque.remove_front()
        last = character_deque.remove_rear()
        if first != last:
            equal = False
        return equal

masukan = input("masukan kata : ")
if palindrom(masukan):
    print("kata " + masukan + " adalah kata palindrom")
else:
    print("kata " + masukan + " bukan kata palindrom")

deque = Deque()
deque.add_front(10)
deque.add_front(12)
deque.add_front("arum")
deque.add_rear(20)
print(deque)