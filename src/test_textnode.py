import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,"boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD,"boot.dev")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2= TextNode("This is a different text node",TextType.BOLD)
        self.assertNotEqual(node,node2)
    
    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node",TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_url_None_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"Boot.dev")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()
