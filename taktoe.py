def tiktoe_board(board):
    for i , row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):                #
            row_str += value
            if j != len(row) - 1:
                row_str += " | "

        print(row_str)
        if i !=len(board) -1:
            print ("-----------")

def get_move(turn, board):
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))

        if row < 1 or row > len(board):
            print("Invalid row, try again.")
        elif col < 1 or col > len(board[row - 1]):
            print("Invalid column, try again.")
        elif board[row - 1 ][col-1] != " ":
            print("Already taken, try again")
        else:
            break
    board[row -1][col - 1] = turn

def check_win(board , turn):
    lines = [
             [(0 ,0), (0,1), (0,2)], 
             [(1 ,0), (1,1), (1,2)],
             [(2 ,0), (2,1), (2,2)],
             [(0 ,0), (1,0), (2,0)],
             [(0 ,1), (1,1), (2,1)],
             [(0 ,2), (1,2), (2,2)],
             [(0 ,0), (1,1), (2,2)],
             [(0 ,2), (1,1), (2,0)]
             ]
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break

        if win:
            return True



board =[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = "X"
turn_number = 0

tiktoe_board(board)

while True:
    print("It is the", turn, "player turn.Please select your move.")

    get_move(turn , board)
    tiktoe_board(board)

    if check_win(board , turn):
      print("The winner was", turn)
      break
    turn_number +=1

    if turn_number == 9:
        print("\nTied Game...")
        break
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
   

    




    