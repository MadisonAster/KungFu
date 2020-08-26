import os, shutil
import unittest
from datetime import datetime

def PrintTree(InputPath):
    InputPath = InputPath.replace('\\','/').rstrip('/')
    result = '\n'
    for root, dirs, files in os.walk(InputPath):
        dirs.sort() #Linux listdir may not come pre-sorted
        files.sort()
        root = root.replace('\\','/') #Windows path sanitization
        indent = '    ' * (len(root.replace(InputPath, '').split('/'))-1)
        result += indent+root.rsplit('/',1)[-1]+'\n'
        for file in files:
            result += indent+'    '+file+'\n'
    print(result)
    return result

class test_PrintTree(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
        self.mock_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')+'/mock'
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
        shutil.rmtree(self.mock_path)

    def create_mock(self, mock_structure):
        for path in mock_structure:
            path = self.mock_path+path
            if '.' in path.rsplit('/',1)[-1]:
                open(path, 'a').close() #touch file
            else:
                os.makedirs(path)
    
    def test_1(self):
        self.create_mock([
            '/folder1',
            '/folder1/file1.txt',
            '/folder1/file2.txt',
            '/folder2',
            '/folder2/file1.txt',
            '/folder2/file2.txt',
            '/folder3',
        ])

        ExpectedResult = \
"""
mock
    folder1
        file1.txt
        file2.txt
    folder2
        file1.txt
        file2.txt
    folder3
"""
        self.assertEqual(PrintTree(self.mock_path), ExpectedResult)

    def test_2(self):
        self.create_mock([
            '/folder1',   
            '/folder2',   
            '/folder2/file1.txt',
            '/folder2/file2.txt',
            '/folder3',
        ])

        ExpectedResult = \
"""
mock
    folder1
    folder2
        file1.txt
        file2.txt
    folder3
"""
        self.assertEqual(PrintTree(self.mock_path), ExpectedResult)
        

if __name__ == '__main__':
    unittest.main()
