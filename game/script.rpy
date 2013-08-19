# This is the initial script the game runs when it is started. In this script, the
# global variables are loaded and depending on the variables themselves, the corresponding
# section of the game is loaded

init python:
    from game_logic import GameLogic
    from intelligent_agent import IntelligentAgent
    from intelligent_agent_2 import IntelligentAgent2
    import affirmation_load
    import becks_inventory_functions
    import random
    import glob
    import os

# The game starts here.
label start:
    call globalvariables
    call user_data
    
    # checks to see if it is the first time the game has been run for the user
    if first_time == True:
        jump introduction
    # if not the first time, load the user's profile page
    else:
        jump part2_menu
        
    return
