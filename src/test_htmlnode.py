import unittest
from unittest.mock import patch
from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        print(f"\nStarting {self.__class__.__name__}")

    def tearDown(self):
        print(f"Completed {self.__class__.__name__}")

    def test_props_to_html_testcase1(self):
        props1 = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        expected_result = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(props1.props_to_html(),expected_result)

    def test_props_to_html_testcase2(self):
        props1 = HTMLNode(props={"href": "https://www.google.com","target": "_blank","test":"additional_test_string"})
        expected_result = 'href="https://www.google.com" target="_blank" test="additional_test_string"'
        self.assertEqual(props1.props_to_html(),expected_result)

    def test_to_html_not_implemented_error_raises(self):
        htmlnode1 = HTMLNode()
        with self.assertRaises(NotImplementedError):
            htmlnode1.to_html()

    @patch('builtins.print')
    def test_HTMLNode_print(self,mock_print):
        htmlnode1 = HTMLNode('<a>','this_is_html_value',['a','b','c','d'],{"href": "https://www.google.com","target": "_blank",})
        print(HTMLNode)
        mock_print.assert_called_once_with(HTMLNode)

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        print(f"\nStarting {self._testMethodName}")

    def tearDown(self):
        print(f"Completed {self._testMethodName}")

    def test_to_html_not_implemented_error_not_raises(self):
        leafnode = LeafNode('p','this_is_html_value',{"href": "https://www.google.com","target": "_blank"})
        print(leafnode)
        try:
            print(leafnode.to_html())
        except NotImplementedError :
            self.fail(f"LeafNode.to_html() raised NotImplementedError unexpectedly")

    def test_LEAFNode_print_to_debug_only(self):
        leafnode = LeafNode('p','this_is_html_value',{"href": "https://www.google.com","target": "_blank"})
        print(leafnode)

    def test_to_html_value_empty(self):
        leafnode = LeafNode('p','',{"href": "https://www.google.com","target": "_blank"})
        with self.assertRaises(ValueError):
            print(leafnode.to_html())

    def test_to_html_value_none(self):
        leafnode = LeafNode('p',None,{"href": "https://www.google.com","target": "_blank"})
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_to_html_tag_empty(self):
        leafnode = LeafNode('','this_is_html_value',{"href": "https://www.google.com","target": "_blank"})
        print(leafnode.to_html())
        self.assertEqual(leafnode.to_html(),leafnode.value)

    def test_to_html_tag_none(self):
        leafnode = LeafNode(None,'this_is_html_value',{"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(leafnode.to_html(),leafnode.value)