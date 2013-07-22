# This script contains all the exercises and protocols used within the game

# define all the narrators in this scene
define protocol_start_n = Character('Exercise', color="#c8ffc8")

label protocol_start:
    protocol_start_n "(random protocol is picked and executed)"
    jump action_checker
    