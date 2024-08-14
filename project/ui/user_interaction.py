# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name = input("Hello, whats your name")

#Check if the name length is greater than "dani"
if len(name) > len("dani"):
    b_size = int(input(f"{name}, please choose board size\ninput:> "))

    # Check if board size is greater than 9
    if b_size > 9:
        print(f"{name}, the board size {b_size} is greater than 9.")
    else:
        # If the board size is 9 or less, continue asking for the number of mines
        mines = int(input(f"{name}, for board size {b_size}, choose number of mines to allocate\ninput:> "))
        print(f"{name}, the board size is: {b_size}, number of mines is: {mines}. ENJOY!")

else:
    print(f"{name}, your name has fewer or equal characters than 'dani'.")



#
# print(f"{name}, the board size is: {b_size}, number of mines is: anfkja")
#
#
# Hello, whats your name
# input:> dani
# dani, please choose board size
# input:> 9
# dani, for board size 9, choose number of mines to allocate
# input:> 7
# dani, the board size is: 9, number of mines is: 7. ENJOY!