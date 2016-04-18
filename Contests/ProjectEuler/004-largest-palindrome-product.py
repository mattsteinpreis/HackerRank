# super slow brute force solution

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def get_3x3_palindromes():
    a = set()
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if is_palindrome(prod):
                a.add(prod)
    return a


def find_largest_palindrome(n, s):
    while n >= 1e5:
        if n in s:
            return n
        n -= 1


def test():
    pals = get_3x3_palindromes()

    assert find_largest_palindrome(101110, pals) == 101101
    assert find_largest_palindrome(800000, pals) == 793397


def hackerrank():
    pals = get_3x3_palindromes()
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        lp = find_largest_palindrome(n, pals)
        print(lp)

if __name__ == '__main__':
    test()
