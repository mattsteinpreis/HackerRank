import math


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vlen(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)


def angle(a, b):
    la = vlen(a)
    lb = vlen(b)
    cosab = dot(a, b) / (la*lb)
    return math.acos(cosab)


def diff(a, b):
    return b[0]-a[0], b[1]-a[1], b[2]-a[2]


def test():
    points = [(0, 0, 0), (2, 0, 0), (2, 2, 1), (0, 2, 1)]
    np = len(points)
    anglesum = 0
    count = 0
    angles = []
    for i in range(np-2):
        for j in range(i+1, np-1):
            for k in range(j+1, np):
                print(i, j, k)
                ba = diff(points[i], points[j])
                bc = diff(points[k], points[j])
                ang = angle(ba, bc)
                angles.append(ang)
                anglesum += ang
                count += 1
    print(anglesum / count)
    print(angles)


def hackerrank():
    np = int(input())
    points = []
    for ni in range(np):
        s = input()
        points.append(tuple([int(i) for i in s.split()]))

    anglesum = 0
    count = 0
    for i in range(np-2):
        for j in range(i+1, np-1):
            for k in range(j+1, np):
                ba = diff(points[i], points[j])
                bc = diff(points[k], points[j])
                ang = angle(ba, bc)
                anglesum += ang
                count += 1
    print(anglesum / count)


if __name__ == '__main__':
    hackerrank()
