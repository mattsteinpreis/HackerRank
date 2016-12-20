
def min_turns(n, k):
    '''
    Naive solution: check both ways, pick lowest
    :param n: int, number of pages in book
    :param k: int, desired page number
    :return: int, minimum number of page turns
    '''
    n = n + 1 if n % 2 == 0 else n
    k = k + 1 if k % 2 == 0 else k

    front = (k - 1) // 2
    back = (n - k) // 2

    return min(front, back)


def test():
    assert min_turns(6, 1) == 0
    assert min_turns(6, 2) == 1
    assert min_turns(6, 3) == 1
    assert min_turns(6, 4) == 1
    assert min_turns(6, 5) == 1
    assert min_turns(6, 6) == 0


def hackerrank():
    n = int(input())
    k = int(input())
    print(min_turns(n, k))


if __name__ == '__main__':
    hackerrank()
