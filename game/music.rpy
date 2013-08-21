# This script is for the function of the music page within Part 2. It allows the user to 
# load in music and create a page where they can browse their collection and read lyrics
# as well as interacting with during exercises

# define all narrators in this scene
define music_n = Character('Music Collection', color="c8ffc8")

# import images used in this scene
image music setup = "images/part2/music/image_music_setup_layout.png"
image music general = "images/part2/music/image_music.png"

# set up music menu layout
screen music_menu_layout:
    imagemap:
        # load unhover and hover page background images
        ground "images/part2/music/image_music_setup.png"
        hover "images/part2/music/image_music_setup_hover.png"
        
        # define clickable hotspots for interactions
        hotspot (232,70,40,460) clicked Return("_previous_song")
        hotspot (974,70,40,460) clicked Return("_next_song")
        
    # create the title box for the music page
    frame id "frame_music_title":
        xpos 232
        ypos 21
        xminimum 628
        xmaximum 628
        yminimum 37
        ymaximum 37

        if music_directory[selected_music] in music_title:
            $ui.text(music_title[music_directory[selected_music]], color="2a3d00ff",xalign=0.5)
            
    # create the music number box for the music page
    frame id "frame_music_number_box":
        xpos 867
        ypos 21
        xminimum 130
        xmaximum 130
        yminimum 37
        ymaximum 37

        $ui.text("No: " + str(selected_music + 1) + " of " + str(music_count),color="#2a3d00ff",xalign=0.5)
        
    # create the lyrics frame for the music page
    frame id "frame_music_lyrics":
        xpos 259
        ypos 70
        xminimum 713
        xmaximum 713
        yminimum 459
        ymaximum 459
        
        # create viewport for lyrics
        viewport id "diary_entry":
            draggable True
            mousewheel True
            scrollbars "vertical"
        
            xpos 0
            ypos 0
            child_size (None,5000)
            
            if music_directory[selected_music] in music_lyrics:
                $ui.text(music_lyrics[music_directory[selected_music]], color="2a3d00ff",xpos=10,ypos=8)  
        
    # create buttons for interactions with the music page
    frame id "refresh_music":
        xpos 23
        ypos 168
        textbutton _("Refresh Music") action Return("_refresh")
        
    frame id "change_title":
        xpos 23
        ypos 228
        textbutton _("Change Title") action Return("_change_music_title")
        
    frame id "add_lyrics":
        xpos 23
        ypos 288
        textbutton _("Add Lyrics") action Return("_add_lyrics")
        
    frame id "back":
        xpos 23
        ypos 348
        textbutton _("Back") action Return("_back")
        
    frame id "stop":
        xpos 685
        ypos 540
        textbutton _("Stop Song") action Return("_stop")
        
    frame id "play":
        xpos 835
        ypos 540
        textbutton _("Play Song") action Return("_play")

# label to set up the music page layout
label music_start:
    $music_path = os.path.join(script_path, "Music/*")
    $music_directory = glob.glob(music_path)
    $music_count = len(music_directory)
    python:
        for i in range(music_count):
            if music_directory[i] not in music_title:
                music_title[music_directory[i]] = os.path.basename(music_directory[i])
    scene music setup
    with fade
    # activate the function of the music page
    jump music_loop
    
label music_loop:
    # loads the required frames and entities in the music page
    call screen music_menu_layout
    # actions by users stored in result
    $result = _return
    
    if result == "_back":
        jump part2_menu
    
    elif result == "_previous_song":
        jump previous_song
    
    elif result == "_next_song":
        jump next_song
    
    elif result == "_refresh":
        jump refresh_music
    
    elif result == "_change_music_title":
        jump change_music_title
    
    elif result == "_add_lyrics":
        jump add_lyrics
        
    elif result == "_play":
        jump play_song
        
    elif result == "_stop":
        jump stop_song
        
label refresh_music:
    $music_path = os.path.join(script_path, "Music/*")
    $music_directory = glob.glob(music_path)
    $music_count = len(music_directory)
    python:
        for i in range(music_count):
            if music_directory[i] not in music_title:
                music_title[music_directory[i]] = os.path.basename(music_directory[i])
    jump music_loop
    
label next_song:
    if selected_music < (music_count-1):
        $selected_music += 1
    jump music_loop
    
label previous_song:
    if selected_music > 0:
        $selected_music -= 1
    jump music_loop
    
label add_lyrics:
    scene music general
    with fade
    $music_lyrics[music_directory[selected_music]] = renpy.input("What are the lyrics to this song?",length=9999)
    jump music_loop
    
label change_music_title:
    scene music general
    with fade
    $music_title[music_directory[selected_music]] = renpy.input("What title would you like to give this song?",length=60)
    jump music_loop
    
label play_song:
    play music music_directory[selected_music]
    jump music_loop
    
label stop_song:
    stop music
    jump music_loop