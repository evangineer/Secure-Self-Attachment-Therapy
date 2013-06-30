image part2_menu setup = "images/part2/image_part2_menu.png"

screen part2_menu_layout:  
    imagemap:
        ground "images/part2/image_part2_menu.png"
        hover "images/part2/image_part2_menu_hover.png"
        
        hotspot (23,366,138,102) clicked Return("affirmation")
        hotspot (171,366,138,102) clicked Return("diary")
        hotspot (23,480,138,102) clicked Return("music")
        hotspot (171,480,138,102) clicked Return("photo")
        
        hotspot (328,72,22,460) clicked Return("previous_page")
        hotspot (986,72,22,460) clicked Return("next_page")
        
    frame id "frame_profile_image":
        xpos 24
        ypos 20
        xminimum 285
        xmaximum 285
        yminimum 285
        ymaximum 285
        
        $ui.image(im.Scale("images/part2/image_part2_profile.png",273,273))
        
    frame id "frame_name":
        xpos 24
        ypos 316
        xminimum 285
        xmaximum 285
        yminimum 39
        ymaximum 39
        
        $ui.text("Caleb Chiu",color="#2a3d00ff",xalign=0.5)
        
    frame id "frame_affirmation": 
        xpos 328
        ypos 20
        xminimum 679   
        xmaximum 679
        yminimum 39
        ymaximum 39
        
        $ui.text("I love myself!",color="#2a3d00ff",xalign=0.5)
        
    frame id "frame_diary_entry":
        xpos 356
        ypos 72
        xminimum 623
        xmaximum 623
        yminimum 459
        ymaximum 459
        
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 0
            ypos 0
            child_size (None,5000)
            
            $ui.text("15th June 1995",color="#ff0002",xpos=10,ypos=8)
            $ui.text("Blah blah blah...",color="#2a3d00ff",xpos=10,ypos=48)
            
    frame id "frame_information":
        xpos 356
        ypos 543
        textbutton _("Information") action Return("information")
    
    frame id "frame_back":
        xpos 765
        ypos 543
        textbutton _("Back") action MainMenu()
        
    frame id "frame_continue":
        xpos 855
        ypos 543
        textbutton _("Continue") action Return("continue")
        
label part2_menu:
    scene part2_menu setup
    with fade
    call screen part2_menu_layout
    $result = _return
    
    #if result == "affirmation":
        
    #elif result == "diary":
        
    #elif result == "music":
        
    #elif result == "photo":
        
    #elif result == "previous_page":
        
    #elif result == "next_page":
    
    if result == "information":
        jump part1_menu
        
    #elif result == "continue":
    
        
    

