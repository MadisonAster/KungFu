import unittest
from datetime import datetime


class SimpleCluster():
    def __init__(self):
        pass
        



        

class test_SimpleCluster(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        pass


if __name__ == '__main__':
    unittest.main()