# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: DID I WIN TIC-TAC-TOE?
#
# NAME:         Julio Arias
# ASSIGNMENT:   Technical HW: Arrays & Maps

# takes a player character and a 2-dimensional
# array as parameters and returns whether the
# player won the game
# HINT: What does a boolean accumulator look like?

def print_2D_board(b):
  for i in range(len(b)):
    print(b[i])

    
def did_I_win_2D(player, board):
  #Make sure the board is the correct size:
  gaps =0
  for i in range(len(board)): #column
    for x in range(len(board[i])):
      gaps+=1
  if gaps != 9: 
    return False
    
  has_won = False

  #checks wins down
  for i in range(len(board)): #column
    down_win = True
    for x in range(len(board[i])): #row
        down_win &= player == board[i][x]
    print ("\t", i, down_win, 'or', has_won)
    has_won |= down_win #has_won = has_won or down_win

  #win across    
  for i in range(len(board)): #column
    left_win = True
    for x in range(len(board[i])): #row
    
        left_win &= player == board[x][i]
    print ("\t", i, left_win, 'or', has_won)
    has_won |= left_win #has_won = has_won or down_win
  
  #win diagonal
    if(board[0][0])==player and board[1][1] == player and board[2][2] == player:
     has_won = True
    if(board[0][2])==player and board[1][1] == player and board[2][0] == player:
      has_won = True
  
  return has_won


def main():
    boards = [ [["X", "O", "O"]] * 3, \
               [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]], \
               [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']], \
               [["O", "O", "X"]] * 3 ]
    for b in boards:
        print_2D_board(b)
        print("X won?", did_I_win_2D("X", b))
        print("O won?", did_I_win_2D("O", b))

# Don't run main on import
if __name__ == "__main__":
    main()
    main()