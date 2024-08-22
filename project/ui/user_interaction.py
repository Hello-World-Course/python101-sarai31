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

# Define variables
name = None
board_size = None
number_of_mines = None

# Player name
name_input = input("Hello, what's your name ")
if len(name_input) < 3:
    print("Your name is too short")
else:
    name = name_input

    # Board size
    board_size_input = input(f"{name}, please choose board size: ")
    try:
        board_size = int(board_size_input)
        if board_size == 0:
            print("Board size cannot be zero")
            board_size = None  # Explicitly set to None if board size is invalid
        elif board_size < 0:
            print("Board size cannot be negative")
            board_size = None
        elif board_size >= 26:  # Check for too large board sizes
            raise ValueError
    except ValueError:
        print(f"{name}, you have entered an illegal board size")
        board_size = None  # Set to None in case of an exception

    # If board_size is None, return None (terminate the process)
    if board_size is None:
        print("Invalid board size, returning None")
    else:
        # Number of mines input
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")
        try:
            number_of_mines = int(number_of_mines_input)
            if number_of_mines <= 0:
                print("Number of mines must be greater than zero")
                number_of_mines = None
            elif number_of_mines >= (board_size * board_size) // 2:  # Limit number of mines
                raise ValueError
        except ValueError:
            print(f"{name}, you have entered an illegal number of mines")
            number_of_mines = None

        # If number_of_mines is None, return None
        if number_of_mines is None:
            print("Invalid number of mines, returning None")

# Output the results
print(f"name = {name}")
print(f"board_size = {board_size}")
print(f"number_of_mines = {number_of_mines}")

