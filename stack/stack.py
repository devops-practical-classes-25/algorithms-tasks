class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return self.top is None

    def push(self, data):
        """Добавляет элемент в стек"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Удаляет и возвращает верхний элемент стека"""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент из пустого стека")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        """Возвращает верхний элемент стека без удаления"""
        if self.is_empty():
            raise IndexError("Невозможно посмотреть верхний элемент в пустом стеке")
        return self.top.data

    def __str__(self):
        """Возвращает строковое представление стека"""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Стек пуст"