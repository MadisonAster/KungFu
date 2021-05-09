#Imports##########################################
from FooFinder import KungFu
import random
##################################################

#Test#############################################
class test_BinarySearch(KungFu.TimedTest):

    def test_1(self):
        Array = list(range(100000))
        self.assertEqual(BinarySearch(Array, Array[-1]), len(Array)-1)

    def test_std(self):
        Array = list(range(100000))
        self.assertEqual(Array.index(Array[-1]), len(Array)-1)
##################################################

#Code#############################################
def BinarySearch(Array, n, low=0, high=None):
    if high == None:
        high = len(Array)-1
    if high >= low:
        mid = low + (high - low) // 2
        if Array[mid] == n:
            return mid
        elif Array[mid] > n:
            return BinarySearch(Array, n, low=low, high=mid-1)
        else:
            return BinarySearch(Array, n, low=mid+1, high=high)
    else:
        return -1
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
