class ArrayBasedList:
    def __init__(self):
        self.items = []
    
    def _validate_character(self, element: str) -> None:
        if not isinstance(element, str):
            raise ValueError("Element must be a string")
        if len(element) != 1:
            raise ValueError("Element must be a single character")
    
    def append(self, element: str) -> None:
        self._validate_character(element)
        self.items.append(element)
    
    def length(self) -> int:
        return len(self.items)
    
    def insert(self, element: str, index: int) -> None:
        self._validate_character(element)
        if index < 0 or index > self.length():
            raise ValueError("Wrong index value.")
        self.items.insert(index, element)
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")
        return self.items.pop(index)
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise ValueError("Wrong index value.")
        return self.items[index]
    
    def deleteAll(self, element: str) -> None:
        self._validate_character(element)
        self.items = [item for item in self.items if item != element]
    
    def clone(self) -> 'ArrayBasedList':
        cloned = ArrayBasedList()
        cloned.items = self.items.copy()
        return cloned
    
    def reverse(self) -> None:
        self.items.reverse()
    
    def findFirst(self, element: str) -> int:
        self._validate_character(element)
        try:
            return self.items.index(element)
        except ValueError:
            return -1
    
    def findLast(self, element: str) -> int:
        self._validate_character(element)
        for i in range(self.length() - 1, -1, -1):
            if self.items[i] == element:
                return i
        return -1
    
    def clear(self) -> None:
        self.items = []
    
    def extend(self, other: 'ArrayBasedList') -> None:
        self.items.extend(other.items.copy())


if __name__ == '__main__':
    alist = ArrayBasedList()
    print("Initial length (expected 0):", alist.length())
    
    for char in "ABCDE":
        alist.append(char)
    print("Length after appending A, B, C, D, E (expected 5):", alist.length())
    
    alist.insert('Z', 2)
    print("Element at index 2 after insert (expected Z):", alist.get(2))
    
    removed = alist.delete(1)
    print("Deleted element at index 1 (expected B):", removed)
    
    alist.append('A')
    alist.deleteAll('A')
    print("findFirst('A') (expected -1):", alist.findFirst('A'))
    
    clone = alist.clone()
    print("Clone length (expected same as original):", clone.length())
    clone.delete(0)
    print("After deleting first element from clone, clone length != original length:", clone.length(), alist.length())
    
    alist.reverse()
    print("After reverse, element at index 0 should be last of original list:", alist.get(0))
    
    print("findFirst('C') (expected index):", alist.findFirst('C'))
    print("findLast('C') (expected index):", alist.findLast('C'))
    
    alist.clear()
    print("Length after clear (expected 0):", alist.length())
    
    list1 = ArrayBasedList()
    list1.append('X')
    list1.append('Y')
    list2 = ArrayBasedList()
    list2.append('Z')
    list1.extend(list2)
    print("Length after extend (expected 3):", list1.length())
    print("Elements after extend:", list1.items)