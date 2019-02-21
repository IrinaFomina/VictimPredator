import math


class SwimmingPool:

    def __init__(self, size):
        self.size = size;

    def get_closest_fish(self, predator, victims):
        max_distance = 0
        if len(victims) > 0:
            target_fish = victims[0]
            for victim_fish in victims:
                distance = math.sqrt(
                    (predator.x - victim_fish.x) * (predator.x - victim_fish.x) + (predator.y - victim_fish.y) * (
                                predator.y - victim_fish.y))
                if max_distance < distance:
                    max_distance = distance
                    target_fish = victim_fish
            return target_fish
        else:
            print ('There are no victim fishes left!')
