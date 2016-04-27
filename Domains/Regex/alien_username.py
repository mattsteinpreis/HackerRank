"""In a galaxy far far away, a planet different from ours,
computer usernames follow a different format.

It has to begin with either an underscore '_' (ascii value 95)
or a dot '.' (ascii value 46)
It has to be immediately followed by one or more occurrences of
digits numbered 0-9
It can then have letters, both uppercase or lowercase, 0 or more in number
It can then end with an optional '_' (ascii value 95)

Your task is to validate whether a username is valid or not"""

import re

PATTERN = r'^[_\.]\d+[a-zA-Z]*_?$'


def is_valid(s):
    return bool(re.match(PATTERN, s))


def print_valid(r):
    if r:
        print('VALID')
    else:
        print('INVALID')


def test():
    res = is_valid('_0898989811abced_')
    assert res
    res = is_valid('_09090909abcD0')
    assert not res


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        test_case = input()
        res = is_valid(test_case)
        print_valid(res)


if __name__ == '__main__':
    hackerrank()
