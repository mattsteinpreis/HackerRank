def n_jumps(l):
    n = len(l)
    i = 0
    count = 0
    while i < n-1:
        if i == n-2 or l[i+2] == '1':
            i += 1
        else:
            i += 2
        count += 1
    return count


def test():
    l = [0,0,1,0,0,0,0]
    assert n_jumps(l) == 4

    l = [0,0,0,0,1,0]
    assert n_jumps(l) == 3


def hackerrank():
    _ = input()
    clouds = input().split()
    print(n_jumps(clouds))


if __name__ == '__main__':
    hackerrank()