def k_in_a_row(b, k, starti, startj, nexti, nextj):
    i = starti
    j = startj
    curX = 0
    curO = 0
    metX = False
    metO = False
    while i < len(b) and j < len(b[0]) and i > -1 and j > -1:
        if metX and metO:
            return True, True
        cur = b[i][j]
        if cur == 'O':
            curO += 1
            curX = 0
        elif cur == 'X':
            curO = 0
            curX += 1
        else:
            curO = curX = 0
        metX = metX or curX >= k
        metO = metO or curO >= k
        i += nexti
        j += nextj
    return metX, metO


def who_won(b, k):
    n = len(b)
    m = len(b[0])
    metX = metO = False
    # check horizontal rows
    for row in range(n):
        resX, resO = k_in_a_row(b, k, row, 0, 0, 1)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'
        resX, resO = k_in_a_row(b, k, row, m-1, 1, -1)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'
        resX, resO = k_in_a_row(b, k, row, 0, 1, 1)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'
    for col in range(m):
        resX, resO = k_in_a_row(b, k, 0, col, 1, 0)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'
        resX, resO = k_in_a_row(b, k, 0, col, 1, 1)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'
        resX, resO = k_in_a_row(b, k, 0, col, 1, -1)
        metX, metO = metX or resX, metO or resO
        if metX and metO:
            return 'NONE'

    if metX:
        return 'LOSE'
    else:
        if metO:
            return 'WIN'
        return 'NONE'


def test():
    assert k_in_a_row(['XXX', '---', 'OOO'], 3, 0, 0, 0, 1) == (True, False)
    assert who_won(['XXX', '---', 'OOO'], 3) == 'NONE'
    assert who_won(['XX-', '---', 'OOO'], 3) == 'WIN'
    assert who_won(['XXX', '---', 'OO-'], 3) == 'LOSE'
    assert who_won(['XXO', '-O-', 'OO-'], 3) == 'WIN'
    assert who_won(['---XXX---', '----O----', '---OO----'], 3) == 'LOSE'


def main():

    n_games = int(input())

    for game in range(n_games):
        nrows, _, k_need = [int(item) for item in input().split()]
        board = []
        for j in range(nrows):
            board.append(input())
        res = who_won(board, k_need)
        print(res)


if __name__ == '__main__':
    main()