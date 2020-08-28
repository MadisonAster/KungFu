import unittest
from datetime import datetime


'''
def compose(func, *args):
    #result = func
    result = 10
    for f in args:
        result = f(result)
    return result

def func1(param):
    return param*2

#@compose(func1)
def func0(param):
    return param*10
'''
class test_decorator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        pass
        #self.assertEqual(decorator(200), 200)


def mult(left, right):
    return None
class test_mult(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        self.assertEqual(mult(None, None), None)


if __name__ == '__main__':
    unittest.main()
