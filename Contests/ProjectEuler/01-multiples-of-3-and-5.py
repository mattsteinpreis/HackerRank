def sum_3_5(n):
    if not n:
        return 0
    f3 = sum_arithmetic_series(3, 3, n)
    f5 = sum_arithmetic_series(5, 5, n)
    f15 = sum_arithmetic_series(15, 15, n)
    return f3 + f5 - f15


def sum_arithmetic_series(a, d, maximum):
    n = int(maximum / d)
    # subtract 1 if maximum is multiple
    if maximum % d == 0:
        n -= 1
    val_sub = n * (2 * a + d * (n - 1))
    # to avoid rounding error, do bitwise right-shift for  a / 2
    val = val_sub >> 1
    return val


def hacker_rank():
    n_cases = int(input())
    for i in range(n_cases):
        max_i = int(input())
        print(sum_3_5(max_i))


def test():
    assert sum_3_5(10) == 23
    assert sum_3_5(100) == 2318
    assert sum_3_5(0) == 0


if __name__ == "__main__":
    test()
