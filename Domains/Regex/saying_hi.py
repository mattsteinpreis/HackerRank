import re

PATTERN = r'^[hH][Ii]\s[^Dd]'


def is_valid(s):
    return re.match(PATTERN, s)


def test():
   ss = ['Hi Alex how are you doing',
        'hI dave how are you doing',
        'Good by Alex',
        'hidden agenda',
        'Alex greeted Martha by saying Hi Martha']
   for s in ss:
       if is_valid(s):
           print(s)


def main():
    n_cases = int(input())
    for i in range(n_cases):
        s = input()
        if is_valid(s):
            print(s)


if __name__ == '__main__':
    main()