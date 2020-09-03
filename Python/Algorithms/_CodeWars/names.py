#Standard Imports#################################
import unittest
##################################################

#Test#############################################
class test_likeformatting(unittest.TestCase):
    def test_0(self):
        self.assertEqual(likeformatting([]), "no one likes this")
    def test_1(self):
        self.assertEqual(likeformatting(["Peter"]), "Peter likes this")
    def test_2(self):
        self.assertEqual(likeformatting(["Jacob", "Alex"]), "Jacob and Alex like this")
    def test_3(self):
        self.assertEqual(likeformatting(["Max", "John", "Mark"]), "Max, John and Mark like this")
    def test_4plus(self):
        self.assertEqual(likeformatting(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")
##################################################

#Code#############################################
def likeformatting(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
##################################################

#Main#############################################
if __name__ == '__main__':
    unittest.main()
##################################################
