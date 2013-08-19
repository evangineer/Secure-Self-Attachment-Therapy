# This script contains the user information and variables within the game. It includes the stress level
# entered by the user and test results from the Beck's Depression and Anxiety Inventories.

label user_data:
    python:

        # Stress Checker Variables

        if not hasattr(renpy.store, "stress"):
            stress = []
            
        if not hasattr(renpy.store, "stress_total"):
            stress_total = 0
            
        # Beck's Depression Inventory Variables
        
        if not hasattr(renpy.store, "beck_depression_question"):
            beck_depression_question = becks_inventory_functions.setup_depression_questions()
            
        if not hasattr(renpy.store, "beck_depression_answer"):
            beck_depression_answer = []
            
        if not hasattr(renpy.store, "beck_depression_score"):
            beck_depression_score = []
            
        if not hasattr(renpy.store, "beck_depression_question_count"):
            beck_depression_question_count = 0
            
        if not hasattr(renpy.store, "beck_depression_count"):
            beck_depression_count = 0
        
        # Beck's Anxiety Inventory Variables
        
        if not hasattr(renpy.store, "beck_anxiety_question"):
            beck_anxiety_question = becks_inventory_functions.setup_anxiety_questions()
        
        if not hasattr(renpy.store, "beck_anxiety_response"):
            beck_anxiety_response = becks_inventory_functions.setup_anxiety_responses()
            
        if not hasattr(renpy.store, "beck_anxiety_answer"):
            beck_anxiety_answer = []
            
        if not hasattr(renpy.store, "beck_anxiety_score"):
            beck_anxiety_score = []
            
        if not hasattr(renpy.store, "beck_anxiety_question_count"):
            beck_anxiety_question_count = 0
            
        if not hasattr(renpy.store, "beck_anxiety_count"):
            beck_anxiety_count = 0
            
    return