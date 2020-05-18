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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    s = input()
    s = s[::-1]

    i = 0
    while True:
        if i <= len(s) - 5 and  s[i:i+5] == "dream"[::-1]:
            i = i+5
        elif i <= len(s) - 5 and s[i:i+5] == "erase"[::-1]:
            i = i+5
        elif i <= len(s) - 6 and s[i:i+6] == "eraser"[::-1]:
            i = i+6
        elif i <= len(s) - 7 and s[i:i+7] == "dreamer"[::-1]:
            i = i+7
        else:
            break
    if i == len(s):
        print("YES")
    else:
        print("NO")