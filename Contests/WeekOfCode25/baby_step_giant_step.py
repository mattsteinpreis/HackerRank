def perform(a, b, d):
    if d == 0:
        return 0
    if d % b == 0:
        return d // b
    if d > b:
        return (d // b) + 1
    if d == a:
        return 1
    return 2


def test():
    assert perform(1, 2, 6) == 3
    assert perform(1, 2, 1000000000) == 500000000
    assert perform(1, 5, 5) == 1


def HackerRank():
    n_queries = int(input())
    for i in range(n_queries):
        a, b, d = [int(item) for item in input().split()]
        print(perform(a, b, d))


if __name__ == '__main__':
    HackerRank()