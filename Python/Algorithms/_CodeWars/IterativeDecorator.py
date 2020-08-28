import unittest
from datetime import datetime
import functools

def IterativeDecorator(*args):
    functionlist = args
    def wrapper_factory(original_function):
        @functools.wraps(original_function)
        def wrapper(N):
            result = original_function(N)
            for f in functionlist:
                result = f(result)
            return result
        return wrapper
    return wrapper_factory

class test_IterativeDecorator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        def f2(N): return N*2
        def f1(N): return N*10

        @IterativeDecorator(f1, f2)
        def f0(N): return N*10

        self.assertEqual(f0(10), 2000)

if __name__ == '__main__':
    unittest.main()
