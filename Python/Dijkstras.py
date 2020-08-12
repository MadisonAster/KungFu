import unittest
from datetime import datetime
import math
import copy

def Dijkstras(Matrix):
    Points = sorted(list(set(list(''.join(Matrix.keys())))))
    Visited = []
    Shortest = [math.inf] * len(Points)
    Previous = [None] * len(Points)
    p = Points[0]
    Shortest[0] = 0
    Previous[0] = ''

    while len(Matrix.keys()) > 0:
        for L in reversed(list(Matrix.keys())):
            if p in L: #Calculate any line segment where p is a point.
                p2 = L.replace(p, '')
                i = Points.index(p)
                j = Points.index(p2)
                if p == Points[0]:
                    Shortest[j] = Matrix[L]
                    Previous[j] = p
                else:
                    if Shortest[i]+Matrix[L] < Shortest[j]:
                        Previous[j] = p
                        Shortest[j] = Shortest[i]+Matrix[L]
                del Matrix[L]
        else: #Find next closest entry to try all neighbors on.
            Visited.append(p)
            newshortest = math.inf
            for l, q in enumerate(list(set(Points[1:]) - set(Visited))):
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