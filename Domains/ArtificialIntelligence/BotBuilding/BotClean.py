def find_dirty_locations(board):
    joined = ''.join(board)
    spots = []
    for loc, ch in enumerate(joined):
        if ch == 'd':
            i = loc // 5
            j = loc % 5
            spots.append((i, j))
    return spots


def direction(b_loc, d_loc):
    diff = (d_loc[0] - b_loc[0], d_loc[1] - b_loc[1])
    if diff[0] > 0:
        return 'DOWN'
    elif diff[0] < 0:
        return 'UP'
    else:
        if diff[1] > 0:
            return 'RIGHT'
        else:
            return 'LEFT'


def move_to_closest(i, j, board):
    # will move in direction of closest 'd'
    locations = find_dirty_locations(board)
    if len(locations) == 0:
        return 'DONE'
    nearest = [None, 10]
    for loc in locations:
        distance = abs(loc[0] - i) + abs(loc[1] - j)
        if distance < nearest[1]:
            nearest = [loc, distance]
    return direction((i, j), nearest[0])


def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        return 'CLEAN'
    return move_to_closest(posr, posc, board)


def test():
    test_board = ['b---d', '-d--d', '--dd-', '--d--', '----d']
    print(next_move(0, 0, test_board))
    test_board = ['----d', 'bd--d', '--dd-', '--d--', '----d']
    print(next_move(1, 0, test_board))
    test_board = ['----d', '-d--d', '--dd-', '--d--', '----d']
    print(next_move(1, 1, test_board))

def main():
    # read bot location from stdin
    x, y = [int(i) for i in input().strip().split()]

    # read board from location
    lines = []
    for i in range(5):
        lines.append(input().strip())

    print(next_move(x, y, lines))


if __name__ == '__main__':
    test()