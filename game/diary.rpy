# This script is for the function of the diary page within Part 2. It allows the user to 
# input diary entries and to review them in the profile page.

# define all narrators in this scene
define diary_n = Character('Diary Entry', color="c8ffc8")

# import all photos used in this scene
image diary setup = "images/part2/diary/image_diary_entry_setup.png"
image diary loaded = "images/part2/diary/image_diary_entry.png"
image diary start = "images/part2/diary/image_diary_start.png"

init python:
    age = None
    entry = None

# pre-diary input setup, prompts user for information regarding their story
label diary_start:
    scene diary start
    with fade
    
    # prompts user for age when the story took place. Repeats if the input age is invalid
    $age = renpy.input("At what age did this story take place?",length=2)
    while age.isdigit() == False:
        $age = renpy.input("At what age did this story take place?",length=2)
    jump diary_entry

# set up the layout for the diary entry page
screen diary_layout:
    frame id "diary_date":
        xpos 234
        ypos 25
        xminimum 764
        xmaximum 764
        yminimum 35
        ymaximum 35
        
        # title of diary entry
        $ui.text("Age " + age,color="#ff0002",xpos=10)

    frame id "diary_entry":
        xpos 234
        ypos 71
        xminimum 764
        xmaximum 764
        yminimum 510
        ymaximum 510
        
        # create a scrollable window for input
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 10
            ypos 0
            child_size (722,None)
            
            # allows user to input their story
            $ui.input(color="#2a3d00ff")

    frame id "change_date":
        xpos 23
        ypos 165
        textbutton _("Change Age") action Return("_change_age")
        
    frame id "back":
        xpos 23
        ypos 228
        textbutton _("Back") action Return("_back")

# The following label is called when the diary button is pressed. It contains the functions
# of the diary page and updates global variables accordingly
label diary_entry:
    scene diary setup
    with fade
    # load diary entry page with a buffer and wait for input
    show diary loaded
    call screen diary_layout
    
    $entry= _return
    
    # return to profile page if back is pressed
    if entry == "_back":
        jump part2_menu
    
    # return to pre-diary input setup
    elif entry == "_change_age":
        jump diary_start
    
    # if story was inputted, update global variables and return
    else:
        $journal_entry.append((age,entry))
        $journal_length = len(journal_entry)
        $journal_current = journal_length
        jump part2_menu
