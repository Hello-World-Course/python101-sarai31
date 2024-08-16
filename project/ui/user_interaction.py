# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE

name = input("Hello, whats your name")
#Check if the name length is greater than "dani"
if len(name) > len("dani"):
    board_size = int(input(f"{name}, please choose board size"))
    # Check if board size is greater than 9
    if board_size > 9:
        print(f"{name}, the board size {board_size} is greater than 9.")
    else:
        # If the board size is 9 or less, continue asking for the number of number_of_mines
        number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
        print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")

# else:
#     print(f"{name}, your name has fewer or equal characters than 'dani'.")
