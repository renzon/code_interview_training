def evaluate(expression):
    for char in expression:
        if char == '.':
            return float(expression)

    return int(expression)


if __name__ == '__main__':
    import unittest
    from unittest.case import TestCase


    class EpressionValidationTeest(TestCase):
        def test_valid_integers(self):
            self.assertEqual(1, evaluate('1'))
            self.assertEqual(12, evaluate('12'))
            self.assertEqual(123, evaluate('123'))
            self.assertEqual(1234, evaluate('1234'))
            self.assertEqual(1234567890, evaluate('1234567890'))

        def test_valid_floats(self):
            self.assertEqual(1.1, evaluate('1.1'))
            self.assertEqual(12.2, evaluate('12.2'))
            self.assertEqual(123.3, evaluate('123.3'))
            self.assertEqual(1234.4, evaluate('1234.4'))
            self.assertEqual(1234567890.0987654321, evaluate('1234567890.0987654321'))

        def test_invalid_floats(self):
            self.assertRaises(InvalidExpression, evaluate,'1.')
            self.assertRaises(InvalidExpression, evaluate,'1.9.')
            self.assertRaises(InvalidExpression, evaluate,'1.9.9')


    unittest.main()
