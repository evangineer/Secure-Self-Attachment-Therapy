define diary_n = Character('Diary Entry', color="c8ffc8")

image diary setup = "images/part2/diary/image_diary_entry_setup.png"
image diary loaded = "images/part2/diary/image_diary_entry.png"
image diary start = "images/part2/diary/image_diary_start.png"

init python:
    age = None
    entry = None

label diary_start:
    scene diary start
    with fade
    
    $age = renpy.input("At what age did this story take place?",length=2)
    while age.isdigit() == False:
        $age = renpy.input("At what age did this story take place?",length=2)
    jump diary_entry

screen diary_layout:
    frame id "diary_date":
        xpos 234
        ypos 25
        xminimum 764
        xmaximum 764
        yminimum 35
        ymaximum 35
        
        $ui.text("Age " + age,color="#ff0002",xpos=10)

    frame id "diary_entry":
        xpos 234
        ypos 71
        xminimum 764
        xmaximum 764
        yminimum 510
        ymaximum 510
        
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 10
            ypos 0
            child_size (722,None)
            
            $ui.input(color="#2a3d00ff")

    frame id "change_date":
        xpos 23
        ypos 165
        textbutton _("Change Age") action Return("_change_age")
        
    frame id "back":
        xpos 23
        ypos 228
        textbutton _("Back") action Return("_back")
        
label diary_entry:
    scene diary setup
    with fade
    show diary loaded
    call screen diary_layout
    
    $entry= _return
    
    if entry == "_back":
        jump part2_menu
        
    elif entry == "_change_age":
        jump diary_start
        
    else:
        $globalvariables.journal_entry.append((age,entry))
        $globalvariables.journal_length = len(globalvariables.journal_entry)
        $globalvariables.journal_current = globalvariables.journal_length
        jump part2_menu
