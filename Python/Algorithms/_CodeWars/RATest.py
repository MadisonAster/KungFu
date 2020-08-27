import os, shutil
import unittest
from datetime import datetime


def calculator(operator, tape):
    def add(a,b, tape=tape):
        c = a+b
        result = str(a)+'+'+str(b)+'='+str(c)
        tape.append(result)
        return result
    def subtract(a,b, tape=tape):
        c = a-b
        result = str(a)+'-'+str(b)+'='+str(c)
        tape.append(result)
        return result
    def divide(a,b, tape=tape):
        c = a/b
        result = str(a)+'/'+str(b)+'='+str(c)
        tape.append(result)
        return result
    def multiply(a,b, tape=tape):
        c = a*b
        result = str(a)+'*'+str(b)+'='+str(c)
        tape.append(result)
        return result
    operator_map = {
        '+' : add,
        '-' : subtract,
        '/' : divide,
        '*' : multiply,
    }
    return operator_map[operator]
class test_calculator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()

    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        tape = []

        func1 = calculator('+', tape)
        self.assertEqual(func1(10,20), '10+20=30')

        func2 = calculator('-', tape)
        self.assertEqual(func2(4,6), '4-6=-2')
        self.assertEqual(func2(8,3), '8-3=5')
        self.assertEqual(tape, ['10+20=30', '4-6=-2', '8-3=5'])


def decorator(left, right):
    return None
class test_decorator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        self.assertEqual(decorator(None, None), None)


def words(filepath):
    with open(filepath, 'r') as file:
        filetext = file.read()
    buffer = ''
    for a in filetext:
        if a.isalpha():
            buffer += a
        else:
            if buffer != '':
                yield buffer
            buffer = ''
class test_words(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
        self.mock_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')+'/mock.txt'

    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
        os.remove(self.mock_path)

    def test_1(self):
        mocktext = 'abcde abcde/abcde-abcde,abcde1abcde'
        with open(self.mock_path, 'w') as file:
            file.write(mocktext)
        self.assertEqual(list(words(self.mock_path)), ['abcde']*5)



def find(nums, target):
    ibuffer = []
    def recurse_find(nums, ibuffer=None):
        for i, a in enumerate(nums):
            ibuffer.append(i)
            if type(a) == list:
                for b in recurse_find(a, ibuffer=ibuffer):
                    yield b
            else:
                yield a
            ibuffer.pop(-1)
    for val in recurse_find(nums, ibuffer=ibuffer):
        if val == target:
            return ibuffer
class test_find(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        nums = [0, 42, [300, [], 200, [[101]]], 1000, 200]
        expected = [2, 3, 0, 0]
        self.assertEqual(find(nums, 101), expected)

        target = nums
        for i in expected:
            target = target[i]
        self.assertEqual(target, 101)


def mult(left, right):
    return None
class test_mult(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        self.assertEqual(mult(None, None), None)


if __name__ == '__main__':
    unittest.main()
