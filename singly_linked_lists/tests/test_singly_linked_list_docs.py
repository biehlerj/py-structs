from singly_linked_list.singly_linked_list import List, Node
import inspect
import unittest


class TestSinglyLinkedListDocs(unittest.TestCase):
    list_funcs = inspect.getmembers(List, inspect.isfunction)
    node_funcs = inspect.getmembers(Node, inspect.isfunction)
    all_funcs = node_funcs + list_funcs

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Documentation .....")
        print("....  For Singly Linked List  ...")
        print(".................................\n\n")

    def test_list_doc_file(self):
        """... documentation for List"""
        actual = List.__doc__
        self.assertIsNotNone(actual)

    def test_node_doc_file(self):
        """... documentation for Node"""
        actual = Node.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in singly_linked_list.py"""
        all_functions = TestSinglyLinkedListDocs.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)
