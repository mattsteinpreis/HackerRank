if __name__ == '__main__':
    n_cases = int(input())
    for i in range(n_cases):
        n_students, threshold = [int(j) for j in input().split()]
        times = [int(j) for j in input().split()]
        on_time = sum([1 for a in times if a <= 0 ])
        if on_time < threshold:
            print('YES')
        else:
            print('NO')
