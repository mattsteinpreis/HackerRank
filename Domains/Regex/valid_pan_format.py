import re

PATTERN = r'^[A-Z]{5}[0-9]{4}[A-Z]$'


def validate(s):
    m = re.findall(PATTERN, s)
    if m:
        return 'YES'
    return 'NO'


def test():
    res = validate('ABCDE0123Z')
    assert res == 'YES'

    res = validate('abcde0123z')
    assert res == 'NO'

    res = validate('ABCD1023EG')
    assert res == 'NO'


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        print(validate(s))


if __name__ == '__main__':
    hackerrank()
