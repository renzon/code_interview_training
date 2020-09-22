def max_subarray_sum(iterator):
    iterable = iter(iterator)

    def max_iter(current_sum, max_sum):
        try:
            next_element = next(iterable)
        except StopIteration:
            return max_sum
        current_sum += next_element
        current_sum = max(current_sum, next_element)
        return max_iter(current_sum, max(current_sum, max_sum))


    return max_iter(0, 0)


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_sum([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(max_subarray_sum([-2, -1, -3, -4, -1, -2, 1, -5, -4]))
print(max_subarray_sum([-2, -1, -3, -4, -1, 1, 1, -5, -4]))
print(max_subarray_sum([]))
