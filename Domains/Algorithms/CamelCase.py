#!/Users/msteinpreis/dsenv/local/bin/python3


def count_words(s):
    capitals = 0
    for ch in s:
        if ord(ch) > 64 and ord(ch) < 91:
            capitals += 1
    return capitals + 1


if __name__ == '__main__':
    s = input()
    print(count_words(s))
