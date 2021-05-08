import unittest
from functools import reduce

class test_bracket_solver(unittest.TestCase):

    def test_1(self) -> None:
        input = '{{{(([]))}}}'
        expected = True
        self.assertEqual(bracket_solver(input), expected)

    def test_2(self) -> None:
        input = '[]'
        expected = True
        self.assertEqual(bracket_solver(input), expected)

    def test_3(self) -> None:
        input = '[][]'*200000
        expected = True
        self.assertEqual(bracket_solver(input), expected)

    def test_4(self) -> None:
        input = '([])([])'
        expected = True
        self.assertEqual(bracket_solver(input), expected)

    def test_5(self) -> None:
        input = '{{{((['
        expected = False
        self.assertEqual(bracket_solver(input), expected)

    def test_6(self) -> None:
        input = '{{{(([]))]}]'
        expected = False
        self.assertEqual(bracket_solver(input), expected)

    def test_7(self) -> None:
        input = '[][][][}'
        expected = False
        self.assertEqual(bracket_solver(input), expected)
    
    def test_8(self) -> None:
        input = '}{'
        expected = False
        self.assertEqual(bracket_solver(input), expected)
    
    def test_92(self) -> None:
        input = '[>[}[}{]{]<]'
        expected = False
        self.assertEqual(bracket_solver(input), expected)
        
    def test_9(self) -> None:
        input = '[}[}[}{]{]{]'
        expected = False
        self.assertEqual(bracket_solver(input), expected)
    
    def test_10(self) -> None:
        input = '[}[}[}{]{]{]'
        expected = False
        self.assertEqual(bracket_solver(input), expected)

def indexof(input, a):
    if a not in input: return 0
    else: return input.index(a)

def indexof2(a, fset = '({[<', rset = '<[{(') -> int:
    if a not in fset: return 0
    else: return fset.index(a) + rset.index(a) * 2

def indexof3(a, fset = ')}]>', rset = '>]})') -> int:
    if a not in fset: return 0
    else: return - fset.index(a) - rset.index(a) * 2

def enforcepositive(a, b):
    if a < 0: return -1
    a += b
    if a < 0: return -1
    else: return a

def bracket_solver(input: str) -> bool:
    count = 0
    
    ####solution3, 0.760s####
    #indicies2 = map(indexof2, input)
    #indicies3 = map(indexof3, input)
    #indicies = map(sum, zip(indicies2, indicies3))
    #count = reduce(enforcepositive, indicies)
    #########################
    
    for a in input:
    
        ####solution1, 0.419s####
        if a in '({[<':
            count += '({[<'.index(a) + '<[{('.index(a) * 2
        elif a in '>]})':
            count -= ')}]>'.index(a) + '>]})'.index(a) * 2
        if count < 0: return False
        #########################
        
        ####solution2, 0.859s####
        #count += indexof('({[<', a) + indexof('<[{(', a) * 2
        #count -= indexof(')}]>', a) + indexof('>]})', a) * 2
        #if count < 0: return False
        #########################
    
    return count == 0
    
if __name__ == '__main__':
    unittest.main()
