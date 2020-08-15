from itertools import permutations

def SkyScrapers3(clues, aslists=True):
    global _DIMENSIONS
    size = _DIMENSIONS
    variants = {i: set() for i in range(size+1)}
    for row in permutations(range(1, size+1)):
        visible = sum(v >= max(row[:i+1]) for i, v in enumerate(row))
        variants[visible].add(row)
        variants[0].add(row)
        
    possible_cols, possible_rows = [], []
    for i in range(size):
        clue_left, clue_right = clues[4*size-1-i], clues[size + i]
        var_left = variants[clue_left]
        var_right = set(map(lambda row: tuple(reversed(row)), variants[clue_right]))
        possible_rows.append(var_left.intersection(var_right))

        clue_top, clue_btm = clues[i], clues[3*size-1-i]
        var_top = variants[clue_top]
        var_btm = set(map(lambda row: tuple(reversed(row)), variants[clue_btm]))
        possible_cols.append(var_top.intersection(var_btm))
        
    while any(len(var_row) > 1 for var_row in possible_rows):
        for i in range(size):
            for j in range(size):
                row_set = set(row[j] for row in possible_rows[i])
                col_set = set(col[i] for col in possible_cols[j])
                union_set = row_set.intersection(col_set)
                possible_rows[i] = [row for row in possible_rows[i] if row[j] in union_set]
                possible_cols[j] = [col for col in possible_cols[j] if col[i] in union_set]
    if aslists:
        result = tuple(row[0] for row in possible_rows)
        return ConvertToLists(result)
    else:
        return tuple(row[0] for row in possible_rows)
def ConvertToLists(tuples):
    result = []
    for row in tuples:
        newrow = list(row)
        result.append(newrow)
    return result
##################################################################################
import unittest
from datetime import datetime
_DIMENSIONS = 6
class test_SkyScrapers3(unittest.TestCase):
    def setUp(self):
        self.startTime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.startTime
        print(str(t), self.id())
        
    def test_4x4_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        clues = (0,0,1,2,
                 0,2,0,0,
                 0,3,0,0,
                 0,1,0,0)
        expected = ((2,1,4,3),
                    (3,4,1,2),
                    (4,2,3,1),
                    (1,3,2,4))
        self.assertEqual(SkyScrapers3(clues, aslists=False), expected)
    
    def test_4x4_2(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        clues = (2,2,1,3,  
                 2,2,3,1,  
                 1,2,2,3,  
                 3,2,1,3)
        expected = ((1,3,4,2),
                    (4,2,1,3),
                    (3,4,2,1),
                    (2,1,3,4))
        self.assertEqual(SkyScrapers3(clues, aslists=False), expected)
    
    def test_6x6_1(self):
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
        self.assertEqual(SkyScrapers3(clues, aslists=False), expected)
    
    def test_6x6_2(self):
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
        self.assertEqual(SkyScrapers3(clues, aslists=False), expected)
    
    def test_6x6_3(self):
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
        self.assertEqual(SkyScrapers3(clues, aslists=False), expected)
        
    def test_7x7_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [7,0,0,0,2,2,3,
                 0,0,3,0,0,0,0,
                 3,0,3,0,0,5,0,
                 0,0,0,0,5,0,4]
        expected = [[1,5,6,7,4,3,2],
                    [2,7,4,5,3,1,6],
                    [3,4,5,6,7,2,1],
                    [4,6,3,1,2,7,5],
                    [5,3,1,2,6,4,7],
                    [6,2,7,3,1,5,4],
                    [7,1,2,4,5,6,3]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_2(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0,2,3,0,2,0,0,
                 5,0,4,5,0,4,0,
                 0,4,2,0,0,0,6,
                 5,2,2,2,2,4,1]
        expected = [[7,6,2,1,5,4,3],
                    [1,3,5,4,2,7,6],
                    [6,5,4,7,3,2,1],
                    [5,1,7,6,4,3,2],
                    [4,2,1,3,7,6,5],
                    [3,7,6,2,1,5,4],
                    [2,4,3,5,6,1,7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_3(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0,2,3,0,2,0,0,
                 5,0,4,5,0,4,0,
                 0,4,2,0,0,0,6,
                 0,0,0,0,0,0,0]
        expected = [[7,6,2,1,5,4,3],
                    [1,3,5,4,2,7,6],
                    [6,5,4,7,3,2,1],
                    [5,1,7,6,4,3,2],
                    [4,2,1,3,7,6,5],
                    [3,7,6,2,1,5,4],
                    [2,4,3,5,6,1,7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)

    def test_7x7_4(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [7, 0, 0, 0, 2, 2, 3,
                 0, 0, 3, 0, 0, 0, 0,
                 3, 0, 3, 0, 0, 5, 0,
                 0, 0, 0, 0, 5, 0, 4]
        expected = [[1, 5, 6, 7, 4, 3, 2],
                    [2, 7, 4, 5, 3, 1, 6],
                    [3, 4, 5, 6, 7, 2, 1],
                    [4, 6, 3, 1, 2, 7, 5],
                    [5, 3, 1, 2, 6, 4, 7],
                    [6, 2, 7, 3, 1, 5, 4],
                    [7, 1, 2, 4, 5, 6, 3]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_5(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [6, 4, 0, 2, 0, 0, 3,
                 0, 3, 3, 3, 0, 0, 4,
                 0, 5, 0, 5, 0, 2, 0,
                 0, 0, 0, 4, 0, 0, 3]
        expected = [[2, 1, 6, 4, 3, 7, 5],
                    [3, 2, 5, 7, 4, 6, 1],
                    [4, 6, 7, 5, 1, 2, 3],
                    [1, 3, 2, 6, 7, 5, 4],
                    [5, 7, 1, 3, 2, 4, 6],
                    [6, 4, 3, 2, 5, 1, 7],
                    [7, 5, 4, 1, 6, 3, 2]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_6(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 0, 0, 5, 0, 0, 3,
                 0, 6, 3, 4, 0, 0, 0,
                 3, 0, 0, 0, 2, 4, 0,
                 2, 6, 2, 2, 2, 0, 0]
        expected = [[3, 5, 6, 1, 7, 2, 4],
                    [7, 6, 5, 2, 4, 3, 1], 
                    [2, 7, 1, 3, 6, 4, 5], 
                    [4, 3, 7, 6, 1, 5, 2], 
                    [6, 4, 2, 5, 3, 1, 7], 
                    [1, 2, 3, 4, 5, 7, 6],
                    [5, 1, 4, 7, 2, 6, 3]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_7(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 0, 5, 0, 0, 0, 6,
                 4, 0, 0, 2, 0, 2, 0, 
                 0, 5, 2, 0, 0, 0, 5, 
                 0, 3, 0, 5, 0, 0, 3]
        expected = [[3, 4, 1, 7, 6, 5, 2],
                    [7, 1, 2, 5, 4, 6, 3],
                    [6, 3, 5, 2, 1, 7, 4],
                    [1, 2, 3, 6, 7, 4, 5],
                    [5, 7, 6, 4, 2, 3, 1],
                    [4, 5, 7, 1, 3, 2, 6],
                    [2, 6, 4, 3, 5, 1, 7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_8(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 0, 5, 3, 0, 2, 0,
                 0, 0, 0, 4, 5, 0, 0,
                 0, 0, 0, 3, 2, 5, 4, 
                 2, 2, 0, 0, 0, 0, 5]
        expected = [[2, 3, 1, 4, 6, 5, 7],
                    [1, 7, 4, 6, 5, 2, 3],
                    [3, 6, 5, 7, 2, 1, 4], 
                    [7, 5, 6, 3, 1, 4, 2], 
                    [6, 2, 7, 5, 4, 3, 1], 
                    [5, 4, 2, 1, 3, 7, 6], 
                    [4, 1, 3, 2, 7, 6, 5]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_9(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 2, 3, 0, 2, 0, 0, 
                 5, 0, 4, 5, 0, 4, 0,
                 0, 4, 2, 0, 0, 0, 6,
                 5, 2, 2, 2, 2, 4, 1]
        expected = [[7, 6, 2, 1, 5, 4, 3],
                    [1, 3, 5, 4, 2, 7, 6],
                    [6, 5, 4, 7, 3, 2, 1],
                    [5, 1, 7, 6, 4, 3, 2],
                    [4, 2, 1, 3, 7, 6, 5],
                    [3, 7, 6, 2, 1, 5, 4],
                    [2, 4, 3, 5, 6, 1, 7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_10(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 2, 3, 0, 2, 0, 0,
                 5, 0, 4, 5, 0, 4, 0, 
                 0, 4, 2, 0, 0, 0, 6, 
                 0, 0, 0, 0, 0, 0, 0]
        expected = [[7, 6, 2, 1, 5, 4, 3], 
                    [1, 3, 5, 4, 2, 7, 6], 
                    [6, 5, 4, 7, 3, 2, 1], 
                    [5, 1, 7, 6, 4, 3, 2],
                    [4, 2, 1, 3, 7, 6, 5],
                    [3, 7, 6, 2, 1, 5, 4], 
                    [2, 4, 3, 5, 6, 1, 7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_11(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 0, 3, 0, 0, 0, 0,
                 3, 0, 3, 0, 0, 5, 0, 
                 0, 0, 0, 0, 5, 0, 4, 
                 7, 0, 0, 0, 2, 2, 3]
        expected = [[2, 6, 1, 5, 7, 4, 3],
                    [3, 1, 2, 7, 4, 5, 6],
                    [4, 3, 7, 2, 6, 1, 5],
                    [7, 5, 6, 1, 2, 3, 4],
                    [6, 4, 5, 3, 1, 7, 2],
                    [5, 7, 4, 6, 3, 2, 1],
                    [1, 2, 3, 4, 5, 6, 7]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_12(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [3, 0, 3, 0, 0, 5, 0,
                 0, 0, 0, 0, 5, 0, 4,
                 7, 0, 0, 0, 2, 2, 3,
                 0, 0, 3, 0, 0, 0, 0]
        expected = [[3, 6, 5, 4, 2, 1, 7], 
                    [4, 5, 1, 3, 7, 2, 6], 
                    [7, 4, 6, 2, 1, 3, 5], 
                    [5, 7, 2, 1, 3, 6, 4], 
                    [1, 2, 7, 6, 5, 4, 3], 
                    [6, 1, 3, 5, 4, 7, 2], 
                    [2, 3, 4, 7, 6, 5, 1]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_13(self):
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [0, 0, 0, 0, 5, 0, 4,
                 7, 0, 0, 0, 2, 2, 3,
                 0, 0, 3, 0, 0, 0, 0,
                 3, 0, 3, 0, 0, 5, 0]
        expected = [[7, 6, 5, 4, 3, 2, 1], 
                    [1, 2, 3, 6, 4, 7, 5], 
                    [2, 7, 1, 3, 5, 4, 6], 
                    [4, 3, 2, 1, 6, 5, 7], 
                    [5, 1, 6, 2, 7, 3, 4], 
                    [6, 5, 4, 7, 2, 1, 3], 
                    [3, 4, 7, 5, 1, 6, 2]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
    def test_7x7_14(self):
        return
        global _DIMENSIONS
        _DIMENSIONS = 7
        clues = [3, 3, 2, 1, 2, 2, 3,
                 4, 3, 2, 4, 1, 4, 2, 
                 2, 4, 1, 4, 5, 3, 2, 
                 3, 1, 4, 2, 5, 2, 3]
        expected = [[2, 1, 4, 7, 6, 5, 3],
                    [6, 4, 7, 3, 5, 1, 2], 
                    [1, 2, 3, 6, 4, 7, 5], 
                    [5, 7, 6, 2, 3, 4, 1], 
                    [4, 3, 5, 1, 2, 6, 7], 
                    [7, 6, 2, 5, 1, 3, 4], 
                    [3, 5, 1, 4, 7, 2, 6]]
        self.assertEqual(SkyScrapers3(clues, aslists=True), expected)
    
if __name__ == '__main__':
    unittest.main()