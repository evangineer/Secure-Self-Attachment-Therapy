# This script is for the function of the photo album page within Part 2. It allows the user
# to load in photos and create a photo album for them to look at and interact with during
# exercises

# define all narrators in this scene
define photo_n = Character('Photo Album', color="c8ffc8")

# import images used in this scene
image photo setup = "images/part2/photo/image_photo_entry_setup_layout.png"
image photo general = "images/part2/photo/image_photo.png"

# set up photo menu layout
screen photo_menu_layout:
    imagemap:
        # load unhover and hover page background images
        ground "images/part2/photo/image_photo_entry_setup.png"
        hover "images/part2/photo/image_photo_entry_setup_hover.png"
        
        # define clickable hotspots for interactions
        hotspot (232,70,40,460) clicked Return("_previous_photo")
        hotspot (974,70,40,460) clicked Return("_next_photo")
        
    # create the title box for the photo page
    frame id "frame_photo_title":
        xpos 232
        ypos 21
        xminimum 628
        xmaximum 628
        yminimum 37
        ymaximum 37
        
        if photo_count != 0:
            if photo_directory[selected_photo] in photo_title:
                $ui.text(photo_title[photo_directory[selected_photo]], color="#2a3d00ff",xalign=0.5)

    # create the photo number box for the photo page
    frame id "frame_photo_number_box":
        xpos 867
        ypos 21
        xminimum 130
        xmaximum 130
        yminimum 37
        ymaximum 37
        
        if photo_count != 0:
            $ui.text("No: " + str(selected_photo + 1) + " of " + str(photo_count),color="#2a3d00ff",xalign=0.5)

    # create the photo album frame for the photo page
    frame id "frame_photo_album":
        xpos 259
        ypos 70
        xminimum 713
        xmaximum 713
        yminimum 459
        ymaximum 459
        
        # create a scrollable window for photo and detail
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 10
            ypos 0
            child_size (None,1500)
            
            if photo_count != 0:
            
                if photo_directory[selected_photo] in photo_detail:
                    $ui.image(im.Scale(photo_directory[selected_photo],450,380,xpos=120,ypos= 30))
                    $ui.text(photo_detail[photo_directory[selected_photo]],color="#2a3d00ff",xpos=10,ypos=450)
                
                else:
                    $ui.image(im.Scale(photo_directory[selected_photo],450,380,xpos=120,ypos= 30))
                    $ui.text("",color="#2a3d00ff",xpos=10,ypos=450)
        
    # create buttons for interactions with the photo page
    frame id "refresh_photo":
        xpos 23
        ypos 168
        textbutton _("Refresh Photos") action Return("_refresh")
        
    frame id "change_title":
        xpos 23
        ypos 228
        textbutton _("Change Title") action Return("_change_title")
        
    frame id "make_profile":
        xpos 23
        ypos 288
        textbutton _("Profile Picture") action Return("_profile_picture")
        
    frame id "add_description":
        xpos 23
        ypos 348
        textbutton _("Add Description") action Return("_add_description")
        
    frame id "back":
        xpos 23
        ypos 408
        textbutton _("Back") action Return("_back")
        
# label to set up the photo page layout
label photo_album_start:
    $photo_path = os.path.join(script_path, "Photos/*")
    $photo_directory = glob.glob(photo_path)
    $photo_count = len(photo_directory)
    scene photo setup
    with fade
    # activates the function of the photo page
    jump photo_loop
   
label photo_loop:
    # loads the required frames and entities in the photo page
    call screen photo_menu_layout
    # actions by users stored in result
    $result = _return
    
    if result == "_back":
        jump part2_menu
    
    elif result == "_previous_photo":
        jump previous_photo
    
    elif result == "_next_photo":
        jump next_photo
    
    elif result == "_refresh":
        jump refresh_photo
    
    elif result == "_change_title":
        jump change_title
    
    elif result == "_profile_picture":
        jump profile_picture
        
    elif result == "_add_description":
        jump add_description
    
label refresh_photo:
    $photo_path = os.path.join(script_path, "Photos/*")
    $photo_directory = glob.glob(photo_path)
    $photo_count = len(photo_directory)
    jump photo_loop
    
label next_photo:
    if selected_photo < (photo_count-1):
        $selected_photo += 1
    jump photo_loop
    
label previous_photo:
    if selected_photo > 0:
        $selected_photo -= 1
    jump photo_loop
    
label profile_picture:
    $profile_set = True
    $profile_picture = photo_directory[selected_photo]
    jump photo_loop
    
label change_title:
    scene blank page
    with fade
    $ui.image(im.Scale(photo_directory[selected_photo],450,380,xcenter=0.5,ycenter=0.40))
    $photo_title[photo_directory[selected_photo]] = renpy.input("What title would you like to give this photo?",length=60)
    jump photo_loop
    
label add_description:
    scene blank page
    with fade
    $ui.image(im.Scale(photo_directory[selected_photo],450,380,xcenter=0.5,ycenter=0.40))
    $photo_detail[photo_directory[selected_photo]] = renpy.input("Please describe the photo above:",length=9999)
    jump photo_loop
    

   