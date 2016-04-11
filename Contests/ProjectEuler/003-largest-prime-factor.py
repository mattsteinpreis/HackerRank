import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_factor(n, div):
    return n % div == 0


def largest_prime_factor(n):
    if is_prime(n):
        return n
    highest_low_prime = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_factor(n, i):
            if is_prime(i):
                highest_low_prime = i
            div = n / i
            if is_prime(div):
                return int(div)
    return int(highest_low_prime)


def test():
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(57864375) == 127
    assert largest_prime_factor(2490871606464375) == 127


def hacker_rank():
    n_cases = int(input())
    for case in range(n_cases):
        num = int(input())
        print(largest_prime_factor(num))


if __name__ == '__main__':
    test()