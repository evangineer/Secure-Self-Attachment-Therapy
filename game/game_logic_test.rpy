# This script is to test the functionality of the game logic

label game_test:
    scene blank page
    call screen game_test_setup
    $result = _return
    
    if result == "attend_go":
        $logic.attend_go()
        
    if result == "attend_dontgo":
        $logic.attend_dontgo()
        
    if result == "ignore_go":
        $logic.ignore_go()
        
    if result == "ignore_dontgo":
        $logic.ignore_dontgo()
        
    $logic.update_matrix()
    jump game_test

screen game_test_setup:
    hbox xalign 0.5 yalign 0.5 spacing 50:
        vbox spacing 50:
            hbox spacing 10:
                textbutton _(str(round(logic.t[0],1)) + "       " + str(round(logic.t[1],1))) action Return("attend_go")
            
            hbox spacing 10:
                textbutton _(str(round(logic.v[0],1)) + "       " + str(round(logic.v[1],1))) action Return("attend_dontgo")
        
        vbox spacing 50:   
            hbox spacing 10:
                textbutton _(str(round(logic.u[0],1)) + "       " + str(round(logic.u[1],1))) action Return("ignore_go")
    
            hbox spacing 10:
                textbutton _(str(round(logic.w[0],1)) + "       " + str(round(logic.w[1],1))) action Return("ignore_dontgo")