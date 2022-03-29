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
  for i in range(3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
      return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
      return True
  return False


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
