# This script contains all the exercises in the Profile Extension Module.
# These exercises aim to build and strengthen the information and profile
# page regarding the player's inner child. 

# define all the narrators in this scene
define profile_extension_n = Character('Profile Extension Exercise', color="c8ffc8")
define photo_description_n = Character('Photo Description', color="c8ffc8")
define affirmation_builder_n = Character('Affirmation Builder', color="c8ffc8")
define journal_entry_n = Character('Journal Entry', color="c8ffc8")
define music_recollection_n = Character('Music Recollection', color="c8ffc8")

label profile_extension:
    profile_extension_n "Profile Extension Exercises aim to build and strengthen the bonds that
                         you have with your inner child. Please follow the instructions of the
                         following exercise."
    jump profile_extension_choose_exercise
    
label profile_extension_choose_exercise:
    $exercise_count = 4
    $number = random.randint(1,exercise_count)
    $label_string = "profile_exercise_" + str(number)
    
    jump expression label_string

# This exercise is named "Photo Description". It shows a photo to the user and asks the player
# to describe the story or information behind the photo.
label profile_exercise_1:
    if photo_count == 0:
        jump profile_extension_choose_exercise
    scene blank page
    with fade
    photo_description_n "Photos capture a moment within one's lifetime. In a moment, a photo will
                       be shown on the screen. Please describe the photo and any stories that
                       are behind it or why the photo is of any importance if any."
    $number = random.randint(0,photo_count-1)

    $ui.image(im.Scale(photo_directory[number],450,380,xcenter=0.5,ycenter=0.40))
    if photo_directory[number] not in photo_title:
        $photo_title[photo_directory[number]] = renpy.input("What title would you like to give this photo?",length=60)
        
    $ui.image(im.Scale(photo_directory[number],450,380,xcenter=0.5,ycenter=0.40))
    if photo_directory[number] not in photo_detail:
        $photo_detail[photo_directory[number]] = renpy.input("Please describe the photo above:",length=9999)
    
    jump profile_extension_end
    
# This exercise is named "Affirmation Builder". It prompts the user to add a new affirmation to 
# his or her page and prompts the player to memorize the affirmation and recite it out loud.
label profile_exercise_2:
    scene blank page
    with fade
    affirmation_builder_n "Affirmations are powerful tools that can motivate or make oneself feel better by just reciting them. 
                           It is important to pick ones that you can relate to, or have a strong emotion towards. In this exercise 
                           you will pick or write an affirmation that suits your current mood. Then it is encouraged that you 
                           memorize this affirmation and try to recite it out loud."
    $exercise_mode = True
    call add_affirmation
    $exercise_mode = False
    
    affirmation_builder_n "You have selected the following affirmation. Please remember and recite it out loud. During this time
                           think of your inner child and your promise to take care of him/her."
    affirmation_builder_n "%(exercise_memory)s"
    
    jump profile_extension_end
    
# This exercise is named "Journal Entry". It prompts the user to write a story they recall from
# childhood or imagine a story where the inner child is at first in distress but calmed later.
label profile_exercise_3:
    scene blank page
    with fade
    journal_entry_n "Memories play an important role in defining us. In this exercise, try to remember a story or event that took
                     place during your childhood that is of importance to you. Try to write it in the 3rd person narrative, as if you 
                     informing your inner child of the events its been through."
    journal_entry_n "If you can not think of a story or an event now. Try to imagine and create a story where you inner child is initially
                     at distress but through an action or a series of event, the inner child managed to calm down and removed from the 
                     stress inducing event or situation."
    
    $age = renpy.input("At what age did this story take place?",length=2)
    while age.isdigit() == False:
        $age = renpy.input("At what age did this story take place?",length=2)
    
    $entry = renpy.input("Please describe the story that took place:",length=9999)
   
    if entry != "":
        $journal_entry.append((age,entry))
        $journal_length = len(journal_entry)
        $journal_current = journal_length
        
    jump action_checker

# This exercise is named "Music Recollection". It prompts the user to add or change the lyrics
# to an existing song. Then asks the user to memorize the lyrics for futher use.
label profile_exercise_4:
    if music_count == 0:
        jump profile_extension_choose_exercise
    scene blank page
    with fade
    music_recollection_n "Music is a powerful tool in accessing past emotions and memories. It is important that you import more music
                          that reminds you of your childhood or just songs that make you feel good in general. In this exercise, you will
                          input the lyrics of the music that you have imported. Once done, it will be shown on the screen where you can 
                          memorize it and recite it for later use."
    $number = random.randint(0,music_count-1)
    play music music_directory[number]
    
    if music_directory[number] not in music_title:
        $music_title[music_directory[number]] = renpy.input("What title would you like to give this song?",length=60)
    
    if music_directory[number] not in music_lyrics:
        $music_lyrics[music_directory[number]] = renpy.input("What are the lyrics to this song?",length=9999)
        
    stop music
    jump action_checker
    
label profile_extension_end:
    jump action_checker