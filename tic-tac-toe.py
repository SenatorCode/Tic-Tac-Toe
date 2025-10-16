import random
import os

board = [x for x in range(1,10)]

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawBoard(board):
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row*3]}   |   {board[row*3+1]}   |   {board[row*3+2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def computer (compChoice):
    while True:
        boardNumber = random.randint(0,8)
        if isinstance(board[boardNumber], int):
            break
        else:
            continue
    board[boardNumber] = compChoice
    clearScreen()
    print(f"Computer played at position {boardNumber + 1}")
    print()
    drawBoard(board)

def player(playerChoice):
    while True:
        try:
            boardNumber = int(input("Enter the board number you want to play into (1-9): "))
            if isinstance(board[boardNumber - 1], int):
                break
            elif boardNumber < 1 or boardNumber > 9:
                print("Enter number within the range 1-9!!!")
            else:
                print("The board number has been used, choose another one")
                continue 
        except ValueError:
            print("Invalid input, enter a number")
        except:
            print("Try again")
    board[boardNumber - 1] = playerChoice
    clearScreen()
    print(f"You played at position {boardNumber}")
    print()
    drawBoard(board)

def freeFields():
    free = []
    for field in board:
        if isinstance(field, int):
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
        return False

    if (board[0] == board[1] and board[0] == board[2]) or (board[0] == board[3] and board[0] == board[6]) or (board[0] == board[4] and board[0] == board[8]):
        return decision(0)
    elif board[3] == board[4] and board[3] == board[5]:
        return decision(3)
    elif board[6] == board[7] and board[6] == board[8]:
        return decision(6)
    elif board[1] == board[4] and board[1] == board[7]:
        return decision(1)
    elif (board[2] == board[5] and board[2] == board[8]) or (board[2] == board[4] and board[2] == board[6]):
        return decision(2)
    else:
        if len(freeFields()) == 1:
            print("There is no winner ")
            return False
        else:
            return True
        
    

def playGame():
    global board
    board = [x for x in range(1,10)]
    clearScreen()
    print("Welcome to the Tic-Tac-Toe arena")
    computerChoice = ""
    playerChoice = input("What option would you like to play as, \"X\" or \"O\": ")
    if playerChoice.lower() == "x":
        computerChoice = "O"
    else:
        computerChoice = "X"
    input("Press Enter to start the game....")
    clearScreen()
    nextRound = [1, True]
    while nextRound[0] < 5 and nextRound[1] == True:
        computer(computerChoice)
        nextRound[1] = winner(board, playerChoice, computerChoice)
        if nextRound[1] == True:
            input("It is your turn, press enter to continue....")
            clearScreen()
            drawBoard(board)
        else:
            clearScreen()
            break
        player(playerChoice)
        nextRound[1] = winner(board, playerChoice, computerChoice)
        nextRound[0] +=1
        if nextRound[1] == True:
            clearScreen()
    
    while True:
        replay = input("Do you want to play again?, Y/N: ")
        if replay.upper() == "Y":
            playGame()
            break
        elif replay.upper() == "N":
            input("Thank you for playing, press enter to quit ....")
            break
        else:
            print("Invalid input")

playGame()