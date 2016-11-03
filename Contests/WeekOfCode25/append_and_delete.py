def find_n_moves(s, t):
    shortest = s
    if len(s) > len(t):
        shortest = t
    for i in range(len(shortest)):
        if s[i] != t[i]:
            i -= 1
            break
    i += 1
    return len(s) + len(t) - 2 * i

def enough(s, t, k, n_moves):
    if k < n_moves:
        return False
    if k > (len(s) + len(t)):
        return True
    return (k - n_moves) % 2 == 0

s = input().strip()
t = input().strip()
k = int(input().strip())
n_moves = find_n_moves(s, t)
result = enough(s, t, k, n_moves)
print({True:'Yes', False:'No'}[result])