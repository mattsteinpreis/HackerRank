import re

def n_finds(p, s):
    m = re.findall(p, s)
    return len(m)


def find_all_words(w, s):
    pattern = r'\b'+w[:-2]+r'[sz]e\b'
    return n_finds(pattern, s)


def test():
    lines = ['hackerrank has such a good ui that it takes no time to familiarise its environment',
             'to familiarize oneself with ui of hackerrank is easy']
    w = 'familiarize'

    s = ' '.join(lines)
    f = find_all_words(w, s)
    print(f)


def main():
    n_lines = int(input())
    lines = []
    for i in range(n_lines):
        lines.append(input())
    s = ' '.join(lines)
    n_words = int(input())
    for i in range(n_words):
        w = input()
        print(find_all_words(w, s))


if __name__ == '__main__':
    main()
