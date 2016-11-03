def check_a(j, l):
    for li in l:
        if j % li != 0:
            return False
    return True

def check_b(j, l):
    for li in l:
        if li % j != 0:
            return False
    return True


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

start = max(a)
end = min(b)
possible = list(range(start, end+1))

count = 0
for i in possible:
    passes_a = check_a(i, a)
    if passes_a:
        passes_b = check_b(i, b)
        if passes_b:
            count += 1

print(count)