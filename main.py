from typing import TypeVar

from heap.heap import Heap, HeapType

T = TypeVar("T")


def heap_sort(items: list[T]) -> list[T]:
    """Сортирует элементы списка.

    :param items: Список элементов для сортировки.
    :return: Список отсортированных элементов.
    """
    heap = Heap(heap_type=HeapType.MIN)

    for item in items:
        heap.push(item)
    
    sorted_items = []
    while len(heap) > 0:
        sorted_items.append(heap.pop())
    
    return sorted_items


def main():
    items = [5, 8, 1, 4, -7, 6, 12, 19, -6]
    print(heap_sort(items))


if __name__ == "__main__":
    main()