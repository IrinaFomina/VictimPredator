import math
import fish


class VictimFish(fish.Fish):

    def __init__(self, x, y):
        fish.Fish.__init__(self, x, y)

    def __str__(self):
        return 'Victim\'s position in Pool is ({}, {})'.format(self.x, self.y)

    def move(self, step, sp):
        return fish.Fish.move(self, 1, sp, self.define_current_move(step, sp))

    def has_been_eaten(self, victims):
        print('Victim ', self, ' has been eaten!')
        try:
            victims.remove(self)
        except ValueError:
            pass
