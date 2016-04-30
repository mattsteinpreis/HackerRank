import re
import sys


def run(l):
    pattern_1 = r'<h3>\[([\w ]+)\]\(\/questions\/(\d+)\/[\w-]+\)<\/h3>'
    pattern_1a = r'<h3><a href="\/questions\/(\d+)\/[\w-]+" '
    pattern_1a += r'class="question-hyperlink">([^<]+)<\/a>'
    pattern_2 = r'class="relativetime">([^<]+)</span>'
    q_i = re.findall(pattern_1, l)
    q_i_a = re.findall(pattern_1a, l)
    t = re.findall(pattern_2, l)
    if q_i:
        q = [(b, a) for (a, b) in q_i]
    else:
        q = q_i_a
    for (a, b), c in zip(q, t):
        print(';'.join([a, b, c]))


def test():
    lines = []
    for i in range(1000):
        line = input()
        if line == 'FINISHED':
            break
        lines.append(line)
    lines = ''.join(lines)
    run(lines)


def hackerrank():
    lines = ''.join(sys.stdin.read().splitlines())
    run(lines)


if __name__ == '__main__':
    hackerrank()
