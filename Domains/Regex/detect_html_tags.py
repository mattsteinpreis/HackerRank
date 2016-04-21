"""
In this challenge, we're using regular expressions to
detect the various tags used in an HTML document.

Given NN lines of HTML, find the tag names (ignore any attributes)
and print them as a single line of lexicographically ordered
semicolon-separated values (e.g.: tag1;tag2;tag3).
"""

import re


def find_unique_tags(l):
    pattern = r"<(\w+)"
    unique = set()
    for s in l:
        matches = re.findall(pattern, s)
        for match in matches:
            unique.add(match)
    sl = sorted(list(unique))
    return sl


def localtest():
    lines = [('<p><a href="http://www.quackit.com/html' +
              '/tutorial/html_links.cfm">Example Link</a></p>'),
             ('<div class="more-info"><a href="http://www.quackit.com' +
              '/html/examples/html_links_examples.cfm">More Link Exam' +
              'ples...</a></div>')]

    result = find_unique_tags(lines)
    p = ';'.join(result)
    print(p)
    assert p == 'a;div;p'


def hackerrank():
    n_cases = int(input())
    lines = []
    for i in range(n_cases):
        lines.append(input())
    results = find_unique_tags(lines)
    print(';'.join(results))


if __name__ == '__main__':
    hackerrank()