#Imports##########################################
from FooFinder import KungFu
import random
from collections import OrderedDict
##################################################

#Test#############################################
class test_LRUCache(KungFu.TimedTest):
    '''
    def test_1(self):
        cache = LRUCache(2)
        #print(cache.put(1, 1))
        #print(cache.put(2, 2))
        self.assertEqual(cache.get(1), 1)
        #print(cache.put(3, 3))
        self.assertEqual(cache.get(2), -1)
        #print(cache.put(4, 4))
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_2(self):
        cache = LRUCache(2)
        #print(cache.put(2, 1))
        #print(cache.put(1, 1))
        #print(cache.put(2, 3))
        #print(cache.put(4, 1))
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 3)

    def test_3(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(2), -1)
        #print(cache.put(2, 6))
        self.assertEqual(cache.get(1), -1)
        #print(cache.put(1, 5))
        #print(cache.put(1, 2))
        self.assertEqual(cache.get(1), 2)
        self.assertEqual(cache.get(2), 6)
    '''
##################################################

#Code#############################################
class LRUCache(object):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key not in self.cache.keys():
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
    
    def put(self, key, value):
        if key not in self.cache.keys():
            while len(self.cache.keys()) > self.capacity-1:
                self.cache.pop(self.cache.keys()[0])
        else:
            self.cache.pop(key)
        self.cache[key] = value
        return self.cache
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
