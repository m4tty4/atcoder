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

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1,  0,  1, -1, 1,-1, 0, 1]

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            elif s[i][j] == '.':
                num = 0
                for a in range(8):
                    ni = i + dx[a]
                    nj = j + dy[a]

                    if (0 <= ni < h) and (0 <= nj < w) and (s[ni][nj] == '#'):
                        num += 1
                s[i][j] = num

    [print(*i,sep='') for i in s]
