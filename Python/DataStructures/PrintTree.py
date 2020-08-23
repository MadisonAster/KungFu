import os, shutil
import unittest
from datetime import datetime

def PrintTree(InputPath):
    InputPath = InputPath.replace('\\','/').rstrip('/')
    result = ''
    for root, dirs, files in os.walk(InputPath):
        dirs.sort()
        files.sort()
        indent = '    ' * (len(root.replace(InputPath, '').split('/'))-1)
        result += indent+root.rsplit('/',1)[-1]+'\n'
        for file in files:
            result += indent+'    '+file+'\n'
    print(result)
    return result

class test_PrintTree(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
        self.FolderPath = os.path.dirname(os.path.abspath(__file__))
        self.create_mock1()
        self.create_mock2()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
        
        shutil.rmtree(self.mock1path)
        shutil.rmtree(self.mock2path)
    def create_mock1(self):
        self.mock1path = self.FolderPath+'/mock1'
        self.mock1 = [
            self.mock1path+'/folder1',
            self.mock1path+'/folder1/file1.txt',
            self.mock1path+'/folder1/file2.txt',
            self.mock1path+'/folder2',
            self.mock1path+'/folder2/file1.txt',
            self.mock1path+'/folder2/file2.txt',
            self.mock1path+'/folder3',
        ]
        for path in self.mock1:
            if '.' in path.rsplit('/',1)[-1]:
                os.mknod(path)
            else:
                os.makedirs(path)
    def create_mock2(self):
        self.mock2path = self.FolderPath+'/mock2'
        self.mock2 = [
            self.mock2path+'/folder1',   
            self.mock2path+'/folder2',   
            self.mock2path+'/folder2/file1.txt',
            self.mock2path+'/folder2/file2.txt',
            self.mock2path+'/folder3',   
        ]
        for path in self.mock2:
            if '.' in path.rsplit('/',1)[-1]:
                os.mknod(path)
            else:
                os.makedirs(path)
    
    def test_1(self):
        ExpectedResult = """mock1
    folder1
        file1.txt
        file2.txt
    folder2
        file1.txt
        file2.txt
    folder3
"""
        self.assertEqual(PrintTree(self.mock1path), ExpectedResult)
        
    def test_2(self):
        ExpectedResult = """mock2
    folder1
    folder2
        file1.txt
        file2.txt
    folder3
"""
        self.assertEqual(PrintTree(self.mock2path), ExpectedResult)

if __name__ == '__main__':
    unittest.main()
