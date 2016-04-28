import re


def is_ip4(s):
    bit = r'(\d{1,3})'
    bitlist = [bit]*4
    pattern = '^' + '\.'.join(bitlist) + '$'
    m = re.match(pattern, s)
    if m:
        for i in range(4):
            n = int(m.group(i+1))
            if n > 255:
                return False
        return True
    return False


def is_ip6(s):
    bit = r'[\da-f]{1,4}'
    bitlist = [bit]*8
    pattern = '^' + ':'.join(bitlist) + '$'
    if re.match(pattern, s):
        return True
    return False


def address_type(s):
    if is_ip4(s):
        return 'IPv4'
    elif is_ip6(s):
        return 'IPv6'
    else:
        return None


def test():
    st = 'This line has junk text'
    res = address_type(st)
    assert res is None

    st = '121.18.19.20'
    res = address_type(st)
    assert res == 'IPv4'

    st = '256.18.19.20'
    res = address_type(st)
    assert res is None

    st = '2001:0db8:0000:0000:0000:ff00:0042:8329'
    res = address_type(st)
    assert res == 'IPv6'


def hackerrank():
    n_cases = int(input())
    for i in range(n_cases):
        st = input()
        res = address_type(st)
        if res:
            print(res)
        else:
            print('Neither')


if __name__ == '__main__':
    hackerrank()