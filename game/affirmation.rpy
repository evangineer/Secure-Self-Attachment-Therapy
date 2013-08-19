# This script is for the function of the affirmation page within Part2. It allows the user
# to choose between pre-defined affirmations or create their own. It also allows the user to
# view the affirmations to remember and to recite and used for later exercises

# define all narrators in this scene
define affirmation_n = Character('Affirmation', color="c8ffc8")

# import images used in this scene
image affirmation load = "images/part2/affirmation/image_affirmation_layout.png"
image affirmation loaded = "images/part2/affitmation/image_affirmation_setup.png"

screen affirmation_menu_layout:
    
    # create the genre box for the affirmation page
    frame id "frame_affirmation_genre":
        xpos 232
        ypos 21
        xminimum 765
        xmaximum 765
        yminimum 37
        ymaximum 37
        
        # load selected affirmation genre
        $ui.text(selected_genre + " Affirmations",color="#ff0002",xalign=0.5)
        
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
            child_size (1000,2000)
     
            # load all affirmation within the selected genre
            if selected_genre == "All":
                $temp_affirmation = []
                for item in general_affirmation:
                    $temp_affirmation.append(item)
                for item in anxiety_affirmation:
                    $temp_affirmation.append(item)
                for item in stress_affirmation:
                    $temp_affirmation.append(item)
                for item in self_esteem_affirmation:
                    $temp_affirmation.append(item)
                $i=5
                for item in temp_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
        
            if selected_genre == "General":
                $i=5
                for item in general_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if selected_genre == "Anxiety":
                $i=5
                for item in anxiety_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if selected_genre == "Stress":
                $i=5
                for item in stress_affirmation:
                    $ui.textbutton(item,clicked=Return(item),ypos=i,xalign=0)
                    $i+=40
                
            if selected_genre == "Self-Esteem":
                $i=5
                for item in self_esteem_affirmation:
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
        
        if selected_affirmation != None:
            $ui.text(selected_affirmation,color="#000000",xpos=110)
        
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
        xpos 680
        ypos 540
        textbutton _("Add Affirmation") action Return("_add")
        
    frame id "remove":
        xpos 875
        ypos 540
        textbutton _("Remove") action Return("_remove")
        
# label to set up the affirmation page layout
label affirmation_start:
    scene affirmation load
    with fade
    # activate the function of the affirmation page
    jump affirmation_loop
    
label affirmation_loop:
    # loads the required frames and entities in the affirmation page
    call screen affirmation_menu_layout
    # actions by users stored in result
    $result = _return
    
    if result == "_back":
        jump part2_menu
        
    elif result == "_all_affirmations":
        $selected_genre = "All"
        $selected_affirmation = None
        jump affirmation_loop
    
    elif result == "_general":
        $selected_genre = "General"
        $selected_affirmation = None
        jump affirmation_loop
    
    elif result == "_anxiety":
        $selected_genre = "Anxiety"
        $selected_affirmation = None
        jump affirmation_loop
    
    elif result == "_stress":
        $selected_genre = "Stress"
        $selected_affirmation = None
        jump affirmation_loop
    
    elif result == "_self_esteem":
        $selected_genre = "Self-Esteem"
        $selected_affirmation = None
        jump affirmation_loop
    
    elif result == "_add":
        jump add_affirmation
    
    elif result == "_remove":
        jump remove
    
    else:
        $selected_affirmation = result
        jump affirmation_loop
        
label remove:
    if selected_affirmation != None:
        if selected_affirmation in general_affirmation:
            $general_affirmation.remove(selected_affirmation)
        elif selected_affirmation in anxiety_affirmation:
            $anxiety_affirmation.remove(selected_affirmation)
        elif selected_affirmation in stress_affirmation:
            $stress_affirmation.remove(selected_affirmation)
        elif selected_affirmation in self_esteem_affirmation:
            $self_esteem_affirmation.remove(selected_affirmation)
    jump affirmation_loop
    
label add_affirmation:
    scene blank page
    with fade
    menu:
        "Would you like to add an existing affirmation or create a new one?"
        "Existing Affirmation":
            jump default_affirmation_loop
        "Custom Affirmation":
            jump custom_affirmation
    
label custom_affirmation:
    scene blank page
    with fade
    $affirmation = renpy.input("Please enter your custom affirmation:",length=60)
    menu:
        "Please select the genre of your custom affirmation"
        "General":
            $general_affirmation.append(affirmation)
            $selected_genre = "General"
        "Anxiety":
            $anxiety_affirmation.append(affirmation)
            $selected_genre = "Anxiety"
        "Stress":
            $stress_affirmation.append(affirmation)
            $selected_genre = "Stress"
        "Self-Esteem":
            $self_esteem_affirmation.append(affirmation)
            $selected_genre = "Self-Esteem"
    if exercise_mode == True:
        $exercise_memory = affirmation
        return
    else:
        jump affirmation_loop

        

