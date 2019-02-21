from random import randint
class Fish:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def define_current_move(self, step, sp):
        possible_moves = [[-step, step], [0, step], [step, step], [step, 0], [step, -step], [0, -step], [-step, -step],
                          [-step, 0]]
        print(len(possible_moves))
        current_move = possible_moves[randint(0, len(possible_moves) - 1)]
        # print("current_move ", current_move)
        return current_move

    def move(self, step, sp, current_move):
        try:
            self.x = self.x + current_move[0]
            self.y = self.y + current_move[1]
        except TypeError:
            print('No current_move defined')

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > sp.size:
            self.x = sp.size
        if self.y > sp.size:
            self.y = sp.size

        return self.x, self.y
