class Node:
    """
    Узел двусвязного списка.

    Узел содержит:
    - `value` (int): значение, хранимое в узле.
    - `next` (`Node` | None): ссылка на следующий узел в списке.
    - `prev` (`Node` | None): ссылка на предыдущий узел в списке.
    """
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    """
    Двусторонняя очередь, построенная на двусвязном списке.

    Двусторонняя очередь позволяет добавлять и удалять элементы с обоих концов.
    Эта реализация поддерживает фиксированный размер и автоматически удаляет
    старые элементы при добавлении новых.

    Основные операции:
    - `appendleft(value)`: добавляет элемент в начало очереди.
    - `pop()`: удаляет и возвращает последний элемент.
    - `get(index)`: получает элемент по индексу (0 — первый, 1 — второй и т. д.).

    Параметры:
    - `max_size` (int): максимальный размер очереди.

    Атрибуты:
    - `size` (int): текущий размер очереди.
    - `head` (`Node` | None): первый элемент очереди.
    - `tail` (`Node` | None): последний элемент очереди.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.tail = None

        for _ in range(max_size):
            self.appendleft(0)

    def appendleft(self, value):
        """Добавляет элемент в начало очереди"""
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        if self.size == self.max_size:
            self.pop()
        else:
            self.size += 1

    def pop(self):
        """Удаляет элемент из конца очереди и возвращает его"""
        if self.tail is None:
            raise IndexError("pop from empty deque")

        value = self.tail.value

        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return value

    def get(self, index):
        """Получает элемент по индексу (0 - первый, 1 - второй и т.д.)"""
        current = self.head
        for _ in range(index):
            if current is None:
                return 0
            current = current.next
        return current.value if current else 0