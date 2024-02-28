print("Enter k:")
k = int(input())
print("Enter n:")
n = int(input())
board = [[0 for i in range(k**2)] for j in range(k**2)]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

d = len(str(n))
def print_board():
    for i in range(k ** 2):
        for j in range(k ** 2):
            if board[i][j] == 0:
                print('|' + ' '*d, end='')
            else:
                print(f'|{board[i][j]:{d}d}', end='')
        print('|')
def make_move(mv):
    box,pos,new = mv
    new_col = (box % k) * k + (pos % k)
    new_row = (box // k) * k + (pos // k)
    previous = board[new_row][new_col]
    board[new_row][new_col] = new
    return previous
def verify_board():
    # check rows
    for row in range(k**2):
        total = 0
        for num in board[row]:
            total += num
        if total > n:
            return -1
        if total < n:
            return 0
    # check columns
    for col in range(k**2):
        total = 0
        for i in range(k**2):
            total += board[i][col]
        if total > n:
            return -1
        if total < n:
            return 0
    # check boxes
    for box in range(k**2):
        total = 0
        start_row = (box // k) * k
        start_col = (box % k) * k
        for row in range(k):
            for col in range(k):
                total += board[start_row + row][start_col + col]
        if total > n:
            return -1
        if total < n:
            return 0
    return 1


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print_board()
print("Next Move:")
command = ""
while command != "end":
    usr_inp = input().split()
    command = usr_inp[0]
    if command == "move":
        move = int(usr_inp[1]), int(usr_inp[2]), int(usr_inp[3])
        prev_val = make_move(move)
        result = verify_board()
        # If not valid move, undo the move
        if -1 == result:
            move = move[0], move[1], prev_val
            make_move(move)
            print_board()
            print("Your move was invalid, please try again:")
        # If the board wins, end the game
        elif 1 == result:
            print_board()
            print("Congratulations! You have solved the puzzle!")
            break
        else:
            print_board()
            print("Next Move:")




