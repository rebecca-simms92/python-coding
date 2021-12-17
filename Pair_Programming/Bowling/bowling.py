import random

class bowling():
    def __init__(self, num_of_frame = 10):
        self.num_of_frame = num_of_frame
        self.score = 0

    def roll(self, pins_left):
        num = random.randint(0, 10)
        pins_left -= num
        return num, max(0, pins_left)


    def frame(self, roll = 2):
        frame_score_current = 0
        pins_left = 10
        while roll != 0 and pins_left > 0:
            (score, pins_left) = self.roll(pins_left)
            roll -= 1
            frame_score_current += score
        print('Start rolling...')
        print('SCORE: ', frame_score_current)
        print('ROLL', roll)
        print('PINS', pins_left)
        return frame_score_current


def play():
    game = bowling()
    total_score = 0
    frame = game.num_of_frame
    while frame != 0:
        frame_score_current = game.frame()
        frame -= 1
        total_score += frame_score_current
        print('Frame: ', frame, '; Score:', total_score)
    print('Total score: ', total_score)

if __name__ == '__main__':
    play()
