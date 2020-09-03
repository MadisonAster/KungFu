'''
           1   2 
 _________________
 |   |   |   |123|
 |   |   |4  |   |
 |   |   |   |   |
 -----------------
 |   |   |   |123|
 |   |   |   |   |2
 |   |   |   |   |
 -----------------
 |   |   |   |123|
1|4  |   |   |   |
 |   |   |   |   |
 -----------------  
 |   |   |   |   | 
 |   |   |   |4  | 
 |   |   |   |   | 
 -----------------
           3
'''

#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
from datetime import datetime
from copy import copy
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Code#############################################
_DIMENSIONS = 4 #Global because the Kata does not supply it as an argument, overridden in unit tests

def SkyScrapers(clues, aslists=False, printgrids=False):
    grid = CreateGrid(_DIMENSIONS)
    if printgrids:
        PrintGrid(grid, clues)
    while CheckLengths(grid) == False:
        for i, clue in enumerate(clues):
            if clue != 0:
                clist = ListClue(grid, i)
                corders = ClueOrders(_DIMENSIONS, clue)
                corders = PruneOrders(clist, corders)
                cposs = CollapsePossibilities(corders)
                clist = ComparePossibilities(clist, cposs)
                PrunePossibilities(clist)
            else:
                clist = ListClue(grid, i)
                PrunePossibilities(clist)
        if printgrids:
            PrintGrid(grid, clues)
    return CollapseResult(grid, aslists)

def CreateGrid(d): #Create grid according to dimensions
    grid = []
    for row in list(range(d)):
        row = []
        for column in list(range(d)):
            row.append(list(range(1,d+1)))
        grid.append(row)
    return grid

def CheckLengths(grid): #Check to see if we're down to a single set of possibilities
    for row in grid:
        for subset in row:
            if len(subset) > 1:
                return False
    else:
        return True

def ListClue(grid, i): #Returns live references of grid, ordered from perspective of clue
    result = []
    for a in YieldClue(grid, i):
        result.append(a)
    return result

def YieldClue(grid, i): #Iterator for ListClue
    d = len(grid[0])
    if i < d:
        for row in grid:
            yield row[i]
    elif i < d*2:
        for column in reversed(grid[i-d]):
            yield column
    elif i < d*3:
        for row in reversed(grid):
            yield row[(i*-1)+(d*3-1)]
    else:
        for column in grid[(i*-1)+(d*4-1)]:
            yield column

def ClueOrders(d, n): #All possible orders for a given dimension d and clue size n
    result = []
    for order in AllOrders(d):
        count = 0
        last = 0
        for a in order:
            if a > last:
                last = a
                count += 1
        if count == n:
            result.append(order)
    return result

def AllOrders(d): #All possible number orders for a given dimension
    result = []
    for order in YieldOrders(list(range(1,d+1))):
        result.append(order)
    return result

def YieldOrders(nlist): #Iterator for AllOrders
    if type(nlist) is int:
        nlist = list(range(1,nlist+1))
    if len(nlist) == 1:
        yield nlist
    else:
        for n in nlist:
            clist = copy(nlist)
            clist.remove(n)
            for subresult in YieldOrders(clist):
                yield [n]+subresult

def PruneOrders(poss, orders): #destructive
    for order in reversed(orders):
        for i, n in enumerate(order):
            if n not in poss[i]:
                orders.remove(order)
                break
    return orders

def CollapsePossibilities(orders): #Collapse list of possible orders to list of possibilities for each cell
    d = len(orders[0])
    
    result = []
    for i in list(range(d)):
        subset = []
        for order in orders:
            subset.append(order[i])
        subset = list(set(subset))
        subset.sort()
        result.append(subset)
    return result

def ComparePossibilities(poss1, poss2): #destructive, Removes possibilities in poss1 that aren't also in poss2
    for a, b in zip(poss1, poss2):
        for n in reversed(a):
            if n not in b:
                a.remove(n)
    return poss1

def PrunePossibilities(poss): #destructive, Prunes possibility list by matching sets, and isolating singles
    msets = []
    for m in list(range(1, len(poss))):
        for a in poss:
            if len(a) == m and poss.count(a) == m:
                if a not in msets:
                    msets.append(a)
    for match in msets:
        for i in match:
            for subset in poss:
                if subset != match and i in subset:
                    subset.remove(i)
    
    for i, subset in enumerate(poss):
        for n in subset:
            if CountAppearances(poss, n) == 1:
                for x in subset:
                    if x != n:
                        subset.remove(x)
                break
    return poss

def CountAppearances(poss, n):
    count = 0
    for subset in poss:
        if n in subset:
            count += 1
    return count

def PrintGrid(grid, clues): #For testing
    d = len(grid)
    spacing = ' '
    spacing2 = ' '*(d-1)
    
    clues = list(copy(clues))
    for i, a in enumerate(clues):
        pass
        #if a == 0:
        #    clues[i] = ' '
    
    print('\n')
    
    #TopClues
    printline = ''
    for clue in clues[0:d]:
        printline += spacing2*2+str(clue)+spacing2*2
    print(printline)
    
    
    print('  '+'___'*(d*d+d))
    for i, row in enumerate(grid):
        printline = str(clues[-i-1])+'|'
        for possibilityset in row:
            chars = len(possibilityset)*3
            fill = int((d*3-chars)/2)
            if chars %2 != 0:
                extrafill = ' '
            else:
                extrafill = ''
            printline += extrafill+(' '*fill)+spacing+str(possibilityset)+spacing+(' '*fill)+'|'
        print(printline+str(clues[i+d]))
        print('  '+'---'*(d*d+d))
    
    #BottomClues
    printline = ''
    for clue in reversed(clues[d*2:d*3]):
        printline += spacing2*2+str(clue)+spacing2*2
    print(printline)
    
    
    print('\n')

def CollapseResult(grid, aslists): #Final Result
    if aslists:
        result = []
        for row in grid:
            newrow = []
            for subset in row:
                newrow.append(subset[0])
            result.append(newrow)
        return result

    else:
        result = ()
        for row in grid:
            newrow = ()
            for subset in row:
                newrow += (subset[0],)
            result += (newrow,)
        return result
##################################################

#Test#############################################

class test_SkyScrapers(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
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
        self.assertEqual(SkyScrapers(clues), expected)
    
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
        self.assertEqual(SkyScrapers(clues), expected)
    
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
        self.assertEqual(SkyScrapers(clues), expected)
    
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
        self.assertEqual(SkyScrapers(clues), expected)
    
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
        self.assertEqual(SkyScrapers(clues), expected)
        
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
        self.assertEqual(SkyScrapers(clues, aslists=True, printgrids=False), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True, printgrids=False), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True, printgrids=False), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    
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
        self.assertEqual(SkyScrapers(clues, aslists=True), expected)
    '''
    def test_7x7_14(self):
        #return
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
        self.assertEqual(SkyScrapers(clues, aslists=True, printgrids=True), expected)
    '''
class test_CheckLengths(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

class test_ListClue(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_top4(self):
        grid = CreateGrid(4)
        grid[0][3] = 0
        grid[1][3] = 1
        grid[2][3] = 2
        grid[3][3] = 3
        self.assertEqual(ListClue(grid, 3), [0,1,2,3])
    def test_right4(self):
        grid = CreateGrid(4)
        grid[0][3] = 3
        grid[0][2] = 2
        grid[0][1] = 1
        grid[0][0] = 0
        self.assertEqual(ListClue(grid, 4), [3,2,1,0])
    def test_bottom4(self):
        grid = CreateGrid(4)
        grid[0][3] = 0
        grid[1][3] = 1
        grid[2][3] = 2
        grid[3][3] = 3
        self.assertEqual(ListClue(grid, 8), [3,2,1,0])
    def test_left4(self):
        grid = CreateGrid(4)
        grid[3][0] = 0
        grid[3][1] = 1
        grid[3][2] = 2
        grid[3][3] = 3
        self.assertEqual(ListClue(grid, 12), [0,1,2,3])
        
    def test_top5(self):
        grid = CreateGrid(5)
        grid[0][3] = 0
        grid[1][3] = 1
        grid[2][3] = 2
        grid[3][3] = 3
        grid[4][3] = 4
        self.assertEqual(ListClue(grid, 3), [0,1,2,3,4])
    def test_right5(self):
        grid = CreateGrid(5)
        grid[0][4] = 4
        grid[0][3] = 3
        grid[0][2] = 2
        grid[0][1] = 1
        grid[0][0] = 0
        self.assertEqual(ListClue(grid, 5), [4,3,2,1,0])
    def test_bottom5(self):
        grid = CreateGrid(5)
        grid[0][3] = 0
        grid[1][3] = 1
        grid[2][3] = 2
        grid[3][3] = 3
        grid[4][3] = 4
        self.assertEqual(ListClue(grid, 11), [4,3,2,1,0])
    def test_left5(self):
        grid = CreateGrid(5)
        grid[3][0] = 0
        grid[3][1] = 1
        grid[3][2] = 2
        grid[3][3] = 3
        grid[3][4] = 4
        self.assertEqual(ListClue(grid, 16), [0,1,2,3,4])

class test_YieldClue(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

class test_ClueOrders(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_4(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(ClueOrders(_DIMENSIONS, 4), [[1,2,3,4]])
    def test_3(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(ClueOrders(_DIMENSIONS, 3), [[1,2,4,3], [1,3,2,4], [1,3,4,2],
                                                     [2,1,3,4], [2,3,1,4], [2,3,4,1]])
    def test_2(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(ClueOrders(_DIMENSIONS, 2), [[1,4,2,3], [1,4,3,2],
                                                     [2,1,4,3], [2,4,1,3], [2,4,3,1],
                                                     [3,1,2,4], [3,1,4,2], [3,2,1,4], [3,2,4,1], [3,4,1,2], [3,4,2,1]])
    def test_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(ClueOrders(_DIMENSIONS, 1), [[4,1,2,3], [4,1,3,2], [4,2,1,3], [4,2,3,1], [4,3,1,2], [4,3,2,1]])
    def test_5_5(self):
        global _DIMENSIONS
        _DIMENSIONS = 5
        self.assertEqual(ClueOrders(_DIMENSIONS, 5), [[1,2,3,4,5]])
    def test_5_4(self):
        global _DIMENSIONS
        _DIMENSIONS = 5
        self.assertEqual(ClueOrders(_DIMENSIONS, 4), [[1,2,3,5,4], [1,2,4,3,5], [1,2,4,5,3], [1,3,2,4,5], [1,3,4,2,5], [1,3,4,5,2],
                                           [2,1,3,4,5], [2,3,1,4,5], [2,3,4,1,5], [2,3,4,5,1]])

class test_AllOrders(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_2(self):
        self.assertEqual(AllOrders(2), [[1,2],
                                        [2,1]])
    def test_3(self):
        self.assertEqual(AllOrders(3), [[1,2,3], [1,3,2],
                                        [2,1,3], [2,3,1],
                                        [3,1,2], [3,2,1]])
    def test_4(self):
        self.assertEqual(AllOrders(4), [[1,2,3,4], [1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2],
                                        [2,1,3,4], [2,1,4,3], [2,3,1,4], [2,3,4,1], [2,4,1,3], [2,4,3,1], 
                                        [3,1,2,4], [3,1,4,2], [3,2,1,4], [3,2,4,1], [3,4,1,2], [3,4,2,1], 
                                        [4,1,2,3], [4,1,3,2], [4,2,1,3], [4,2,3,1], [4,3,1,2], [4,3,2,1]])

class test_YieldOrders(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

class test_PruneOrders(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

class test_CollapsePossibilities(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_4_4(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(CollapsePossibilities(ClueOrders(_DIMENSIONS,4)), [[1], [2], [3], [4]])
        
    def test_4_3(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(CollapsePossibilities(ClueOrders(_DIMENSIONS,3)), [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4]])
        
    def test_4_2(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(CollapsePossibilities(ClueOrders(_DIMENSIONS,2)), [[1,2,3], [1,2,4], [1,2,3,4], [1,2,3,4]])

    def test_4_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        self.assertEqual(CollapsePossibilities(ClueOrders(_DIMENSIONS,1)), [[4], [1,2,3], [1,2,3], [1,2,3]])

class test_ComparePossibilities(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        
    def test_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        a = CollapsePossibilities(ClueOrders(_DIMENSIONS,3))
        b = CollapsePossibilities(ClueOrders(_DIMENSIONS,2))
        self.assertEqual(ComparePossibilities(a,b), [[1,2], [1,2], [1,2,3,4], [1,2,3,4]])

class test_PrunePossibilities(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_1(self):
        global _DIMENSIONS
        _DIMENSIONS = 4
        a = CollapsePossibilities(ClueOrders(_DIMENSIONS,3))
        b = CollapsePossibilities(ClueOrders(_DIMENSIONS,2))
        c = ComparePossibilities(a,b)
        self.assertEqual(PrunePossibilities(c), [[1,2], [1,2], [3,4], [3,4]])
    
class test_PrintGrid(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_4(self):
        grid = CreateGrid(4)
        clues = [0,0,1,2,0,2,0,0,0,3,0,0,0,1,0,0]
        #PrintGrid(grid, clues)
        pass

class test_CollapseResult(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
##################################################


#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
