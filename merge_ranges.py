# http://codercareer.blogspot.com.br/2014/08/no-54-merge-ranges.html


def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda r: r[0])  # sorted_ranges = [[5, 13], [8, 19], [27, 39], [31, 37]]

    def merge_rec(s_ranges):  # s_ranges = [[5, 19], [27, 39], [31, 37]]
        if len(s_ranges) <= 1:
            return s_ranges

        # merge case
        first_range = s_ranges[0]  # [5, 19]
        sec_range = s_ranges[1]  # [27, 39]
        if first_range[1] >= sec_range[0]:
            return merge_rec([(first_range[0], sec_range[1])] + s_ranges[2:])
        return [first_range] + merge_rec(s_ranges[1:])

    return merge_rec(sorted_ranges)


print(merge_ranges([[5, 13], [27, 39], [8, 19], [31, 37]]))