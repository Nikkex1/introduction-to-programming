# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if y not in range(0,3) or x not in range(0,3):
        return False
    elif game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [['O', '', ''], ['X', '', 'O'], ['X', 'O', 'X']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)