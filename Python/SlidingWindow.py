import unittest
from datetime import datetime
import itertools

def SlidingWindow(InputArray, k):
	iterator = iter(InputArray)
	result = tuple(itertools.islice(iterator, k))
	if len(result) == k:
		yield result
	for n in iterator:
		result = result[1:] + (n,)
		yield result

class test_SlidingWindow(unittest.TestCase):
	def setUp(self):
		self.starttime = datetime.now()
	def tearDown(self):
		t = datetime.now() - self.starttime
		print(str(t), self.id())

	def test_1(self):
		A = [0,1,2,3,4,5,6,7,8,9]
		result = list(SlidingWindow(A,2))
		print(result)

		self.assertEqual(SlidingWindow(A,2), [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)])

if __name__ == '__main__':
	unittest.main()
