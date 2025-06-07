import unittest
from linked_lists.array_based import ArrayBasedList


class TestArrayBasedList(unittest.TestCase):
    def setUp(self):
        self.list = ArrayBasedList()
        for char in "ABCDE":
            self.list.append(char)
    
    def test_initial_empty_state(self):
        empty_list = ArrayBasedList()
        self.assertEqual(empty_list.length(), 100)
    
    def test_length(self):
        self.assertEqual(self.list.length(), 5)
        empty_list = ArrayBasedList()
        self.assertEqual(empty_list.length(), 0)
    
    def test_append_and_get(self):
        self.list.append('F')
        self.assertEqual(self.list.get(5), 'F')
        self.assertEqual(self.list.length(), 6)
        
        empty_list = ArrayBasedList()
        empty_list.append('X')
        self.assertEqual(empty_list.get(0), 'X')
        self.assertEqual(empty_list.length(), 1)
    
    def test_insert(self):
        self.list.insert('Z', 2)
        self.assertEqual(self.list.get(2), 'Z')
        self.assertEqual(self.list.get(3), 'C')
        self.assertEqual(self.list.length(), 6)
        
        self.list.insert('Y', 0)
        self.assertEqual(self.list.get(0), 'Y')
        self.assertEqual(self.list.get(1), 'A')
        
        original_length = self.list.length()
        self.list.insert('W', original_length)
        self.assertEqual(self.list.get(original_length), 'W')
        
        with self.assertRaises(ValueError):
            self.list.insert('Q', -1)
        with self.assertRaises(ValueError):
            self.list.insert('Q', 100)
    
    def test_delete(self):
        removed = self.list.delete(1)
        self.assertEqual(removed, 'B')
        self.assertEqual(self.list.get(1), 'C')
        self.assertEqual(self.list.length(), 4)
        
        removed = self.list.delete(0)
        self.assertEqual(removed, 'A')
        self.assertEqual(self.list.length(), 3)
        
        last_index = self.list.length() - 1
        last_element = self.list.get(last_index)
        removed = self.list.delete(last_index)
        self.assertEqual(removed, last_element)
        
        with self.assertRaises(ValueError):
            self.list.delete(-1)
        with self.assertRaises(ValueError):
            self.list.delete(10)
    
    def test_deleteAll(self):
        self.list.append('A')
        self.list.append('A')
        initial_length = self.list.length()
        self.list.deleteAll('A')
        self.assertEqual(self.list.findFirst('A'), -1)
        self.assertLess(self.list.length(), initial_length)
        
        initial_length = self.list.length()
        self.list.deleteAll('Z')
        self.assertEqual(self.list.length(), initial_length)
    
    def test_clone(self):
        clone = self.list.clone()
        self.assertEqual(clone.length(), self.list.length())
        for i in range(self.list.length()):
            self.assertEqual(clone.get(i), self.list.get(i))
        
        clone.delete(0)
        self.assertNotEqual(clone.length(), self.list.length())
        
        empty_list = ArrayBasedList()
        empty_clone = empty_list.clone()
        self.assertEqual(empty_clone.length(), 0)
    
    def test_reverse(self):
        original = [self.list.get(i) for i in range(self.list.length())]
        self.list.reverse()
        for i in range(len(original)):
            expected = original[len(original) - 1 - i]
            actual = self.list.get(i)
            self.assertEqual(actual, expected)
        
        empty_list = ArrayBasedList()
        empty_list.reverse()
        self.assertEqual(empty_list.length(), 0)
        
        single_list = ArrayBasedList()
        single_list.append('X')
        single_list.reverse()
        self.assertEqual(single_list.get(0), 'X')
    
    def test_find_operations(self):
        self.assertEqual(self.list.findFirst('C'), 2)
        self.assertEqual(self.list.findLast('C'), 2)
        
        self.list.append('C')
        self.assertEqual(self.list.findFirst('C'), 2)
        self.assertEqual(self.list.findLast('C'), 5)
        
        self.assertEqual(self.list.findFirst('Z'), -1)
        self.assertEqual(self.list.findLast('Z'), -1)
        
        empty_list = ArrayBasedList()
        self.assertEqual(empty_list.findFirst('A'), -1)
        self.assertEqual(empty_list.findLast('A'), -1)
    
    def test_clear(self):
        self.assertGreater(self.list.length(), 0)
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
    
    def test_extend(self):
        other = ArrayBasedList()
        other.append('X')
        other.append('Y')
        
        original_length = self.list.length()
        self.list.extend(other)
        
        self.assertEqual(self.list.length(), original_length + 2)
        self.assertEqual(self.list.get(original_length), 'X')
        self.assertEqual(self.list.get(original_length + 1), 'Y')
        
        empty_other = ArrayBasedList()
        current_length = self.list.length()
        self.list.extend(empty_other)
        self.assertEqual(self.list.length(), current_length)
    
    def test_edge_cases_empty_list(self):
        empty_list = ArrayBasedList()
        
        with self.assertRaises(ValueError):
            empty_list.get(0)
        
        with self.assertRaises(ValueError):
            empty_list.delete(0)
    
    def test_validation_errors(self):
        with self.assertRaises(ValueError):
            self.list.append(123)
        
        with self.assertRaises(ValueError):
            self.list.append("AB")
        
        with self.assertRaises(ValueError):
            self.list.append("")
        
        with self.assertRaises(ValueError):
            self.list.insert(123, 0)
        
        with self.assertRaises(ValueError):
            self.list.findFirst(123)
        
        with self.assertRaises(ValueError):
            self.list.findLast("")
        
        with self.assertRaises(ValueError):
            self.list.deleteAll("AB")
    
    def test_boundary_indices(self):
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(4), 'E')
        
        with self.assertRaises(ValueError):
            self.list.get(-1)
        
        with self.assertRaises(ValueError):
            self.list.get(5)
    
    def test_multiple_operations_sequence(self):
        test_list = ArrayBasedList()
        
        test_list.append('A')
        test_list.append('B')
        test_list.insert('C', 1)
        self.assertEqual(test_list.get(1), 'C')
        self.assertEqual(test_list.get(2), 'B')
        
        removed = test_list.delete(0)
        self.assertEqual(removed, 'A')
        self.assertEqual(test_list.get(0), 'C')
        
        test_list.reverse()
        self.assertEqual(test_list.get(0), 'B')
        self.assertEqual(test_list.get(1), 'C')
    
    def test_duplicate_elements(self):
        test_list = ArrayBasedList()
        for char in "AABBC":
            test_list.append(char)
        
        self.assertEqual(test_list.findFirst('A'), 0)
        self.assertEqual(test_list.findLast('A'), 1)
        self.assertEqual(test_list.findFirst('B'), 2)
        self.assertEqual(test_list.findLast('B'), 3)
        
        test_list.deleteAll('A')
        self.assertEqual(test_list.findFirst('A'), -1)
        self.assertEqual(test_list.length(), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)