def reduce(s):
    reduced = []
    last = ''
    for ch in s:
        if ch != last:
            reduced.append(ch)
            last = ch
        else:
            _ = reduced.pop()
            if len(reduced) == 0:
                last = ''
            else:
                last = reduced[-1]
    if len(reduced) == 0:
        return "Empty String"
    return ''.join(reduced)


def localtest():
    assert reduce('aaabccddd') == 'abd'
    assert reduce('baab') == 'Empty String'
    assert reduce('aa') == 'Empty String'


def hackerrank():
    ss = input()
    print(reduce(ss))


if __name__ == '__main__':
    hackerrank()
