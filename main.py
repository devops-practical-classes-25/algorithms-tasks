from stack.stack import Stack

def is_brackets_balanced(expression: str) -> bool:
    """
    Проверяет правильность расстановки скобок в арифметическом выражении.
    Возвращает True, если скобки расставлены правильно, иначе False.
    """
    pass

def main():
    expression = "3 + 2 * (5 - [4 / {2 + 1}])"
    print(f"Проверка правильности скобок в выражении: {expression}")
    result = "Yes" if is_brackets_balanced(expression) else "No"
    print("Результат:", result)

if __name__ == "__main__":
    main()