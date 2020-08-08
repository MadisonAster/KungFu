import unittest

'''
def last_digit_func(lst):
    mapping = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    if lst == []: #taken from OP
        return 1
    last_digit = lst[0] % 10
    if 0 in lst[1:]: #edge case 0 as a power
        return 1
    if last_digit == 0: #edge case 0 at start
        return last_digit

    for current_power in lst[1:]:
        if len(mapping[last_digit]) == 1:
            return last_digit
        ind = current_power % len(mapping[last_digit])
        ind -= 1 #zero indexing, but powers start from 1. 
        last_digit = mapping[last_digit][ind]
    return last_digit

def last_digit(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            out = n**out
            if out > 2:
                out -= 2
                out %= 4
                out += 2
    return lst[0] ** out % 10
'''

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

class test_last_digt(unittest.TestCase):
    def test_1(self):
        print("---start test 1---")
        self.assertEqual(last_digit([5, 20]), 5)
        print("---start test 2---")
        self.assertEqual(last_digit([3, 4, 2]), 1)
        print("---start test 3---")
        self.assertEqual(last_digit([12, 30, 21]), 6)
        print("---start test 4---")
        self.assertEqual(last_digit([7, 6, 21]), 1)
        print("---start test 5---")
        self.assertEqual(last_digit([123232,694022,140249]), 6)

if __name__ == '__main__':
    unittest.main()