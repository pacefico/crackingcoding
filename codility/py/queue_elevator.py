"""
queue_elevator
Ps: Bad approach for time complexity, need to test with larger inputs and adapt

A - people weight
B - floor to stop

M - floors available
X - people capacity
Y - max weight capacity
"""

from Queue import Queue

def solution(A, B, M, X, Y):
    my_queue = Queue()

    count = 0
    stops = 0
    while count < len(A):
        free_cap = Y
        actual_floor = 0
        people_count = 0

        while True:
            weight = A[count]
            if weight <= free_cap:
                my_queue.put(count)
                free_cap -= weight
                print("get: {} w:{} free_w:{}".format(count, weight,free_cap))
                count += 1
                people_count +=1
            else:
                break

            if people_count == X or count == len(A):
                break

        while not my_queue.empty():
            val = my_queue.get()
            people_floor = B[val]
            print ("leave: {} floor:{}".format(val, people_floor))
            if actual_floor != people_floor:
                stops += 1
                actual_floor = people_floor
            else:
                print("same floor")

            my_queue.task_done()

        print("come back!")
        stops += 1

    print("stops: {}".format(stops))


def test_1():
    A = [40, 40, 100, 80, 20]
    B = [3, 3, 2, 2, 3]

    solution(A, B, 3, 5, 200)

def test_2():
    A = [40, 60, 100, 80, 20]
    B = [3, 3, 2, 2, 3]

    solution(A, B, 3, 5, 200)

def test_3():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 3]

    solution(A, B, 3, 5, 200)

def test_4():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 5]

    solution(A, B, 3, 6, 200)

def test_5():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 5]

    solution(A, B, 3, 6, 201)

def test_6():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 5]

    solution(A, B, 1, 1, 201)

def test_7():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 5]

    solution(A, B, 5, 1, 201)


def test_7():
    A = [40, 61, 100, 80, 20]
    B = [3, 3, 2, 2, 5]

    solution(A, B, 5, 2, 199)

def test_8():
    A = [1]
    B = [1]

    solution(A, B, 5, 2, 199)

test_8()
