import sys
import unittest
from datetime import datetime

class TimedTest(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

if __name__ == '__main__':
    unittest.main()