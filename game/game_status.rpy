# This script contains the score of the user and any other information that indicates the 
# progress of the user. It also acts as a screen where the user can determine the the type 
# of protocol or exercise that needs to be performed for the next round. This is where the
# Intelligent Agent is prompted to make a move

# define all narrators used in this scene
define game_status_n = Character('Game Status', color="#c8ffc8")

# define all images used in this scene
image part3_menu setup = "images/part3/menu/part3_menu_setup.png"
image part3 protocol ai = "images/part3/protocol/image_part3_ai_self_attachment_protocol.png"
image part3 profile_extension ai = "images/part3/profile_extension/image_part3_ai_profile_extension.png"
        
screen game_status_menu_layout:
    imagemap:
        # load unhover and hover page background images
        ground "images/part3/menu/part3_menu_layout.png"
        hover "images/part3/menu/part3_menu_layout_hover.png"
        
        # define clickable hotspots for interactions
        hotspot (705,290,289,283) clicked Return("_play")
    
    if rounds_played == 0:
        $ui.image("images/part3/menu/part3_menu_round_1.png",xpos=840,ypos=38)
    elif rounds_played == 1:
        $ui.image("images/part3/menu/part3_menu_round_2.png",xpos=840,ypos=38)   
    elif rounds_played == 2:
        $ui.image("images/part3/menu/part3_menu_round_3.png",xpos=840,ypos=38) 
    elif rounds_played == 3:
        $ui.image("images/part3/menu/part3_menu_round_4.png",xpos=840,ypos=38) 
    elif rounds_played == 4:
        $ui.image("images/part3/menu/part3_menu_round_5.png",xpos=840,ypos=38) 
        
    # create frame for photo and score
    frame id "part3_frame":
        xpos 43
        ypos 105
        xminimum 627
        xmaximum 627
        yminimum 391
        ymaximum 391
        
        $ui.text("Round Scores",color="#ff0002",xpos=10,ypos=8)
        if score == []:
            $ui.text("Total Score: 0",color="#ff0002",xpos=10,ypos=343)
        else:
            $ui.text("Total Score: " + str(sum(score)),color="#ff0002",xpos=10,ypos=343)            
        
        if len(score) == 1:
            $ui.text("Round 1: " + str(score[0]),color="#2a3d00ff",xpos=10,ypos=58)
        if len(score) == 2:
            $ui.text("Round 1: " + str(score[0]),color="#2a3d00ff",xpos=10,ypos=58)
            $ui.text("Round 2: " + str(score[1]),color="#2a3d00ff",xpos=10,ypos=98)
        if len(score) == 3:
            $ui.text("Round 1: " + str(score[0]),color="#2a3d00ff",xpos=10,ypos=58)
            $ui.text("Round 2: " + str(score[1]),color="#2a3d00ff",xpos=10,ypos=98)
            $ui.text("Round 3: " + str(score[2]),color="#2a3d00ff",xpos=10,ypos=138)
        if len(score) == 4:
            $ui.text("Round 1: " + str(score[0]),color="#2a3d00ff",xpos=10,ypos=58)
            $ui.text("Round 2: " + str(score[1]),color="#2a3d00ff",xpos=10,ypos=98)
            $ui.text("Round 3: " + str(score[2]),color="#2a3d00ff",xpos=10,ypos=138)
            $ui.text("Round 4: " + str(score[3]),color="#2a3d00ff",xpos=10,ypos=178)
        
    # button to return to the profile page
    frame id "frame_back":
        xpos 43
        ypos 524
        textbutton _("Back") action Return("_back")
        
    # button to view player scores
    frame id "frame_scores":
        xpos 138
        ypos 524
        textbutton _("View Scores") action Return("_scores")
        
    # button to toggle AI guide
    frame id "frame_ai_guide":
        xpos 305
        ypos 524
        if ai_guide == True:
            textbutton _("AI Guide: On") action Return("_ai_guide")
        else:
            textbutton _("AI Guide: Off") action Return("_ai_guide")
    
    # button to view all debug functions
    if config.developer == True:
        frame id "frame_debug":
            xpos 480
            ypos 524
            textbutton _("Debug") action Return("_debug")
        
# label to set up the game status menu layout
label game_status_menu:
    scene part3_menu setup
    with fade
    # activate the functions of the game status menu
    jump game_status_loop
    
label game_status_loop:
    # loads the required frames and entities in the game status menu
    call screen game_status_menu_layout
    $result = _return
    
    if result == "_back":
        jump part2_menu
        
    elif result == "_scores":
        jump score_history
    
    elif result == "_debug":
        jump debug
    
    elif result == "_play":
        jump round_play
        
    elif result == "_ai_guide":
        if ai_guide == True:
            $ai_guide = False
        else:
            $ai_guide = True
        jump game_status_loop
    
label debug:
    scene blank page
    with fade
    menu:
        "Player Game Logic":
            jump game_test
        "Intelligent Agent 1":
            jump ai_test
        "Intelligent Agent 2":
            jump ai2_test
    
label round_play:
    if ai_guide == True:
        $move = ai2.move()
        
        if move[0] == "ignore":
            scene part3 profile_extension ai
            with fade
            game_status_n "AI guide chooses: Profile Extension Exercise"
            jump profile_extension
        
        else:
            scene part3 protocol ai
            with fade
            game_status_n "AI guide chooses: Secure Self-Attachment Protocol"
            jump protocol_start    
            
    else:
        scene blank page
        with fade
        menu:
            "Please choose the type of exercise for this round"
            "Profile Extension Exercise":
                jump profile_extension
            "Secure Self-Attachment Protocol":
                jump protocol_start
                
label score_history:
    scene blank page
    with fade
    call screen score_layout
    $result = _return
    if result == "_back":
        jump game_status_menu
    
screen score_layout:
# create the title frame for score history
    frame id "frame_score_history_title":
        xpos 232
        ypos 21
        xminimum 765
        xmaximum 765
        yminimum 37
        ymaximum 37
        
        # load selected affirmation genre
        $ui.text("Score History",color="#ff0002",xalign=0.5)
        
    # create frame for list of affirmations
    frame id "frame_score_history_list":
        xpos 232
        ypos 70
        xminimum 765
        xmaximum 765
        yminimum 409
        ymaximum 409
        
        # create viewport for affirmation list
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 0
            ypos 0
            child_size (None,2000)
            
            if len(score_history) != 0:
                $i = 8
                $count = 1
                for number in score_history:
                    $ui.text("Set " + str(count) +": "+ str(score_history[count-1]), color="2a3d00ff",xpos=10,ypos=i)
                    $i += 30
                    $count += 1
                    
    frame id "score_back":
        xpos 23
        ypos 528
        textbutton _("Back") action Return("_back")