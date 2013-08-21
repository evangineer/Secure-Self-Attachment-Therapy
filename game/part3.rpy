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
define score_n = Character('Final Score', color="#c8ffc8")

# load all images used in this scene
image blank page = "images/test/image_blank.png"
image part3 introduction = "images/part3/introduction/image_part3_introduction.png"
image part3 introduction transparent = im.MatrixColor("images/part3/introduction/image_part3_introduction.png",im.matrix.brightness(0.75))
image prompt ignore dontgo = "images/part3/prompt/image_prompt_default.png"
image prompt ignore go = "images/part3/prompt/image_prompt_ignore_go.png"
image prompt attend dontgo = "images/part3/prompt/image_prompt_attend_dontgo.png"
image prompt attend go = "images/part3/prompt/image_prompt_attend_go.png"
image score final = "images/part3/score/image_final_score.png"

# Introduction to section 3 of the game 
label part3_intro:
    scene part3 introduction
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
    scene part3 introduction transparent
    with dissolve
    menu:
        stress_n "On a scale of one to five, how stressed are you currently feeling?"
        "No Stress":
            $stress.append(0)
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
    jump user_data_input

label action_checker:
    scene prompt ignore dontgo
    with fade
    
    # set up booleans to determine selected action
    $adult_attend = False
    $child_go = False
    
    menu:
        action_n "Did you manage to complete the exercise?"
        "Yes":
            # the adult attended to the inner child
            $adult_attend = True
            scene prompt attend dontgo
            with dissolve
        "No":
            $adult_attend = False
    menu:
        action_n "Did the exercise reduce your negative emotions?"
        "Yes":
            # the inner child responded and goes to the adult
            $child_go = True
            if adult_attend == True:
                scene prompt attend go
                with dissolve
            else:
                scene prompt ignore go
                with dissolve
        "No":
            $child_go = False
    
    # update game logic with action
    if (adult_attend and child_go):
        $score.append(20)
        $logic.attend_go()
        action_n "Round score: 20"
    elif (adult_attend and not child_go):
        $score.append(15)
        $logic.attend_dontgo()
        action_n "Round score: 15"
    elif (not adult_attend and child_go):
        $score.append(5)
        $logic.ignore_go()
        action_n "Round score: 5"
    else:
        $score.append(0)
        action_n "Round score: 0"
    
    # update the number of rounds of protocols the user has played
    $logic.update_matrix()
    
    jump prompt
             
label prompt:
    $total_rounds += 1
    $rounds_played += 1
    
    if rounds_played == 5:
        $rounds_played = 0
        $score_history.append(sum(score))
        $score = []
        $score_count += 1
        # go to score page
        jump final_score
    else:
        jump game_status_menu
        
label final_score:
    scene score final
    with fade
    score_n "Your final score for this set of rounds is..."
    $temp_score = score_history[-1]
    $ui.text(str(temp_score),color="#000000ff",size=150,xpos=575,ypos=139)
    score_n "%(temp_score)d / 100"
    jump part2_menu
