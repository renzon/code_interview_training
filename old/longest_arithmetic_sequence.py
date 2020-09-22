# http://codercareer.blogspot.com.br/2014/03/no-53-longest-arithmetic-sequence.html
def longest_arithmetic_sequence(seq):
    s = sorted(seq)  # [1, 3, 5, 6, 7, 9]

    def long_rec(sorted_seq):
        sec_len = len(sorted_seq)
        if sec_len <= 2:
            return sec_len
        next = sorted_seq[1]
        rate = next - sorted_seq[0]
        longest = 2
        next += rate
        for item in sorted_seq[2:]:
            if next == item:
                next += rate
                longest += 1
            elif next < item:
                break

        remaining = sorted_seq[1:]

        if len(remaining) <= longest:
            return longest
        return max(longest, long_rec(remaining))

    return long_rec(s)


print(longest_arithmetic_sequence([1, 6, 3, 5, 9, 7, 11, 78, 89 , 110]))