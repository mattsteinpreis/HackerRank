import re

LANGUAGES = (':C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE'
            ':BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO'
            ':D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC:')


def is_language(s):
    su = s.upper()
    if re.search(':'+su+':', LANGUAGES):
        return 'VALID'
    return 'INVALID'


def test():
    ss = ['LUA', 'BRAINFUCK', 'S', 'pascal']
    for s in ss:
        print(is_language(s))


def main():
    n_cases = int(input())
    for i in range(n_cases):
        case = input().split()
        s = case[1]
        print(is_language(s))


if __name__ == '__main__':
    main()