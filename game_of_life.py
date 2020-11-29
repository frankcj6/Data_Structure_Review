#  bit manipulation google interview
def game_of_life(board):
    m = len(board)
    n = len(board[0])
    for i in range(0,m):
        for j in range(0,n):
            count = 0
            for row, column in ((i-1, j),(i+1, j),
                                (i, j+1), (i, j-1),
                                (i-1, j-1), (i-1, j+1),
                                (i+1, j-1), (i+1, j+1)):
                if 0<= row<m and 0<=column<n:
                    if board[row][column]&1:
                        count += 1
            if board[i][j] == 1:
                if count<2 or count>3:
                    continue
                else:
                    board[i][j] |= 2
            else:
                if count == 3:
                    board[i][j] |= 2

    for i in range(0,m):
        for j in range(0,n):
            board[i][j] = board[i][j]>>1

    return board

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(game_of_life(board))

