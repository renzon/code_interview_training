# problem from here: http://blog.codility.com/2011/03/solutions-for-task-equi.html



def solution(A):
    # write your code in Python 2.7
    sum_left = 0  # start
    previous = 0
    sum_right = sum(A)

    for i, current in enumerate(A):
        sum_left += previous
        sum_right -= current
        if sum_left == sum_right:
            return i
        previous = current

    return -1


# Time O(n) once it takes O(n) to make first left_sum and after that Other O(n) in worst case to pass on entire list
# O(1) in memory because this time was used an generator expression to make some instead of

print(solution([]))
print(solution([1]))
print(solution([1, 1]))
print(solution([1, 0]))
print(solution([3, 1, 3]))
print(solution([3, 1, 2, 3]))
print(solution([-1, 3, -4, 5, 1, -6, 2, 1]))
