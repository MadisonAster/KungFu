import os
import unittest
from datetime import datetime


def WordIterator(filepath):
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
class test_WordIterator(unittest.TestCase):
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
        self.assertEqual(list(WordIterator(self.mock_path)), ['abcde']*5)


if __name__ == '__main__':
    unittest.main()
