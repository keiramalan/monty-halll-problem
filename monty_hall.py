##
# monty_hall.py
# Monty Hall Problem - testing probabilities
# 3 doors, two with goats one with a car
# annika munro

import random


def randomize_prizes():
    """ Creates a dictionary with 3 values assigned with booleans
    to randomise the prizes behind each door"""

    car = True
    goat_1 = False
    goat_2 = False
    prize_list = [car, goat_1, goat_2]

    # shuffle list to ensure random outcome
    random.shuffle(prize_list)

    set_doors = {1: prize_list[0], 2: prize_list[1], 3: prize_list[2]}

    return set_doors


def stay():
    """Monty Hall problem when player chooses to stick with the same door"""

    set_doors = randomize_prizes()

    choice_list = [1, 2, 3]
    choice = random.randint(1, 3)

    choice_list.remove(choice)  # So Monty can remove a door with a goat

    # Take away a door
    print("The door you have chosen is: {}".format(choice))

    if set_doors[choice_list[0]] is False:
        print("Door {} has a goat".format(choice_list[0]))
        print("Your choice is still Door {}".format(choice))

    else:
        print("Door {} has a goat".format(choice_list[1]))
        print("Your choice is still Door {}".format(choice))

    # Check what prize has been won
    if set_doors[choice] is True:
        return True

    else:
        return False


def switch():
    """Monty Hall problem when the player chooses to switch doors"""

    set_doors = randomize_prizes()

    choice_list = [1, 2, 3]
    choice = random.randint(1, 3)

    choice_list.remove(choice)  # So Monty can remove a door with a goat

    # Take away a door
    print("The door you have chosen is: {}".format(choice))

    if set_doors[choice_list[0]] is False:
        print("Door {} has a goat".format(choice_list[0]))
        choice = choice_list[1]
        print("Your choice has been switched to door {}"
              .format(choice_list[1]))

    else:
        print("Door {} has a goat".format(choice_list[1]))
        choice = choice_list[0]
        print("Your choice has been switched to door {}"
              .format(choice_list[0]))

    # Check what prize has been won
    if set_doors[choice] is True:
        return True

    else:
        return False


def switch_or_stay():
    """Pick whether to calculate percentage of wins for either switching
    doors or sticking with your original choice"""

    win_count = []

    switch_or_stay = input("Switch doors or stay? ").strip().lower()

    if switch_or_stay == 'stay':
        for i in range(10):
            prize = stay()

            if prize is True:
                print("Congrats on your new car!")
                win_count.append("car")

            else:
                print("Your goat collection has a new member :)")
                win_count.append("goat")

    elif switch_or_stay == 'switch':
        for i in range(10):
            prize = switch()

            if prize is True:
                print("Congrats on your new car!")
                win_count.append("car")

            else:
                print("Your goat collection has a new member :)")
                win_count.append("goat")

    else:
        print("Enter 'stay' or 'switch' please")

    return win_count


def main():
    win_count = switch_or_stay()
    car_count = 0
    goat_count = 0

    for prize in win_count:
        if prize == 'car':
            car_count += 1

        else:
            goat_count += 1

    # Calculates percentage chance of winning a car
    car_chance = car_count / len(win_count) * 100

    # calculates percentage chance of winning a goat
    goat_chance = goat_count / len(win_count) * 100

    print("The chance of winning a car this time was {}%".format(car_chance))
    print("The chance of winning a goat this time was {}%".format(goat_chance))


main()
