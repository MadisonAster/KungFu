import TestKit

class Game():
    def __init__(self):
        self.rolls = []
    def roll(self, pins):
        self.rolls.append(pins)
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

class BowlingGameTest(TestKit.TimedTest):
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