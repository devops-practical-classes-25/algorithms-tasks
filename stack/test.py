import unittest

from main import Stack

class TestStack(unittest.TestCase):
    """Тесты для проверки работы стека"""

    def test_push_pop(self):
        """Проверка корректности работы push и pop"""
        stack = Stack()

        self.assertTrue(stack.is_empty())
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    def test_peek(self):
        """Проверка корректности работы peek"""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_empty_stack_pop(self):
        """Проверка попытки извлечь элемент из пустого стека"""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_empty_stack_peek(self):
        """Проверка попытки посмотреть верхний элемент в пустом стеке"""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_str(self):
        """Проверка строкового представления стека"""
        stack = Stack()
        self.assertEqual(str(stack), "Стек пуст")
        stack.push(10)
        stack.push(20)
        self.assertEqual(str(stack), "20 -> 10")

if __name__ == "__main__":
    unittest.main()