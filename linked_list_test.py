import unittest
from collections import defaultdict

from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_delete_left_one_data(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.delete(1)
        self.assertEqual(2, len(ll))
        self.assertEqual([2, 3], ll.get_list())

    def test_delete_left_more_data(self):
        ll = LinkedList([1, 1, 2, 3])
        self.assertEqual(4, len(ll))
        ll.delete(1)
        self.assertEqual(2, len(ll))
        self.assertEqual([2, 3], ll.get_list())

    def test_delete_middle_one_data(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.delete(2)
        self.assertEqual(2, len(ll))
        self.assertEqual([1, 3], ll.get_list())

    def test_delete_middle_more_data(self):
        ll = LinkedList([1, 2, 2, 3])
        self.assertEqual(4, len(ll))
        ll.delete(2)
        self.assertEqual(2, len(ll))
        self.assertEqual([1, 3], ll.get_list())

    def test_delete_data_from_one_seq(self):
        ll = LinkedList([1])
        self.assertEqual(1, len(ll))
        ll.delete(1)
        self.assertEqual(0, len(ll))
        self.assertEqual([], ll.get_list())

    def test_delete_data_from_empty_seq(self):
        ll = LinkedList([])
        self.assertEqual(0, len(ll))
        ll.delete(1)
        self.assertEqual(0, len(ll))
        self.assertEqual([], ll.get_list())

    def test_delete_not_exist_data(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.delete(5)
        self.assertEqual(3, len(ll))
        self.assertEqual([1, 2, 3], ll.get_list())

    def test_delete_data_from_not_sorted_seq(self):
        ll = LinkedList([1, 2, 3, 1, 1, 4, 5, 1, 1])
        self.assertEqual(9, len(ll))
        ll.delete(1)
        self.assertEqual(4, len(ll))
        self.assertEqual([2, 3, 4, 5], ll.get_list())

    def test_append_to_empty_seq(self):
        ll = LinkedList([])
        self.assertEqual(0, len(ll))
        ll.append(1)
        self.assertEqual(1, len(ll))
        self.assertEqual([1], ll.get_list())

    def test_append_to_not_empty_seq(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.append(4)
        self.assertEqual(4, len(ll))
        self.assertEqual([1, 2, 3, 4], ll.get_list())

    def test_append_left_to_empty_seq(self):
        ll = LinkedList([])
        self.assertEqual(0, len(ll))
        ll.append_left(1)
        self.assertEqual(1, len(ll))
        self.assertEqual([1], ll.get_list())

    def test_append_left_to_not_empty_seq(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.append_left(0)
        self.assertEqual(4, len(ll))
        self.assertEqual([0, 1, 2, 3], ll.get_list())

    def test_insert_to_empty_seq_1(self):
        ll = LinkedList([])
        self.assertEqual(0, len(ll))
        ll.insert(0, 1)
        self.assertEqual(1, len(ll))
        self.assertEqual([1], ll.get_list())

    def test_insert_to_empty_seq_2(self):
        ll = LinkedList([])
        self.assertEqual(0, len(ll))
        ll.insert(1, 1)
        self.assertEqual(1, len(ll))
        self.assertEqual([1], ll.get_list())

    def test_insert_to_not_empty_seq_right_1(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.insert(3, 4)
        self.assertEqual(4, len(ll))
        self.assertEqual([1, 2, 3, 4], ll.get_list())

    def test_insert_to_not_empty_seq_right_2(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.insert(4, 4)
        self.assertEqual(4, len(ll))
        self.assertEqual([1, 2, 3, 4], ll.get_list())

    def test_insert_to_not_empty_seq_left(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.insert(0, 0)
        self.assertEqual(4, len(ll))
        self.assertEqual([0, 1, 2, 3], ll.get_list())

    def test_insert_to_not_empty_seq_middle(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        ll.insert(1, 4)
        self.assertEqual(4, len(ll))
        self.assertEqual([1, 4, 2, 3], ll.get_list())

    def test_counter_for_empty_seq(self):
        ll = LinkedList()
        res = ll.counter()
        self.assertEqual(0, len(res))
        self.assertIsInstance(res, defaultdict)

    def test_counter(self):
        ll = LinkedList([1, 1, 2, 3, 3, 3, 4, 5, 5])
        res = ll.counter()
        self.assertEqual(5, len(res))
        self.assertIsInstance(res, defaultdict)
        self.assertEqual({1: 2, 2: 1, 3: 3, 4: 1, 5: 2}, dict(res))

    def test_pop_from_empty_seq(self):
        ll = LinkedList()
        item = ll.pop()
        self.assertIsNone(item)
        self.assertEqual(0, len(ll))

    def test_pop_from_one_data_seq(self):
        ll = LinkedList([1])
        self.assertEqual(1, len(ll))
        item = ll.pop()
        self.assertIsInstance(item, Node)
        self.assertEqual(1, item.data)
        self.assertEqual(0, len(ll))

    def test_pop_from_more_data_seq(self):
        ll = LinkedList([1, 2])
        self.assertEqual(2, len(ll))
        item = ll.pop()
        self.assertIsInstance(item, Node)
        self.assertEqual(2, item.data)
        self.assertEqual(1, len(ll))

    def test_pop_first_from_empty_seq(self):
        ll = LinkedList()
        item = ll.pop(0)
        self.assertIsNone(item)
        self.assertEqual(0, len(ll))

    def test_pop_first_from_one_data_seq(self):
        ll = LinkedList([1])
        self.assertEqual(1, len(ll))
        item = ll.pop(0)
        self.assertIsInstance(item, Node)
        self.assertEqual(1, item.data)
        self.assertEqual(0, len(ll))

    def test_pop_first_from_more_data_seq(self):
        ll = LinkedList([1, 2])
        self.assertEqual(2, len(ll))
        item = ll.pop(0)
        self.assertIsInstance(item, Node)
        self.assertEqual(1, item.data)
        self.assertEqual(1, len(ll))

    def test_pop_middle_from_more_data_seq(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(3, len(ll))
        item = ll.pop(1)
        self.assertIsInstance(item, Node)
        self.assertEqual(2, item.data)
        self.assertEqual(2, len(ll))

    def test_contains(self):
        ll = LinkedList([1, 2, 3])
        self.assertTrue(2 in ll)

    def test_contains_negative(self):
        ll = LinkedList([1, 2, 3])
        self.assertFalse(4 in ll)

    def test_contains_empty_seq(self):
        ll = LinkedList()
        self.assertFalse(1 in ll)

    def test_reverse(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        ll.reverse()
        self.assertEqual([5, 4, 3, 2, 1], ll.get_list())

    def test_reverse_empty(self):
        ll = LinkedList()
        ll.reverse()
        self.assertFalse(ll.get_list())

    def test_reverse_one_item(self):
        ll = LinkedList([1])
        ll.reverse()
        self.assertEqual([1], ll.get_list())

    def test_is_palindrome_false_1(self):
        ll = LinkedList(['a', 'b', 'c', 'd'])
        self.assertFalse(ll.is_palindrome())

    def test_is_palindrome_false_2(self):
        ll = LinkedList(['a', 'b'])
        self.assertFalse(ll.is_palindrome())

    def test_is_palindrome_empty(self):
        ll = LinkedList()
        self.assertTrue(ll.is_palindrome())

    def test_is_palindrome_one_item(self):
        ll = LinkedList('a')
        self.assertTrue(ll.is_palindrome())

    def test_is_palindrome_true_1(self):
        ll = LinkedList(['a', 'a'])
        self.assertTrue(ll.is_palindrome())

    def test_is_palindrome_true_2(self):
        ll = LinkedList(['a', 'b', 'a'])
        self.assertTrue(ll.is_palindrome())

    def test_is_palindrome_true_3(self):
        ll = LinkedList(['a', 'b', 'b', 'a'])
        self.assertTrue(ll.is_palindrome())


if __name__ == '__main__':
    unittest.main()
