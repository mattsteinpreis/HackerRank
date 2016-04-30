import re


def convo_type(s):
    if re.search(r'^hackerrank.', s):
        return 1
    if re.search(r'.hackerrank$', s):
        return 2
    if re.search(r'^hackerrank$', s):
        return 0
    return -1


def test():
    res = convo_type('i love hackerrank')
    assert res == 2

    res = convo_type('hackerrank is the best')
    assert res == 1

    res = convo_type('hackerrank')
    assert res == 0

    res = convo_type('what is hacker rank')
    assert res == -1


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        print(convo_type(s))


if __name__ == '__main__':
    hackerrank()