import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]

    a = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                a[i][j] = '#'

    for i in range(h):
        for j in range(w):
            if (s[i][j] == '#'):
                if i == 0:
                    if j == 0:
                        incre(i, j, a, i, j+1)
                        incre(i, j, a, i+1, j)
                        incre(i, j, a, i+1, j+1)
                    elif 0 < j < w - 1:
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i+1, j)
                        incre(i, j, a, i-1, j+1)
                        incre(i, j, a, i, j+1)
                        incre(i, j, a, i+1, j+1)
                    elif j == w-1:
                        incre(i, j, a, i, j-1)
                        incre(i, j, a, i-1, j-1)
                        incre(i, j, a, i+1, j)
                elif 0 < i < h - 1:
                    if j == 0:
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i-1, j+1)
                        incre(i, j, a, i, j+1)
                        incre(i, j, a, i+1, j)
                        incre(i, j, a, i+1, j+1)
                    elif 0 < j < w - 1:
                        incre(i, j, a, i-1, j-1)
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i-1, j+1)
                        incre(i, j, a, i, j-1)
                        incre(i, j, a, i, j+1)
                        incre(i, j, a, i+1, j-1)
                        incre(i, j, a, i+1, j)
                        incre(i, j, a, i+1, j+1)
                    elif j == w-1:
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i-1, j-1)
                        incre(i, j, a, i, j-1)
                        incre(i, j, a, i+1, j-1)
                        incre(i, j, a, i+1, j)
                elif i == h-1:
                    if j == 0:
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i-1, j+1)
                        incre(i, j, a, i, j+1)
                    elif 0 < j < w - 1:
                        incre(i, j, a, i-1, j-1)
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i-1, j+1)
                        incre(i, j, a, i, j-1)
                        incre(i, j, a, i, j+1)
                    elif j == w-1:
                        incre(i, j, a, i-1, j-1)
                        incre(i, j, a, i-1, j)
                        incre(i, j, a, i, j-1)
    
    [print(*i, sep="") for i in a]

def incre(h, w, a, i, j):
    print(h, w, i, j)
    if a[i][j] != '#':
        a[i][j] += 1
