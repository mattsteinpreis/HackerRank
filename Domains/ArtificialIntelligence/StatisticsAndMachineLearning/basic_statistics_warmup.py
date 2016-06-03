import numpy as np


def mode(l):
    s = set(l)
    counts = [(i, l.count(i)) for i in s]
    counts.sort(key=lambda x:(-x[1], x[0]))
    return counts[0][0]

def statistics(l):
    n = len(l)
    mn = np.mean(l).round(1)
    print(mn)
    print(np.median(l).round(1))
    print(mode(l))
    stdev = np.std(l).round(1)
    print(stdev)
    ci1 = mn-stdev*1.96/np.sqrt(n)
    ci2 = mn+stdev*1.96/np.sqrt(n)
    print(ci1.round(1), ci2.round(1))


def test():
    inp = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'
    numbers = [int(i) for i in inp.split()]
    statistics(numbers)


def main():
    _ = int(input())
    numbers = [int(i) for i in input().split()]
    statistics(numbers)


if __name__ == '__main__':
    main()