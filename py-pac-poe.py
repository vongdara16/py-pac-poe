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
turn = 'X'
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

  display_board = f'''
      A   B   C 
  1)  {board['a1']} | {board['b1']} | {board['c1']} 
     -----------
  2)  {board['a2']} | {board['b2']} | {board['c2']} 
     -----------
  3)  {board['a3']} | {board['b3']} | {board['c3']} 
  '''
  
  print(display_board)

  print(f"It is Player {turn}'s turn!")

init()


# Change Turns
  # this will change the turn variable

def change_turns():
  global turn
  turn = 'X' if turn == 'O' else 'O'

# Set Player Move
  # this will set the move on the board dictionary
  # it will call change turns 

def player_move():
  global board


# Check Win
  # this will check for a win 
  # this will check by checking the spaces in the board
  # this will return true or false















































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
