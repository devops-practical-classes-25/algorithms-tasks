import unittest
from main import is_brackets_balanced

class TestBracketsBalance(unittest.TestCase):
    """Тесты для проверки функции расставления скобок"""

    def test_balanced_brackets(self):
        """Проверка корректных выражений с правильно расставленными скобками"""
        test_data = [
            ("3 + 2 * (5 - [4 / {2 + 1}])", True),
            ("(3 + 2) * [5 - {4 / (2 + 1)}]", True),
            ("{[()()]}", True),
            ("()", True),
            ("{}", True),
            ("[]", True),
            ("123 + (456 * {789})", True),
            ("(12 + 34) * [56 - {78 + 90}]", True)
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_unbalanced_brackets(self):
        """Проверка некорректных выражений с ошибками в расставленных скобках"""
        test_data = [
            ("3 + 2 * (5 - [4 / {2 + 1}])", True),
            ("(3 + 2) * [5 - {4 / (2 + 1)}", False),
            ("{[()()}", False),
            ("[3 + 2] * {5 - (4 / 2", False),
            ("{[()()]}", True),
            ("(3 + 2", False),
            ("", True),
            ("(", False),
            ("123 + (456 * {789})", True),
            ("(12 + 34) * [56 - {78 + 90}", False) 
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_edge_cases(self):
        """Проверка крайних случаев"""
        test_data = [
            ("()", True),
            ("((()))", True),
            ("[{()}]", True),
            ("(((((((((((((((())))))))))))))))", True),
            ("(((((((((((((((()))))))))))))))", False),
            ("123 + (456)", True),
            ("(12 + 34) * 56", True)
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_single_brackets(self):
        """Тестирование выражений с одиночными скобками"""
        test_data = [
            ("(", False),
            (")", False),
            ("[", False),
            ("]", False),
            ("{", False),
            ("}", False),
            ("(123)", True),
            ("[456]", True),
            ("{789}", True)
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_mixed_brackets(self):
        """Тестирование выражений с разными типами скобок"""
        test_data = [
            ("(}", False),
            ("[)", False),
            ("{)", False),
            ("{[()()]}", True),
            ("[{(})]", False),
            ("(123 + 456)", True),
            ("[789 + (12 * 34)]", True)
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_empty_expression(self):
        """Проверка пустого выражения"""
        self.assertEqual(is_brackets_balanced(""), True)  # Пустое выражение считается сбалансированным

    def test_expression_with_only_one_type_of_bracket(self):
        """Проверка выражений с только одним типом скобок"""
        test_data = [
            ("()", True),
            ("(())", True),
            ("((()))", True),
            ("(()))", False),
            ("(()", False),
            ("123 + (456)", True), 
            ("(12 + 34) * 56", True) 
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_expression_with_multiple_brackets_of_same_type(self):
        """Проверка выражений с несколькими одинаковыми скобками"""
        test_data = [
            ("(((((((((())))))))))", True),
            ("(((((((((()))))))))", False),
            ("(123 + (456))", True),
            ("((12 + 34) * (56 + 78))", True)
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

if __name__ == "__main__":
    unittest.main()