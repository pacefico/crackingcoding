# Uses python3
#encoding: utf-8
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    while left <= right:
        middle = int((left + right) / 2)
        if x == a[middle]:
            return middle
        if x < a[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def test0():
    a = [5, 1, 5, 8, 12, 13]
    x = [5, 8, 1, 23, 1, 11]

    out = [2, 0, -1, 0, -1]

    binary_search(a[1:], x[1:])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]

    for x in data[n + 2:]:
        #replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')
