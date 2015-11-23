import operator

OPERATIONS_MAP = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


class InvalidExpression(Exception):
    pass


def calculate(tokens):
    tokens_reversed = list(reversed(tokens))
    stack = []

    def simplify_tail_operations():
        while len(stack) > 1 and stack[-2] != '(':
            second_number = stack.pop()
            operation = stack.pop()
            first_number = stack.pop()
            result = OPERATIONS_MAP[operation](first_number, second_number)
            stack.append(result)

    while tokens_reversed:
        token = tokens_reversed.pop()
        if token == ')':
            simplify_tail_operations()
            number = stack.pop()
            stack.pop()  # removing respective "("
            stack.append(number)
        else:
            stack.append(token)

    simplify_tail_operations()
    return stack[0]


def evaluate(expression):
    tokens = tokenizer(expression)

    return calculate(tokens)


def tokenizer(expression):
    tokens = []
    current_token = []
    previous_char_is_sign = False
    parenthesis_count = 0
    for char in expression:
        if char in OPERATIONS_MAP.keys():
            if previous_char_is_sign:
                raise InvalidExpression('Sign can not be followed by another sign')

            previous_char_is_sign = True
            if current_token:
                tokens.append(evaluate_number(current_token))
            tokens.append(char)
            current_token = []
        else:
            previous_char_is_sign = False
            if char == '(':
                parenthesis_count += 1
                tokens.append(char)
            elif char == ')':
                parenthesis_count -= 1
                if current_token:
                    tokens.append(evaluate_number(current_token))
                tokens.append(char)
                current_token = []
            else:
                current_token.append(char)
    if parenthesis_count != 0:
        raise InvalidExpression('Parenthesis unbalanced')
    if current_token:
        tokens.append(evaluate_number(current_token))
    return tokens


def evaluate_number(expression):
    dot_found = False
    expression = ''.join(expression)

    for char in expression:
        if char == '.':
            if dot_found:
                raise InvalidExpression('%s is not an valid float' % expression)
            else:
                dot_found = True

    if dot_found and expression[-1] == '.':
        raise InvalidExpression('%s is not an valid float' % expression)

    if dot_found:
        return float(expression)

    return int(expression)


if __name__ == '__main__':
    import unittest
    from unittest.case import TestCase


    class EvaluationTests(TestCase):
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

        def test_invalid_floats_with_dot_but_no_decimal(self):
            self.assertRaises(InvalidExpression, evaluate, '1.')
            self.assertRaises(InvalidExpression, evaluate, '12323.')

        def test_invalid_floats_with_2_dots(self):
            self.assertRaises(InvalidExpression, evaluate, '1..')
            self.assertRaises(InvalidExpression, evaluate, '1.9.')
            self.assertRaises(InvalidExpression, evaluate, '1.9.9')

        def test_valid_sum(self):
            self.assertEqual(2, evaluate('1+1'))
            self.assertEqual(14, evaluate('1+1+12'))

        def test_expression_with_2_sum_signs(self):
            self.assertRaises(InvalidExpression, evaluate, '1++')
            self.assertRaises(InvalidExpression, evaluate, '1++1')

        def test_valid_float_sum(self):
            self.assertEqual(2.0, evaluate('1+1.0'))
            self.assertEqual(14.0, evaluate('1.0+1+12'))

        def test_valid_subtraction(self):
            self.assertEqual(0, evaluate('1-1'))
            self.assertEqual(-8, evaluate('1-9'))

        def test_valid_multiplication(self):
            self.assertEqual(1, evaluate('1*1'))
            self.assertEqual(0, evaluate('0*0'))
            self.assertEqual(625, evaluate('25*25'))

        def test_valid_division(self):
            self.assertEqual(1, evaluate('1/1'))
            self.assertEqual(2, evaluate('4/2'))
            self.assertEqual(2.5, evaluate('5/2'))

        def test_simple_parenthesis(self):
            self.assertEqual(2, evaluate('(1+1)'))

        def test_multiple_parenthesis(self):
            self.assertEqual(6, evaluate('(1+1)+(2*2)'))

        def test_multilevel_parenthesis(self):
            self.assertEqual(34, evaluate('(31+1)+(2*2/((4-1)-1))'))

        def test_unbalanced_parenthesis(self):
            self.assertRaises(InvalidExpression, evaluate, '(31+1)+(2*2/((4-1)-1)')


    for token in tokenizer('(31+1)+(2*2/((4-1)-1))'):
        print('Token: %s' % token, 'Type: %s' % type(token))

    unittest.main()
