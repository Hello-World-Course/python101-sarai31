# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
# name = input("Hello, whats your name")
# #Check if the name length is greater than "dani"
# if len(name) > len("dani"):
#     board_size = int(input(f"{name}, please choose board size"))
#     # Check if board size is greater than 9
#     if board_size > 9:
#         print(f"{name}, the board size {board_size} is greater than 9.")
#     else:
#         # If the board size is 9 or less, continue asking for the number of number_of_mines
#         number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
#         print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")

# else:
#     print(f"{name}, your name has fewer or equal characters than 'dani'.")

#define variables
name = None
board_size = None
number_of_mines = None

# Player name
name_input = input("Hello, whats your name")
if len(name_input) < 3:
    print("Your name is too short")
    exit()
else:
    name = name_input

    # Board size
    board_size_input = input(f"{name}, please choose board size")
    try:
        board_size = int(board_size_input)  # Try to convert to integer
        if board_size == 0:
            print(f"{name}, you have entered illegal board size")
            board_size = None  # Set to None if board size is 0
        elif board_size < 0:
            print(f"{name}, you have entered illegal board size")
            board_size = None  # Set to None if board size is negative
        elif board_size >= 26:  # Check for too large board sizes
            print(f"{name}, you have entered an illegal board size")
            board_size = None  # Set to None if board size is too large
    except ValueError:
        print(f"{name}, you have entered an illegal board size")
        board_size = None  # Set to None in case of invalid input

    # Check if board_size is valid before asking for number of mines
    if board_size is not None:  # Continue only if board_size is valid
        # Number of mines input
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
        try:
            number_of_mines = int(number_of_mines_input)  # Try to convert to integer
            if number_of_mines <= 0 or number_of_mines >= (board_size * board_size) // 2:
                print(f"{name}, you have entered illegal number of mines")
                number_of_mines = None  # Set to None if number of mines is invalid
        except ValueError:
            print(f"{name}, you have entered illegal number of mines")
            number_of_mines = None  # Set to None in case of invalid input

print(f"name = {name}")
print(f"board_size = {board_size}")
print(f"number_of_mines = {number_of_mines}")

