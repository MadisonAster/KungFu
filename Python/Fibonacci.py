import unittest
from datetime import datetime
from functools import lru_cache


@lru_cache(None)
def fibstring(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    else:
        return fibstring(n-1) + fibstring(n-2)

@lru_cache(None)
def fibindex(n):
    if n in (0, 1):
        return 1
    if n & 1:
        return fibindex((n+1)//2-1) * (2*fibindex((n+1)//2) - fibindex((n+1)//2-1))
    a, b = fibindex(n//2-1), fibindex(n//2)
    return a**2 + b**2

def fibonacci(n):
    return fibindex(n-1)

class test_fibonacci(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
    
    def test_1(self):
        self.assertEquals(fibonacci(10), 55)
    def test_2(self):
        self.assertEquals(fibonacci(100), 354224848179261915075)
    def test_3(self):
        self.assertEquals(fibonacci(3), 2)

class test_fibstring(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_0(self):
        self.assertEqual(fibstring(0), '0')
    def test_1(self):
        self.assertEqual(fibstring(1), '01')
    def test_2(self):
        self.assertEqual(fibstring(2), '010')
    def test_3(self):
        self.assertEqual(fibstring(3), '01001')
    def test_4(self):
        self.assertEqual(fibstring(4), '01001010')
    def test_5(self):
        self.assertEqual(fibstring(5), '0100101001001')
    def test_10(self):
        print(len(fibstring(10)))
    def test_42(self):
        print(len(fibstring(42)))
    #def test_100(self):
    #    print(len(fibstring(100)))

if __name__ == '__main__':
    unittest.main()