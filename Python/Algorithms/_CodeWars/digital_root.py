#Standard Imports#################################
import unittest
##################################################

#Test#############################################
class test_digital_root(unittest.TestCase):
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
##################################################

#Code#############################################
def digital_root(n):
    return n%9 or n and 9
##################################################

#Main#############################################
if __name__ == '__main__':
    unittest.main()
##################################################
