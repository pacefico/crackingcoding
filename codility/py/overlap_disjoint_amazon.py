# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import random
import itertools

def join(tuple_a, tuple_b):
    # A <= L <= B   and   C <= L <= D
    # -4 <= 1 <= 2 True
    # -4 <= 5 <= 2 False
    # 1 <= -4 <= 5 False
    # 1 <= 2 <= 5 True

    first = tuple_b[0] <= tuple_a[0] <= tuple_b[1] or tuple_b[0] <= tuple_a[1] <= tuple_b[1]
    if first and tuple_a[0] <= tuple_b[0] <= tuple_a[1] or tuple_a[0] <= tuple_b[1] <= tuple_a[1]:
        return min(tuple_a[0], tuple_b[0]), max(tuple_a[1], tuple_b[1])

    # first = (tuple_a[0] >= tuple_b[0] and tuple_a[0] <= tuple_b[1]
    #     or tuple_a[1] >= tuple_b[0] and tuple_a[1] <= tuple_b[1])
    # if first and (tuple_b[0] >= tuple_a[0] and tuple_b[0] <= tuple_a[1]
    #     or tuple_b[1] >= tuple_a[0] and tuple_b[1] <= tuple_a[1]):
    #         return min(tuple_a[0], tuple_b[0]), max(tuple_a[1], tuple_b[1])

    # if (1 >= -4 and 1 <= 2 or 5 >= -4 and 5 <= 2):
    #     print(True)
    # if (-4 >= 1 and -4 <= 5 or 2 >= 1 and 2 <= 5):
    #     print(True)

    return None

def solution2(A,B):
    from itertools import chain
    def get_first(seq):
        return (x for x in seq)

    common = set(get_first(A)).intersection(get_first(B))
    # And again, python makes it really easy to merge sets using just a A+B+C
    # overlap = [tup for tup in A + B + C if tup[0] in set_ABC]

    # overlap = [tup for tup in A + B if tup in set_AB]
    #
    # print (overlap)

    #a = [x for x in chain(A, B) if x[0] not in seen and not seen.add(x[0])]
    # print (common)
    # [(1, 2), (2, 3), (4, 5), (5, 2), (6, 3)]

def solution(A, B):
    # write your code in Python 2.7

    elements = 0
    #compare size of both arrays to assure equality
    if len(A) == len(B):
        while len(A) > 0:
            tuple_a = (A[0], B[0])
            # remove first tuple to compare to others
            del A[0]
            del B[0]

            result = None
            for i in range(len(A)):
                tuple_b = (A[i], B[i])
                #print ("comparing {} to {}".format(tuple_a, tuple_b))
                result = join(tuple_a, tuple_b)
                if result is not None:
                    # if tuple joined remove second tuple from the list
                    del A[i]
                    del B[i]
                    elements += 1
                    #print("ok! {} lenA:{}, lenB:{}".format(result, len(A), len(B)))
                    break
            if not result:
                elements += 1
            #print("lenA:{}, lenB:{}".format(len(A), len(B)))
        #print(elements)

    return elements


def generate_files():
    with open("inputA0.txt", 'w+') as f_a:
        with open("inputB0.txt", 'w+') as f_b:
            for i in range(100):
                randA = random.randint(-100, 100)
                randB = random.randint(-100, 100)
                f_a.writelines("{}\n".format(randA))
                f_b.writelines("{}\n".format(randB))

def from_file():
    import time
    inputA = []
    inputB = []

    with open("inputA.txt", 'r') as f_a:
        with open("inputB.txt", 'r') as f_b:
            n = 50000
            for i in range(n):
                inputA.append(int(f_a.readline()))
                inputB.append(int(f_b.readline()))

    start = time.clock()
    print(solution(inputA, inputB))
    end = time.clock()
    print ("time: %.2gs" % (end - start))

def from_memory():
    import time
    N = 1000000
    inputA = []
    inputB = []

    n = 100000
    for i in range(n):
        randA = random.randint(-N, N)
        randB = random.randint(-N, N)
        inputA.append(int(randA))
        inputB.append(int(randB))

    print("starting...")
    start = time.clock()
    print(solution(inputA, inputB))
    #print("({}, {})".format(inputA, inputB))
    end = time.clock()
    print ("time: %.2gs" % (end - start))



def test_case_0():
    A = [1, 12, 42, 70, 36, -4, 43, 15]
    B = [5, 15, 44, 72, 36, 2, 69, 24]

    print(solution(A,B))

# def test_case_1():
#     A = [1, 12, 42, 70, 36, -4, 43, 15]
#     B = [5, 15, 44, 72, 36, 2, 69, 24]
#
#     print(solution(A,B))

#test_case_0()
#from_file()
from_memory()