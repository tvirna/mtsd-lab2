class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def _validate_character(self, element: str) -> None:
        if not isinstance(element, str):
            raise ValueError("Element must be a string")
        if len(element) != 1:
            raise ValueError("Element must be a single character")

    def append(self, element: str) -> None:
        self._validate_character(element)
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def length(self) -> int:
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def insert(self, element: str, index: int) -> None:
        self._validate_character(element)
        if index < 0 or index > self.length():
            raise ValueError("Wrong index value.")

        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                new_node.next = new_node
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                new_node.next = self.head
                self.head = new_node
                current.next = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")

        if self.length() == 1:
            data = self.head.data
            self.head = None
            return data

        if index == 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            data = self.head.data
            self.head = self.head.next
            current.next = self.head
            return data
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            data = prev.next.data
            prev.next = prev.next.next
            return data

    def deleteAll(self, element: str) -> None:
        self._validate_character(element)
        if not self.head:
            return

        while self.head and self.head.data == element:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                self.head = self.head.next
                current.next = self.head

        current = self.head
        while current.next != self.head:
            if current.next.data == element:
                current.next = current.next.next
            else:
                current = current.next

    def clone(self) -> 'CircularLinkedList':
        cloned_list = CircularLinkedList()
        if not self.head:
            return cloned_list

        current = self.head
        cloned_list.append(current.data)
        while current.next != self.head:
            current = current.next
            cloned_list.append(current.data)
        return cloned_list

    def reverse(self) -> None:
        if not self.head or self.head.next == self.head:
            return

        prev = None
        current = self.head
        start = self.head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev

    def findFirst(self, element: str) -> int:
        self._validate_character(element)
        if not self.head:
            return -1
        index = 0
        current = self.head
        while True:
            if current.data == element:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def findLast(self, element: str) -> int:
        self._validate_character(element)
        if not self.head:
            return -1
        index = 0
        last_index = -1
        current = self.head
        while True:
            if current.data == element:
                last_index = index
            current = current.next
            index += 1
            if current == self.head:
                break
        return last_index

    def clear(self) -> None:
        self.head = None

    def extend(self, elements: 'CircularLinkedList') -> None:
        if not elements.head:
            return

        current = elements.head
        while True:
            self.append(current.data)
            current = current.next
            if current == elements.head:
                break


if __name__ == '__main__':
    clist = CircularLinkedList()
    print("Initial length (expected 0):", clist.length())

    clist.append('A')
    clist.append('B')
    clist.append('C')
    print("Length after appending A, B, C (expected 3):", clist.length())

    clist.insert('D', 0)
    print("Element at index 0 after insert (expected D):", clist.get(0))
    clist.insert('E', 2)
    print("Element at index 2 after insert (expected E):", clist.get(2))

    deleted = clist.delete(1)
    print("Deleted element at index 1 (expected A):", deleted)
    print("Length after deletion:", clist.length())

    clist.append('B')
    clist.append('B')
    print("Length before deleteAll('B'):", clist.length())
    clist.deleteAll('B')
    print("Length after deleteAll('B'):", clist.length())

    cloned = clist.clone()
    print("Length of cloned list (expected same):", cloned.length())

    clist.reverse()
    print("First element after reverse:", clist.get(0))

    pos_first = clist.findFirst('C')
    pos_last = clist.findLast('C')
    print("findFirst('C') (expected index):", pos_first)
    print("findLast('C') (expected index):", pos_last)

    clist.clear()
    print("Length after clear (expected 0):", clist.length())

    list1 = CircularLinkedList()
    list1.append('X')
    list1.append('Y')
    list2 = CircularLinkedList()
    list2.append('Z')
    list1.extend(list2)
    print("Length after extend (expected 3):", list1.length())