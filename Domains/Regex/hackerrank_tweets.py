import re

def case_insensitive_pattern(s):
    p = ''
    for ch in s:
        p = p + '(' + ch + '|' + ch.upper() + ')'
    return p


def contains(s, p):
    m = re.findall(p, s)
    return bool(m)


def test():
    word = 'hackerrank'
    pattern = case_insensitive_pattern(word)

    a = 'I just scored 27 points in the Picking Cards challenge on #HackerRank'
    res = contains(a, pattern)
    assert res


def easy_non_re(s):
    return 'hackerrank' in s.lower()


def hackerrank():
    n_cases = int(input())
    pattern = case_insensitive_pattern('hackerrank')
    count = 0
    for i in range(n_cases):
        s = input()
        if contains(s, pattern):
            count += 1
    print(count)


if __name__ == '__main__':
    hackerrank()