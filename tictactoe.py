# tictactoe.py

import numpy as np 
import display
import random

def main():
    # Stores all possible sizes for the tic tac toe board
    sizes = [3,4,5,6,7]
    
    # Prints the board size options for the user
    print("1: 3 X 3")
    print("\n")
    print("2: 4 X 4")
    print("\n")
    print("3: 5 X 5")
    print("\n")
    print("4: 6 X 6")
    print("\n")
    print("5: 7 X 7")
    print("\n")

    # Asks for user input on board size
    size_choice = 0
    print("Choose size of tic tac toe board:")
    print("\n")
    size_choice = input()

    # If statement handles invalid user inputs
    if (int(size_choice) < 1) or (int(size_choice) > 5):
        size_choice = 1

    # Sets size of 2D array
    size = 0
    size = sizes[int(size_choice) - 1]
    state = np.zeros((size,size))

    # Create instance of board display
    board = display.Display(size)

    #Print an empty board to start game
    # winner is false
    # X is player 1 and 2 is computer 
    board.print_board(state)
    winner = False
    player = 1
    computer = 2

    # While there is no winner yet
    # Keep playing the game
    while winner == False:
        # Ask user for the row and column of their move
        row = 0
        column = 0
        print("Enter row and then column coordinate to make a move")
        print("\n")
        row, column = input().split(" ")

        print ("Going to check if valid move")
        # Check if user input is a valid move
        if(validMove(row, column, state, size) == False):
            print("Move invalid! Try another location...")
            print("\n")
            continue

        # Update the state of the board
        # Print the newly updated board
        (state)[int(row)][int(column)] = 1
        board.print_board(state)

        # Check if the most recent move creates a win for the human player
        if (checkWinner(row, column, state, size, player)):
            print("Player " + str(player) + " Wins!")
            print("\n")
            winner = True
            continue

        # Check for tie
        count = 0
        for i in range(size):
            for j in range(size):
                if (state[i][j] != 0):
                    count = count + 1

        if (count == (size * size)):
            print("Tie! No winner!")
            print("\n")
            break

        # Let computer make a random move
        # Checks if computer wins
        if (computerMove(state, size, computer, board)):
            print("Computer Wins!")
            print("\n")
            winner = True
            continue

        # Check for tie
        count = 0
        for i in range(size):
            for j in range(size):
                if (state[i][j] != 0):
                    count = count + 1

        if (count == (size * size)):
            print("Tie! No winner!")
            print("\n")
            break

    return 0

# This function checks if the player input is even a valid move
def validMove(row, col, state, size):
    # If the location is out of bounds
    if int(row) > (size - 1):
        return False

    if int(col) > (size - 1):
        return False 

    # If the location is already taken
    if ((state)[int(row)][int(col)] != 0):
        return False

    return True

# This function handles the computer making a move
# Also handles checking if computer wins games
def computerMove(state, size, player, board):
    row = 0
    col = 0

    # Get a random number for row
    ran = random.randrange(0, size)
    row = ran

    # Get a random number for col
    ran = random.randrange(0, size)
    col = ran

    while validMove(row, col, state, size) == False:
        # Get a random number for row
        ran = random.randrange(0, size)
        row = ran
        print(row)

        # Get a random number for col
        ran = random.randrange(0, size)
        col = ran
        print(col)

    # Update the state of the board
    # Print the newly updated board
    print("Computer moves to (" + str(row) + ", " + str(col) + ")")
    print("\n")
    (state)[int(row)][int(col)] = 2
    board.print_board(state)

    # Check and return if computer wins
    return checkWinner(row, col, state, size, player)

# This function checks if most recent move results in a win
def checkWinner(row, col, state, size, player):
    
    # Check horizontal win
    count = 0

    # Check right side of the column
    temp_col = col
    while (int(temp_col) + 1) <= (size - 1):
        temp_col = int(temp_col) + 1
        if (state)[int(row)][int(temp_col)] == player:
            count = count + 1

    # Check left side of the column
    temp_col = col
    while (int(temp_col) - 1 >= 0):
        temp_col = int(temp_col) - 1
        if ((state)[int(row)][int(temp_col)] == player):
            count = count + 1

    # Reset temp_col
    temp_col = col

    # Increment count by one to also count the most recent move
    count = count + 1

    # If a row is all filled out then player is the winner
    if (count == size):
        return True

    # Check vertical win
    count = 0

    # Check above the row
    temp_row = row
    while (int(temp_row) - 1 >= 0):
        temp_row = int(temp_row) - 1
        if ((state)[int(temp_row)][int(col)] == player):
            count = count + 1

    # Check bottom of the row
    temp_row = row
    while (int(temp_row) + 1 <= size - 1):
        temp_row = int(temp_row) + 1
        if ((state)[int(temp_row)][int(col)] == player):
            count = count + 1

    # Reset temp_row
    temp_row = row

    # Increment count by one to also count the most recent move
    count = count + 1

    # If a column is all filled out then player is the winner
    if (count == size):
        return True

    # Check diagnol win
    count = 0

    # heck bottom right
    temp_row = row
    temp_col = col
    while ((int(temp_col) + 1 <= size - 1) and (int(temp_row) + 1 <= size - 1)):
        temp_col = int(temp_col) + 1
        temp_row = int(temp_row) + 1
        if ((state)[int(temp_row)][int(temp_col)] == player):
            count = count + 1

    # Check top left
    temp_row = row
    temp_col = col
    while ((int(temp_col) - 1 >= 0) and (int(temp_row) - 1 >= 0)):
        temp_col = int(temp_col) - 1
        temp_row = int(temp_row) - 1
        if ((state)[int(temp_row)][int(temp_col)] == player):
            count = count + 1

    # Reset temp_row and temp_col
    temp_row = row
    temp_col = col

    # Increment count by one to also count the most recent move
    count = count + 1

    # If a diagnol is all filled out then player is the winner
    if (count == size):
        return True

    # Check SECOND diagnol win
    count = 0

    # Check bottom left
    temp_row = row
    temp_col = col
    while ((int(temp_col) - 1 >= 0) and (int(temp_row) + 1 <= size - 1)):
        temp_col = int(temp_col) - 1
        temp_row = int(temp_row) + 1
        if ((state)[int(temp_row)][int(temp_col)] == player):
            count = count + 1

    # Check upper right
    temp_row = row
    temp_col = col
    while ((int(temp_col) + 1 <= size - 1) and (int(temp_row) - 1 >= 0)):
        temp_col = int(temp_col) + 1
        temp_row = int(temp_row) - 1
        if ((state)[int(temp_row)][int(temp_col)] == player):
            count = count + 1

    # Reset temp_row and temp_col
    temp_row = row
    temp_col = col

    # Increment count by one to also count the most recent move
    count = count + 1

    # If a diagnol is all filled out then player is the winner
    if (count == size):
        return True
    
    # If no winner then return false
    return False

main()