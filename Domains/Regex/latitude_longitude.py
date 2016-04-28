import re
SUB = r'[+-]?((?:0|[1-9][0-9]{0,2})(?:\.[0-9]+)?)'
PATTERN = r'^\(' + SUB + ', ' + SUB + r'\)$'


def pattern(s):
    m = re.match(PATTERN, s)
    return m


def is_valid(s):
    m = pattern(s)
    if not m:
        return 'Invalid'
    lat = float(m.group(1))
    lon = float(m.group(2))
    if lat <= 90 and lon <= 180:
        return "Valid"
    return "Invalid"


def test():
    l = ['(75, 180)',
         '(+90.0, -147.45)',
         '(77.11112223331, 149.99999999)',
         '(+90, +180)',
         '(90, 180)',
         '(90.00000, -180.0000)',
         '(75, 280)',
         '(+190.0, -147.45)',
         '(77.11112223331, 249.99999999)',
         '(+90, +180.2)',
         '(90., 180.)',
         '(-090.00000, -180.0000)']
    v = ['Valid']*6 + ['Invalid']*6

    for i, s in enumerate(l):
        res = is_valid(s)
        assert res == v[i]


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        print(is_valid(s))


if __name__ == '__main__':
    hackerrank()
