# Refined implementation of LinkList in Python
# Not thread safe

class LinkNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, items=None):
        self.length = 0
        # Dummy Head
        self.head = LinkNode(None)
        # Insert From Tail
        self.tail = self.head
        for item in list(items):
            self.tail.next = LinkNode(item)
            self.tail = self.tail.next
            self.length += 1

    def __len__(self):
        return self.length

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value):
        self.tail.next = LinkNode(value)
        self.tail = self.tail.next
        self.length += 1

    def delAt(self, index: int):
        def innerDel(preNode):
            nonlocal self
            preNode.next = preNode.next.next
            self.length -= 1

        if index == 0 or (index + self.length) == 0:
            self.head.next = self.head.next.next
            self.length -= 1
        elif index == self.length:
            raise IndexError("Out of Bound")
        else:
            self._actOnNode(index - 1, innerDel)

    # Insert at the beginning
    def prepend(self, value):
        self.insert(value, 0)

    def insert(self, value, index):
        def innerInsert(preNode):
            nonlocal value
            nonlocal self
            oldNext = preNode.next
            preNode.next = LinkNode(value)
            preNode.next.next = oldNext
            self.length += 1

        if index == 0 or (index + self.length) == 0:
            oldNext = self.head.next
            self.head.next = LinkNode(value)
            self.head.next.next = oldNext
            self.length += 1
        elif index == self.length:
            self.append(value)
        else:
            self._actOnNode(index - 1, innerInsert)

    def __getitem__(self, index: int):
        if isinstance(index, slice):
            start, stop, step = index.indices(self.length)
            return type(self)((self[i] for i in range(start, stop, step)))
        return self._actOnNode(index, lambda p: p.value)

    def __setitem__(self, index: int, value):
        def setValue(p):
            nonlocal value
            p.value = value

        if isinstance(index, slice):
            start, stop, step = index.indices(self.length)
            values = list(value)
            if len(range(start, stop, step)) != len(values):
                raise IndexError("Out of Bound")

            for i, v in zip(range(start, stop, step), values):
                self[i] = v
            return

        self._actOnNode(index, setValue)

    def __iter__(self):
        p = self.head.next
        while p:
            yield p.value
            p = p.next

    def __repr__(self):
        return " -> ".join((str(x) for x in self)) \
            + " -> None" \
            + f" (Length {self.length})"

    # helper function
    def _actOnNode(self, index: int, action):
        p = self.head
        result = None

        index = self._normalizeIndex(index)

        if index < self.length and index >= 0:
            for i in range(0, index + 1):
                p = p.next
            result = action(p)
        else:
            raise IndexError("Out of Bound")
        return result

    # support negative index
    # normalize index
    def _normalizeIndex(self, index: int) -> int:
        return index if index >= 0 else self.length + index


# Test Cases
listA = LinkList([1, 2, 3, 4])
print(listA)

listA[1:3] = ['c', 'd']

print(listA)
