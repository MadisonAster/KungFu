import unittest

def digital_rootO(n):
    count = 0
    for d in str(n):
        count += int(d)
    if len(str(count)) > 1:
        return digital_root(count)
    else:
        return count

def digital_root(n):
  return n%9 or n and 9

class likestest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    
    def test_9(self):
        self.assertEqual(digital_root(9), 9)
    
    def test_16(self):
        self.assertEqual(digital_root(16), 7)
    
    def test_942(self):
        self.assertEqual(digital_root(942), 6)
        
    def test_132189(self):
        self.assertEqual(digital_root(132189), 6)
        
    def test_493193(self):
        self.assertEqual(digital_root(493193), 2)
    
if __name__ == '__main__':
    unittest.main()
