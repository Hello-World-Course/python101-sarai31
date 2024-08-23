# def is_name_valid(name):
#     return len(name) > 2
#
# # will print False:
# # print(is_name_valid("Mi"))
#
# def is_board_size_valid(board_size):
#     return 0 < board_size < 26
# # will print False:
# # print(is_board_size_valid(-1))
#
# def is_number_of_mines_valid(board_size, number_of_mines):
#     max_mines = (board_size * board_size) // 2
#     return 1 <= number_of_mines <= max_mines
#
# def register_user():
#     # get account/name
#     name = input("Hello, whats your name?")
#     if not is_name_valid(name):
#         print("Your name is too short")
#         return None, None, None
#
#     # get bord size
#     board_size_input = input(f"{name}, please choose board size: ")
#     try:
#         board_size = int(board_size_input)
#     except ValueError:
#         print(f"{name}, you have entered illegal board size")
#         return None, None, None
#
#     if not is_board_size_valid(board_size):
#         print(f"{name}, you have entered illegal board size")
#         return None, None, None
#
#     # get mines input
#     number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
#     try:
#         number_of_mines = int(number_of_mines_input)
#     except ValueError:
#         print(f"{name}, you have entered illegal number of mines")
#         return None, None, None
#
#     if not is_number_of_mines_valid(board_size, number_of_mines):
#         print(f"{name}, you have entered illegal number of mines")
#         return None, None, None
#
#     # return value
#     return name, board_size, number_of_mines

# user_name, user_board_size, user_num_mines = register_user()
# print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")

def parse_cmd(command):
    # split space
    parts = command.split()

    #
    cmd_name = parts[0]  # command name
    params = parts[1:]  # paramters

    return cmd_name, params

# command, parameters = parse_cmd("test_command a b c d e")
# # will print 'test_command'
# print(command)
# # will print ['a', 'b', 'c', 'd', 'e']
# print(parameters)
# # will print 'c'
# print(parameters[2])

def is_on_board(x, y, board):
    # Check if x and y are within the bounds of the board
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    return False

board_test = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# will print True
print(is_on_board(0, 2, board_test))

def safe_set_value(x, y, value, board):
    # בדיקה אם הקורדינטות חוקיות באמצעות is_on_board
    if is_on_board(x, y, board):
        # הצבת הערך בלוח
        board[x][y] = value
        return True
    return False

board_test = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# # True - legal
# print(is_on_board(0, 2, board_test))
#
# # False - Coordinates out of bounds
# print(is_on_board(0, 3, board_test))
#
# # False - Coordinates out of bounds
# print(is_on_board(4, 2, board_test))
