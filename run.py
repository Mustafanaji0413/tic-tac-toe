
"""
tic tac toe board
[
    [x, -, -,],
    [-, -, -,],
    [-, -, -,]
]

user_input -> something between 1-9
if they input somthing else say: Wrong input, try again!
check if the user input has already been taken
add it to the board
check if somone won: check rows, colums and diagonals
jump between users after each correct move
"""

    
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user = True # when boolian is true it refers to user X, otherwise user O
turns = 0

def print_board(board):
    """
    Print game board
    """
    for row in board:
        for slot in row:
            print(f"{slot}  ", end="")
        print()

def quit(user_input):
     """
    Allow user to quit the game
    """
    if user_input.lower() == "q":
        print("Thank you for playing!")
        return True
    else: return False

def check_input(user_input):
    """
    Check if user input is a number
    """
    if not isnum(user_input): return False
    user_input = int(user_input)
    if not bounds(user_input): return False
    return True

def isnum(user_input):
    """
    Check if user input is a number
    """
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True
def bounds(user_input):
    """
    check if the number inserted is between the number 1-9
    """
    if user_input > 9 or user_input < 1:
        print("This number is not in range")
        return False
    else: return True    

def istaken(coords, board):
    """
    check if the psotion is already occupied
    """
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This posotion is already taken, try again.")
        return True
    else: return False    


def coordinates(user_input):
    """
    enter the cordinates of the board positons
    """
    row = int(user_input / 3)
    col = user_input 
    if col > 2: col = int(col % 3)
    return (row,col)

def add_to_board(coords, board, active_user):
    """
    add the user input to the board 
    """
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    """
    check who is the current winner
    """
    if user: return "x"
    else: return "o"

def iswin(user, board):
    """
    check to see if anyone has won through rowm col or diag
    """
    if check_row(user, board): return True
    if check_col(user, board): return True 
    if check_diag(user, board): return True
    return False

def check_row(user, board):
    """
    check to see if anyone has won through row
    """
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board):
    """
    check to see if anyone has won through col
    """
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False
        
def check_diag(user, board):
    """
    check to see if anyone has won through diag
    """
    #from top left to bottom right 
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
    #from top right bottom left
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False


while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please choose a position 1 through 9 or enter \"q\" to quit: \n")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again!")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again!")
        continue
    add_to_board(coords,board, active_user)
    if iswin(active_user, board):
       print(f"{active_user.upper()} Won!")
       break
    turns += 1
    if turns == 9: print("It's a draw -_-")
    user = not user