# print('hello')  # sanity check


# User Stories
# AAU I want to see a welcome message when I start: Lets play Py-Pac-Poe! DONE
# AAU before being prompted a move, I want to see the board printed out in the console so i know what moves are available
# AAU I want to be prompted with which players turn
# AAU I want to be prompted on how to enter a valid move so i dont make mistakes 
# example: Player X's move (example move: B2)
# AAU I want to be able to enter my moves column letter in upper or lower case as a move
# AAU if i enter a move in invalid format or select an occupied cell, i want a message to try again and prompts again
# AAU end of game i want to see who won or a tie

# Ice Box
# enter players names
# automatically alternate between players

# Py-Pac-Poe Begin

# print("------------------------\nLet's Play Py-Pac-Poe!!!\n------------------------")

# enter players names here (maybe) 



# Variables
  # this will have the board as a dictionary
  # also the turn variable

board = {}
turn = 'O'
x_win = 0
o_win = 0
move = None
choice_list = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
welcome = "------------------------\nLet's Play Py-Pac-Poe!!!\n------------------------"

# Game Init
  # this will have the board
  # who's starting turn
  # display starting game msg

def init():
  print(welcome)
  global board, turn
  board = {
    'a1': ' ', 'b1': ' ', 'c1': ' ',
    'a2': ' ', 'b2': ' ', 'c2': ' ',
    'a3': ' ', 'b3': ' ', 'c3': ' '
  }

  # print(f"\nIt is Player {turn}'s turn!") # maybe move this print

# init()

# Change Turns
  # this will change the turn variable

def change_turns():
  global turn
  turn = 'X' if turn == 'O' else 'O'
  print(f"\nIt is Player {turn}'s turn!")

# Display Board
  # displays game board
def display_board():
  global board
  board_display = f'''
      A   B   C 
  1)  {board['a1']} | {board['b1']} | {board['c1']} 
     -----------
  2)  {board['a2']} | {board['b2']} | {board['c2']} 
     -----------
  3)  {board['a3']} | {board['b3']} | {board['c3']} 
  '''

  print(board_display)

# display_board(board)

# Get Move
  # this will get the players move

def get_move():
  # global turn # might not need since we aren't modifying it
  global move
  move = input(f"Player {turn}, please select a move: ").lower()
  # return move

# Check Move
  # checks if the move is valid

def check_move():
  global board, move, choice_list
  # choice_list = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
  if move in choice_list:
    return True
  else: 
    print('not a valid move')
    # get_move()
    return False

# Set Player Move
  # this will set the move on the board dictionary
  # it will call change turns 

def player_move():
  global board, turn, move, choice_list
  # if check_move():
  #   board[move] = turn
  board[move] = turn
  choice_list.remove(move)




# Check Win
  # this will check for a win 
  # this will check by checking the spaces in the board
  # this will return true or false

def check_win():
  global board
  # print(board)
  if ((board['a1'] == board['b1']) and (board['a1'] == board['c1'])):
    if not(board['a1'] == ' '):
      print('124')
      return True
  elif ((board['a1'] == board['a2']) and (board['a1'] == board['a3'])):
    if not(board['a1'] == ' '):
      print('127')
      return True
  elif ((board['b1'] == board['b2']) and (board['b1'] == board['b3'])):
    if not(board['b1'] == ' '):
      print('130')
      return True
  elif ((board['c1'] == board['c2']) and (board['c1'] == board['c3'])):
    if not(board['c1'] == ' '):
      print('133')
      return True
  elif ((board['a2'] == board['b2']) and (board['a2'] == board['c2'])):
    if not(board['a2'] == ' '):
      print('136')
      return True
  elif ((board['a3'] == board['b3']) and (board['a3'] == board['c3'])):
    if not(board['a3'] == ' '):
      print('139')
      return True
  elif ((board['a1'] == board['b2']) and (board['a1'] == board['c3'])):
    if not(board['a1'] == ' '):
      print('142')
      return True
  elif ((board['a3'] == board['b2']) and (board['a3'] == board['c1'])): 
    if not(board['a3'] == ' '):
      print('145')
      return True
  



def play_game():
  global x_win, o_win
  init()
  display_board()

  for x in range(9):
    change_turns()
    get_move()
    while not(check_move()):
      get_move()
    player_move()
    display_board()
    
    if x > 3:
      if check_win():
        print(f"Player {turn} Won!")
        if turn == 'X':
          x_win += 1
        else: 
          o_win += 1
        print(f"Player X wins: {x_win} | Player O wins: {o_win}")
        break

  if not(check_win()):
    print('TIE!')

play_game()



































# for x in range(3):
#   a1, b1, c1 = ['X', ' ', ' ']
#   a2, b2, c2 = [' ', 'O', ' ']
#   a3, b3, c3 = [' ', ' ', ' ']

#   # a3 = 'K'
#   # b3 = 'M'
#   # c3 = 'L'

#   board = f'''
#     A   B   C 
#   1) {a1} | {b1} | {c1} 
#     -----------
#   2) {a2} | {b2} | {c2} 
#     -----------
#   3) {a3} | {b3} | {c3} 
#   '''

#   print(board)

#   choice = input('player input: ')
#   # print(choice)
#   print(choice[0])
#   print(choice[1])
#   letters = ['a', 'b', 'c']
#   nums = ['1', '2', '3']

#   if choice[0] in letters and choice[1] in nums:
#     print('good move')
#     if choice[0] == 'a':
#       move = a + int(choice[1])
#       print(move)
#   else:
#     print('bad move')


# for x in range(3):

  # row1 = ['X', ' ', ' ']
  # row2 = [' ', 'O', ' ']
  # row3 = [' ', ' ', ' ']
  # row3[0] = 'M'

  # b_list = [
  #   ['X', ' ', ' '],
  #   [' ', 'O', ' '],
  #   [' ', ' ', ' ']
  # ]
  

  # board = f'''
  #   A   B   C 
  # 1) {b_list[0][0]} | {b_list[0][1]} | {b_list[0][2]} 
  #   -----------
  # 2) {b_list[1][0]} | {b_list[1][1]} | {b_list[1][2]} 
  #   -----------
  # 3) {b_list[2][0]} | {b_list[2][1]} | {b_list[2][2]} 
  # '''

  # print(board)

  # choice = input('player input: ')
  # column = 0
  # row = 0
  # letters = ['a', 'b', 'c', 'A', 'B', 'C']
  # nums = ['1','2','3']


  # if choice[0] in letters and choice[1] in nums:
  #   print('good')
  #   if choice[0] == 'a':
  #     column = 0
  #     row = int(choice[1])
  #     print(row)
  #     print(type(row))
  #     # b_list[column][row] = 'X'
  # else:
  #   print('bad')




















# print(
# '''
#    A   B   C 
# 1)   |   |   
#   -----------
# 2)   |   |   
#   -----------
# 3)   |   |   
# '''
# )

# print(board[18]) # LETTER A1
# print(board[22]) # LETTER B1
# print(board[26]) # LETTER C1

# print(board[46]) # LETTER A2
# print(board[50]) # LETTER B2
# print(board[54]) # LETTER C2

# print(board[74]) # LETTER A3
# print(board[78]) # LETTER B3
# print(board[82]) # LETTER C3
