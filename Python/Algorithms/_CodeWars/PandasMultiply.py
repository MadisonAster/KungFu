import unittest
from datetime import datetime
import functools

import pandas

def mult(left, right):
    a = pandas.Series((100, 1, 10, 65), dtype=object)
    b = pandas.Series((-85, -234, 32, 104), dtype=int)
    c = pandas.Series((205.3, 3.5, 234.3, 8403.32), dtype=float)
    df = pandas.DataFrame(dict(a=a, b=b, c=c))
    for _ in range(int(1e4)):
        df[left] * df[right]

class test_IterativeDecorator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        mult('a', 'b')
    def test_2(self):
        mult('a', 'c')
    def test_3(self):
        mult('b', 'c')

if __name__ == '__main__':
    unittest.main()
