import random 
board = [x for x in range(1,10)]
print(board)

def drawBoard(board):
    for row in range (3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row*3]}   |   {board[(row*3)+1]}   |   {board[(row*3)+2]}   |")
    print("+-------+-------+-------+")

drawBoard(board)

def computer (compChoice):
    while True:
        boardNumber = random.randint(1,9)
        if isInstance(board[boardNumber], int):
            break
        else:
                continue
    board[boardNumber] = option
    drawBoard(board)

def player(playerChoice):
    while True:
        try:
            boardNumber = int(input("Enter the board number you want to play into: "))
            if isInstance(board[boardNumber], int):
                break
            else:
                print("The board number have been used, choose another one")
                continue 
        except valueError:
            print("Invalid input, enter a number")
        except:
            print("Try again")
    board[boardNumber] = playerChoice
    drawBoard(board)

def freeFields():
    free = []
    for field in board:
        if not isInstance(field, int):
            free.append(field)
        else:
            continue
    return free

def winner(board, playerChoice, compChoice):
    def decision(const):
        if board[const] == playerChoice:
            print("You won !!!")
        else:
            print("You lose")
    if (board[0] == board[1] and board[0] == board[2]) or (board[0] == board[3] and board[0] == board[6]) or (board[0] == board[4] and board[0] == board[8]):
        decision(0)
    elif board[3] == board[4] and board[3] == board[5]:
        decision(3)
    elif board[6] == board[7] and board[6] == board[8]:
        decision(6)
    elif board[1] == board[4] and board[1] == board[7]:
        decision(1)
    elif (board[2] == board[5] and board[2] == board[8]) or (board[2] == board(4) and board[2] == board[6]):
        decision(2)

