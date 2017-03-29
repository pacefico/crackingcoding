# Uses python3
#n = int(input())
#a = [int(x) for x in input().split()]
n = 0
a = []

assert(len(a) == n)

def max_parwise_product(n, a):
    result = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if float(a[i]) * float(a[j]) > result:
                result = float(a[i]) * float(a[j])
    #print("{:.0f}".format(result))
    return result


def max_parwise_product_fast(n, a):
    max1 = 0
    max2 = 0
    for i in range(0, n):
        if a[i] > max1:
            max1 = a[i]
    for i in range(0, n):
        if a[i] > max2 and a[i] != max1:
            max2 = a[i]

    result = float(max1) * float(max2)
    print("{:.0f}".format(result))
    return result


#max_parwise_product_fast(n, a)


def test_stress():
    import random
    import time
    N = 16

    length = 1
    for i in range(1, N):
        length = length * 2
        print("it: {}. Qty:{}".format(i, length))
        my_vec = []
        for j in range(length):
            value = random.randint(0, 99999)
            my_vec.append(value)

        start = time.clock()
        result1 = max_parwise_product(len(my_vec), my_vec)
        print("Normal time: {}".format(time.clock() - start))
        start = time.clock()
        result2 = max_parwise_product_fast(len(my_vec), my_vec)
        print("Faster time: {}".format(time.clock() - start))

        if result1 != result2:
            print("Error!. result1:{} result2:{}".format(result1, result2))
            break


test_stress()

