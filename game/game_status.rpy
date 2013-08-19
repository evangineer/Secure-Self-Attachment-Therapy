# This script contains the score of the user and any other information that indicates the 
# progress of the user. It also acts as a screen where the user can determine the the type 
# of protocol or exercise that needs to be performed for the next round. This is where the
# Intelligent Agent is prompted to make a move

# define all narrators used in this scene
define game_status_n = Character('Game Status', color="#c8ffc8")

label game_status:
    scene blank page
    game_status_n "This is the game status page"
    game_status_n "The Intelligent Agent will now make a move"
    $move = ai2.move()
    #game_status_n "%(move[0])s & %(move[1])s"
    
    if move[0] == "ignore" and move[1] == "dontgo":
        game_status_n "User Data Input Exercise"
        jump user_data_input
        
    elif move[0] == "ignore" and move[1] == "go":
        game_status_n "Profile Extension Exercise"
        jump profile_extension
        
    else:
        jump protocol_start
    