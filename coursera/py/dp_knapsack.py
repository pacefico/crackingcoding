# Uses python3

def optimal_weight(W, w):
    c = [0] * (W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            sub = c[j - w[i]] + w[i]
            if c[j] < sub:
                c[j] = sub
    return c[W]

def test0():
    a = [10, 3]
    b = [1, 4, 8]
    print(optimal_weight(a[0], b))

# test0()

W, n = list(map(int, input().split()))
w = list(map(int, input().split()))
print(optimal_weight(W, w))