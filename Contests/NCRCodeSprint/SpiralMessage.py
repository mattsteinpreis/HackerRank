def unspiral(mat):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    message = ''
    dnow = len(mat)
    dnext = len(mat[0])-1
    i, j = len(mat), 0
    while dnow > 0:
        # traverse
        for n in range(dnow):
            i += dirs[0][0]
            j += dirs[0][1]
            message += mat[i][j]
        # update
        dirs = dirs[1:] + dirs[:1]
        dnow, dnext = dnext, dnow-1
    return message


def count_words(mat):
    message = unspiral(mat)
    words = message.split('#')
    ct = sum([1 for word in words if len(word) > 0])
    return ct


def test():
    assert unspiral(['stw', 'eso', 'tdr']) == 'testwords'
    #  t  h  e  #  #
    #  #  t  u  r  w
    #  s  #  s  n  o
    #  a  #  d  l  r
    assert count_words(['the##','#turw', 's#sno', 'a#dlr']) == 4


def hackerrank():
    nr, nc = [int(i) for i in input().split()]
    rows = []
    for row in range(nr):
        rows.append(input())
    print(count_words(rows))


if __name__ == '__main__':
    hackerrank()
