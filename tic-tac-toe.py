# tic tac toe 
# board display
def display_board(board):
    
    print(board[1]+'_|_'+board[2]+'_|_'+board[3])
    
    print(board[4]+'_|_'+board[5]+'_|_'+board[6])
    
    print(board[7]+' | '+board[8]+' | '+board[9])

# asking player to choose either X or O
def player_input():
    marker = ''
    #keep asking for right input from player 1 
    
    while marker != 'X' and marker != 'O':
        marker= input('Player 1, choose either X or O :')
        
    player1=marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2='X'
        
    return (player1,player2)
    
#placing mark at desired position

def place_marker(board, marker, position):
    board[position] = marker

#condition for winning
  # all element in a row should be equal or we can say of same mark 
  # or all element in a coulumn be equal 
  # or all element in diagonal be same

def win_check(board,mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[3] == mark and board[5] == mark and board[7] == mark)) 
     

# random selection who goes first
from random import *
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# free space on board 

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True
    
# asking for the next position and writing value over there if that place is not filled

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
# asking for new match 
def replay():
    choice = input('Play again? Enter Yes or No')
    
    return chioce == 'yes'
    
                       # ********** game *********
print("Let's Play Tic Tac Toe")
while True:
     #board
     the_board = [' '] * 10
     player1_marker, player2_marker = player_input()
     turn = choose_first()
     print(turn + ' will go first')
     play_game = input('Ready to play? Enter Yes or No.')
    
     if play_game == 'Yes':
          game_on = True
     else:
          game_on = False

     while game_on:
         if turn == 'Player 1': 
             display_board(the_board)
             position = player_choice(the_board)
             place_marker(the_board, player1_marker, position)

             if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player1 won the game!')
                game_on = False
             else:
                 if full_board_check(the_board):
                     display_board(the_board)
                     print('Game Tie!')
                     break
                 else:
                     turn = 'Player 2'

         else:
             display_board(the_board)
             position = player_choice(the_board)
             place_marker(the_board, player2_marker, position)
             if win_check(the_board, player2_marker):
                 display_board(the_board)
                 print('Player2 won!')
                 game_on = False
             else:
                 if full_board_check(the_board):
                     display_board(the_board)
                     print('Game Tie!')
                     break
                 else:
                     turn = 'Player 1'

     if not replay():
         break




