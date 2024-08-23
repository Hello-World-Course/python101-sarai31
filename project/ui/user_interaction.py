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
# name = None
# board_size = None
# number_of_mines = None
#
# # Player name
# name_input = input("Hello, whats your name")
# if len(name_input) < 3:
#     print("Your name is too short")
# else:
#     name = name_input
#
#     # Board size
#     board_size_input = input(f"{name}, please choose board size")
#     try:
#         board_size = int(board_size_input)  # Try to convert to integer
#         if board_size == 0:
#             print(f"{name}, you have entered illegal board size")
#             board_size = None
#         elif board_size < 0:
#             print(f"{name}, you have entered illegal board size")
#             board_size = None
#         elif board_size >= 26:  # Check for too large board sizes
#             print(f"{name}, you have entered an illegal board size")
#             board_size = None
#     except ValueError:
#         print(f"{name}, you have entered an illegal board size")
#
#     # Check if board_size is valid before asking for number of mines
#     if board_size is not None:  # Continue only if board_size is valid
#         # Number of mines input
#         number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
#         try:
#             number_of_mines = int(number_of_mines_input)  # Try to convert to integer
#             if number_of_mines <= 0 or number_of_mines >= (board_size * board_size) // 2:
#                 print(f"{name}, you have entered illegal number of mines")
#                 number_of_mines = None
#         except ValueError:
#             print(f"{name}, you have entered illegal number of mines")
#             number_of_mines = None

def is_name_valid(name):
    return len(name) > 2

# will print False:
# print(is_name_valid("Mi"))

def is_board_size_valid(board_size):
    return 0 < board_size < 26
# will print False:
# print(is_board_size_valid(-1))

def is_number_of_mines_valid(board_size, number_of_mines):
    max_mines = (board_size * board_size) // 2
    return 1 <= number_of_mines <= max_mines


def register_user():
    # get account/name
    name = input("Hello, whats your name?")
    if not is_name_valid(name):
        print("Your name is too short")
        return None, None, None

    # get bord size
    board_size_input = input(f"{name}, please choose board size: ")
    try:
        board_size = int(board_size_input)
    except ValueError:
        print(f"{name}, you have entered illegal board size")
        return None, None, None

    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return None, None, None

    # get mines input
    number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
    try:
        number_of_mines = int(number_of_mines_input)
    except ValueError:
        print(f"{name}, you have entered illegal number of mines")
        return None, None, None

    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return None, None, None

    # return value
    return name, board_size, number_of_mines

user_name, user_board_size, user_num_mines = register_user()
print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")
