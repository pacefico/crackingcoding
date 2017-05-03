#python 3


def optimal_solution(n):
    if n == 1:
        return 0, [1]
    ops = [0]*(n+1)

    for i in range(1, n+1):
        seq = [ops[i - 1] + 1]
        if i % 2 == 0: seq.append(ops[i // 2] + 1)
        if i % 3 == 0: seq.append(ops[i // 3] + 1)
        ops[i] = min(seq)

    sequence = []
    while (n>=1):
        sequence.append(n)
        if ops[n - 1] == ops[n] - 1:
            n = n - 1
        elif n % 2 == 0 and ops[n // 2] == ops[n] - 1:
            n = n // 2
        elif n % 3 == 0 and ops[n // 3] == ops[n] - 1:
            n = n // 3

    return ops[-1]-1, reversed(sequence)


def output(n):
    ops, sequence = list(optimal_solution(n))
    print(ops)
    for x in sequence:
        print(x, end=" ")


def test0():
    output(5)


def test1():
    output(1)


def test2():
    output(96234)


n = int(input())
output(n)

# test0()
# test1()
# test2()