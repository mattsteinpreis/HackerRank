def find_princess(grid):
    n = len(grid)
    locs = [[0, 0], [0, n-1], [n-1, 0], [n-1, n-1]]
    for loc in locs:
        if grid[loc[0]][loc[1]] == 'p':
            return loc


def displayPathtoPrincess(m, grid):
    start = [m // 2, m // 2]
    end = find_princess(grid)
    moves_v = end[0] - start[0]
    if moves_v > 0:
        move = 'DOWN'
    else:
        move = 'UP'
    for i in range(abs(moves_v)):
        print(move)
    moves_h = end[1] - start[1]
    if moves_h > 0:
        move = 'RIGHT'
    else:
        move = 'LEFT'
    for i in range(abs(moves_h)):
        print(move)


def test():
    n = 3
    grid = ['---', '-m-', 'p--']
    displayPathtoPrincess(n, grid)


if __name__ == '__main__':
    test()