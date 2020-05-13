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
        input = """20 2 5"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 4 16"""
        output = """4554"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n, a, b = map(int, input().split())

    List = []
    for i in range(1, n + 1):
        x, y, z, w, v= 0, 0, 0, 0, 0
        x = i % 10
        if i >= 10:
            y = (i - x) % 100
            y = int(y / 10)
        if i >= 100:
            z = (i - x - y) % 1000
            z = int(z / 100)
        if i >= 1000:
            w = (i - x - y - z) % 10000
            w = int(w / 1000)
        if i >= 10000:
            v = (i - x - y - z) % 100000
            v = int(v / 10000)
        sumnum = x + y + z + w + v
        if sumnum >= a and sumnum <= b:
            List.append(int(i))
    print(sum(List))