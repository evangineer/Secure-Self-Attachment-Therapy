# This script contains all the exercises and protocols used within the game

# define all the narrators in this scene
define protocol_start_n = Character('Secure Self-Attachment Protocol', color="#c8ffc8")
define protocol_low_1 = Character('Sing Along', color="#c8ffc8")
define protocol_low_2 = Character('Affirmation Recitation', color="#c8ffc8")
define protocol_standard_1 = Character('Music Dance', color="#c8ffc8")
define protocol_standard_2 = Character("Mother's Touch", color="#c8ffc8")
define protocol_high_1 = Character('Imaginative Play: Stressful Situation', color="#c8ffc8")
define protocol_high_2 = Character('Imaginative Play: Inner Child Struggle', color="#c8ffc8")

# define all images used in this scene
image part3 protocol = "images/part3/protocol/image_part3_self_attachment_protocol.png"
image protocol affirmation = "images/part3/protocol/image_protocol_affirmation_recite.png"
image protocol affirmation do = "images/part3/protocol/image_protocol_affirmation_recite_do.png"
image protocol mother = "images/part3/protocol/image_protocol_mothers_touch.png"
image protocol mother do = "images/part3/protocol/image_protocol_mothers_touch_do.png"
image protocol dance = "images/part3/protocol/image_protocol_music_dance.png"
image protocol dance do = "images/part3/protocol/image_protocol_music_dance_do.png"
image protocol sing = "images/part3/protocol/image_protocol_sing_along.png"
image protocol sing do = "images/part3/protocol/image_protocol_sing_along_do.png"
image protocol imagination_child = "images/part3/protocol/image_protocol_imagination_child.png"
image protocol imagination_child do1= "images/part3/protocol/image_protocol_imagination_child_do1.png"
image protocol imagination_child do2= "images/part3/protocol/image_protocol_imagination_child_do2.png"
image protocol imagination_child do3= "images/part3/protocol/image_protocol_imagination_child_do3.png"
image protocol imagination_stress = "images/part3/protocol/image_protocol_imagination_stress.png"
image protocol imagination_stress do1= "images/part3/protocol/image_protocol_imagination_stress_do1.png"
image protocol imagination_stress do2= "images/part3/protocol/image_protocol_imagination_stress_do2.png"

label protocol_start:
    scene part3 protocol
    with fade
    protocol_start_n "Secure Self-Attachment Protocols aim to provide you with tools in order to relieve your inner child's
                      distress. I seeks to reinforce good and healthy neural connections and seeks to strengthen them."
    
    $low_count = 2              # number of low level protocols
    $standard_count = 2         # number of standard level protocols
    $high_count = 2             # number of high level protocols
    
    # finds the most recent recoreded stress level of user
    $current_stress = stress[-1]

    # loads the corresponding random protocol
    if current_stress <= 1:
        $number = random.randint(1,low_count)
        $label_string = "protocol_low_" + str(number)
        
    elif current_stress > 1 and current_stress <= 3:
        $number = random.randint(1,standard_count)
        $label_string = "protocol_standard_" + str(number)

    else:
        $number = random.randint(1,high_count)
        $label_string = "protocol_high_" + str(number)
        
    jump expression label_string
    
# low level protocols

# This protocol is named "Sing Along". It prompts the player to sing along to the song played
# in the background.
label protocol_low_1:
    if music_count == 0:
        jump protocol_start
    scene protocol sing
    with fade
    protocol_low_1 "Music is a powerful tool in changing or exciting one's emotion. Singing a happy song can not only make you feel
                    happier but also helps form healthy secure neural connections in your brain. In this exercise, a song that was 
                    imported is played and while the song is playing, try to focus on your inner child and imagine singing directly
                    to him or her. Please click when you are ready."
    $number = random.randint(0,music_count-1)
    scene protocol sing do
    with dissolve
    play music music_directory[number]
    protocol_low_1 "Sing Along! Click to stop the song."
    stop music
    
    jump protocol_end
    
# This protocol is named "Affirmation Recitation". It prompts the user to choose and recite aloud an affirmation of their choice.
label protocol_low_2:
    if len(general_affirmation) == 0 and len(anxiety_affirmation) == 0 and len(stress_affirmation) ==0 and len(self_esteem_affirmation) ==0:
        jump profile_exercise_2
    scene protocol affirmation
    with fade
    protocol_low_2 "Affirmations are powerful tools that can motivate or make oneself feel better by just reciting them. 
                    It is important to pick ones that you can relate to, or have a strong emotion towards."
    scene protocol affirmation do
    with dissolve
    protocol_low_2 "In this exercise, a random affirmation that you have picked will be shown. Then it is encouraged that 
                     you memorize this affirmation and try to recite it out loud."
    $temp_affirmation = general_affirmation + anxiety_affirmation + stress_affirmation + self_esteem_affirmation
    $count = len(temp_affirmation)
    $number = ranom.randint(0,count)
    $affirmation = temp_affirmation[number]
    scene blank page
    with dissolve
    $ui.text(affirmation, color="000000ff",size = 35,xcenter=0.5,ycenter=0.5) 
    protocol_low_1 "Recite the following affirmation: %(affirmation)s"
    
    jump protocol_end

# standard protocols

label protocol_standard_1:
    if music_count == 0:
        jump protocol_start
    scene protocol dance
    with fade
    protocol_standard_1 "Dancing to music excites the brain and makes us feel good. In this exercise, a song that was 
                         imported is played and while the song is playing, try to dance along to the music."
    $number = random.randint(0,music_count-1)
    play music music_directory[number]
    scene protocol dance do
    with dissolve
    protocol_standard_1 "Dance! Click to stop the song."
    stop music
    
    jump protocol_end
    
label protocol_standard_2:
    if music_count == 0:
        jump protocol_start
    scene protocol mother
    with fade
    protocol_standard_2 "Secure Self-Attachment Therapy protocols stem a lot from the interactions that mothers have with their infants. 
                         Through contact and caressing, mothers are able to calm down infants who are at distress."
    scene protocol mother do
    with dissolve
    protocol_standard_2 "In this exercise, imagine that your inner child is at distress. Try to feel the anxiety and stress build up within
                         you. Then using your hands, carefully and slowly caress and stroke your head and imagine calming down your inner 
                         child as if you took on the role of its mother. Please click once completed."
    
    jump protocol_end

# high level protocols

label protocol_high_1:
    scene protocol imagination_stress
    with fade
    protocol_high_1 "Imaginative play is a powerful tool to prepare and relieve the mind of stressful situations. Stress and anxiety 
                     is an uncomfortable feeling to have and learning how to deal with these feelings is an important part of this 
                     therapy."
    scene protocol imagination_stress do1
    with dissolve
    protocol_high_1 "In this exercise, imagine a stressful situation that you have experienced recently or fabricate a stressful situation
                     in your head."
    scene protocol imagination_stress do2
    with dissolve
    protocol_high_1 "With this stressful situation in your head, narrate the story to remove yourself from this situation and imagine yourself
                     calming down and relieved. Please click when finished."
    jump protocol_end
    
label protocol_high_2:
    scene protocol imagination_child
    with fade
    protocol_high_2 "Imaginative play is a powerful tool to prepare and relieve the mind of stressful situations. Stress and anxiety 
                     is an uncomfortable feeling to have and learning how to deal with these feelings is an important part of this 
                     therapy."
    scene protocol imagination_child do1
    with dissolve
    protocol_high_2 "In this exercise, imagine a stressful situation that occured during your childhood. Try to be as detailed while imagining
                     as possible."
    scene protocol imagination_child do2
    with dissolve
    protocol_high_2 "However imagine yourself as an adult stepping into the scene and removing the the child away from the situation."
    scene protocol imagination_child do3
    with dissolve
    protocol_high_2 "Then attempt to relieve and calm the child as its primaryy caregiver.
                     Please click when completed"

    jump protocol_end
    
# end of protocol
label protocol_end:
    jump action_checker