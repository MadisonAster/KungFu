#Standard Imports#################################
import unittest
##################################################

#Test#############################################
class test_next_bigger(unittest.TestCase):
    def test_1(self):
        self.assertEqual(next_bigger(9827410), 9840127)
        self.assertEqual(next_bigger(4444444), -1)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(2710), 7012)
##################################################

#Code#############################################
def next_bigger(n):
    if str(n) == ''.join(list(reversed(sorted(str(n))))):
        return -1

    stored = ""
    for a, b in zip(str(n), reversed(sorted(str(n)))):
        if a == b:
            stored += b
        else:
            break
    rightslice = str(n)[len(stored):]

    for i, a in reversed(list(enumerate(rightslice[:-1]))):
        if a < rightslice[i+1]:
            target = a
            targetindex = i
            break

    left = rightslice[:targetindex]
    right = sorted(rightslice[targetindex+1:])
    for i, a in enumerate(right):
        if a > target:
            replacement = a
            right[i] = target
            break
    right = ''.join(sorted(right))

    return int(stored + left + replacement + right)
##################################################

#Main#############################################
if __name__ == '__main__':
    unittest.main()
##################################################
