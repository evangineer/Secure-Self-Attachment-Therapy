# Part 3 is the iterated portion of the game.

#  Flow Chart                                                            update_table
#                                                                             |
#  --> part3_intro --> stress_checker --> game_logic --> protocols --> action_checker --> prompt ---\
#                                              |                                                     |
#  <------------------------------------------------------------------------------------------------/

# define all narrators in this scene
define part3_n = Character('Exercise', color="#c8ffc8")
define stress_n = Character('Stress Level', color="#c8ffc8")
define action_n = Character('Review', color="#c8ffc8")
define prompt_n = Character('Review', color="#c8ffc8")

# load all images used in this scene
image blank page = "images/test/image_blank.png"

# Introduction to section 3 of the game
label part3_intro:
    scene blank page
    with fade
    
    part3_n "Welcome to the exercise portion of the game. In this section, we will explore the different exercises and protocols
             that have proven to be effective when faced with stressful situations in your work or personal life."
    part3_n "It is recommended that you perform these protocols when you find yourself overwhelmed by strong emotions such as anger
             or fear"
    part3_n "This is an iterated game, meaning that the your progress is reviewed at the end of each round of protocols and exercises.
             At the end of each round, the game will prompt you on whether you managed to complete the exercise and whether it helped
             reduce your stress levels or helped you calm these emotions."
    part3_n "It is recommended that each exercise is to be performed but in situations that you are not in the mood to perform the 
             exercise or that the exercise is too hard, they can be dismissed. However, make sure to answer the questions 
             truthfully as they will help you on your progress."
    
    jump stress_checker
             
# prompts user to enter the level of stress they are feeling now and add the integer value to the stress list
label stress_checker:
    menu:
        stress_n "On a scale of one to five, how stressed are you currently feeling?"
        "1":
            $stress.append(1)
        "2":
            $stress.append(2)
        "3":
            $stress.append(3)
        "4":
            $stress.append(4)
        "5":
            $stress.append(5)
    
    # update times stress level has been checked
    $stress_total += 1
    jump protocol_start

label action_checker:
    # set up booleans to determine selected action
    $adult_attend = False
    $child_go = False
    
    menu:
        action_n "Did you manage to complete the exercise?"
        "Yes":
            # the adult attended to the inner child
            $adult_attend = True
            "cool"
        "No":
            "dude"
    menu:
        action_n "Did the exercise reduce your negative emotions?"
        "Yes":
            # the inner child responded and goes to the adult
            $child_go = True
            "cool"
        "No":
            "dude"
            
    if (adult_attend and child_go):
        "attend and go"
        $logic.attend_go()
    elif (adult_attend and not child_go):
        "attend and don't go"
        $logic.attend_dontgo()
    elif (not adult_attend and child_go):
        "ignore and go"
        $logic.ignore_go()
    else:
        "ignore and don't go"
    
    # update the number of rounds of protocols the user has played
    $logic.update_matrix()
    $rounds_played += 1
    jump prompt
             
label prompt:
    menu:
        prompt_n "Would you like to attempt another exercise?"
        "Yes":
            jump protocol_start
        "No":
            jump part2_menu
