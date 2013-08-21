# This script loads the default affirmations. It also contains the screen
# for adding existing affirmations. 

# define all narrators in this scene
define affirmation_default_n = Character('Affirmation', color="c8ffc8")

# import images used in this scene
# uses the images from affirmation

screen default_affirmation_menu_layout:
    
    # create the genre box for the affirmation page
    frame id "frame_affirmation_genre":
        xpos 232
        ypos 21
        xminimum 765
        xmaximum 765
        yminimum 37
        ymaximum 37
        
        # load selected affirmation genre
        $ui.text(default_selected_genre + " Affirmations (Existing)",color="#ff0002",xalign=0)
        
    # create frame for list of affirmations
    frame id "frame_affirmation_list":
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
            scrollbars "both"
        
            xpos 0
            ypos 0
            child_size (1000,4000)
     
            # load all affirmation within the selected genre
            if default_selected_genre == "All":
                $temp_affirmation = []
                for item in default_general_affirmation:
                    $temp_affirmation.append(item)
                for item in default_anxiety_affirmation:
                    $temp_affirmation.append(item)
                for item in default_stress_affirmation:
                    $temp_affirmation.append(item)
                for item in default_self_esteem_affirmation:
                    $temp_affirmation.append(item)
                $i=5
                for item in temp_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
        
            if default_selected_genre == "General":
                $i=5
                for item in default_general_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if default_selected_genre == "Anxiety":
                $i=5
                for item in default_anxiety_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if default_selected_genre == "Stress":
                $i=5
                for item in default_stress_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if default_selected_genre == "Self-Esteem":
                $i=5
                for item in default_self_esteem_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
        
    # create frame for the selected affirmation
    frame id "frame_affirmation_selected":
        xpos 233
        ypos 492
        xminimum 765
        xmaximum 765
        yminimum 37
        ymaximum 37
        
        # show selected affirmation
        $ui.text("Selected: ",color="#ff0002",xpos=8)
        
        if default_selected_affirmation != None:
            $ui.text(default_selected_affirmation,color="#000000",xpos=110)
        
    frame id "all_affirmations":
        xpos 23
        ypos 158
        textbutton _("All Affirmations") action Return("_all_affirmations")
        
    frame id "general":
        xpos 23
        ypos 218
        textbutton _("General") action Return("_general")
        
    frame id "anxiety":
        xpos 23
        ypos 278
        textbutton _("Anxiety") action Return("_anxiety")

    frame id "stress":
        xpos 23
        ypos 338
        textbutton _("Stress") action Return("_stress")

    frame id "self_esteem":
        xpos 23
        ypos 398
        textbutton _("Self-Esteem") action Return("_self_esteem")

    frame id "back":
        xpos 23
        ypos 528
        textbutton _("Back") action Return("_back")
        
    frame id "add":
        xpos 810
        ypos 540
        textbutton _("Add Affirmation") action Return("_add")
        
# label to set up the affirmation page layout
label default_affirmation_start:
    scene affirmation load
    with fade
    # activate the function of the affirmation page
    jump default_affirmation_loop
    
label default_affirmation_loop:
    # loads the required frames and entities in the affirmation page
    call screen default_affirmation_menu_layout
    # actions by users stored in result
    $result = _return
    
    if result == "_back":
        if exercise_mode == True:
            jump add_affirmation
        else:
            jump affirmation_start
        
    elif result == "_all_affirmations":
        $default_selected_genre = "All"
        $default_selected_affirmation = None
        jump default_affirmation_loop
    
    elif result == "_general":
        $default_selected_genre = "General"
        $default_selected_affirmation = None
        jump default_affirmation_loop
    
    elif result == "_anxiety":
        $default_selected_genre = "Anxiety"
        $default_selected_affirmation = None
        jump default_affirmation_loop
    
    elif result == "_stress":
        $default_selected_genre = "Stress"
        $default_selected_affirmation = None
        jump default_affirmation_loop
    
    elif result == "_self_esteem":
        $default_selected_genre = "Self-Esteem"
        $default_selected_affirmation = None
        jump default_affirmation_loop
    
    elif result == "_add":
        if exercise_mode == True:
            return
        else:
            jump default_add_affirmation
    
    else:
        $default_selected_affirmation = result
        $exercise_memory = result
        jump default_affirmation_loop
    
label default_add_affirmation:
    if default_selected_affirmation != None:
        if default_selected_affirmation in default_general_affirmation:
            $general_affirmation.append(default_selected_affirmation)
            $selected_genre = "General"
        elif default_selected_affirmation in default_anxiety_affirmation:
            $anxiety_affirmation.append(default_selected_affirmation)
            $selected_genre = "Anxiety"
        elif default_selected_affirmation in default_stress_affirmation:
            $stress_affirmation.append(default_selected_affirmation)
            $selected_genre = "Stress"
        elif default_selected_affirmation in default_self_esteem_affirmation:
            $self_esteem_affirmation.append(default_selected_affirmation)
            $selected_genre = "Self-Esteem"
        jump affirmation_start

        

