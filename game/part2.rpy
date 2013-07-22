# Part 2 contains the profile page for the user's inner child. Within this section, the user has the
# ability to construct a strong sense of his or her chilhood, through stories, music, affirmations and
# photos.

# load images used in this scene
image part2_menu setup = "images/part2/image_part2_menu_layout.png"

# set up profile page layout
screen part2_menu_layout:  
    imagemap:
        # load unhover and hover page background images
        ground "images/part2/image_part2_menu.png"
        hover "images/part2/image_part2_menu_hover.png"
        
        # define clickable hotspots for interactions
        hotspot (23,366,138,102) clicked Return("affirmation")
        hotspot (171,366,138,102) clicked Return("diary")
        hotspot (23,480,138,102) clicked Return("music")
        hotspot (171,480,138,102) clicked Return("photo")
        
        hotspot (328,72,22,460) clicked Return("previous_page")
        hotspot (986,72,22,460) clicked Return("next_page")
    
    # create profile image for user's favourite photo
    frame id "frame_profile_image":
        xpos 24
        ypos 20
        xminimum 285
        xmaximum 285
        yminimum 285
        ymaximum 285
        
        # scale image to fit the frame
        $ui.image(im.Scale("images/part2/image_part2_profile.png",273,273))
    
    # create text box for the name of the user
    frame id "frame_name":
        xpos 24
        ypos 316
        xminimum 285
        xmaximum 285
        yminimum 39
        ymaximum 39
        
        $ui.text(name,color="#2a3d00ff",xalign=0.5)
        
    # create text box for selected affirmation
    frame id "frame_affirmation": 
        xpos 328
        ypos 20
        xminimum 679   
        xmaximum 679
        yminimum 39
        ymaximum 39
        
        $ui.text("I love myself!",color="#2a3d00ff",xalign=0.5)
    
    # create scrollable frame to contain the selected diary entry
    frame id "frame_diary_entry":
        xpos 356
        ypos 72
        xminimum 623
        xmaximum 623
        yminimum 459
        ymaximum 459
        
        # create a scrollable and draggable viewport
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 0
            ypos 0
            child_size (None,5000)
            
            # title of diary entry
            $ui.text("Age "+temp_age,color="#ff0002",xpos=10,ypos=8)
            
            # content of diary entry
            $ui.text(temp_entry,color="#2a3d00ff",xpos=10,ypos=48)
    
    # button to the Information and Tuturial page
    frame id "frame_information":
        xpos 356
        ypos 543
        textbutton _("Information") action Return("information")
    
    # button to return to the Main Menu
    frame id "frame_back":
        xpos 765
        ypos 543
        textbutton _("Back") action MainMenu()
    
    # button to continue to section 3
    frame id "frame_continue":
        xpos 855
        ypos 543
        textbutton _("Continue") action Return("continue")

# label to set up the part 2 profile layout
label part2_menu:
    # load up selected diary entry
    python:
        temp_age,temp_entry = journal_entry[journal_current-1]
    scene part2_menu setup
    with fade
    # activates the function of the part 2 menu
    jump part2_menu_loop
    
label part2_menu_loop:
    # loads the required frames and entities in the profile page
    call screen part2_menu_layout
    # actions by users stored in result
    $result = _return
    
    #if result == "affirmation":
    
    if result == "diary":
        # diary page is loaded
        jump diary_start
        
    #elif result == "music":
        
    #elif result == "photo":
        
    elif result == "previous_page":
        # checks and excecutes if a previous diary entry is available
        if journal_current > 1:
            jump previous_page
        else:
            # do nothing
            jump part2_menu_loop
        
    elif result == "next_page":
        # checks and excecutes if a next diary entry is available
        if journal_current != journal_length:
            jump next_page
        else:
            # do nothing
            jump part2_menu_loop
    
    elif result == "information":
        # jump part1_menu
        jump game_test
        
    elif result == "continue":
        # jump game_test
        jump part3_intro

# enable the previous page button function
label previous_page:
    # updates global variables
    python:
        journal_current = journal_current - 1
        temp_age,temp_entry = journal_entry[journal_current-1]
    # reload profile page with previous page
    jump part2_menu_loop

# enable the next page button function
label next_page:
    # update global variables
    python:
        journal_current = journal_current + 1
        temp_age,temp_entry = journal_entry[journal_current-1]
    # reload profile page with next page
    jump part2_menu_loop

        
        
    

