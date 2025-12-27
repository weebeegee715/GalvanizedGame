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

##  Basic Male Voice 1
    def guy_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guy.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
## Basic Male Voice 2
    def guylow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guylow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
        
##  Basic Female Voice 1
    def girl_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girl.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
##  Basic Female Voice 2
    def girllow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girllow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    
            
define v = Character("Val", callback=val_beep, color="#de9c01")
define m = Character("Mira", image = "mira", callback=mira_beep, color="#329b15")
define k = Character("Knight", callback=guylow_beep, color="#417ce4")


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

image side mira angry: 
    "side mira angry.png"
    pause 2
    "side mira angry blink.png"
    pause 0.4
    "side mira angry.png"
    pause 0.5
    "side mira angry blink.png"
    pause 0.4
    repeat

image side mira happy: 
    "side mira happy.png"
    pause 2
    "side mira happy blink.png"
    pause 0.4
    "side mira happy.png"
    pause 0.5
    "side mira happy blink.png"
    pause 0.4
    repeat

image side mira confused: 
    "side mira confused.png"
    pause 2
    "side mira confused blink.png"
    pause 0.4
    "side mira confused.png"
    pause 0.5
    "side mira confused blink.png"
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
    play music [ "fallingleaves.mp3", "Pirate4.mp3", "Jonquill.mp3" , "Pirate5.mp3" ] fadeout 1.0 fadein 1.0 volume 0.5

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

    "The Sylvanian Heart, said to be the key to creating the mythical stone."
    "But, you don't quite know what this Sylvanian Heart is..."
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
    "{i}You make your way into the woods.{/i}"

    scene placeholderforest
    with fade

    m neutral "I'm getting tired..."
    "I've been walking for hours, but haven't made any progress!"
    "I'd figured the Heart would've been some kind of odd flower, but there is nothing here but these {i}trees!{/i}"

    
    show small mira test with dissolve
    "You see someone coming! Maybe you could ask them for help?"
    hide small mira test
    show mira test
    k "You! get away from here!"

    m neutral "Why? What's going on? Are you ok, sir?"
    "Clearly, he's not. This guy needs help before his wounds get infected. Good thing I brought my bag."
    k "We were fighting that {i}thing! {/i} I don't have time to explain this to you, I need to get out of here!"
    m neutral "I'm a doctor! At least let me help you before you go."
    "He calms down a bit."
    k ". . . Alright. Think I've ran far enough to be safe."
    m "Sit. I'll get out my things."

    hide mira test
    scene black
    with fade
    "Laying your supplies out, you begin to work."
    scene healcg
    with Dissolve (2.0)

    
    
    m "What happened to you? What on earth were you fighting?"
    k "There's a m-monster in these woods. We'd been paid by some men, men of high rank, to kill it! As soon as I saw it, I knew we'd made a mistake. It did all this to me in seconds! I ran away before it got any worse..."
    m "Some kind of large animal? Surely you've faced beasts before."
    k "Of course I have, but nothing like that! It wasn't a beast at all. It was something else entirely! And by God, it was huge!"
    m "How awful!"
    k "I'm not supposed to tell you but they're not killing it to keep citizens safe! Those alchemists, they want its heart!"
    m "...It's heart?"
    k "Ah! I've already told you too much. {i}I'll say no more!{/i}"

    scene placeholderforest with fade
    show mira test
    k "Shall we be off? I lost my horse, so we'll have to walk back."
    "I really should go, but can I? I may never have a chance to get the Heart again!"
    m neutral "I'm sorry, but I can't leave just yet."
    k "{i}Thank you miss!{/i}"
    hide mira test with moveoutright
    "He ran off!"
    show side mira neutral
    "I should've known I wasn't the only one to be looking for the Heart! It'd be bad if I ran into any sanctioned alchemists - they'd throw me in jai if they found I knew anything their craft!"
    "It seems I'm woefully underprepared too. I wasn't coming here for a fight!"


    # This ends the game.

    return

