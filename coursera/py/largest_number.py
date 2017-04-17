#Uses python3
#encoding: utf-8

""""
answer = empty string
while Digits is not empty:
    maxDigit = -00
    for digit in Digits:
        if digit ≥ maxDigit:
            maxDigit = digit

        append maxDigit to answer
        remove maxDigit from Digits
return answer
"""""

def is_greater_or_equal(a, b):
    if len(str(a)) != len(str(b)):
        res1 = "{}{}".format(a, b)
        res2 = "{}{}".format(b, a)
        response = int(res1) >= int(res2)
    else:
        response = a >= b
    return response


def largest_number(a):
    a.sort(reverse=True)
    res = ""
    while len(a) > 0:
        maxdigit = 0
        index = -1
        for i in range(len(a)):
            if is_greater_or_equal(a[i], maxdigit):
                maxdigit = a[i]
                index = i
        res += str(a[index])
        del a[index]
    return res


def test0():
    a = [1, 5, 4, 9]
    print(largest_number(a))

def test1():
    n = 2
    a = [21, 2]
    print(largest_number(a))
    output = 221

def test2():
    n = 5
    a = [9, 4, 6, 1, 9]
    print(largest_number(a))
    output = 99641

def test3():
    n = 3
    a = [23, 39, 92]
    print(largest_number(a))
    output = 923923

# test1()
# test2()
# test3()

if __name__ == '__main__':
    import sys
    n = int(input())
    a = [int(x) for x in input().split()]

    print(largest_number(a))
    
