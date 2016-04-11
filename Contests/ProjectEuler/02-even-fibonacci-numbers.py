def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def even_fib_sum(n):
    s = 0
    ni = 0
    while True:
        f = fib(ni)
        if f > n:
            return s
        if f % 2 == 0:
            s += f
        ni += 1
    return s


def test():

    res = even_fib_sum(0)
    assert res == 0

    res = even_fib_sum(1)
    assert res == 0

    res = even_fib_sum(2)
    assert res == 2

    res = even_fib_sum(10)
    assert res == 10

    res = even_fib_sum(100)
    assert res == 44


def hacker_rank():
    n_cases = int(input())
    for i in range(n_cases):
        num = int(input())
        print(even_fib_sum(num))


if __name__ == "__main__":
    test()