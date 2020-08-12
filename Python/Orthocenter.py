import unittest
from datetime import datetime
from fractions import Fraction

def OrthoCenter(A, B, C):
    ### m = (y2-y1) / (x2-x1) ###
    Em = Fraction((B[1] - A[1]), (B[0] - A[0]))
    Fm = Fraction((C[1] - B[1]), (C[0] - B[0]))
    #Gm = Fraction((A[1] - C[1]), (A[0] - C[0]))

    ### b = y - mx ###
    #Eb = B[1] - Em*B[0]
    #Fb = C[1] - Fm*C[0]
    #Gb = A[1] - Gm*A[0]

    ### y = mx + b ###
    #B[1] = Em*B[0] + Eb
    #C[1] = Fm*C[0] + Fb
    #A[1] = Gm*A[0] + Gb

    ### reciporacal = -1 / m ###
    Tm = Fraction(-1, Em)
    Um = Fraction(-1, Fm)
    #Vm = Fraction(-1 / Gm)

    ### b = y - mx ###
    Tb = C[1] - Tm*C[0]
    Ub = A[1] - Um*A[0]
    #Vb = B[1] - Vm*B[0]

    ### y = mx + b ###
    #C[1] = Tm*C[0] + Tb
    #A[1] = Um*A[0] + Ub
    #B[1] = Vm*B[0] + Vb

    ### mx + b = mx + b ###
    #Tm*x + Tb = Um*x + Ub
    #(Tm*x - Um*x) / (Tm - Um) = (Ub - Tb) / (Tm - Um)
    x = Fraction((Ub - Tb), (Tm - Um))

    ### y = mx + b ###
    y = Tm*x + Tb

    return [float(x), float(y)]

class test_OrthoCenter(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        self.assertEqual(OrthoCenter([3,9],[1,3],[10,2]), [2.5, 4.5])

if __name__ == '__main__':
    unittest.main()
