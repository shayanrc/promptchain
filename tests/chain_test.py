import unittest

from promptchain import Node, Chain, Message
import unittest


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.chain_1 = Chain([self.node_1])
        self.chain_2 = Chain([self.node_1, self.node_2])

    def test_str(self):
        self.assertEqual(str(self.node_1), '1')

    def test_repr(self):
        self.assertEqual(repr(self.node_1), 'Node(1)')

    def test_add(self):
        self.assertEqual(self.node_1 + self.node_2, Chain([self.node_1, self.node_2]))
        # self.assertEqual(self.node_1 + self.chain_1, Chain([self.node_1, self.node_1]))
        with self.assertRaises(TypeError):
            self.node_1 + 5

class TestChain(unittest.TestCase):
    def setUp(self):
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.chain_1 = Chain([self.node_1])
        self.chain_2 = Chain([self.node_1, self.node_2])

    def test_repr(self):
        self.assertEqual(repr(self.chain_1), 'Chain([Node(1)])')
        self.assertEqual(repr(self.chain_2), 'Chain([Node(1), Node(2)])')

    def test_add(self):
        self.assertEqual(self.chain_1 + self.node_2, Chain([self.node_1, self.node_2]))
        with self.assertRaises(TypeError):
            self.chain_1 + 5

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message_1 = Message("user", "Hello")
        self.message_2 = Message("assistant", "Hi")
        self.chain_1 = Chain([self.message_1])
        self.chain_2 = Chain([self.message_1, self.message_2])

    def test_str(self):
        self.assertEqual(str(self.message_1), "{'role': 'user', 'content': 'Hello'}")

    def test_repr(self):
        self.assertEqual(repr(self.message_1), "Message('user', 'Hello')")

    def test_add(self):
        self.assertEqual(self.message_1 + self.message_2, Chain([self.message_1, self.message_2]))
        self.assertEqual(self.message_1 + self.chain_1, Chain([self.message_1, self.message_1]))
        with self.assertRaises(TypeError):
            self.message_1 + 5

    def test_value(self):
        self.assertEqual(self.message_1.value, {'role': 'user', 'content': 'Hello'})

if __name__ == '__main__':
    unittest.main()