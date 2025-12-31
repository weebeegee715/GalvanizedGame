# The script of the game goes in this file.


# Thug Shake
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

        Shake = renpy.curry(_Shake)
    #

#

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


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
    
## Define Characters (Giving Them Color and Voices) 
define c = Character("Coachman", callback=guy_beep, color="#917dc8")
define mv = Character("???", callback=val_beep, color="#de9c01", what_size=40)          
define v = Character("Val", callback=val_beep, color="#de9c01", what_size=40)
define m = Character("Mira", image = "mira", callback=mira_beep, color="#329b15")
define mt = Character("Mira", image="nothing", color="#329b15", what_italic=True)
define k = Character("Knight", callback=guylow_beep, color="#417ce4")


### Mira's Images. Lots of them.
image sprite test = "sprite test.png"
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

image side mira scared: 
    "side mira scared.png"
    pause 2
    "side mira scared blink.png"
    pause 0.4
    "side mira scared.png"
    pause 0.5
    "side mira scared blink.png"
    pause 0.4
    repeat


# The game starts here.

label start:
    play music [ "fallingleaves.mp3", "piratesong.mp3", "Jonquil.mp3" , "piratesong2.mp3" ] fadeout 2.0 fadein 1.0 volume 0.5

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

    "The Darkheart, said to be the key to creating the mythical stone."
    "But, you don't quite know what this Darkheart is..."
    "But you know it is somewhere here.... Somewhere."

    scene forestentrance 
    with Dissolve (3.0)

    show sprite test
    c "I won't be taking you any further, miss."
    m angry "What!? But I need to go {i}through{/i} the forest! Why are we stopping at its entrance?"
    c "The sun is nearly setting, and I'm not getting caught in this place at night. Wouldn't taake you much farther in the day, either."
    m angry "You couldn't have told me this earlier?! This is a matter of urgency!"
    c "...I'm turning back now. Are you coming or not?"
    m angry "Most certainly not!"
    c "Suit yourself."
    hide sprite test with moveoutright
    
    show sprite test with dissolve
    m "This is absurd! how am I supposed to get through a place like this without a horse!? This is going to take ages."
    mt "And here I thought the locals were exaggerating about these woods! This explains why the property is so cheap around here, and why they'd even consider {i}my{/i} offer in the first place..."
    m "..."
    mt "It doesn't matter. I've already come all this way, and I'm not stopping now!"
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You make your way into the woods.{/i}"

    scene placeholderforest
    with fade
    m angry "I'm getting tired..."
    mt "I've been walking for hours, but haven't made any progress!"
    mt "I'd figured the Heart would've been some kind of odd flower, but there is nothing here but these {i}trees!{/i}"

    
    show small mira test with dissolve
    "You see someone coming! Maybe you could ask them for help?"
    hide small mira test
    show sprite test
    k "You! get away from here!"

    m confused "Why? What's going on? Are you ok, sir?"
    "Clearly, he's not. This guy needs help before his wounds get infected. Good thing I brought my bag."
    k "We were fighting that {i}thing! {/i} I don't have time to explain this to you, I need to get out of here!"
    m neutral "I'm a doctor! At least let me help you before you go."
    "He calms down a bit."
    k ". . . Alright. Think I've ran far enough for something quick."
    m happy "Good. I'll get out my things."

    hide sprite test
    scene black
    with fade
    play sound 'audio/bag.mp3'
    "Laying your supplies out, you begin to work."
    scene healcg
    with Dissolve (2.0)

    
    
    m "What happened to you? What on earth were you fighting?"
    k "There's a m-monster in these woods. We'd been paid by some men, men of high rank, to kill it! As soon as I saw it, I knew we'd made a mistake."
    k "That thing bested us in seconds! I ran away before it got any worse..."
    m "Surely you've faced this kind beast before?"
    k "No! This wasn't some typical monster, it was something else entirely! And by God, it was huge! it blocked out the moon!"
    m "Really? That's terrifying!"
    k "Yes, but, {i} we must be going now!{/i}"

    scene placeholderforest at truecenter
    with fade 
    show sprite test with dissolve
    k "{i}Thank you for all your help! Let's make haste!{/i}"
    "Should I go with him? I'm scared to continue, but, I may never have a chance like this to get the Heart again!"
    m sad "I'm sorry, but I can't leave just yet."
    k "{i}What?! Well, I'm not waiting around!{/i}"
    hide sprite test with moveoutright
    "He ran off!"

    show sprite test with dissolve
    mt "{i}How horrible... these woods truly are cursed! But... I need the heart! I won't give up!{/i}"
    # pls draw progressively more upset sprites plzzz
    show sprite test
    mt "{i}I'm woefully underprepared too... That man was armed to the teeth, and still made a run for it.{/i}"
    show sprite test
    mt "{i}...{/i}"
    # >:[ 
    show sprite test
    mt "I can't give up."
    
    hide sprite test with dissolve
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You go the direction the man you helped fled from.{/i}"

    show placeholderrevealblocked with fade
    m confused "...Huh?"
    show placeholderreveal

    show facereveal with fade
    mt "This... this is no monster! This is a person! Who would do this to s"
    mt "I... I need to help!"
    scene black
    with fade 
    play sound 'audio/bag.mp3'
    "You hardly have enough gauze to do anything of note. But you try."
    show facerevealhelped with fade

    mt "I didn't do much... but it's better than nothing."
    show facerevealhuh 
    mv "...hmmph?"
    m scared "{sc}Aah!{sc}"
    show facerevealawake
    mv "Aah!"
    
    show placeholderforest
    
    mv "Who are you?! What did you do to me?!"
    m scared "I-I'm sorry! You were bleeding!"
    mv "Huh?"
    "She turns her attention to your work."
    mv "Oh..."
    mv "Why would you do something like this for me?"
    m scared "I don't know! I won't bother you anymore, just don't hurt me!"
    mv "I won't! I'm terribly sorry for scaring you like that... Why're you in a place like this? At this hour?"
    m scared "I..."
    mv "I forget myself. I must be terrifying to you."

### SKIPPING LOL

I'm looking for something! I read that it only showed itself at night, but that's the only clue I have right now."

    
    
    
    
    

    # This ends the game.

    return

