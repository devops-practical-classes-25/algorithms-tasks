from stack.stack import Stack

def is_brackets_balanced(expression: str) -> str:
    "Проверяет правильность расстановки скобок в арифметическом выражении."
    staples = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()

    for char in expression:
        if char in staples:
            stack.push(char)
        elif char in staples.values():
            if stack.is_empty() or staples[stack.pop()] != char:
                return "No"

    return "Yes" if stack.is_empty() else "No"

def main():
    expression = "3 + 2 * (5 - [4 / {2 + 1}])"
    print(f"Проверка правильности скобок в выражении: {expression}")
    print("Результат:", is_brackets_balanced(expression))

if __name__ == "__main__":
    main()