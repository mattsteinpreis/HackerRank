from operator import mul
from functools import reduce


def largest_product(l, k):
    if isinstance(l, str):
        l = [int(i) for i in l]
    n = len(l)
    largest = 0
    for i in range(n-k+1):
        li = l[i:(i+k)]
        prod = reduce(mul, li, 1)
        largest = max(prod, largest)
    return largest


def test():
    s = '3675356291'
    assert largest_product(s, 5) == 3150
    l = [int(i) for i in s]
    assert largest_product(l, 5) == 3150

    s = '2709360626'
    assert largest_product(s, 5) == 0


def main():
    n_cases = int(input())
    for i in range(n_cases):
        n, k = [int(i) for i in input().split()]
        s = input()
        print(largest_product(s, k))


if __name__ == '__main__':
    test()
