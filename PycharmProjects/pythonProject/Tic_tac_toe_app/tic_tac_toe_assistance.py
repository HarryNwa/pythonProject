def draw_board(cells):

    play_board = (f"|{cells[1]}|{cells[2]}|{cells[3]}|\n"
                  f"|{cells[4]}|{cells[5]}|{cells[6]}|\n"
                  f"|{cells[7]}|{cells[8]}|{cells[9]}|")
    print(play_board)


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_for_win(cells):
    if (cells[1] == cells[2] == cells[3]) \
            or (cells[4] == cells[5] == cells[6]) \
            or (cells[7] == cells[8] == cells[9]):
        return True

    elif (cells[1] == cells[4] == cells[7]) \
            or (cells[2] == cells[5] == cells[8]) \
            or (cells[3] == cells[6] == cells[9]):
        return True

    elif (cells[1] == cells[5] == cells[9]) \
            or (cells[3] == cells[5] == cells[7]):
        return True

    else:
        return False
