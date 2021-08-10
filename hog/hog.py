""" Functions from the Hog assignment of 'Composing Programs'. """
from random import randint, triangular

# goalscore is the score needed to win the game
goal_score = 50


def six_sided():
    """Simulate one roll of a fair six-sided die.

    Returns the simulated result of rolling a six-sided die.
    """
    return randint(1, 6)


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the dice exactly num_rolls > 0 times.

    Parameters :
        num_rolls (int) : The number of dice rolls that will be made.
        dice (int) : A function that simulates the result of a single dice roll.

    Return :
    the sum of the rolls unless any of the rolls is 1. In that case, return 1.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    dice_roll_one = False
    sum_rolls = 0
    for i in range(num_rolls):
        score = dice()
        if score == 1:
            dice_roll_one = True
        elif score != 1:
            sum_rolls += score
    if dice_roll_one:
        return 1
    return sum_rolls


if __name__ == '__main__':
    # Interactively roll the dice until you reach the goal score.
    print(f"""
    Simulate rolling of dice.  Each turn you can roll 1 or more dice.
    You get the sum of the dice values, except if ANY of the dice roll
    a 1 then you get 1 for that turn.
    Try to achieve {goal_score} points in the fewest number of turns.
    """)
    total_score = 0
    n = 0
    while total_score < goal_score:
        print("Your score is", total_score)
        num_dice = input("How many dice to roll? ")
        num_dice = int(num_dice)
        score = roll_dice(num_dice)
        total_score += score
        n += 1
        print("You rolled", score)
    # reached the goal score
    print(f"Game over! you scored {total_score} in {n} rolls.")
