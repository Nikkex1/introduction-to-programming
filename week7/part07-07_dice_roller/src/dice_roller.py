# Write your solution here
import random

#Roll any of the three dice
def roll(die: str):
    dice = {"A": [3,3,3,3,3,6], "B": [2,2,2,5,5,5], "C": [1,4,4,4,4,4]}
    dice_roll = random.sample(dice[die], 1)
    return dice_roll[0] #dice_roll is a list, [0] returns the value

def play(die1: str, die2: str, times: int):
    die1_score = 0
    die2_score = 0
    ties = 0
    for rolls in range(times):
        x1 = roll(die1)
        x2 = roll(die2)
        if x1 > x2:
            die1_score += 1
        elif x2 > x1:
            die2_score += 1
        elif x1 == x2:
            ties += 1

    results_tuple = (die1_score, die2_score, ties)
    return results_tuple

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "B", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)