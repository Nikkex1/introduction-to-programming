# Write your solution here
def who_won(game_board: list):
    score1 = 0
    score2 = 0
    for row in game_board:
        for element in row:
            if element == 1:
                score1 += 1
            elif element == 2:
                score2 += 1

    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    example = [[0,1,2],[1,2,2],[1,1,0]]
    print(who_won(example))