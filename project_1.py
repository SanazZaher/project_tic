import random

# Step 1: Evaluate the board
board = "--------------------"

def evaluate(board):
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" in board:
        return ""
    elif "-" not in board:
        return "!"

print("Step 1: Board Evaluation")
print(evaluate(board))

# Step 2: Move function
def move(board, mark, position):
    new_board = board[:position] + mark + board[position:]
    return new_board

# Validation for correct position
position = int(input("Enter your position number: "))
if 0 <= position <= 19:
    mark = input("Enter mark (x or o): ")
    valid_marks = ["x", "o"]

    #checking if the position is empty and mark is correct

    if mark in valid_marks and board[position] == "-":
        board = move(board, mark, position)
        print("Step 2: Player's Move")
        print(board)
    elif mark not in valid_marks:
        print("Invalid mark. You can choose 'x' or 'o'.")
    else:
        print("Invalid position. This number has been chosen before or is out of bounds.")
else:
    print("Invalid position. Choose a number between 0 and 19.")



# Step 3: Player's Move
print("Step 3: Player's Move")

def player_move(board, mark):
    while True:
        player_position = int(input("Enter your position number (between 0-19):"))

        if 0 <= player_position <= 19 and board[player_position] == "-":
            new_board = move(board, mark, player_position)
            return new_board
        elif player_position < 0:
            print("Your position number has to be a positive number.")
        elif player_position > 19:
            print("Your number has to be between 0 and 19.")
        else:
            print("Invalid position, this number has been chosen before.")

board = player_move(board, mark)
print(board)

# Step 4: Computer's Move
def pc_move(board, mark):
    while True:
        pc_position = random.randint(0, 19)
        #computer marks where there is an empty space
        if board[pc_position] == "-":
            new_board = move(board, mark, pc_position)
            return new_board
        #checking if the place is occupide before
        else:
            print("This position has been taken before. ")

# choosing the computer's mark based on the player's mark. if player has chosen x, then computes mark is o...
computer_mark = "o" if mark == "x" else "x"
board = pc_move(board, computer_mark)
print(board)



import random

# Step 1: Evaluate the board

def evaluate(board):
    if "xxx" in board: # x is the winner
        return "x"
    elif "ooo" in board: # o is the winner
        return "o"
    elif "-" in board: # there are spaces in the game, continue
        return "-"
    elif "-" not in board: # there are no space, draw
        return "!"


# Step 2: Move function
def move(board, mark, position):
    new_board = board[:position] + mark + board[position + 1:]
    return new_board

# Step 3: Player's Move

def player_move(board, mark):

    while True: # running the loop until i get the correct answer

        player_position = int(input("Enter your position number (between 0-19):")) # asking for the player to choose a position in the board

        if 0 <= player_position <= 19 and board[player_position] == "-": # checking if the input is between 0 to 19 and if the selected position is an empty space

            board = move(board, mark, player_position)
            print(board)
            return board

        elif player_position < 0: # for the condition of negative numbers
            print("Your position number has to be a positive number.")
        elif player_position > 19: #cfor the condition of numbers higher than 19
            print("Your number has to be between 0 and 19.")
        else:
            print("Invalid position, this number has been chosen before.") # for the condition of the position being chosen in an occupied position


# Step 4: pc Move
def pc_move(board, mark):

    while True: # running the loop
        pc_position = random.randint(0, 19) # random position betweeen 0 to 19

        if board[pc_position] == "-": #computer marks where there is an empty space
            board= move(board, mark, pc_position)
            print(board)
            return board

        else: # if the position is occupied send this
            print("This position has been taken before. ")




# Step 5

def play_1D_tictactoe():
    board = "--------------------"

    while True:
        board = player_move(board, "x") # calling the player move function to run the player move with x mark
        board = pc_move(board, "o") #calling the pc move function to mark player move
        game_status = evaluate(board) # evaluating the board

        if game_status == "x" or game_status == "o":
            print(" you won!")
            break
        elif game_status == "!":
            print("It's a draw!")
            break

    print(board)

# Call the game function to start playing
play_1D_tictactoe()
