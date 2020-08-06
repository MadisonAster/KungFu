import unittest, time
from datetime import datetime
import math

def get_divisors(n):
    for i in range(1, n+1):
        if (n%i == 0):
            yield i
def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        sum = 0
        for d in get_divisors(i):
            sum += d*d
        if math.sqrt(sum) % 1 > 0:
            continue
        else:
            result.append([i, sum])
    return result
    
class list_squared_test(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
        #print(str(t.seconds)+'.'+str(t.microseconds)+' seconds '+self.id())
        
    def test_1(self):
        result = list_squared(1,250)
        self.assertEqual(list_squared(1,250), [[1,1], [42,2500], [246, 84100]])
    
    def test_2(self):
        self.assertEqual(list_squared(42,250), [[42,2500], [246, 84100]])
    
    def test_3(self):
        self.assertEqual(list_squared(250,500), [[287, 84100]])

if __name__ == '__main__':
    unittest.main()