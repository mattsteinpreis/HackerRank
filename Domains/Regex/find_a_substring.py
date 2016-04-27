import re

# Problem with Test-Case 2: all good except 'to': found 6, actual 19
# problem with test-case 6: all good except 'rope': found 3, actual 4

def parse_words(s):
    words = s.split()
    good_words = []
    for word in words:
        if re.search(r'^\w+$', word):
            good_words.append(word)
    return good_words

def subs(s, t):
    pattern = r'(?<=\w)' + t + r'(?=\w)'
    matches = re.findall(pattern, s)
    return len(matches)


def count_matches(wl, t):
    count = 0
    for w in wl:
        count += subs(w, t)
    return count


def test():
    a = 'existing pessimist optimist this is'
    aw = parse_words(a)

    res = count_matches(aw, 'is')
    assert res == 3
    res = count_matches(aw, 'i')
    assert res == 7
    res = count_matches(aw, 's')
    assert res == 5
    res = count_matches(parse_words('test_one test.two test)three'), 's')
    assert res == 1


def hackerrank():
    n_sentences = int(input())
    words = []
    for i in range(n_sentences):
        sentence = input()
        words.extend(parse_words(sentence))
    n_targets = int(input())
    for i in range(n_targets):
        target = input()
        print(count_matches(words, target))


if __name__ == '__main__':
    hackerrank()


