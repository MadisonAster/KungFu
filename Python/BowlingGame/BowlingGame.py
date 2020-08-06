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