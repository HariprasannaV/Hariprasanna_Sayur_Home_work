"""
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial.
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A.

Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions
"""
import random

try:
    # Get input for the number of rows, columns, and maximum points
    rows = int(input("No. of Rows    : "))
    columns = int(input("No. of Columns : "))
    max_points = int(input("Maximum Points : "))

    # Initialize the game board with '*' in each cell
    board = []
    for i in range(rows):
        i_th_row = []
        for j in range(columns):
            i_th_row.append("*")
        board.append(i_th_row)

    # print(board)

    # Function to print the current state of the board
    def printing_board(li):
        for i in li:
            for j in i:
                print(j, end=" ")
            print("")
        print("\n\n\n")

    # Print the initial state of the board
    printing_board(board)

    # Initialize points for Player A and Player B
    a_points = 0
    b_points = 0

    # main game loop
    while True:
        # Check if either player has reached the maximum points
        if (a_points >= max_points) or (b_points >= max_points):
            # Determine the winner or declare a draw
            if a_points > b_points:
                print("A Wins")
            elif b_points > a_points:
                print("B Wins")
            else:
                print("Match Draw")
            break

        # Player A's turn
        print("Player A Turn")

        # rolling a die for row and column selection
        die_rolling = input("Press Enter to Roll The Die : ")
        row_a = random.randint(1, rows)
        print(row_a)

        die_rolling2 = input("Press Enter to Roll The Die : ")
        col_a = random.randint(1, columns)
        print(col_a)

        # Check the selected cell on the board and update points accordingly
        if board[(row_a - 1)][col_a - 1] != "B":
            board[(row_a - 1)][col_a - 1] = "A"

        elif board[(row_a - 1)][col_a - 1] == "B":
            board[(row_a - 1)][col_a - 1] = "A"
            a_points += 1

        # Print the updated board
        printing_board(board)

        # Player B's turn
        print("Player B Turn")

        # rolling a die for row and column selection for Player B
        die_rolling3 = input("Press Enter to Roll The Die : ")
        row_b = random.randint(1, rows)
        print(row_b)

        die_rolling4 = input("Press Enter to Roll The Die : ")
        col_b = random.randint(1, columns)
        print(col_b)

        # Check the selected cell on the board and update points accordingly for Player B
        if board[(row_b - 1)][col_b - 1] != "A":
            board[(row_b - 1)][col_b - 1] = "B"

        elif board[(row_b - 1)][col_b - 1] == "A":
            board[(row_b - 1)][col_b - 1] = "B"
            b_points += 1

        # Print the updated board
        printing_board(board)

        # Print the current points for both players
        print(f"Points of Player A : {a_points}\nPoints of Player B : {b_points}\n______________________________\n\n\n")

except:
    # Handle invalid data type input
    print("Invalid data type")
