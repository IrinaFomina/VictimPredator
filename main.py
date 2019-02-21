import swimming_pool
import predator_fish
import victim_fish

from random import randint
victims = []
predators = []

victims_population = 5
predators_population = 3

iteration = 30
predator_step = 2

victim_step = 1
i = j = k = 0

sp = swimming_pool.SwimmingPool(5)

print('Victims:')
while i < victims_population:
    victim = victim_fish.VictimFish(randint(0, sp.size - 1), randint(0, sp.size - 1))
    victims.append(victim)
    print(victims[i].x, victims[i].y)
    i += 1

print('Predators:')
while j < predators_population:
    predator = predator_fish.PredatorFish(randint(0, sp.size - 1), randint(0, sp.size - 1))
    predators.append(predator)
    print(predators[j].x, predators[j].y)
    j += 1

# Main loop

while k < iteration:
    for predator in predators:
        print('**** for predator in predators ****')
        closest_victim = sp.get_closest_fish(predator, victims)
        predator.move(predator_step, sp, predator.move_to_closest_fish(victim, predator_step, sp))
        if predator.x == victim.x and predator.y == victim.y:
            victim.has_been_eaten(victims)

    for predator in predators:
        print(predator)
    for victim in victims:
        print(victim)
    if len(victims) == 0:
        print('Moddeling has been finished. All victims are eaten')
        break
    else:
        print(len(victims), 'victims and', len(predators), 'predators has left')
    k+=1