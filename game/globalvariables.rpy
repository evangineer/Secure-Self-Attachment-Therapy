# This file is used to store all the global variables and functions that can be called throughout the game

label globalvariables:
    python:
        # General Variables

        if not hasattr(renpy.store, "first_time"):
            first_time = False  #used to indicate whether it is the user's first time running the game

        if not hasattr(renpy.store, "name"):
            name = "Caleb Chiu"

        # Part 2 Variables

        # Diary Variables
        
        if not hasattr(renpy.store, "journal_entry"):
            journal_entry = [("3","When he was 3...")]
        if not hasattr(renpy.store, "journal_length"):
            journal_length = 1
        if not hasattr(renpy.store, "journal_current"):
            journal_current = 1

        # Part 3 Variables

        if not hasattr(renpy.store, "rounds_played"):
            rounds_played = 0

        # Stress Checker Variables

        if not hasattr(renpy.store, "stress"):
            stress = []
        if not hasattr(renpy.store, "stress_total"):
            stress_total = 0
            
        # Game Logic Variables
        
        if not hasattr(renpy.store, "logic"):
            logic = GameLogic()
            
        if not hasattr(renpy.store, "ai"):
            ai = IntelligentAgent()

    return