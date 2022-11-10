# tic tac toe

"""
tic tac toe board
[
    [-, -, -,],
    [-, -, -,],
    [-, -, -,]
]

user_input -> somthing between 1-9
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

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}  ", end="")
        print()
             
print_board(board)

def quit(user_input):
    if user_input == "q": 
        print("Thank you for playing!")
        return True
    else: return False

def check_input(user_input):
    # check if its a number
    if not isnum(user_input): return False
    #check if its the number 1-9
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True


while True:
    print_board(board)
    user_input = input("Please choose a position 1 through 9 or enter \"q\" to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again!")
        continue