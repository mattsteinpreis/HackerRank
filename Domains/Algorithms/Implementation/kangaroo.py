def will_they_meet(x1, v1, x2, v2):

    # if same velocities, must start at the same spot
    if v1 == v2:
        return x1 == x2

    # if they meet, n will be positive integer
    n = (x2 - x1)/(v1 - v2)
    return n > 0 and int(n) == n


if __name__ == '__main__':
    pos1, vel1, pos2, vel2 = [int(i) for i in input().strip().split()]

    result = will_they_meet(pos1, vel1, pos2, vel2)

    print({True: 'YES', False: 'NO'}[result])