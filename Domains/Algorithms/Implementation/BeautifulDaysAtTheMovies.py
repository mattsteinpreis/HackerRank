def divisible(n, div):
    return n % div == 0


def reverse(n):
    s = str(n)
    s = s[::-1]
    return int(s)


def brute(day1, day2, div):
    count = 0
    for day in range(day1, day2+1):
        rev = reverse(day)
        dif = abs(rev-day)
        if divisible(dif, div):
            count += 1
    return count


def main():
    i, j, k = [int(ii) for ii in input().split()]
    print(brute(i, j, k))


if __name__ == '__main__':
    main()