import unittest
from main import is_brackets_balanced

class TestBracketsBalance(unittest.TestCase):
    """Тесты для проверки функции расставления скобок"""

    def test_balanced_brackets(self):
        """Проверка корректных выражений с правильно расставленными скобками"""
        test_data = [
            ("3 + 2 * (5 - [4 / {2 + 1}])", "Yes"),
            ("(3 + 2) * [5 - {4 / (2 + 1)}]", "Yes"),
            ("{[()()]}", "Yes"),
            ("()", "Yes"),
            ("{}", "Yes"),
            ("[]", "Yes"),
            ("123 + (456 * {789})", "Yes"),
            ("(12 + 34) * [56 - {78 + 90}]", "Yes")
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_unbalanced_brackets(self):
        """Проверка некорректных выражений с ошибками в расставленных скобках"""
        test_data = [
            ("3 + 2 * (5 - [4 / {2 + 1}])", "Yes"),
            ("(3 + 2) * [5 - {4 / (2 + 1)}", "No"),
            ("{[()()}", "No"),
            ("[3 + 2] * {5 - (4 / 2", "No"),
            ("{[()()]}", "Yes"),
            ("(3 + 2", "No"),
            ("", "Yes"),
            ("(", "No"),
            ("123 + (456 * {789})", "Yes"),
            ("(12 + 34) * [56 - {78 + 90}", "No") 
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_edge_cases(self):
        """Проверка крайних случаев"""
        test_data = [
            ("()", "Yes"),
            ("((()))", "Yes"),
            ("[{()}]", "Yes"),
            ("(((((((((((((((())))))))))))))))", "Yes"),
            ("(((((((((((((((()))))))))))))))", "No"),
            ("123 + (456)", "Yes"),
            ("(12 + 34) * 56", "Yes")
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_single_brackets(self):
        """Тестирование выражений с одиночными скобками"""
        test_data = [
            ("(", "No"),
            (")", "No"),
            ("[", "No"),
            ("]", "No"),
            ("{", "No"),
            ("}", "No"),
            ("(123)", "Yes"),
            ("[456]", "Yes"),
            ("{789}", "Yes")
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_mixed_brackets(self):
        """Тестирование выражений с разными типами скобок"""
        test_data = [
            ("(}", "No"),
            ("[)", "No"),
            ("{)", "No"),
            ("{[()()]}", "Yes"),
            ("[{(})]", "No"),
            ("(123 + 456)", "Yes"),
            ("[789 + (12 * 34)]", "Yes")
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_empty_expression(self):
        """Проверка пустого выражения"""
        self.assertEqual(is_brackets_balanced(""), "Yes")  # Пустое выражение считается сбалансированным

    def test_expression_with_only_one_type_of_bracket(self):
        """Проверка выражений с только одним типом скобок"""
        test_data = [
            ("()", "Yes"),
            ("(())", "Yes"),
            ("((()))", "Yes"),
            ("(()))", "No"),
            ("(()", "No"),
            ("123 + (456)", "Yes"), 
            ("(12 + 34) * 56", "Yes") 
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

    def test_expression_with_multiple_brackets_of_same_type(self):
        """Проверка выражений с несколькими одинаковыми скобками"""
        test_data = [
            ("(((((((((())))))))))", "Yes"),
            ("(((((((((()))))))))", "No"),
            ("(123 + (456))", "Yes"),
            ("((12 + 34) * (56 + 78))", "Yes")
        ]
        
        for expression, expected in test_data:
            self.assertEqual(is_brackets_balanced(expression), expected)

if __name__ == "__main__":
    unittest.main()