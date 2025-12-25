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
image mira test = "mira neutral.png"

image side mira neutral: 
    "side mira neutral.png"
    pause 3
    "side mira neutral blink.png"
    pause 0.3
    repeat

# Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            ("?", "? {w=.15}"),
            ("!", "! {w=.15}"),
            (",", ", {w=.1}"),
            ( "...", "... {w=.15}"),
        ]

        for item in replacements:
            what = what.replace(item[0],item[1])
        
        return what
    
    config.say_menu_text_filter = typography
    

# Val's points
default chill_points = 0

# The game starts here.

label start:
    play music 'audio/fallingleaves.mp3' fadein 0.3 volume 0.5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene paper1
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



        

    # These display lines of dialogue.

    "The Philosopher's Stone. The all-powerful stone said to grant untold powers to it's wielder."
    
    "Most chase it for eternal youth, or Midas' golden touch. But those don't matter to you. What you seek is greater."

    scene paper2
    with dissolve

    "The Panacea, A substance to cure all illness, lift all curses, and bring perferct health to the human form. The very pinnacle of medicine."
    "You have tried mixing sulfur and mercury in every fashion to no avail. But there is one thing you haven't tried..."

    scene paper3
    with dissolve

    "The Heart of Darkness, said to be the key to creating the mythical stone."
    "But, you don't quite know what this Heart of Darkness is..."
    "But you know it is somewhere here. Somewhere.{w=0.6}{nw}"

    scene scarytree 
    with Dissolve (3.0)

    m neutral "God, how am I supposed to get through a place like this?"
    m "{sc}This is absurd!{/sc} I thought the locals were exaggerating..."
        

    show mira test with moveinleft
    "Mira" "yoo wsg!!"
    m neutral "AAA wtf"
    "Mira" "I'm you bro"
    m neutral "no tf you're not!!!"
    "Mira" "tighten up z..."
    hide mira test with moveoutright

    
   
    


    # This ends the game.

    return

