import unittest
from deque import Deque


class TestDeque(unittest.TestCase):
    """Тесты для проверки работы двусвязной очереди Deque"""

    def test_initialization(self):
        """Тест инициализации очереди с нулями"""
        deque = Deque(5)
        self.assertEqual([deque.get(i) for i in range(5)], [0, 0, 0, 0, 0])

    def test_appendleft(self):
        """Тест добавления элемента в начало очереди"""
        deque = Deque(3)
        deque.appendleft(10)
        self.assertEqual(deque.get(0), 10)

        deque.appendleft(20)
        self.assertEqual(deque.get(0), 20)
        self.assertEqual(deque.get(1), 10)

        deque.appendleft(30)
        self.assertEqual(deque.get(0), 30)
        self.assertEqual(deque.get(1), 20)
        self.assertEqual(deque.get(2), 10)

    def test_appendleft_overflow(self):
        """Тест на перезапись самого старого элемента"""
        deque = Deque(3)
        deque.appendleft(1)
        deque.appendleft(2)
        deque.appendleft(3)
        deque.appendleft(4) 

        self.assertEqual(deque.get(0), 4)
        self.assertEqual(deque.get(1), 3)
        self.assertEqual(deque.get(2), 2)

    def test_pop(self):
        """Тест удаления элемента из конца"""
        deque = Deque(3)
        deque.appendleft(1)
        deque.appendleft(2)
        deque.appendleft(3)

        last_value = deque.pop()  
        self.assertEqual(last_value, 0)

        self.assertEqual(deque.get(0), 3)
        self.assertEqual(deque.get(1), 2)
        self.assertEqual(deque.get(2), 1)

    def test_pop_empty(self):
        """Тест попытки удаления из пустой очереди"""
        deque = Deque(3)
        deque.pop()
        deque.pop()
        deque.pop()

        with self.assertRaises(IndexError):
            deque.pop()

    def test_get(self):
        """Тест получения элемента по индексу"""
        deque = Deque(4)
        deque.appendleft(5)
        deque.appendleft(10)
        deque.appendleft(15)

        self.assertEqual(deque.get(0), 15)
        self.assertEqual(deque.get(1), 10)
        self.assertEqual(deque.get(2), 5)
        self.assertEqual(deque.get(3), 0)

    def test_get_out_of_bounds(self):
        """Тест получения элемента за границами"""
        deque = Deque(2)
        deque.appendleft(7)
        deque.appendleft(9)

        self.assertEqual(deque.get(0), 9)
        self.assertEqual(deque.get(1), 7)
        self.assertEqual(deque.get(2), 0)

if __name__ == "__main__":
    unittest.main()
