#Standard Imports#################################
import unittest
##################################################

#Test#############################################
class test_array_diff(unittest.TestCase):
    def test_1(self):
        self.assertEqual(array_diff([1,2], [1]), [2])
        
    def test_2(self):
        self.assertEqual(array_diff([1,2,2], [1]), [2,2])
        
    def test_3(self):
        self.assertEqual(array_diff([1,2,2], [2]), [1])
        
    def test_4(self):
        self.assertEqual(array_diff([1,2,2], []), [1,2,2])
        
    def test_5(self):
        self.assertEqual(array_diff([], [1,2]), [])
##################################################

#Code#############################################
def array_diff(a, b):
    result = []
    for aa in a:
        if aa not in b:
            result.append(aa)
    return result
##################################################
       
#Main############################################# 
if __name__ == '__main__':
    unittest.main()
##################################################
