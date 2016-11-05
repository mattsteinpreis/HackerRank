def count_mistakes(arr):
    ct = 0
    last = 0
    for ch in arr:
        cur = int(ch)
        if cur != last + 1:
            ct += 1
        last, cur = cur, last
    return ct

n = int(input())
numbers = input().split()
print(count_mistakes(numbers))