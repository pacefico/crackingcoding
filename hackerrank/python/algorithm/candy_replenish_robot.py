
def play(maxcandies, time, vet):
    replenish = 0
    candies = maxcandies
    minimum = min(time, len(vet))
    for i in range(minimum):
        remove = vet[i]
        candies = candies - remove
        if (candies < 5 and i < time-1):
            add = maxcandies - candies
            replenish = replenish + add
            candies = candies + add
    return replenish

def test_case(first, second):
    n = play(first[0], first[1],second)
    #print("n:{}".format(n))

def case0():
    first = [8,4]
    second = [3, 1, 7, 5]
    test_case(first,second)

def case1():
    first = [8,3]
    second = [5,2,4]
    test_case(first, second)

def case2():
    import random
    for _ in range(100000):
        n = random.randint(5,100)
        t = random.randint(1,100)
        v = []

        for i in range(n):
            v.append(random.randint(5,n))

        try:
            test_case([n, t], v)
        except:
            print("\nerror!!!")
            print("n: {} t:{} v:{}".format(n, t, v))
            break

case0()
case1()
case2()
