from singly_linked_list.singly_linked_list import Node, List
import unittest


class TestSinglyLinkedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("....  For Singly Linked List  ...")
        print(".................................\n\n")

    def test_push_empty(self):
        llist = List()
        value = 88
        llist.push(value)
        self.assertEqual(llist.head.value, value)
        self.assertEqual(llist.tail.value, value)

    def test_push_non_empty(self):
        llist = List()
        value = 33
        llist.push(88)
        llist.push(value)
        self.assertEqual(llist.head.value, value)
        self.assertNotEqual(llist.tail.value, value)

    def test_delete_first_empty(self):
        llist = List()
        self.assertRaises(IndexError, llist.deleteFirst)

    def test_delete_first_single_node(self):
        llist = List()
        llist.push(88)
        try:
            llist.deleteFirst()
            self.assertIsNone(llist.head)
            self.assertIsNone(llist.tail)
        except IndexError:
            self.fail("deleteFirst() unexpectedly raised an IndexError")

    def test_delete_first_from_multi_node(self):
        llist = List()
        llist.push(88)
        llist.push(33)
        try:
            llist.deleteFirst()
            self.assertIsNotNone(llist.head)
            self.assertEqual(llist.head.value, 88)
        except IndexError:
            self.fail("deleteFirst() unexpectedly raised an IndexError")

    def test_append_empty(self):
        llist = List()
        value = 88
        llist.append(value)
        self.assertEqual(llist.head.value, value)
        self.assertEqual(llist.tail.value, value)

    def test_append_non_empty(self):
        llist = List()
        value = 88
        llist.append(33)
        llist.append(value)
        self.assertNotEqual(llist.head.value, value)
        self.assertEqual(llist.tail.value, value)

    def test_delete_last_empty(self):
        llist = List()
        self.assertRaises(IndexError, llist.deleteLast)

    def test_delete_last_one(self):
        llist = List()
        llist.append(88)
        try:
            llist.deleteLast()
            self.assertIsNone(llist.head)
            self.assertIsNone(llist.tail)
        except IndexError:
            self.fail("deleteLast() unexpectedly raised an IndexError")

    def test_delete_last_multi(self):
        llist = List()
        llist.append(88)
        llist.append(33)
        try:
            llist.deleteLast()
            self.assertIsNotNone(llist.head)
            self.assertEqual(llist.tail.value, 88)
        except IndexError:
            self.fail("deleteLast() unexpectedly raised an IndexError")

    def test_insert_before_first(self):
        llist = List()
        value = 88
        llist.push(5)
        llist.insertBefore(llist.tail, value)
        self.assertEqual(llist.head.value, value)
        self.assertEqual(llist.tail.value, 5)

    def test_insert_before_middle(self):
        llist = List()
        value = 88
        llist.push(5)
        llist.push(6)
        llist.insertBefore(llist.head.next, value)
        self.assertEqual(llist.head.next.value, value)

    def test_insert_before_nonexistent(self):
        llist = List()
        value = 88
        llist.push(88)
        llist.insertBefore(None, value)
        self.assertEqual(llist.tail.value, value)

    def test_insert_after_single(self):
        llist = List()
        value = 88
        llist.push(33)
        llist.insertAfter(llist.tail, value)
        self.assertEqual(llist.head.value, 33)
        self.assertEqual(llist.tail.value, value)

    def test_insert_after_multi(self):
        llist = List()
        value = 88
        llist.push(33)
        llist.push(69)
        llist.insertAfter(llist.head, value)
        self.assertEqual(llist.head.next.value, value)

    def test_delete_empty_list(self):
        llist = List()
        self.assertRaises(IndexError, llist.delete, 69)

    def test_delete_from_list(self):
        llist = List()
        llist.push(88)
        llist.push(33)
        try:
            llist.delete(88)
        except IndexError:
            self.fail("delete() unexpectedly raised an IndexError")

    def test_delete_nonexistent(self):
        llist = List()
        llist.push(88)
        self.assertRaises(IndexError, llist.delete, 33)

    def test_display_multi_node(self):
        llist = List()
        llist.push(88)
        llist.push(33)
        llist.display()

    def test_display_one_node(self):
        llist = List()
        llist.push(88)
        llist.display()

    def test_display_empty(self):
        llist = List()
        llist.display()
