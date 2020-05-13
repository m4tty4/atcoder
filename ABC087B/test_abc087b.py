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
2
2
100"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1
0
150"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
40
50
6000"""
        output = """213"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    X = int(input())

    count = 0

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if (500 * i + 100 * j + 50 * k) == X:
                    count = count + 1

    print(count)

