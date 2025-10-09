# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List, Union


class ListView:
    """
    A class to represent contiguous sublists in a list with a constant

    >>> l = ListView([1, 2, 3, 4, 5, 6, 7])
    >>> len(l)
    7
    >>> slc = l[1:6]
    >>> slc
    [2, 3, 4, 5, 6]
    >>> l
    [1, 2, 3, 4, 5, 6, 7]
    >>> len(slc)
    5
    >>> slc[0]
    2
    >>> first_half, second_half = l.bissect()
    >>> first_half
    [1, 2, 3, 4]
    >>> second_half
    [5, 6, 7]
    >>> first_half, second_half = second_half.bissect()
    >>> first_half
    [5, 6]
    >>> second_half
    [7]
    >>> first_half, second_half = first_half.bissect()
    >>> first_half
    [5]
    >>> second_half
    [6]
    >>> first_half, second_half = first_half.bissect()
    >>> first_half
    [5]
    >>> second_half
    []
    """


    def __init__(self, l: List, begin_index: int = 0, new_len: int = None):
        self._l = l
        self._begin_index = begin_index
        self._len = len(l) if new_len is None else new_len

    def __len__(self):
        return max(self._len, 0)

    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, slice):
            start = index.start
            if start is None:
                start = 0
            stop = index.stop
            if stop is None:
                stop = len(self)
            return ListView(self._l, self._begin_index + start, min(stop - start, len(self)))
        elif index < 0:
            index = len(self) + index
        if index >= len(self):
            raise IndexError(f'Index {index} out of range')
        return self._l[self._begin_index + index]

    def __add__(self, other):
        return ListView(list(self) + list(other))

    def __repr__(self):
        return repr(list(self))

    def middle_index(self):
        return (len(self) + 1) // 2


    def bissect(self):
        return self[:self.middle_index()], self[self.middle_index():]


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    >>> find_median_sorted_arrays([], [2])
    2.0
    >>> find_median_sorted_arrays([3], [])
    3.0
    >>> find_median_sorted_arrays([4], [2])
    3.0
    >>> find_median_sorted_arrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17])
    9.0
    >>> find_median_sorted_arrays([1,2,3,4,5, 6,7,8,9,10,11,12,13], [14,15,16,17])
    9.0
    >>> find_median_sorted_arrays([1,2,3,4,5, 6,7,8,9,10,11,12,13], [14,15,16,17, 18])
    9.5
    >>> find_median_sorted_arrays([1,2,3,4,5, 6,7,8,9], [10,11,12,13 ,14,15,16,17, 18])
    9.5
    >>> find_median_sorted_arrays([2,2,4,4], [2,2,4,4])
    3.0
    >>> find_median_sorted_arrays([2,2,4,4], [2,2,2,4,4])
    2.0
    >>> find_median_sorted_arrays([1,2,2], [1,2,3])
    2.0
    >>> find_median_sorted_arrays([0,0,0,0,0], [-1,0,0,0,0,0,1])
    0.0
    >>> find_median_sorted_arrays([1,2,3], [1,2])
    2.0
    >>> find_median_sorted_arrays([2], [1,3,4])
    2.5
    >>> find_median_sorted_arrays([4], [1,2,3,5])
    3.0
    >>> find_median_sorted_arrays([1, 2], [-1, 3])
    1.5
    >>> find_median_sorted_arrays([3], [1,2,4,5])
    3.0
    >>> find_median_sorted_arrays([1, 3], [2, 7])
    2.5
    >>> find_median_sorted_arrays([1,2,3,4,5], [6,7,8,9,10])
    5.5
    >>> find_median_sorted_arrays([6,7,8,9,10], [1,2,3,4,5])
    5.5
    >>> find_median_sorted_arrays([4, 6, 8, 10, 10], [2, 4])
    6.0
    >>> find_median_sorted_arrays([0,0], [0,0])
    0.0
    >>> find_median_sorted_arrays([2, 4], [4])
    4.0
    >>> find_median_sorted_arrays([4, 6], [2, 4])
    4.0
    >>> find_median_sorted_arrays([4, 6, 8], [2, 4])
    4.0
    >>> find_median_sorted_arrays([4, 6, 8, 10], [2, 4])
    5.0
    >>> find_median_sorted_arrays([], [1,2,3,4])
    2.5
    >>> find_median_sorted_arrays([2], [1,3,4,5,6])
    3.5
    >>> find_median_sorted_arrays([2], [1,3,4,5,6,7,8])
    4.5
    >>> find_median_sorted_arrays([5], [1,2,3,4,6])
    3.5
    """
    list_view_min, list_view_max = sorted([ListView(nums1), ListView(nums2)], key=len)
    total_len = len(list_view_max) + len(list_view_min)
    i = (total_len - 1) // 2
    j = (total_len) // 2

    while len(list_view_max) > 2 and list_view_min:
        min_first_half, min_second_half = list_view_min.bissect()
        max_first_half, max_second_half = list_view_max.bissect()

        first_halfs_last_idx = len(min_first_half) + len(max_first_half) - 1

        if j <= first_halfs_last_idx:
            if len(min_second_half) == 0:
                if min_first_half[0] > max_second_half[0]:
                    min_first_half=min_first_half[0:0]
                else:
                    max_second_half = max_second_half[0:0]
            elif min_second_half[0] == max_second_half[0]:
                max_second_half = max_second_half[0:0]
                min_second_half = min_second_half[0:0]
            elif min_second_half[0] > max_second_half[0]:
                min_second_half = min_second_half[0:0]
            else:
                max_second_half = max_second_half[0:0]
        elif i > first_halfs_last_idx:
            if max_first_half[-1] <= min_first_half[-1]:
                i -= len(max_first_half)
                j -= len(max_first_half)
                max_first_half = max_first_half[0:0]
            else:
                i -= len(min_first_half)
                j -= len(min_first_half)
                min_first_half = min_first_half[0:0]
        elif max_first_half[-1] == min_first_half[-1]:
            if i == first_halfs_last_idx:
                max_first_half = max_first_half[0:0]
                min_first_half = min_first_half[len(min_first_half) - 1:]
                i -= first_halfs_last_idx
                j -= first_halfs_last_idx
        elif max_first_half[-1] > min_first_half[-1]:
            i-=len(min_first_half)
            j-=len(min_first_half)
            min_first_half = min_first_half[0:0]
        else:
            i -= len(max_first_half)
            j -= len(max_first_half)
            max_first_half = min_first_half[0:0]

        list_view_max = max_first_half + max_second_half
        list_view_min = min_first_half + min_second_half
        list_view_min, list_view_max = sorted([list_view_max, list_view_min], key=len)

    if len(list_view_min)==0:
        lst= list_view_max
    else:
        lst = sorted(list_view_max[:2] + list_view_min[:2])
    return (lst[i] + lst[j]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return find_median_sorted_arrays(nums1, nums2)
