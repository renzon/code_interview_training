# http://www.programcreek.com/2013/01/leetcode-valid-palindrome-java/
import unittest


def is_palindrome(s):
    class IndexNotFound(Exception):
        pass

    start = 0
    end = len(s) - 1

    def find_alpha_index_and_lower_char(current_idx, op):
        while 0 <= current_idx < len(s):
            char = s[current_idx]
            if char.isalpha():
                return current_idx, char.lower()
            else:
                current_idx = op(current_idx)
        raise IndexNotFound()

    try:
        while True:
            start, s_char = find_alpha_index_and_lower_char(start, lambda i: i + 1)
            end, e_char = find_alpha_index_and_lower_char(end, lambda i: i - 1)
            if start > end:
                return True
            elif s_char == e_char:
                start += 1
                end -= 1
            else:
                return False
    except IndexNotFound:
        return False


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_palindrome('Red rum, sir, is murder'))
        self.assertFalse(is_palindrome('Programcreek is awesome'))
