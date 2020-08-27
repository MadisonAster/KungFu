import unittest
import random
from datetime import datetime


def QuickSort(Array,low = 0,high = None):
    if high == None:
        high = len(Array)-1

    def partition(Array,low,high): 
        rmark = random.randint(low,high)
        Array[low], Array[rmark] = Array[rmark], Array[low] #Solve for worst case scenario

        i = low-1
        pivot = Array[high] #pivot
        for j in range(low , high):   
            if Array[j] < pivot:           
                i = i+1 
                Array[i],Array[j] = Array[j],Array[i] 
        Array[i+1],Array[high] = Array[high],Array[i+1] 
        return i+1
    
    if low < high:
        pi = partition(Array,low,high)
        QuickSort(Array, low=low, high=pi-1)
        QuickSort(Array, low=pi+1, high=high)
    return Array

class test_QuickSort(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(reversed(range(100000)))
        self.assertEqual(QuickSort(Array), list(range(100000)))

    def test_2(self):
        Array = list(range(100000))
        random.shuffle(Array)
        self.assertEqual(QuickSort(Array), list(range(100000)))

    def test_std_sort(self):
        Array = list(range(100000))
        random.shuffle(Array)
        self.assertEqual(sorted(Array), list(range(100000)))


if __name__ == '__main__':
    unittest.main()
