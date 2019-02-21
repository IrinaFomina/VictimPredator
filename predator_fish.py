import fish
import swimming_pool
class PredatorFish(fish.Fish):

    def __init__(self, x, y):
        fish.Fish.__init__(self, x, y)

    def __str__(self):
        return 'Predator\'s position in Pool is ({}, {})'.format(self.x, self.y)

    def move(self, step, sp, current_move):
        fish.Fish.move(self, step, sp, current_move)

    def move_to_closest_fish(self, victim, step, sp):
        x_direction = (victim.x - self.x) * step
        if x_direction < -step:
            x_direction = -step
        if x_direction > step:
            x_direction = step

        y_direction = (victim.y - self.y) * step
        if y_direction < -step:
            y_direction = -step
        if y_direction > step:
            y_direction = step

        current_move = [x_direction, y_direction]
        self.move(step, sp, current_move)
