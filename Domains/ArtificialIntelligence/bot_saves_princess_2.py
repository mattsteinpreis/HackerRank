def nextMove(n, r, c, grid):
    bot_i = r
    bot_j = c
    for i, row in enumerate(grid[:(r+1)]):
        if 'p' in row:
            if i < bot_i:
                return 'UP'
            for j in range(bot_j):
                if row[j] == 'p':
                    return 'LEFT'
            return 'RIGHT'
    return 'DOWN'


def main():
    n = int(input())
    r, c = [int(i) for i in input().strip().split()]
    grid = []
    for i in range(n):
        print(i)
        grid.append(input())
    print(nextMove(n, r, c, grid))


if __name__ == '__main__':
    main()