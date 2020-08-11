import unittest
from datetime import datetime
from functools import lru_cache

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

if __name__ == '__main__':
    unittest.main()