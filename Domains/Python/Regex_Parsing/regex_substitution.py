import re

def wordify(match):
    if match.group(0) == ' &&':
        return ' and'
    else:
        return ' or'

pattern = re.compile(r'\s([&\|])\1(?=\s)')

N = int(input())
for i in range(N):
    line = input()
    print(re.sub(pattern, wordify, line))