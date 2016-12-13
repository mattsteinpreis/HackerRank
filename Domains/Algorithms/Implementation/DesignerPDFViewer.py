def word_size(word, heights):
    max_h = 0
    for l in word:
        h = heights[ord(l)-97]
        max_h = max(max_h, h)
    return max_h * len(word)


def main():
    n = [int(j) for j in input().split()]
    w = input()
    print(word_size(w, n))


if __name__ == '__main__':
    main()
