# This file is used to store all the global variables and functions that can be called throughout the game

label globalvariables:
    python:
        # General Variables
        
        if not hasattr(renpy.store, "script_path"):
            #script_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
            script_path = "/Users/ZERO/Computing/GitHub/Secure Self-Attachment Therapy"

        if not hasattr(renpy.store, "first_time"):
            first_time = False  #used to indicate whether it is the user's first time running the game

        if not hasattr(renpy.store, "name"):
            name = "Caleb Chiu"

        # Part 2 Variables

        if not hasattr(renpy.store, "profile_set"):
            profile_set = False
            
        if not hasattr(renpy.store, "profile_picture"):
            profile_picture = None
            
        # Affirmation Variables
        
        if not hasattr(renpy.store, "selected_genre"):
            selected_genre = "All"
            
        if not hasattr(renpy.store, "selected_affirmation"):
            selected_affirmation = None
        
        if not hasattr(renpy.store, "general_affirmation"):
            general_affirmation = []
            
        if not hasattr(renpy.store, "anxiety_affirmation"):
            anxiety_affirmation = []
            
        if not hasattr(renpy.store, "stress_affirmation"):
            stress_affirmation = []
            
        if not hasattr(renpy.store, "self_esteem_affirmation"):
            self_esteem_affirmation = []
            
        if not hasattr(renpy.store, "default_selected_genre"):
            default_selected_genre = "All"
            
        if not hasattr(renpy.store, "default_selected_affirmation"):
            default_selected_affirmation = None

        if not hasattr(renpy.store, "default_general_affirmation"):
            default_general_affirmation = affirmation_load.load_general_affirmations()
            
        if not hasattr(renpy.store, "default_anxiety_affirmation"):
            default_anxiety_affirmation = affirmation_load.load_anxiety_affirmations()
            
        if not hasattr(renpy.store, "default_stress_affirmation"):
            default_stress_affirmation = affirmation_load.load_stress_affirmations()
            
        if not hasattr(renpy.store, "default_self_esteem_affirmation"):
            default_self_esteem_affirmation = affirmation_load.load_self_esteem_affirmations()
            
        # Diary Variables
        
        if not hasattr(renpy.store, "journal_entry"):
            journal_entry = [("3","When he was 3...")]
            
        if not hasattr(renpy.store, "journal_length"):
            journal_length = 1
            
        if not hasattr(renpy.store, "journal_current"):
            journal_current = 1
            
        # Photo Album Variables
        
        if not hasattr(renpy.store, "photo_count"):
            photo_count = 0
            
        if not hasattr(renpy.store, "selected_photo"):
            selected_photo = 0
        
        if not hasattr(renpy.store, "photo_directory"):
            photo_directory = []
            
        if not hasattr(renpy.store, "photo_title"):
            photo_title = {}
            
        if not hasattr(renpy.store, "photo_detail"):
            photo_detail = {}
            
        # Music Variables
        
        if not hasattr(renpy.store, "music_count"):
            music_count = 0

        if not hasattr(renpy.store, "selected_music"):
            selected_music = 0
            
        if not hasattr(renpy.store, "music_directory"):
            music_directory = []
            
        if not hasattr(renpy.store, "music_title"):
            music_title = {}
            
        if not hasattr(renpy.store, "music_lyrics"):
            music_lyrics = {}

        # Part 3 Variables
        
        if not hasattr(renpy.store, "exercise_mode"):
            exercise_mode = False 
            
        if not hasattr(renpy.store, "exercise_memory"):
            exercise_memory = None 
            
        if not hasattr(renpy.store, "rounds_played"):
            rounds_played = 0
            
        # Game Logic Variables
        
        if not hasattr(renpy.store, "logic"):
            logic = GameLogic()
            
        if not hasattr(renpy.store, "ai"):
            ai = IntelligentAgent()
            
        if not hasattr(renpy.store, "ai2"):
            ai2 = IntelligentAgent2()

    return