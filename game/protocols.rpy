# This script contains all the exercises and protocols used within the game

# define all the narrators in this scene
define protocol_start_n = Character('Exercise', color="#c8ffc8")
define protocol_low_1 = Character('Low Protocol 1', color="#c8ffc8")
define protocol_standard_1 = Character('Standard Protocol 1', color="#c8ffc8")
define protocol_high_1 = Character('High Protocol 1', color="#c8ffc8")

label protocol_start:
    
    protocol_start_n "(random protocol is picked and executed)"
    
    $low_count = 1              # number of low level protocols
    $standard_count = 1         # number of standard level protocols
    $high_count = 1             # number of high level protocols
    
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
label protocol_low_1:
    protocol_low_1 "Low-Protocol 1 is chosen"
    jump protocol_end

# standard protocols

label protocol_standard_1:
    protocol_standard_1 "Standard-Protocol 1 is chosen"
    jump protocol_end

# high level protocols

label protocol_high_1:
    protocol_high_1 "High-Protocol 1 is chosen"
    jump protocol_end
    
# end of protocol
label protocol_end:
    jump action_checker