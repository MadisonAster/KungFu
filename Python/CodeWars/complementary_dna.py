import unittest

def complementary_dna(dna):
    return dna

class likestest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_1(self):
        self.assertEqual(complementary_dna('ATTGC'), 'TAACG')
        
    def test_2(self):
        self.assertEqual(complementary_dna('GTAT'), 'CATA')
    
if __name__ == '__main__':
    unittest.main()
