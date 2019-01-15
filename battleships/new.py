from random import randint

board = []
ships = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    s = " "
    print(s.join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)
""" 
  Test
"""
def guess():
  if guess_row == ship_row and guess_col == ship_col:
    return 0
  else:
    if guess_row not in range(5) or \
       guess_col not in range(5):
      return 1
    elif(board[guess_row][guess_col] == "X"):
      return 2
    else:
      return 3

for turn in range(4):
  
  print(turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  code = guess()

  if code == 0:
    print("Congratulations! You sunk my battleship!")
    break
  elif code == 1:
    print("Oops, that's not even in the ocean.")
  elif code == 2:
    print("You guessed that one already.")  
  elif code == 3:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"

  print_board(board)
