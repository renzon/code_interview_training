def evaluate(expression):
    return int(expression)


if __name__ == '__main__':
    import unittest
    from unittest.case import TestCase

    VALID_EXPRESSION = '12+5*(7-8)/2'


    class EpressionValidationTeest(TestCase):
        def test_valid_integers(self):
            self.assertEqual(1, evaluate('1'))
            self.assertEqual(12, evaluate('12'))
            self.assertEqual(123, evaluate('123'))
            self.assertEqual(1234, evaluate('1234'))
            self.assertEqual(1234567890, evaluate('1234567890'))


    unittest.main()
