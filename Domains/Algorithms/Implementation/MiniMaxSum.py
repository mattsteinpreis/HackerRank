def minimax(l, k):
    l.sort()
    return sum(l[:k]), sum(l[(len(l) - k):])


def test():
    n = [1,2,3,4,5]
    assert minimax(n, 4) == (10, 14)


def hackerrank():
    n = [int(i) for i in input().split()]
    mnmx = minimax(n, 4)
    print(*mnmx)


if __name__ == '__main__':
    hackerrank()