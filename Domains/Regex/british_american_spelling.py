import re

def n_finds(p, s):
    m = re.findall(p, s)
    return len(m)


def find_all_words(w, s):
    if w.endswith('ze'):
        pattern = r'\b'+w[:-2]+r'[sz]e\b'
    else:
        sub_p = r'^([a-z]+)our([a-z]*)$'
        m = re.match(sub_p, w)
        pattern = r'\b'+m.group(1)+r'ou?r'+m.group(2)+r'\b'
    return n_finds(pattern, s)


def test():
    lines = ['hackerrank has such a good ui that it takes no time to familiarise its environment',
             'to familiarize oneself with ui of hackerrank is easy']
    w = 'familiarize'
    s = ' '.join(lines)
    f = find_all_words(w, s)
    assert f == 2

    lines = ['the odour coming out of the left over food was intolerable',
             'ammonia has a very pungent odor']
    w = 'odour'
    s = ' '.join(lines)
    assert find_all_words(w, s) == 2

    # lines = ['labour however salty access stream strange odor favorite dancing milligram',
    #          'anxious spoon formal lesson vapor close soft drunk odour pt',
    #          'text labor instead knit shop flavor find humor critical driving']
    # words = []


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
