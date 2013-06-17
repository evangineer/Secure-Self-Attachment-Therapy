define introduction_n = Character('Introduction', color="#c8ffc8")
define game_background_n = Character('Game Background', color="#c8ffc8")

label introduction:
    introduction_n "The feelings of depression, anxiety and other mental disorders are unwanted and can be hard to bear at times.
                    With neglect and improper treatment, these conditions can affect an individual's quality of life."
    introduction_n "From simple symptoms of lack of energy to severe cases such as suicidal thoughts, depression is a vast problem facing society today.
                    However, mental disorders are not as uncommon as you may think."

    menu:
        introduction_n "Can you guess how many people develop at least one mental or neurological disorder at some stage in life?"
        "1 in every 4 people":
            jump correct
        "1 in every 400 people":
            jump wrong
        "1 in every 40,000 people":
            jump wrong
    
    label correct:
        introduction_n "Corrent! In a study done by the World Health Organization, at some stage in life, one in every four people develop at least one mental or neurological disorder."
        jump game_background
    label wrong:
        introduction_n "Actually, in a study done by the World Health Organization, at some stage in life, 1 in every 4 people develop at least one mental or neurological disorder."
        jump game_background
     
label game_background:
    game_background_n "This game is designed to help you feel better and teach you important tools and exercises to help you cope with any negative emotions. 
                       It is based on the principles of Secure Self-Attachment Therapy."
    game_background_n "This game is designed to help people recreate and reinforce neural connections relating to healthy secure attachment types. 
                       It consists of three sections; each is fundamental to the therapy."
    game_background_n "The first section is to understand the background principles and scientific basis behind the therapy. 
                       It is important for the user to be aware of the workings of the therapy in order to make it more effective."
    game_background_n "This section must be completed to continue with the game and can be accessed again through the menu screen."
    game_background_n "The second section seeks to stimulate emotions rooting from your childhood. 
                       In this section you will have the chance to create childhood photo albums, listen to childhood songs and to document childhood stories."
    game_background_n "It is important that you expose yourself to these emotions, and do not be afraid if it gets overwhelming, as this is part of the therapy!"
    game_background_n "The third section of the game revolves around exercises that promote secure attachment type and it seeks to help you cope with any negative issues. 
                       Some of the exercises are instructional and some require more interaction and activity from you."
    game_background_n "It is important that you complete and understand earlier exercises before attempting later ones."
    game_background_n "Overall, Secure self-attachment therapy is firmly based on scientific principles, and it is important to have at least a basic understanding of these principles before undertaking the therapy.
                       There are three reasons for this:"
    game_background_n "1) To establish an understanding of the reasonableness of the therapy, even when some of the exercises might feel rather silly"
    game_background_n "2) To stimulate cognition and provide the mild to moderate levels of interest which are required for the formation of new neural pathways"
    game_background_n "3) To enable you to adapt the therapy's exercises to suit what works best for you."
    game_background_n "This game is designed to help you apply the protocols of secure self-attachment therapy through repetition.
                       By repeatedly applying the principles of the therapy they will become more effective, at the end of each round you will be asked how it affected you."
    game_background_n "This is used as part of the scoring to determine how well you are progressing."
    game_background_n "So it is important to be honest!"
    
    if globalvariables.first_time == True:
        game_background_n "Now lets begin with some background information regarding the therapy."
        jump therapy_background
        
label therapy_background:
        1