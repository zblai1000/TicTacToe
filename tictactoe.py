#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
    

#if game is still going 
game_still_going = True

#Who won? Or tie?
winner = None

#Who's turn is it
current_player = None
player_1 = None
player_2 = None


#This is the display board 
def display_board():
    global board
    print("")
    print("▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █▀▀▄ ▄ ")
    print("▒█░▄▄ █▄▄█ █░▀░█ █▀▀ 　 █▀▀▄ █░░█ █▄▄█ █▄▄▀ █░░█ ░ ")
    print("▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀░ ▀▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀░ ▀ ")
    print("")
    print("Please refer to the numerical position of board for reference: ")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("-------------------------------------------------------------------------")
    print(board[0] + " | " + board [1] + " | " + board [2])
    print(board[3] + " | " + board [4] + " | " + board [5])
    print(board[6] + " | " + board [7] + " | " + board [8])

def play_game():
    
    #display initial board
    welcome_message()
    display_board()
    rules_of_the_game()
    choose_player()
    
    
    #While the game is still going
    while game_still_going:

        #Handle turn of each player 
        handle_turn(current_player)

        #Check if game ended or not 
        check_if_game_is_over()

        #Swith players alternatively  
        flip_player()

    #The game has ended, choose to go for another round or quit 
    if winner == player_1 or winner == player_2:
        print("CONGRATULATIONS to ___ " + winner + "___ , YOU HAVE WON!!!")
        print("")
        print("")
        print("▒█▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ ▀▀█ █ █ █ 　 ▄ ▀▄ ")
        print("▒█░░░ █░░█ █░░█ █░▀█ █▄▄▀ █▄▄█ ░░█░░ ▄▀░ ▀ ▀ ▀ 　 ░ ░█ ")
        print("▒█▄▄█ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▄ ▄ ▄ 　 ▀ ▄▀ ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        
    elif winner == None:
        print("▀█▀ ▀▀█▀▀ █ █▀▀ 　 █▀▀█ 　 ▀▀█▀▀ ░▀░ █▀▀ 　 ▄ ▄▀") 
        print("▒█░ ░░█░░ ░ ▀▀█ 　 █▄▄█ 　 ░░█░░ ▀█▀ █▀▀ 　 ░ █░")
        print("▄█▄ ░░▀░░ ░ ▀▀▀ 　 ▀░░▀ 　 ░░▀░░ ▀▀▀ ▀▀▀ 　 ▀ ▀▄")
        print("")
        print("")

    try_again()


def try_again():    
    while True:
        print("▀▀█▀▀ █▀▀█ █░░█ 　 █▀▀█ █▀▀▀ █▀▀█ ░▀░ █▀▀▄ ▀█ 　 ▄ ▀▄ ")
        print("░▒█░░ █▄▄▀ █▄▄█ 　 █▄▄█ █░▀█ █▄▄█ ▀█▀ █░░█ █▀ 　 ░ ░█ ")
        print("░▒█░░ ▀░▀▀ ▄▄▄█ 　 ▀░░▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀░░▀ ▄░ 　 ▀ ▄▀ ")
        print("")
        print("")
        try_again = None
        try_again = input("Select 1 to play again or select 0 to end the game: ")
        if try_again == "1":
            global board
            board = ["-","-","-",
                     "-","-","-",
                     "-","-","-",]
            
            global game_still_going
            global current_player
            global player_1
            global player_2
            global winner
            game_still_going = True
            current_player = None
            player_1 = None
            player_2 = None
            winner = None
           
            
            play_game()
            return
            
            
            break
            
            
        elif try_again == "0":
            print("▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ █░█ 　 █░░█ █▀▀█ █░░█ 　 █▀▀ █▀▀█ █▀▀█")
            print("░▒█░░ █▀▀█ █▄▄█ █░░█ █▀▄ 　 █▄▄█ █░░█ █░░█ 　 █▀▀ █░░█ █▄▄▀") 
            print("░▒█░░ ▀░░▀ ▀░░▀ ▀░░▀ ▀░▀ 　 ▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀░░ ▀▀▀▀ ▀░▀▀")  
            print("")
            print("█▀▀█ █░░ █▀▀█ █░░█ ░▀░ █▀▀▄ █▀▀▀") 
            print("█░░█ █░░ █▄▄█ █▄▄█ ▀█▀ █░░█ █░▀█")
            print("█▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░░▀ ▀▀▀▀") 
            print("")
            print("▀▀█▀▀ ░▀░ █▀▀ ░░ ▀▀█▀▀ █▀▀█ █▀▀ ░░ ▀▀█▀▀ █▀▀█ █▀▀") 
            print("░▒█░░ ▀█▀ █░░ ▀▀ ░▒█░░ █▄▄█ █░░ ▀▀ ░▒█░░ █░░█ █▀▀") 
            print("░▒█░░ ▀▀▀ ▀▀▀ ░░ ░▒█░░ ▀░░▀ ▀▀▀ ░░ ░▒█░░ ▀▀▀▀ ▀▀▀") 
            import sys
            sys.exit()
            break
        else:
            print("Invalid input. Select 1 to play again or select 0 to end the game: ")
         

#Handle a single turn of the current player 
def handle_turn(current_player):

    print(current_player + "'s turn")
    position = input("Game board format: \nColumn, row \nExample: \n1,1 is 1 \n1,2 is 2 \n2,1 is 4 \nChoose a position from 1-9: ")

    valid = False
    while not valid:
    
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1 to 9: ")
        
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't click that location. Choose a different position")

    board[position] = current_player
    display_board()

def check_if_game_is_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there's a winner
        winner = row_winner
    elif column_winner:
        #there's a winner
        winner = column_winner
    elif diagonal_winner:
        #there's a winner
        winner = diagonal_winner
    else:
        #there is no win
        winner = None
    return


def check_rows():
    #Set up global variables 
    global game_still_going
    #Check if any of the rows have the same value and is not empty 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row does has a match, then it is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner (player_1 or player_2)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
 

def check_columns():
    #Set up global variables 
    global game_still_going
    #Check if any of the columns have the same value and is not empty 
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #If any columns does has a match, then it is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner (player_1 or player_2)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    #Set up global variables 
    global game_still_going
    #Check if any of the diagonals have the same value and is not empty 
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #If any diagonals does has a match, then it is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #Return the winner (player_1 or player_2)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
    

def check_if_tie():
    global game_still_going 
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #Set up global variables 
    global current_player
    #If current player was player_1, then change it to player_2
    if current_player == player_1:
        current_player = player_2
    #If current player was player_2, then change it to player_1
    elif current_player == player_2:
        current_player = player_1
    return

def welcome_message():
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")
    print("▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")
    print("")
    print("▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀                           ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█")
    print("▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀                           ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█ ")
    print("▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄                           ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█")
    print("")
    print("▀▀█▀▀ ▒█▀▀▀█ 　 ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀                ▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ ▄  ")
    print("░▒█░░ ▒█░░▒█ 　 ░▒█░░ ▒█▀▀█ ▒█▀▀▀ 　 ▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀                ▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ ░  ")
    print("░▒█░░ ▒█▄▄▄█ 　 ░▒█░░ ▒█░▒█ ▒█▄▄▄　  ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄                ▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ ▀ ")
    print("")
    print("▒█▀▀▀█ ▒█▀▀▀                                                                ▒█░░░ █▀▀ 　 ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀█ 　 ▒█▀▀▀ ░▀░ █▀▀▄ █▀▀")
    print("▒█░░▒█ ▒█▀▀▀                                                                ▒█░░░ █▀▀ 　 ▒█▀▀▄ █░░█ █░░█ █▄▄█ 　 ▒█▀▀▀ ▀█▀ █░░█ █▀▀")
    print("▒█▄▄▄█ ▒█░░░                                                                ▒█▄▄█ ▀▀▀ 　 ▒█▄▄█ ▀▀▀▀ ▀░░▀ ▀░░▀ 　 ▒█░░░ ▀▀▀ ▀▀▀░ ▀▀▀")
    print("")
    print("▀▀█▀▀ ▀█▀ ▒█▀▀█ ░░ ▀▀█▀▀ ░█▀▀█ ▒█▀▀█ ░░ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀             ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█ 　 ▀▄▒▄▀ 　 ▒█▀▀▀█")
    print("░▒█░░ ▒█░ ▒█░░░ ▀▀ ░▒█░░ ▒█▄▄█ ▒█░░░ ▀▀ ░▒█░░ ▒█░░▒█ ▒█▀▀▀             ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█ 　 ░▒█░░ 　 ▒█░░▒█")
    print("░▒█░░ ▄█▄ ▒█▄▄█ ░░ ░▒█░░ ▒█░▒█ ▒█▄▄█ ░░ ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄             ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█ 　 ▄▀▒▀▄ 　 ▒█▄▄▄█")
    print("")
    print("")
    
def choose_player():
    global current_player
    global i
    global player_1
    global player_2



#each player are able to insert their preferred name / symbol / number
    
    player_1 = input("Player 1, please key in name/ symbol / number of your preference: ")
    player_2 = input("Player 2, please key in name/ symbol / number of your preference: ")
    valid = False
    while not valid:
        if player_1 == "" or player_2 == "":
            print("Invalid. Both players need to key in name / symbol / number of your preference")
            player_1 = input("Player 1, please key in name/ symbol / number of your preference: ")
            player_2 = input("Player 2, please key in name/ symbol / number of your preference: ")
        else:
            valid = True

    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 11 or i == 13 or i == 15 or i == 17 or i == 19 or i == 21 or i == 23 or i == 25 or i == 27:
            current_player = player_1
            i += 1
            valid = True

    else:
        current_player = player_2
        i += 1
        valid = True


def rules_of_the_game():
    print("Before starting, please key in your preferred number / symbol / name")
    print("Player 1 will begin first only its player 2 turn")
    print("Both of you will be placing your respective symbol alternatively")
    print("until 1 of you achieve 3 of your own symbol positioned diagonally,")
    print("in row or in column")



i = 1
play_game() 


