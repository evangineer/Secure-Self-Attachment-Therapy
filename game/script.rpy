# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
        import globalvariables

# The game starts here.
label start:

    if globalvariables.first_time == True:
        jump introduction
    else:
        jump part2_menu

    return
