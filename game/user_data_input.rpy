# This script contains the exercises concerned with the user data. It contains the screens for the Beck's
# Depression and Anxiety Inventories. It is activated when the Intelligent Agent chooses Ignore and Don't Go
# representing emotional and cognitive withdraw, so the player is prompted to do a user data exercise.

# define all narrators used in this scene
define inventory_result = Character('Results', color="#c8ffc8")
define becks_depression_n = Character("Beck's Depression Inventory", color="#c8ffc8")
define becks_anxiety_n = Character("Beck's Anxiety Inventory", color="#c8ffc8")

label user_data_input:
    $exercise_count = 2
    $choice = random.randint(1,exercise_count)
    if choice == 1:
        jump becks_depression_inventory
    elif choice == 2:
        jump becks_anxiety_inventory
        
label becks_depression_inventory:
    scene blank page
    becks_depression_n "The following questions are made to determine the level of depression that you are currently feeling. It reults will be shown when all 21 questions
                        are answered. Please answer all the questions truthfully to allow it to better assess you current state."

    call becks_depression_questions
    call becks_depression_questions
    call becks_depression_questions
        
    if beck_depression_question_count == 21:
        $beck_depression_count += 1
        $beck_depression_score.append(sum(beck_depression_answer))
        $beck_depression_answer = []
        $beck_depression_question_count = 0
        jump becks_depression_result
    else:
        jump prompt
        
label becks_depression_questions:
    $answer_1 = beck_depression_question[beck_depression_question_count][0]
    $answer_2 = beck_depression_question[beck_depression_question_count][1]
    $answer_3 = beck_depression_question[beck_depression_question_count][2]
    $answer_4 = beck_depression_question[beck_depression_question_count][3]
    $question = beck_depression_question_count+1
    menu:
        "Question %(question)d"
        "%(answer_1)s":
            $beck_depression_answer.append(0)
        "%(answer_2)s":
            $beck_depression_answer.append(1)
        "%(answer_3)s":
            $beck_depression_answer.append(2)
        "%(answer_4)s":
            $beck_depression_answer.append(3)
    $beck_depression_question_count += 1
    return
        
label becks_depression_result:
    $score = beck_depression_score[-1]
    $explaination = becks_inventory_functions.depression_score_meaning(beck_depression_score[-1])
    inventory_result "Thank you for answering all the questions, your total score for the Beck's Depression Inventory is "
    inventory_result "%(score)d"
    inventory_result "%(explaination)s"
    jump prompt
    
label becks_anxiety_inventory:
    scene blank page
    becks_anxiety_n "The following questions are made to determine the level of anxiety that you are currently feeling. It reults will be shown when all 21 questions
                     are answered. Please answer all the questions truthfully to allow it to better assess you current state."

    call becks_anxiety_questions
    call becks_anxiety_questions
    call becks_anxiety_questions
        
    if beck_anxiety_question_count == 21:
        $beck_anxiety_count += 1
        $beck_anxiety_score.append(sum(beck_anxiety_answer))
        $beck_anxiety_answer = []
        $beck_anxiety_question_count = 0
        jump becks_anxiety_result
    else:
        jump prompt
        
label becks_anxiety_questions:
    $answer_1 = beck_anxiety_response[0]
    $answer_2 = beck_anxiety_response[1]
    $answer_3 = beck_anxiety_response[2]
    $answer_4 = beck_anxiety_response[3]
    $question = beck_anxiety_question[beck_anxiety_question_count]
    $question_count = beck_anxiety_question_count+1
    menu:
        "Question %(question_count)d"
        "During the past month, including today, have you felt the follwing symtoms:"
        "%(question)s"
        "%(answer_1)s":
            $beck_anxiety_answer.append(0)
        "%(answer_2)s":
            $beck_anxiety_answer.append(1)
        "%(answer_3)s":
            $beck_anxiety_answer.append(2)
        "%(answer_4)s":
            $beck_anxiety_answer.append(3)
    $beck_anxiety_question_count += 1
    return
        
label becks_anxiety_result:
    $score = beck_anxiety_score[-1]
    $explaination = becks_inventory_functions.anxiety_score_meaning(beck_anxiety_score[-1])
    inventory_result "Thank you for answering all the questions, your total score for the Beck's Anxiety Inventory is "
    inventory_result "%(score)d"
    inventory_result "%(explaination)s"
    jump prompt        
        
        
    