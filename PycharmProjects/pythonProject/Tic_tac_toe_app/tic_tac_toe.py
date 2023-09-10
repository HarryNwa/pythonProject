from tic_tac_toe_assistance import draw_board
import os
cells = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5",
         6 : "6", 7 : "7", 8 : "8", 9 : "9"}

play = True

while play:
    os.system("cls" if os.name == "nt" else "clear")
    draw_board(cells)
    player_choice = input()
    if player_choice == "o":
        play = False