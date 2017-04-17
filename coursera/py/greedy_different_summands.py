# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k = n
    i = 0
    partial = 0
    while i < n:
        i += 1
        if k <= 2*i:
            while i <= n:
                if partial + i == n:
                    partial += i
                    summands.append(i)
                    i = n
                    break
                i += 1
        else:
            partial += i
            summands.append(i)
        k = k - i
    return summands


def test0():
    input = 6
    print(optimal_summands(input))
    output = (3, [1,2,3])


def test1():
    input = 8
    print(optimal_summands(input))
    output = (3, [1, 2, 5])


def test2():
    input = 2
    print(optimal_summands(input))
    output = (2, [2])


def test3():
    input = 10
    print(optimal_summands(input))
    output = (4, [1, 2, 3, 4])


def test4():
    input = 15
    print(optimal_summands(input))
    output = (4, [1, 2, 3, 4, 5])


def test5():
    input = 27
    print(optimal_summands(input))
    output = (4, [1, 2, 3, 4])


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
