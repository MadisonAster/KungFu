import unittest
import datetime

def human_readable_time(n):
    dt = datetime.datetime.fromtimestamp(n)
    delta = datetime.timedelta(seconds = n)
    hours = str(delta.days*24+int(str(delta).rsplit(' ',1)[-1].split(':',1)[0]))
    return hours+dt.strftime(':%M:%S')
    
class human_readable_time_test(unittest.TestCase):
    def startUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_1(self):
        self.assertEqual(human_readable_time(359999), '99:59:59')

if __name__ == '__main__':
    unittest.main()

