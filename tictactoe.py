import itertools 

def win(current_game):
    #Horizontal winner
    for row in game:                                                    #Minden elemen végigfut
        if row.count(row[0]) == len(row) and row[0] != 0:               #count megszámolja hogy a game-n belül mennyi azonos van mint a row[0].-ja (de ugye raw az nő) Ez visszaadja, hogy pl 2, de a len 3-at ad vissza szóval bukta.
            print(f"Player {row[0]} is the winner horizontally (-)!")   #f és {} segítségével lehet megadni változót. 

    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:           
        print(f"Player {diags[0]} is the winner diagonally (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:           
        print(f"Player {diags[0]} is the winner diagonally (\\)!")

    #Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")



def game_board(game_map, player=0, row=0, column=0, just_display = False):  
    try:    
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False    
        print("   0  1  2")
        if not just_display:
                game_map[row][column] = player          
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False
 



play = True
players = [1, 2]
while (play):     
    game =  [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],]

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current_player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            raw_choice = int(input("What raw do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, raw_choice, column_choice)
            if game:
                played = True







#game_board(game_map = game, just_display = True)

'''
print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)
    #for item in row:
        #print(item)
'''
