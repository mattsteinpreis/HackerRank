n_queries = int(input())

def perform(a, b, d):
    if d == 0:
        return 0
    if d % b == 0:
        return d / b
    if d > b:
        return (d // b) + 1
    if d == a:
        return 1
    return 2

for i in range(n_queries):
    a, b, d = [int(item) for item in input().split()]
    print(perform(a, b, d))