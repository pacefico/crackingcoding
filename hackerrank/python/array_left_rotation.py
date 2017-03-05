"""
A left rotation operation on an array of size  shifts each of the array's elements
unit to the left. For example, if left rotations are performed on array , then the
array would become .

Given an array of  integers and a number, , perform  left rotations on the array.
Then print the updated array as a single line of space-separated integers.

url: https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""


def test_left_array(a, n, k):
    for iter in range(k):
        a.append(a[0])
        del a[0]
    return a

def case0():
    i1 = "5 4"
    i2 = "1 2 3 4 5"

    n, k = list(map(int, i1.strip().split(' ')))
    a = list(map(int, i2.strip().split(' ')))

    return test_left_array(a, n, k)

assert case0() == [5, 1, 2, 3, 4]
