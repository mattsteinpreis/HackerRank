def divisible_sum_pairs(l, k):
    count = 0
    for i, ai in enumerate(l[:-1]):
        for aj in l[(i+1):]:
            if (ai + aj) % k == 0:
                count += 1
    return count


def test():
    n, k = (6, 3)
    l = [1, 3, 2, 6, 1, 2]
    n_good = divisible_sum_pairs(l, k)
    assert n_good == 5


def main():
    n, k = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    print(divisible_sum_pairs(l, k))


if __name__ == '__main__':
    main()