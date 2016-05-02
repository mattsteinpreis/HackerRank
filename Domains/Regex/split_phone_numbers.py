import re

PATTERN = r'^(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})$'

def split_number(s):
    m = re.match(PATTERN, s)
    return m.groups()


def print_groups(g):
    s = 'CountryCode={},'.format(g[0])
    s += 'LocalAreaCode={},'.format(g[1])
    s += 'Number={}'.format(g[2])
    print(s)


def test():
    s = ['1 877 2638277', '91-011-23413627']
    for ss in s:
        m = split_number(ss)
        print_groups(m)


def main():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        m = split_number(s)
        print_groups(m)


if __name__ == '__main__':
    main()