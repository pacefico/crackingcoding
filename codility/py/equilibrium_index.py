# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    equilibrum = -1
    for idx in range(len(A)):
        to_verify = A[idx]

        # get the sum of all lower than actual index and all higher than actual index
        lower = sum(A[:idx])
        higher = sum(A[idx:])

        # assert if the sum of actual and the lower is equal the sum of the higher
        if to_verify + lower == higher:
            equilibrum = idx
            break

    # return any element
    return equilibrum

def test_case_0():
    A = [-1, 3, -4, 5, 1, -6, 2, 1]
    response = solution(A)
    print(response)
    return response

def test_case_1():
    A = [9, -3, 10, -1, 3, -4, 5, 1, -6, 2, 1, 10, -3, 9]
    response = solution(A)
    print(response)
    return response

assert test_case_0() == 1
assert test_case_1() == 4
