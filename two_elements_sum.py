from unittest.case import TestCase


def _binary_search(sorted_sequence, start, end, element):
    '''
    Good Case: last element is on of the same. In this case, we only need one bynary search, so it is log(n)
    Worst Case: Sum is not there and minor in
    '''
    if start >= end:
        return start
    else:
        mid = (start + end) // 2
        mid_element = sorted_sequence[mid]
        if mid_element == element:
            return mid
        elif mid_element < element:
            return _binary_search(sorted_sequence, mid + 1, end, element)

        else:
            return _binary_search(sorted_sequence, start, mid_element - 1, element)


def _element_sum_rec(sorted_sequence, start, end, sum):
    if start >= end:
        raise ElementsNotFound()
    bigger_value = sorted_sequence[end]
    other_element = sum - bigger_value
    other_element_index = _binary_search(sorted_sequence, start, end, other_element)
    minor_element = sorted_sequence[other_element_index]
    if minor_element == other_element:
        return minor_element, bigger_value
    return _element_sum_rec(sorted_sequence, other_element_index, end - 1, sum)


def elements_sum(sorted_sequence, sum):
    start = 0
    end = len(sorted_sequence) - 1
    return _element_sum_rec(sorted_sequence, start, end, sum)


class ElementsNotFound(Exception):
    pass


class ElementsSumK(TestCase):
    def test_empty_list(self):
        self.assertRaises(ElementsNotFound, elements_sum, [], 0)

    def test_one_element(self):
        self.assertRaises(ElementsNotFound, elements_sum, [1], 0)

    def test_two_elements_with_sum(self):
        self.assertEqual((1, 2), elements_sum([1, 2], 3))

    def test_sum_on_midle(self):
        self.assertEqual((13, 14), elements_sum(list(range(9)) + [13, 14] + list(range(29, 39)), 27))

    def test_sum_not_found(self):
        self.assertRaises(ElementsNotFound, elements_sum, list(range(10)), 20)
