import re

PATTERN = r'^[a-z]{,3}\d{2,8}[A-Z]{3,}'


def validate(s):
    m = re.findall(PATTERN, s)
    if m:
        return 'VALID'
    else:
        return 'INVALID'


def test():
    res = validate('abc012333ABCDEEEE')
    assert res == 'VALID'

    res = validate('0123AB')
    assert res == 'INVALID'


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        print(validate(s))


if __name__ == '__main__':
    hackerrank()
