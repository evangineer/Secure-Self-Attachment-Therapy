# This is the initial script the game runs when it is started. In this script, the
# global variables are loaded and depending on the variables themselves, the corresponding
# section of the game is loaded

init python:
    from game_logic import GameLogic
    from intelligent_agent import IntelligentAgent

# The game starts here.
label start:
    call globalvariables
    
    # checks to see if it is the first time the game has been run for the user
    if first_time == True:
        jump introduction
    # if not the first time, load the user's profile page
    else:
        jump part2_menu
        
    return
