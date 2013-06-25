define introduction_n = Character('Introduction', color="#c8ffc8")
define game_background_n = Character('Game Background', color="#c8ffc8")
define attachment_n = Character('Attachment Theory', color="#c8ffc8")
define brain_n = Character('Physical Brain', color="#c8ffc8")
define attachment_therapy_n = Character('Secure Self-Attachment Therapy', color="c8ffc8")
define forming_connection_n = Character('Forming Inner Child Bond', color="c8ffc8")
define strengthen_connection_n = Character('Strenthening Inner Child Bond', color="c8ffc8")
define protocol_n = Character('Attachment Exercises', color="c8ffc8")

image introduction 1 = "images/part1/introduction/image_introduction_1.png"
image introduction 2 = "images/part1/introduction/image_introduction_2.png"
image introduction 3 = "images/part1/introduction/image_introduction_3.png"
image introduction 4 = "images/part1/introduction/image_introduction_4.png"
image introduction 5 = "images/part1/introduction/image_introduction_5.png"
image introduction 6 = "images/part1/introduction/image_introduction_6.png"
image introduction 7 = "images/part1/introduction/image_introduction_7.png"
image introduction 8 = "images/part1/introduction/image_introduction_8.png"
image introduction 8 transparent = im.MatrixColor("images/part1/introduction/image_introduction_8.png",im.matrix.brightness(0.75))
image introduction 9 = "images/part1/introduction/image_introduction_9.png"
image introduction 10 = "images/part1/introduction/image_introduction_10.png"
image introduction 11 = "images/part1/introduction/image_introduction_11.png"
image introduction 12 = "images/part1/introduction/image_introduction_12.png"

image game_background 1 = "images/part1/game_background/image_game_background_1.png"
image game_background 2 = "images/part1/game_background/image_game_background_2.png"
image game_background 3 = "images/part1/game_background/image_game_background_3.png"
image game_background 4 = "images/part1/game_background/image_game_background_4.png"
image game_background 5 = "images/part1/game_background/image_game_background_5.png"
image game_background 6 = "images/part1/game_background/image_game_background_6.png"
image game_background 7 = "images/part1/game_background/image_game_background_7.png"
image game_background 8 = "images/part1/game_background/image_game_background_8.png"
image game_background 9 = "images/part1/game_background/image_game_background_9.png"
image game_background 10 = "images/part1/game_background/image_game_background_10.png"

image attachment_theory 1 = "images/part1/attachment_theory/image_attachment_theory_1.png"
image attachment_theory 2 = "images/part1/attachment_theory/image_attachment_theory_2.png"
image attachment_theory 3 = "images/part1/attachment_theory/image_attachment_theory_3.png"
image attachment_theory 4 = "images/part1/attachment_theory/image_attachment_theory_4.png"
image attachment_theory 5 = "images/part1/attachment_theory/image_attachment_theory_5.png"
image attachment_theory 6 = "images/part1/attachment_theory/image_attachment_theory_6.png"
image attachment_theory 7 = "images/part1/attachment_theory/image_attachment_theory_7.png"
image attachment_theory 8 = "images/part1/attachment_theory/image_attachment_theory_8.png"
image attachment_theory 9 = "images/part1/attachment_theory/image_attachment_theory_9.png"
image attachment_theory 10 = "images/part1/attachment_theory/image_attachment_theory_10.png"
image attachment_theory 11 = "images/part1/attachment_theory/image_attachment_theory_11.png"
image attachment_theory 12 = "images/part1/attachment_theory/image_attachment_theory_12.png"

image physical_brain 1 = "images/part1/physical_brain/image_physical_brain_1.png"
image physical_brain 2 = "images/part1/physical_brain/image_physical_brain_2.png"
image physical_brain 3 = "images/part1/physical_brain/image_physical_brain_3.png"
image physical_brain 4 = "images/part1/physical_brain/image_physical_brain_4.png"
image physical_brain 5 = "images/part1/physical_brain/image_physical_brain_5.png"
image physical_brain 6 = "images/part1/physical_brain/image_physical_brain_6.png"
image physical_brain 7 = "images/part1/physical_brain/image_physical_brain_7.png"
image physical_brain 8 = "images/part1/physical_brain/image_physical_brain_8.png"
image physical_brain 9 = "images/part1/physical_brain/image_physical_brain_9.png"
image physical_brain 10 = "images/part1/physical_brain/image_physical_brain_10.png"
image physical_brain 11 = "images/part1/physical_brain/image_physical_brain_11.png"
image physical_brain 12 = "images/part1/physical_brain/image_physical_brain_12.png"

init python:
    part1_menu_content = [
        ("introduction", "Introduction and Game Background"),
        ("attachment_theory", "Attachment Theory"),
        ("brain", "Physical Brain"),
        ("attachment_therapy", "Secure Self-Attachment Therapy"),
        ("forming_connection", "Forming Inner Child Bond"),
        ("strengthen_connection", "Strengthen Inner Child Bond"),
        ("protocol", "Game Exercises")
        ]

screen part1_menu_layout:

    side "c r":
        area (256,150,512,350)
        viewport:
            
            vbox:
                for label, name in part1_menu_content:
                    button:
                        action Return(label)
                        xfill True
                        
                        hbox:
                            text name style "button_text" min_width 500
                            
                null height 20
                
                textbutton "Back":
                    xfill True
                    #action Quit(confirm=True)
                    action Jump(label='transition')
                    
label part1_menu:
    call screen part1_menu_layout()
    call expression _return

label introduction:
    show introduction 1
    with fade
    
    if globalvariables.first_time == True:
        introduction_n "Welcome to the Secure-Self Attachment game!"
        
    introduction_n "The feelings of depression, anxiety and other mental disorders are unwanted and can be hard to bear at times.
                    With neglect and improper treatment, these conditions can affect an individual's quality of life."
    
    introduction_n "Feelings of stress and anxiety are often easily provoked by stressful situations."
    
    show introduction 2
    introduction_n "A few examples include work problems"
    show introduction 3
    introduction_n "relationship problems"
    show introduction 4
    introduction_n "family issues"
    show introduction 5
    introduction_n "problems relating to death"
    show introduction 6
    introduction_n "and financial problems."
    show introduction 1
    with hpunch
    with Pause(0.5)
    show introduction 8
    with Dissolve(1.5)
    show introduction 9
    with fade
    
    introduction_n "These problems may cause overwhelming levels of stress and anxiety and without proper treatment and care..."
    show introduction 10
    introduction_n "may lead to more serious mental issues including depression and other mental disorders."
    
    show introduction 8
    with fade
    show introduction 8 transparent
    with Dissolve(0.5)

    menu:
        introduction_n "Can you guess how many people develop at least one mental or neurological disorder at some stage in life?"
        "1 in every 4 people":
            jump correct
        "1 in every 400 people":
            jump wrong
        "1 in every 40,000 people":
            jump wrong
    
    label correct:
        show introduction 11
        with dissolve
        introduction_n "Corrent! In a study done by the World Health Organization, at some stage in life, one in every four people develop at least one mental or neurological disorder."
        show introduction 12
        with dissolve
        introduction_n "Hence mental disorder is a global and serious problem facing humanity and this game seeks to provide an alternate method for treatment."
        jump game_background
    
    label wrong:    
        show introduction 11
        with dissolve
        introduction_n "Actually, in a study done by the World Health Organization, at some stage in life, 1 in every 4 people develop at least one mental or neurological disorder."
        show introduction 12
        with dissolve
        introduction_n "Hence mental disorder is a global and serious problem facing humanity and this game seeks to provide an alternate method for treatment."
        jump game_background
     
label game_background:
    show game_background 1
    with fade
    game_background_n "This game is designed to help you feel better and teach you important tools and exercises to help you cope with any negative emotions. 
                       It is based on the principles of Secure Self-Attachment Therapy."
    show game_background 2
    with dissolve
    game_background_n "This game is designed to help people recreate and reinforce neural connections relating to healthy secure attachment types."
    game_background_n "It consists of three sections; each is fundamental to the therapy."
    show game_background 3
    with fade
    show game_background 4
    with dissolve
    game_background_n "The first section is to understand the background principles and scientific basis behind the therapy. 
                       It is important for the user to be aware of the workings of the therapy in order to make it more effective."
    game_background_n "This section must be completed to continue with the game and can be accessed again through the menu screen."
    show game_background 5
    with fade
    show game_background 6
    with dissolve
    game_background_n "The second section seeks to stimulate emotions rooting from your childhood. 
                       In this section you will have the chance to create childhood photo albums, listen to childhood songs and to document childhood stories."
    game_background_n "It is important that you expose yourself to these emotions, and do not be afraid if it gets overwhelming, as this is part of the therapy!"
    show game_background 7
    with fade
    game_background_n "The third section of the game revolves around exercises that promote secure attachment type and it seeks to help you cope with any negative issues."
    show game_background 8
    with dissolve
    show game_background 9
    with dissolve
    game_background_n "Some of the exercises are instructional and some require more interaction and activity from you."
    game_background_n "It is important that you complete and understand earlier exercises before attempting later ones."
    show game_background 10
    with fade
    game_background_n "Overall, Secure self-attachment therapy is firmly based on scientific principles, and it is important to have at least a basic understanding of these principles before undertaking the therapy.
                       There are three reasons for this:"
    game_background_n "First, to establish an understanding of the reasonableness of the therapy, even when some of the exercises might feel rather silly"
    game_background_n "Second, to stimulate cognition and provide the mild to moderate levels of interest which are required for the formation of new neural pathways"
    game_background_n "Third, to enable you to adapt the therapy's exercises to suit what works best for you."
    game_background_n "This game is designed to help you apply the protocols of secure self-attachment therapy through repetition.
                       By repeatedly applying the principles of the therapy they will become more effective, at the end of each round you will be asked how it affected you."
    game_background_n "This is used as part of the scoring to determine how well you are progressing."
    game_background_n "So it is important to be honest!"
    
    if globalvariables.first_time == True:
        game_background_n "Now lets begin with some background information regarding the therapy."
        jump attachment_theory
    else:
        jump part1_menu
        
label attachment_theory:
    show attachment_theory 1
    with fade
    attachment_n "Attachment theory is a psychological model developed by John Bowlby and Mary Ainsworth. 
                  It is the study of bonds between people and their lasting impacts on psychological well being."
    show attachment_theory 2
    with fade
    attachment_n "The theory concerns the need of every infant to develop an emotionally supportive and dependent relationship with a primary caregiver, whom they become attached to."
    show attachment_theory 3
    with dissolve
    attachment_n "The main focus is the type of attachment that develops for the individual infant to their caregiver."
    show attachment_theory 4
    with dissolve
    show attachment_theory 5
    with dissolve
    attachment_n "The attachment type the individual develops during childhood could have a lasting impact on the individual.
                  In order to develop a normal social and emotional behavior, am infant should develop a 'secure' attachment relationship with at least one caregiver."
    show attachment_theory 6
    with dissolve
    show attachment_theory 7
    with Dissolve(1.0)
    show attachment_theory 8
    attachment_n "Depending on the relationship between the infant and the caregiver, the infant could develop an insecure attachment relationship with their caregiver. 
                  This could be problematic in later stages of life in forms of mental and behavioral problems."
    show attachment_theory 9
    with fade
    attachment_n "There are three types of insecure attachments, avoidant, disorganized and anxious attachment."
    show attachment_theory 10
    with fade
    attachment_n "Without a secure attachment, the patterns that are formed during infancy have a big effect on the individual at later stages of life."
    show attachment_theory 11
    with dissolve
    show attachment_theory 12
    with dissolve
    attachment_n "The lack of a secure attachment during an individual's childhood can have a profound negative impact on an adult's interpersonal relationships and parenting ability, 
                  as well as the individual's contentment at work."
    
    if globalvariables.first_time == True:
        attachment_n "To understand the workings of the therapy, we must first start from understanding the structure of our physical brain."
        jump brain
    else:
        jump part1_menu
    
label brain:
    show physical_brain 1
    with fade
    with Pause(1.2)
    show physical_brain 2
    with fade
    brain_n "'The Truine Brain' theory states that the brain is composed of 3 components."
    show physical_brain 3
    with dissolve
    brain_n "Each of these components represents the different levels of sophistication developed throughout evolution."
    show physical_brain 4
    with dissolve
    brain_n "The first component is known as the 'Reptilian Brain', which is the most basic component and acts as the core of the brain."
    show physical_brain 5
    with dissolve
    brain_n "The second component is known as the 'Limbic System', which processes emotions and memories."
    show physical_brain 6
    with dissolve
    brain_n "The third component is known as the 'Cerebral Cortex', which is responsible for reasoning and the overall consciousness of the individual."
    show physical_brain 7
    with dissolve
    show physical_brain 8
    with dissolve
    brain_n "The cerebral cortex is further divided into four lobes."
    show physical_brain 9
    with dissolve
    brain_n "The frontal lobe is responsible with reasoning and attention.occipital lobe deals with visual processing."
    show physical_brain 10
    with dissolve
    brain_n "The occipital lobe deals with visual processing."
    show physical_brain 11
    with dissolve
    brain_n "The parietal lobe controls the body and movement."
    show physical_brain 12
    with dissolve
    brain_n "Finally the temporal lobe is responsible with language, hearing and memories."
    show physical_brain 5
    with dissolve
    brain_n "The limbic system contains the amygdala, which deals with emotional understanding and fear. It also contains the hippocampus, which is associated with the modulation of memory and emotion."
    brain_n "Although a generalization, some functions in the brain are lateralized meaning that they are predominantly processed in either the right or left side of the brain."
    brain_n "In simplified terms, the left side of the brain is responsible for logic and language and the right side of the brain is responsible for creativity and emotion."
    brain_n "The integration and communication between the two sides or hemispheres of the brain is essential in therapy. The reason is that the cerebral cortex has many connections to the hippocampus, amygdala and other limbic system structures."
    brain_n "Many psychological disorders, including depression and anxiety are associated with a lower efficiently in the communication between the brain's two hemispheres."
    brain_n "Secure Self-Attachment Therapy focuses on these neuron connections and seeks to form and reinforce healthy and efficient connections."
    
    if globalvariables.first_time == True:
        brain_n "To understand the workings of the therapy, we must first start from understanding the structure of our physical brain."
        jump attachment_therapy
    else:
        jump part1_menu
        
label attachment_therapy:
    attachment_therapy_n "Secure Self-Attachment Therapy is a new technique developed to treat individuals suffering from problems rooting from unhealthy attachment developed during infancy. 
                          It aims to form and strengthen an attachment link that mirrors the relationship between a caregiver and a child internally."
    attachment_therapy_n "The therapy seeks to form the missing or weak neural connections between the left and right hand side of the subject's brain. 
                          During the therapy and through normal healthy attachment, the active right hand side of the brain will seek to establish a connection or attachment with the left hand side of the brain."
    attachment_therapy_n "The metaphor that is commonly used to describe this therapy is that the right hand side of the brain takes the role of the adult caregiver and the right hand side of the brain takes the role of the individual's inner child."
    attachment_therapy_n "Through mental process, the neural patterns that represent a healthy attachment can be formed and gradually strengthened."
    
    if globalvariables.first_time == True:
        attachment_therapy_n "Secure Self-Attachment Therapy is composes of 3 critical processes. It is important that we understand these processes before starting this game. The first process of the therapy is to form a connection between the 'adult' and the 'inner child'."
        jump forming_connection
    else:
        jump part1_menu

label forming_connection:
    forming_connection_n "Forming a compassionate and devoted bond with your inner child is a crucial process in this therapy. 
                          The neural connections associated to falling in love with or caring deeply for another person, in this case your inner child, must be established as this is where the basis of the therapy stems from."
    forming_connection_n "In this game, a profile of a child is built. This child is a representation of you as a child. Through this profile, you should build a strong sense of your childhood as well as concentrating on how lovable this child is."
    forming_connection_n "Once ready, the game will prompt you to make a promise to care and look after this child. It is important that this promise is genuine so please do not rush this decision!"
    forming_connection_n "If you are unsure of this decision, it is suggested to spend more time with building your child's profile."
    
    if globalvariables.first_time == True:
        forming_connection_n "The second process that is crutial to Secure Self-Attachment Therapy is to strengthen the connection and bond between you and your inner child."
        jump strengthen_connection
    else:
        jump part1_menu
        
label strengthen_connection:
    strengthen_connection_n "It is important that once an emotional bond for your inner child is formed, that this neural connection is strengthened. 
                             Once these healthy attachment connections are strengthened enough, the previous neural connections relating to unhealthy insecure attachment can be overshadowed."
    strengthen_connection_n "In this game, there are 2 tools that are repeatedly used to aid the process of the therapy."
    strengthen_connection_n "The first tool is the use of affirmations. It is important that you choose affirmations that you identify yourself with and to memorize and recite them."
    strengthen_connection_n "The second tool is the use of music. You should try to pick songs of particular resonance to your childhood or songs that make you feel positive."
    strengthen_connection_n "This game will allow you to learn the lyrics to allow you to recite and sing the songs with ease, especially during times of stress or while being overwhelmed with negative emotions. 
                             The aim of listening to or singing these songs is to remind you of the strong commitment you have made with your inner child."
    strengthen_connection_n "You should make a conscious effort to associate the affirmations and songs with your bond with your inner child."
    
    if globalvariables.first_time == True:
        strengthen_connection_n "The third and final process that is crutial to Secure Self-Attachment Therapy is to exercise with protocols that activate healthy attachment connections."
        jump protocol
    else:
        jump part1_menu
        
label protocol:
    protocol_n "Secure Self-Attachment Therapy involves protocols and exercises that seek to enforce positive emotions and to further strengthen the bond between you and your inner child."
    protocol_n "The protocols are either instructional or requires interaction from you. 
                These protocols are based on Game Theory and designed so that your progress can be recorded, analyzed and structured to best cater the individual playing the game."
    protocol_n "Through repetitions of these protocols,  the neural connections relating to healthy attachment can be reinforced and help to overshadow the insecure attachment connections."
    
    if globalvariables.first_time == True:
        jump transition
    else:
        jump part1_menu
    
label transition:
    menu:
        "Hopefully you will now have a good understanding of the workings and structure of this game as well as the scientific principles behind it. Would you like to go through any of the topics again?"
        "Yes":
            jump part1_menu
            
        "No":
            $globalvariables.first_time = False
            "Remember if you wish to revisit the introduction and background information, it can be accessed in the main menu."
            "Let's begin the game by creating your inner child profile"
        