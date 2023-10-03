from tic_tac_toe_assistance import draw_board, check_turn, check_for_win

cells = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5",
         6 : "6", 7 : "7", 8 : "8", 9 : "9"}

play = True
finish = False
turn = 0
previous = -1

while play:

    draw_board(cells)
    if previous == turn:
        print("Invalid cell chosen, please pick another one.")
    previous = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your cell or press o to quit")
    player_choice = input()
    if player_choice == "O":
        play = False
    elif str.isdigit(player_choice) and int(player_choice) in cells:
        if not cells[int(player_choice)] in {"x", "o"}:
            turn += 1
            cells[int(player_choice)] = check_turn(turn)

    if check_for_win(cells): play, finish = False, True
    if turn > 8: play = False

draw_board(cells)

if finish:
    if check_turn(turn) == "X":
        print("First player wins!")
    else:
        print("Second player wins")
else:
    print("No winner!")

print("Thanks for playing TIC-TAC-TOE. Hope you enjoyed it.")