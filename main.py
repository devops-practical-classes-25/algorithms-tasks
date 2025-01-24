from stack.stack import Stack

def is_brackets_balanced(expression: str) -> bool:
    """
    Проверяет правильность расстановки скобок в арифметическом выражении.
    Возвращает True, если скобки расставлены правильно, иначе False.
    """
    staples = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()

    for char in expression:
        if char in staples:
            stack.push(char)
        elif char in staples.values():
            if stack.is_empty() or staples[stack.pop()] != char:
                return False

    return stack.is_empty()

def main():
    expression = "3 + 2 * (5 - [4 / {2 + 1}])"
    print(f"Проверка правильности скобок в выражении: {expression}")
    result = "Yes" if is_brackets_balanced(expression) else "No"
    print("Результат:", result)

if __name__ == "__main__":
    main()