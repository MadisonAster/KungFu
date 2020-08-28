import unittest
from datetime import datetime

def TapeCalculator(operator, tape):
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
class test_TapeCalculator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()

    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        tape = []

        func1 = TapeCalculator('+', tape)
        self.assertEqual(func1(10,20), '10+20=30')

        func2 = TapeCalculator('-', tape)
        self.assertEqual(func2(4,6), '4-6=-2')
        self.assertEqual(func2(8,3), '8-3=5')
        self.assertEqual(tape, ['10+20=30', '4-6=-2', '8-3=5'])


if __name__ == '__main__':
    unittest.main()
