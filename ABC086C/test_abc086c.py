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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    T = [list(map(int, input().split())) for i in range(n)]
    T.insert(0, [0, 0, 0])

    for i, now in enumerate(T):
        if i == 0:
            continue
        prev = T[i-1]

        timelapse = now[0] - prev[0]
        stepdiff = (now[1] - prev[1]) + (now[2] - prev[2])

        if (timelapse % 2) != (stepdiff % 2) or (abs(stepdiff) > timelapse):
            print("No")
            exit()
    print("Yes")