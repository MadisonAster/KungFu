#Imports##########################################
from FooFinder import KungFu
import random
##################################################

#Test#############################################
class test_LinearSearch(KungFu.TimedTest):

    def test_1(self):
        Array = list(reversed(range(100000)))
        Array[len(Array)-1] = -5
        self.assertEqual(LinearSearch(Array, -5), len(Array)-1)

    def test_2(self):
        Array = list(range(100000))
        random.shuffle(Array)
        Array[len(Array)-1] = -5
        self.assertEqual(LinearSearch(Array, -5), len(Array)-1)

    def test_3(self):
        Array = list(range(100000))
        random.shuffle(Array)
        Array[500] = -5
        self.assertEqual(LinearSearch(Array, -5), 500)

    def test_std(self):
        Array = list(range(100000))
        random.shuffle(Array)
        Array[len(Array)-1] = -5
        self.assertEqual(Array.index(-5), len(Array)-1)
##################################################

#Code#############################################
def LinearSearch(Array, n):
    for i, m in enumerate(Array):
        if m == n:
            return i
    else:
        return -1
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
