
def nested_min_recursive(min_str = "min(int, {})", n=2):
    if n == 2:
        return min_str.format("int")
    elif n < 2:
        return ''
    return min_str.format(nested_min_recursive(n=n-1))

def nested_min(n):
    min_str = "min(int, {})"
    result = min_str.format("int")
    for i in range(n-2):
        result = min_str.format(result)

    print(result)

def case0():
    n = 2
    nested_min(n)

def case1():
    n = 4
    nested_min(n)

def case2():
    print(nested_min_recursive(n=3))

case0()
case1()
case2()