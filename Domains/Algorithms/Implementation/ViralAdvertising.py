def advertise(start, n):
    count = 0
    for i in range(n):
        start = start // 2
        count += start
        start = start * 3
    return count


def test():
    assert advertise(5, 1) == 2
    assert advertise(5, 2) == 5
    assert advertise(5, 3) == 9


def main():
    ndays = int(input())
    print(advertise(5, ndays))


if __name__ == '__main__':
    main()
