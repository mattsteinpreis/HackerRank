def n_divisible_sum_pairs(l, k):
    l.sort()
    ct = 0
    for i, n1 in enumerate(l[:-1]):
        for n2 in l[i+1:]:
            if (n1 + n2) % k == 0:
                ct += 1
    return ct


if __name__ == '__main__':
    _, k_input = [int(i) for i in input().strip().split()]
    numlist = [int(i) for i in input().strip().split()]

    res = n_divisible_sum_pairs(numlist, k_input)
    print(res)