import unittest
from itertools import permutations, chain
_DIMENSIONS = 4
def SkyScrapers2(clues):
    global _DIMENSIONS
    size = _DIMENSIONS
    for poss in permutations(permutations(range(1, size+1), size), size):
        for i in range(size):
            if len(set(row[i] for row in poss)) < size:
                break
        else:
            cols_top = [[row[i] for row in poss] for i in range(size)]
            rows_right = [list(reversed(row)) for row in poss]
            cols_btm = [[row[i] for row in reversed(poss)] for i in reversed(range(size))]
            rows_left = list(reversed(poss))
            for i, row in enumerate(chain(cols_top, rows_right, cols_btm, rows_left)):
                if not clues[i]:
                    continue
                visible = 0
                for j, v in enumerate(row):
                    visible += v >= max(row[:j+1])
                if visible != clues[i]:
                    break
            else:
                return poss
'''
class test_SkyScrapers2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_4x4_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        clues = (0,0,1,2,
                 0,2,0,0,
                 0,3,0,0,
                 0,1,0,0)
        self.assertEqual(SkyScrapers2(clues), ((2,1,4,3),
                                              (3,4,1,2),
                                              (4,2,3,1),
                                              (1,3,2,4)))
    
    def test_4x4_2(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        clues = (2,2,1,3,  
                 2,2,3,1,  
                 1,2,2,3,  
                 3,2,1,3)
        self.assertEqual(SkyScrapers2(clues), ((1,3,4,2),
                                              (4,2,1,3),
                                              (3,4,2,1),
                                              (2,1,3,4)))
    
    def test_6x6_1(self):
        #return
        global _DIMENSIONS
        _DIMENSIONS = 6
        clues = ( 3, 2, 2, 3, 2, 1,
                  1, 2, 3, 3, 2, 2,
                  5, 1, 2, 2, 4, 3,
                  3, 2, 1, 2, 2, 4)
        expected = (( 2, 1, 4, 3, 5, 6 ),
                    ( 1, 6, 3, 2, 4, 5 ),
                    ( 4, 3, 6, 5, 1, 2 ),
                    ( 6, 5, 2, 1, 3, 4 ),
                    ( 5, 4, 1, 6, 2, 3 ),
                    ( 3, 2, 5, 4, 6, 1 ))
        self.assertEqual(SkyScrapers2(clues), expected)
    
    def test_6x6_2(self):
        return
        global _DIMENSIONS
        _DIMENSIONS = 6
        clues = ( 0, 0, 0, 2, 2, 0,
                  0, 0, 0, 6, 3, 0,
                  0, 4, 0, 0, 0, 0,
                  4, 4, 0, 3, 0, 0)
        expected = (( 5, 6, 1, 4, 3, 2 ), 
                    ( 4, 1, 3, 2, 6, 5 ), 
                    ( 2, 3, 6, 1, 5, 4 ), 
                    ( 6, 5, 4, 3, 2, 1 ), 
                    ( 1, 2, 5, 6, 4, 3 ), 
                    ( 3, 4, 2, 5, 1, 6 ))
        self.assertEqual(SkyScrapers2(clues), expected)
    
    def test_6x6_3(self):
        return
        global _DIMENSIONS
        _DIMENSIONS = 6
        clues = ( 0, 3, 0, 5, 3, 4, 
                  0, 0, 0, 0, 0, 1,
                  0, 3, 0, 3, 2, 3,
                  3, 2, 0, 3, 1, 0)
        expected = (( 5, 2, 6, 1, 4, 3 ), 
                    ( 6, 4, 3, 2, 5, 1 ), 
                    ( 3, 1, 5, 4, 6, 2 ), 
                    ( 2, 6, 1, 5, 3, 4 ), 
                    ( 4, 3, 2, 6, 1, 5 ), 
                    ( 1, 5, 4, 3, 2, 6 ))
        self.assertEqual(SkyScrapers2(clues), expected)


if __name__ == '__main__':
    unittest.main()
'''