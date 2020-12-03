# http://www.programcreek.com/2014/02/leetcode-reverse-words-in-a-string-java/#

class NotFound(Exception):
    pass


import unittest


def longest(s):
    chars_right_index = {}

    for current_end, char in enumerate(s):
        chars_right_index[char] = current_end
        if len(chars_right_index) == 2:
            break
    else:
        raise NotFound()

    current_start = min_start = 0
    current_end += 1
    min_end = current_end

    s_len = len(s)

    def max_interval(start, end, start2, end2):
        if (end - start) >= (end2 - start2):
            return start, end
        return start2, end2

    while current_start < s_len:
        for current_end in range(current_end, s_len):
            current_end_char = s[current_end]
            if current_end_char in chars_right_index:
                chars_right_index[char] = current_end
            else:
                break
        else:
            min_start, min_end = max_interval(min_start, min_end, current_start, current_end + 1)
            break

        min_start, min_end = max_interval(min_start, min_end, current_start, current_end)
        index_char_lst = sorted((v, k) for k, v in chars_right_index.items())
        left_most_char = index_char_lst[0][1]
        right_most_index = index_char_lst[1][0]
        chars_right_index.pop(left_most_char)
        current_start = right_most_index
        chars_right_index[current_end_char] = current_end
        current_end += 1

    return s[min_start: min_end]


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals("bcbbbbcccb", longest("abcbbbbcccbdddadacb"))

    def test_empty(self):
        self.assertRaises(NotFound, longest, "")

    def test_one_char(self):
        self.assertRaises(NotFound, longest, "a_com_fatia_linar")
        self.assertRaises(NotFound, longest, "a_com_fatia_linar" * 2)
        self.assertRaises(NotFound, longest, "a_com_fatia_linar" * 3)
        self.assertRaises(NotFound, longest, "a_com_fatia_linar" * 20)
