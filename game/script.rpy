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
define m = Character("Mira", callback=mira_beep, color="#329b15")

# Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            (".", ". {w=.2}"),
            ("?", "? {w=.25}"),
            ("!", "! {w=.25}"),
            (",", ", {w=.15}"),
        ]

        for item in replacements:
            what = what.replace(item[0],item[1])
        
        return what
    
    config.say_menu_text_filter = typography


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "I bet this will be a {i}short scene{/i}, yeah?"

    v "yeah, probably like one scene at most to learn to make it."

    m "It'll have a simple point system, probably."

    v "I bet it will."

    m "Looking forward to making the UI for it!"

    v "Are we?"

    m"...no."

    # This ends the game.

    return
