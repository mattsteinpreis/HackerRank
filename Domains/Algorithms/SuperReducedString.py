#!/Users/msteinpreis/dsenv/local/bin/python3


def super_reduced(s):
    stack = []
    for ch in s:
        stack.append(ch)
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) > 0:
        return ''.join(stack)
    else:
        return 'Empty String'


if __name__ == '__main__':
    print(super_reduced(input()))
