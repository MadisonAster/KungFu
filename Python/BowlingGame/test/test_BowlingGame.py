import unittest
from datetime import datetime

import BowlingGame

class TimedTest(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
        self.game = BowlingGame.Game()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
        
class BowlingGameTest(TimedTest):
    #def setUp(self):
    #    print('\nsetUp')
    #    self.game = BowlingGame.Game()
        
    #def tearDown(self):
    #    print('tearDown')
        
        
        
        
    def rollMany(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)
    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)
    def rollStrike(self):
        self.game.roll(10)
        
        
        
        
        
        
    def test_GutterGame(self):
        self.rollMany(20, 0)
        self.assertEqual(self.game.score(), 0)
    def test_AllOnes(self):
        self.rollMany(20, 1)
        self.assertEqual(self.game.score(), 20)
    def test_OneSpare(self):
        self.rollSpare()
        self.game.roll(3)
        self.rollMany(17,0)
        self.assertEqual(self.game.score(), 16)
    def test_OneStrike(self):
        self.rollStrike()
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(16,0)
        self.assertEqual(self.game.score(), 24)
    def test_AllSpares(self):
        self.rollMany(21, 5)
        self.assertEqual(self.game.score(), 150)
    def test_PerfectGame(self):
        for i in range(12):
            self.rollStrike()
        self.assertEqual(self.game.score(), 300)
    def test_OneLastSpare(self):
        self.rollMany(19, 0)
        self.game.roll(10)
        #self.game.roll(5)
        self.assertEqual(self.game.score(), 10)

if __name__ == '__main__':
    unittest.main()