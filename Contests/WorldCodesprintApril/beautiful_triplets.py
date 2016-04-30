# should memoize
def is_good_pair(a, b, d):
    return (b - a) == d


def n_beautiful(l, d):
    count = 0
    n = len(l)
    for i in range(n - 2):
        skip = False
        j = i + 1
        while not skip:
            if j == n - 2:
                skip = True
            if (l[j] - l[i]) > d:
                skip = True
            if is_good_pair(l[i], l[j], d):
                skip2 = False
                k = j + 1
                while not skip2:
                    if k == n - 1:
                        skip2 = True
                    if (l[k] - l[j] > d):
                        skip2 = True
                    if is_good_pair(l[j], l[k], d):
                        count += 1
                    k += 1
            j += 1
    return count


def test():
    l = [1,2,4,5,7,8,10]
    assert n_beautiful(l, 3) == 3


def hackerrank():
    digs = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    print(n_beautiful(l, digs[1]))


if __name__ == '__main__':
    hackerrank()