import re


def find_word(w, s):
    pattern = r'\b'+w+r'\b'
    f = re.findall(pattern, s)
    return len(f)


def test():
    s = "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."
    w = 'foo'
    print(find_word(w, s))


def main():
    n_s = int(input())
    lines = []
    for i in range(n_s):
        lines.append(input())
    s = ' '.join(lines)
    n_w = int(input())
    for i in range(n_w):
        w = input()
        print(find_word(w, s))


if __name__ == '__main__':
    main()

