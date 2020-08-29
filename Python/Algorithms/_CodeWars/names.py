import unittest

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

class likestest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_0(self):
        self.assertEqual(likes([]), "no one likes this")
    def test_1(self):
        self.assertEqual(likes(["Peter"]), "Peter likes this")
    def test_2(self):
        self.assertEqual(likes(["Jacob", "Alex"]), "Jacob and Alex like this")
    def test_3(self):
        self.assertEqual(likes(["Max", "John", "Mark"]), "Max, John and Mark like this")
    def test_4plus(self):
        self.assertEqual(likes(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")

if __name__ == '__main__':
    unittest.main()
