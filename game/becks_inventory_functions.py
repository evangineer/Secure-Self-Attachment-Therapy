# This script contains the functions required for setting up and maintaining Beck's
# Depressino and Anxiety Inventory. 

def setup_depression_questions():
    return [["I do not feel sad.","I feel sad.","I am sad all the time and I can't snap out of it.","I am so sad and unhappy that I can't stand it."],\
            ["I am not particularly discouraged about the future.","I feel discouraged about the future.","I feel I have nothing to look forward to.","I feel the future is hopeless and that things cannot improve."],\
            ["I do not feel like a failure.","I feel I have failed more than the average person.","As I look back on my life, all I can see is a lot of failures.","I feel I am a complete failure as a person."],\
            ["I get as much satisfaction out of things as I used to.","I don't enjoy things the way I used to.","I don't get real satisfaction out of anything anymore.","I am dissatisfied or bored with everything."],\
            ["I don't feel particularly guilty.","I feel guilty a good part of the time.","I feel quite guilty most of the time.","I feel guilty all of the time."],\
            ["I don't feel I am being punished.","I feel I may be punished.","I expect to be punished.","I feel I am being punished."],\
            ["I don't feel dissapointed in myself","I am disappointed in myself.","I am disgusted with myself.","I hate myself."],\
            ["I don't feel I am any worse than anybody else.","I am critical of myself for my weaknesses or mistakes.","I blame myself all the time for my faults.","I blame myself for everything bad that happens."],\
            ["I don't have any thoughts of killing myself.","I have thoughts of killing myself, but I would not carry them out.","I would like to kill myself.","I would kill myself if I had the chance."],\
            ["I don't cry any more than usual.","I cry more now than I used to.","I cry all the time now.","I used to be able to cry, but now I can't cry even though I want to."],\
            ["I am no more irratated by things than I ever was.","I am slightly more irritated now than usual.","I am quite annoyed or irritated a good deal of the time.","I feel irritated all the time."],\
            ["I have not lost interest in other people.","I am less interested in other people than I used to be.","I have lost most of my interest in other people.","I have lost all of my interest in other people."],\
            ["I make decisions about as well as I ever could.","I put off making dicisions more than I used to.","I have greater difficulty in making decisions more than I used to.","I can't make decisions at all anymore."],\
            ["I don;t feel that I look any worse than I used to.","I am worried that I am looking old or unattractive.","I feel there are permanent changes in my appearance that make me look unattractive.","I believe that I look ugly."],\
            ["I can work about as well as before.","It takes extra effort to get started at doing something.","I have to push myself very hard to do anything.","I can't do any work at all."],\
            ["I can sleep as well as usual.","I don't sleep as well as I used to.","I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.","I wake up several hours earlier than I used to and cannot get back to sleep."],\
            ["I don't get more tired than usual.","I get tired more easily than I used to.","I get tired from doing anything.","I am too tired to do anything."],\
            ["My appetite is no worse than usual.","My appetite is not as good as it used to be.","My appetite is much worse now.","I have no appetite at all anymore."],\
            ["I haven't lost much weight, if any, lately.","I have lost more than five pounds.","I have lost more than ten pounds.","I have lost more than fifteen pounds."],\
            ["I am no more worried about my health then usual.","I am worried about my physical problems like aches, pains, upset stomach, or constipation.","I am very worried about physical problems and it's hard to think of much else.",\
             "I am so worried about my physical problems that I cannot think of anything else."],\
            ["I have not noticed any recent change in my interest in sex.","I am less interested in sex than I used to be.","I have almost no interest in sex.","I have lost interest in sex completely."]]
    
def depression_score_meaning(score):
    if score == 0:
        return "No Depression"
    elif score >= 1 and score <= 10:
        return "These ups and downs are considered normal"
    elif score >= 11 and score <= 16:
        return "Mild mood disturbance"
    elif score >= 17 and score <= 20:
        return "Borderline clinical depression"
    elif score >= 21 and score <= 30:
        return "Moderate depression"
    elif score >= 31 and score <= 40:
        return "Severe depression"
    elif score >= 41:
        return "Extreme depression"
    else:
        return "Invalid Score!"
    
def setup_anxiety_questions():
    return ["Numbness or tingling.",\
            "Feeling hot.",\
            "Wobbliness in legs.",\
            "Unable to relax.",\
            "Fear of worst happening.",\
            "Dizzy or lightheaded.",\
            "Heart pounding/racing.",\
            "Unsteady.",\
            "Terrified or affraid.",\
            "Nervous.",\
            "Feeling of choking.",\
            "Hands trembling.",\
            "Shaky/unsteady.",\
            "Fear of losing control.",\
            "Difficulty in breathing.",\
            "Fear of dying.",\
            "Scared.",\
            "Indigestion.",\
            "Faint/lightheaded.",\
            "Face flushed.",\
            "Hot/cold sweats."]
    
def setup_anxiety_responses():
    return ["Not at all.","Mildly but it didn't bother me much.","Moderately - it wasn't pleasant at times.","Severely - it bothered me a lot."]
    
def anxiety_score_meaning(score):
    if score >= 0 and score <= 21:
        return "Very low anxiety. That is usually a good thing. However, it is possible that you might be unrealistic in either your assessment which would be denial or that you have learned to 'mask' the symptoms commonly \
                associated with anxiety. Too little 'anxiety' could indicate that you are detached from yourself, others, or your environment."
    elif score >= 22 and score <= 35:
        return "Moderate anxiety. Your body is trying to tell you something. Look for patterns as to when and why you experience the symptoms described above. For example, if it occurs prior to public speaking and your job \
            requires a lot of presentations you may want to find ways to calm yourself before speaking or let others do some of the presentations. You may have some conflict issues that need to be resolved. Clearly, it \
            is not 'panic' time but you want to find ways to manage the stress you feel."
    elif score >= 36:
        return "Severe Anxiety. This is a potential for concern. Look for patterns or times when you tend to feel the symptoms you have described. Persistent and high anxiety is not a sign of personal weakness or failure. It \
            is, however, something that needs to be proactively treated or there could be significant impacts to you mentally and physically. You may want to consult a physician or counselor if the feeling persists."