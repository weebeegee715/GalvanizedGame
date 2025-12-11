# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def val_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("val.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def mira_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("mira.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
define v = Character("Val", callback=val_beep, color="#de9c01")
define m = Character("Mira", image = "mira", callback=mira_beep, color="#329b15")


# images of doom 

image side mira = "side mira neutral.png"


# Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            (".", ". {w=.15}"),
            ("?", "? {w=.15}"),
            ("!", "! {w=.15}"),
            (",", ", {w=.1}"),
        ]

        for item in replacements:
            what = what.replace(item[0],item[1])
        
        return what
    
    config.say_menu_text_filter = typography
    

default chill_points = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg house window with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "..."

    "Mira and Val are going to argue about a (TW) man! In my yuri!"

    
    show val annoyed with dissolve

    v "Are you off to see Heinrich again, Mira?"

    menu argue_start:
        "Yes, but I don't know why you say it like that.":
            $ chill_points += 1
            m annoyed "Yes, but I don't know why you say it like that."
            show val angry
            v "Like what?"
            m "Like that"
        "I have to be confidential about these things.":
            show val smirk
            m "Val, you know I'm not supposed to tell you that."
            v "Yes, yes... but you {i}are{/i}, right?"
            m annoyed "Val, I can't do this with you!"
        "No...":
            $ chill_points -= 1
            show val angry
            v "And now you are lying to me about it, Mira?"
            m sad " Oh, what do you want me to {i}say{/i} Val?!"
        
    m angry "He's a patient of mine, you understand that? I'm his doctor."

    show val annoyed

    v "I know that? What the hell are we even talking about Emie, you can go!"

    m annoyed "I can go You dont need to tell me! Why are you being so weird about this?"
    
    show val angry

    v "He tried to kill me. I get to be weird about it, Mira. "

    menu:
        "And you almost killed him too.":
            m sad "I understand you're uncomfortable, but I only have to do this because you tried to kill him too."
        "You {i}know{/i} how they lie to them, Val!":
            m sad "You know the lies they tell about you! They don't know you like I do. No one does."
            show val annoyed
            v "They blame me for every little problem in their lives, and try to kill me for it! You expect me to kindly educate them about how I'm actually quite pleasant when you get to know me while they're trying to gouge out my eyes?"
            m angry "I didn't say that! You just have to be better than them, Val."
            show val smirk
            v "I am better than them. What do you even mean by that?"
            m annoyed "It means you can't hurt them like you do. It's a horrible thing to do."
            show val angry 
            v "I can't {i}defend{/i} myself? Don't be ridiculous Mira, they have fucking swords."
            m angry "And you're... you."
            show val smirk
            v "I'm me?"
            m smile "You have an axe, you have your magic,  "


    # This ends the game.

    return

