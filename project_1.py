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