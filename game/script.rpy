# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



## Val's Voice
init python:
    def val_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("val.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## Mira's Voice
    def mira_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("mira2.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

## 2 Basic Male Voices
    def guy_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guy.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def guylow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guylow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
        
## 2 Basic Female Voices
    def girl_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girl.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def girllow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girllow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    
            
define v = Character("Val", callback=val_beep, color="#de9c01")
define m = Character("Mira", image = "mira", callback=mira_beep, color="#329b15")
define k = Character("Knight", callback=girllow_beep, color="#417ce4")


### Mira's Images. Lots of them.

image mira test = "mira neutral.png"
image small mira test = "dark small mira neutral.png"

image side mira neutral: 
    "side mira neutral.png"
    pause 2
    "side mira neutral blink.png"
    pause 0.4
    "side mira neutral.png"
    pause 0.5
    "side mira neutral blink.png"
    pause 0.4
    repeat

image side mira sad: 
    "side mira sad.png"
    pause 2
    "side mira sad blink.png"
    pause 0.4
    "side mira sad.png"
    pause 0.5
    "side mira sad blink.png"
    pause 0.4
    repeat


### Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            ("?", "? {w=.15}"),
            ("! ", "! {w=.15}"),
            (",", ", {w=.1}"),
            ( ". . .", ". . . {w=.15}"),
            (". ", ". {w=.15}"),
        ]

        for item in replacements:
            what = what.replace(item[0],item[1])
        
        return what
    
    config.say_menu_text_filter = typography

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
    "But you know it is somewhere here. Somewhere.{w=0.67}{nw}"

    scene scarytree 
    with Dissolve (3.0)

    m neutral "God, how am I supposed to get through a place like this?"
    m "{sc}This is absurd!{/sc} I thought the locals were exaggerating about these woods..."
    m "..."
    m "It doesn't matter. I've already come all this way, and I'm not stopping now!"
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You make your way into the wood.{/i}"

    scene placeholderforest
    with fade

    m neutral "I'm getting tired..."
    "You've been walking for hours, but haven't made any progress."
    "You'd figured the Heart would've been some kind of odd flower, but there is nothing here but gnarled, dark roots."

    
    show small mira test with dissolve
    "You see someone coming! Maybe you could ask them for help?"
    hide small mira test
    show mira test
    k "You! get away from here!"

    m neutral "Why? What's going on? Are you ok, sir?"
    "Clearly, he's not. You don't need your training to know this man is injured."
    k "We were fighting that {i}thing! {/i} I don't have time to explain this to you, I need to get out of here!"
    m neutral "I'm a doctor! At least let me help you before you go!"
    k "...Alright."
    
    hide mira test with moveoutright
    "He ran off!"
    
    m neutral "What did I just walk into? Maybe this was a bad idea..."
    m neutral "There must be more men that way. What if they need help?"

    v "lol. voice test words longwords short wprd ababava lelaluuu "
    m "omg do they sound next to eachothre"
    v "blebelne blah"
    m "this is most of the game honesly"
    v "bleha last aisblah"
   
    


    # This ends the game.

    return

