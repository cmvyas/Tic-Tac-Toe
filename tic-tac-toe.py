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
    
player1_marker , player2_marker = player_input()
     