import unittest
from datetime import datetime
import math
import copy

def Dijkstras(Matrix):
    Points = sorted(list(set(list(''.join(Matrix.keys())))))
    Visited = []
    print('Points', Points)
    

    #Result = {p: (math.inf, None) for p in Points} 
    
    Shortest = [math.inf] * len(Points)
    Previous = [None] * len(Points)
    
    p = Points[0]
    Shortest[0] = 0
    Previous[0] = ''

    #for i, p in enumerate(Points):
    while len(Matrix.keys()) > 0:
        print('p', p, Matrix.keys())
        for L in reversed(list(Matrix.keys())):
            if p in L:
                print('p', p)
                print('L', L)
                print('Matrix[L]', Matrix[L])
                p2 = L.replace(p, '')
                i = Points.index(p2)
                if p == Points[0]:
                    Shortest[i] = Matrix[L]
                    Previous[i] = p
                else:
                    s = Matrix[L]
                    v = p2
                    while v not in ['', None]:
                        j = Points.index(v)
                        s += Shortest[j]
                        v = Previous[j]
                    if s < Shortest[i]:
                        Shortest[i] = Matrix[L]
                        Previous[i] = p                
                del Matrix[L]
        else:
            Visited.append(p)
            newshortest = math.inf
            for l, q in enumerate(list(set(Points) - set(Visited))):
                if l == 0:
                    p = q
                k = Points.index(q)
                if Shortest[k] < newshortest:
                    newshortest = Shortest[k]
                    p = q
    return list(zip(Points, Shortest, Previous))


class test_Dijkstras(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        self.assertEqual(
            Dijkstras({
                'AB': 6,
                'AD': 1,
                'BC': 5,
                'BD': 2,
                'BE': 2,
                'CE': 5,
                'DE': 1,
            }), 
            [
                ('A', 0, ''),
                ('B', 3, 'D'),
                ('C', 7, 'E'),
                ('D', 1, 'A'),
                ('E', 2, 'D'),
            ]
        )

if __name__ == '__main__':
    unittest.main()