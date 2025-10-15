board = [x for x in range(1,10)]
print(board)

def drawBoard(board):
    for row in range (3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row*3]}   |   {board[(row*3)+1]}   |   {board[(row*3)+2]}   |")
    print("+-------+-------+-------+")

drawBoard(board)