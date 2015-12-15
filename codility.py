# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"



def solution(A):
    # write your code in Python 2.7
    sum_left = sum(A[:-2])  # start
    sum_right = A[-1]
    start_index = len(A) - 2

    for i in xrange(start_index, 0, -1):
        if sum_left == sum_right:
            return i
        else:
            sum_left -= A[i-1]
            sum_right += A[i]

    return -1

# Time O(n) once it takes O(n) to make first left_sum and after that Other O(n) in worst case to pass on entire list
# O(n) because it needs to slice for the first left_sum

print(solution([3,1,3]))
print(solution([3,1,2,3]))
print(solution([-1, 3, -4, 5, 1, -6, 2, 1]))
