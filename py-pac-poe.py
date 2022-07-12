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
# 

# Py-Pac-Poe Begin

print("------------------------\nLet's Play Py-Pac-Poe!!!\n------------------------")

# enter players names here
x = 'X'

a1, b1, c1 = [' ', ' ', ' ']
a2, b2, c2 = [' ', ' ', ' ']
a3, b3, c3 = [' ', ' ', ' ']


board = f'''
   A   B   C 
1) {a1} | {b1} | {c1} 
  -----------
2) {a2} | {b2} | {c2} 
  -----------
3) {a3} | {b3} | {c3} 
'''
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

# board[18] = 'X'

print(board)