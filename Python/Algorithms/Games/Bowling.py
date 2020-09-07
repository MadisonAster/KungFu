#Standard Imports#################################
import sys, os, unittest
from importlib import machinery
import subprocess, shlex
##################################################

#Relative Imports#################################
if 'KungFu' not in sys.modules.keys(): #Relative import handling for testing individual modules that rely on base classes
    sys.modules['KungFu'] = machinery.SourceFileLoader('KungFu', os.path.dirname(os.path.abspath(__file__)).replace('\\','/').rsplit('/',3)[0]+'/KungFu.py').load_module()
import KungFu
##################################################

#Test#############################################
class test_Bowling(KungFu.TimedTest):
    def test_GutterGame(self):
        game = Bowling()
        game.rollMany(20, 0)
        self.assertEqual(game.score(), 0)
    
    def test_AllOnes(self):
        game = Bowling()
        game.rollMany(20, 1)
        self.assertEqual(game.score(), 20)
    
    def test_OneSpare(self):
        game = Bowling()
        game.rollSpare()
        game.roll(3)
        game.rollMany(17,0)
        self.assertEqual(game.score(), 16)
    
    def test_OneStrike(self):
        game = Bowling()
        game.rollStrike()
        game.roll(3)
        game.roll(4)
        game.rollMany(16,0)
        self.assertEqual(game.score(), 24)

    def test_AllSpares(self):
        game = Bowling()
        game.rollMany(21, 5)
        self.assertEqual(game.score(), 150)

    def test_PerfectGame(self):
        game = Bowling()
        for i in range(12):
            game.rollStrike()
        self.assertEqual(game.score(), 300)

    def test_OneLastSpare(self):
        game = Bowling()
        game.rollMany(19, 0)
        game.roll(10)
        game.rollMany(2, 0)
        self.assertEqual(game.score(), 10)
##################################################

#Code#############################################
class Bowling():
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def rollMany(self, rolls, pins):
        for i in range(rolls):
            self.roll(pins)

    def rollSpare(self):
        self.roll(5)
        self.roll(5)

    def rollStrike(self):
        self.roll(10)

    def isStrike(self, roll):
        ball0 = self.rolls[roll+0]
        return ball0 == 10

    def isSpare(self, roll):
        ball0 = self.rolls[roll+0]
        ball1 = self.rolls[roll+1]
        return (ball0 + ball1) == 10
        
    def scoreFrame(self, roll):
        ball0 = self.rolls[roll+0]
        ball1 = self.rolls[roll+1]
        return (ball0 + ball1)

    def scoreExtra(self, roll):
        ball2 = self.rolls[roll+2]
        return ball2

    def score(self):
        roll, score = 0, 0
        for frame in range(10):
            score += self.scoreFrame(roll)
            if self.isStrike(roll) or self.isSpare(roll):
                score += self.scoreExtra(roll)
            if self.isStrike(roll):
                roll += 1
            else:
                roll += 2
        return score
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################