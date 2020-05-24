def incre(h, w, a, i, j):
    if 0 <= i <= h-1 and 0 <= j <= w-1 and a[i][j] != '#':
        a[i][j] += 1

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

a = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            a[i][j] = '#'

print(s)
print(a)
for i in range(h):
    for j in range(w):
        if (s[i][j] == '#'):
            if i == 0:
                if j == 0:
                    incre(h, w, a, i, j+1)
                    incre(h, w, a, i+1, j)
                    incre(h, w, a, i+1, j+1)
                elif 0 < j < w - 1:
                    incre(h, w, a, i, j-1)
                    incre(h, w, a, i, j+1)
                    incre(h, w, a, i+1, j-1)
                    incre(h, w, a, i+1, j)
                    incre(h, w, a, i+1, j+1)

                elif j == w-1:
                    incre(h, w, a, i, j-1)
                    incre(h, w, a, i-1, j-1)
                    incre(h, w, a, i+1, j)
            elif 0 < i < h - 1:
                if j == 0:
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i-1, j+1)
                    incre(h, w, a, i, j+1)
                    incre(h, w, a, i+1, j)
                    incre(h, w, a, i+1, j+1)
                elif 0 < j < w - 1:
                    incre(h, w, a, i-1, j-1)
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i-1, j+1)
                    incre(h, w, a, i, j-1)
                    incre(h, w, a, i, j+1)
                    incre(h, w, a, i+1, j-1)
                    incre(h, w, a, i+1, j)
                    incre(h, w, a, i+1, j+1)
                elif j == w-1:
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i-1, j-1)
                    incre(h, w, a, i, j-1)
                    incre(h, w, a, i+1, j-1)
                    incre(h, w, a, i+1, j)
            elif i == h-1:
                if j == 0:
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i-1, j+1)
                    incre(h, w, a, i, j+1)
                elif 0 < j < w - 1:
                    incre(h, w, a, i-1, j-1)
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i-1, j+1)
                    incre(h, w, a, i, j-1)
                    incre(h, w, a, i, j+1)
                elif j == w-1:
                    incre(h, w, a, i-1, j-1)
                    incre(h, w, a, i-1, j)
                    incre(h, w, a, i, j-1)

[print(*i, sep="") for i in a]

