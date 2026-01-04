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
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=4)


### Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            ("? ", "? {w=.15}"),
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
define mv = Character("???", image="val", callback=val_beep, color="#de9c01", what_size = 37)          
define v = Character("Val", image = "val",callback=val_beep, color="#de9c01", what_size = 37)
define m = Character("Mira", image = "mira", callback=mira_beep, color="#329b15")
define mt = Character("Mira", image="nothing", color="#329b15", what_italic=True)
define k = Character("Knight", callback=guylow_beep, color="#417ce4")
define o = Character("O'Keefe", callback=guylow_beep, color="#ca4c4c")
define l = Character("Lavinia", callback=girl_beep, color="#128f9aff")


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
    "Guarded by a terrible beast in a tall, dark wood, only showing itself in the dead of night."
    "But, you scarcely believe in monsters..."
  

    scene forestentrance 
    with Dissolve (3.0)

    show sprite test
    c "I won't be taking you any further, miss."
    m angry "What!? But I need to go {i}through{/i} the forest! Why are we stopping at its entrance?"
    c "The sun is nearly setting, and I'm not getting caught in this place at night. Wouldn't taake you much farther in the day, either."
    m angry "You couldn't have told me this earlier?! This is a matter of urgency!"
    c "I'm turning back now. Are you coming or not?"
    m angry "Most certainly not!"
    c "Suit yourself."
    hide sprite test with moveoutright
    
    show sprite test with dissolve
    m "This is absurd! how am I supposed to get through a place like this without a horse!? This is going to take ages."
    mt "And here I thought the locals were exaggerating about these woods! This explains why the property is so cheap around here, and why they'd even consider {i}my{/i} offer in the first place."
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
    mt "I'd figured the Heart would've been some kind of odd flower, but there is {i}nothing{/i} here!"

    
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
    k "That thing bested us in seconds! I ran away before it got any worse."
    m "Surely you've faced this kind beast before?"
    k "No! This wasn't some typical monster, it was something else entirely! It had magic, like a witch! And by God, it was huge! it blocked out the moon!"
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
    mt "{i}How horrible... these woods truly are cursed! But I need the heart! I won't give up!{/i}"
    # pls draw progressively more upset sprites plzzz
    show sprite test
    mt "{i}I'm woefully underprepared too. That man was armed to the teeth, and still made a run for it.{/i}"
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

    scene placeholderrevealblocked with fade
    m confused "Huh?"
    scene placeholderreveal
    ""

    scene facereveal with fade
    mt "This is no monster! This is a person! Who would do this to s"
    mt "I- I need to help!"
    scene black
    with fade 
    play sound 'audio/bag.mp3'
    "You hardly have enough gauze to do anything of note. But you try."
    scene facerevealhelped with fade

    mt "I didn't do much, but it's better than nothing."
    scene facerevealhuh 
    mv "...hmmph?"
    m scared "{sc}Aah!{sc}"
    scene facerevealawake
    mv "Aah!"


    "LOL WHAT DO I EVEN PUT BETWEEN THIS?"

    ####

    scene librarydark1 at truecenter 
    with fade

    m confused "Where am I?"
    mt "This isn't my bed. I haven't slept this well in a while."

    "You try and throw the sheet off of you. It's much heavier than you expected it to be... "
    m confused "...huh?"

    
    "Early morning light shines through the room from an excessively large window behind you, but you cannot make out the walls. It's like this room goes on forever."
    m confused "Where's the door?!"

    scene librarydark2 at truecenter
    with dissolve

    
    "More light spills into the room, and it begins to yawn before you."
    m scared "What is this place?!"
    mt "It's huge! My head is starting to spin."

    "You hear something through the wall."

    # "I didn't want to wake you then." < :[
    mv "{bt=3}{size=45}This is taking foreverrr...{/size}{/bt}"
    mv "{bt=3}{size=45}Is she {i}seriously{/i} still asleep?{/size}{/bt}"
    
    mt "That voice! From last night! Don't tell me..."
    "You feel the ground, no doubt some shelf or table, shake beneath you as the witch comes closer." with sshake
    m sad "What do I do?"
    mv "..." with sshake
    ## wallking sfx
    mt "Hide!"
    scene darklairthrow
    "You pull the heavy quilt back over your head. "
    scene black with dissolve
    mt "This was a horrible idea! A horrible, no good, awful idea!"
    #### door creak
    mt "She must be staring dead at me..."
    mv "I know you're up. I heard you."
    scene librarydark2
    with dissolve
    show val blue desk sleepy with dissolve
    m scared "..."
    "She doesn't seem to be fazed by your expression of abject terror. She looks like she hasn't slept all night."
    mv "{i}Finally.{/i} I felt like I was waiting forever. Let's do this quickly."
    mv "You want to leave this place, don't you?"
    m "{sc=3}{size=27}yes. please.{/size}{/sc}"
    mv "Good. Here's how this is going to go. I'm going to apport us to the edge of the woods, you're going to go back to wherever you came from, and then we never have to see eachother again. Okay?"
    m "{sc=3}{size=27}{i}apport{/i} us? like, with magic?{/size}{/sc}"
    mv "What, you think I'm going to hike you there? Yes, magic. Come now."
    scene handwalk with fade
    "She reaches her hand out to you. It's odd walking from the flat table to her shifting hand."
    mv "Okay..."
    "She pulls something heavy from under the table with her off-hand."
    scene teleport1 with fade
    m scared "{sc=5}Why do you have an axe?!{/sc}"
    mv "God, stop yelling. It's my wand, and we're not going anywhere without it."
    m neutral "{sc=3}Well...{/sc} okay."
    scene teleport2
    mv "This is going to take a bit. I'm real tired."
    m "So, you're okay from yesterday? Did you sleep?"
    mv "Huh? Yeah, I'm fine. I usually sleep during the day anyway. Less people at night."
    m "You can't heal with magic?"
    mv "{i}No.{/i} If people could heal with spells, wouldn't you be out of a job?"
    m "...I suppose."
    mv "..."
    m "You live alone?"
    mv "Of course I do. There's no one else here."
    m happy "I'm Mira. Do you have a name?"
    mv "..You talk too much, Mira."
    mt "I do not!"
    scene teleport3 with fade 
    m scared "Aah!"
    mt "That felt really, really weird! How is she used to that?!"
    scene teleport4
    mv "Well, we're here. What were you even doing here to begin with?"
    m sad "I was looking for an ingredient for a drug. A cure-all, essentially. But now, I'm right back where I started."
    mv "Really?"
    # chased from last town?
    m sad "I bought a property right by here, too! I planned to work and live here until it was completed, but it seems it was all a waste."
    mt "I don't think she cares very much, but it's nice to talk to someone."
    mv "I see."
    scene black with dissolve
    "She sets you down, and you ungracefully climb out of her hand."
    scene forestentrance with fade
    mt "I wonder what I'll do now..."
    mv "Mira?"
    "You must be quite far away from her now, but can hear her clear as day."
    m sad "Yes?"
    v "...Im Val. Valencia. But just call me Val."
    m happy "You have a pretty name, Val."
    "..."
    mt "I guess she left."
    m scared "God, what time is it? I need to get back!"

    scene end1 with fade
    "{b}Part 1 '' End.{/b}" 

    scene black with fade
    "Part 2 '"

    m confused "An actual witch... I never thougt I'd meet one."
    mt "I'm still trying to make sense of it all... She wasn't very cruel, at least not to me. Aren't they supposed to be wicked? Even more so, giants?"
    mt "I didn't even know they were real! Sure, you have monsters, and they get quite large, but they aren't people! They don't talk and joke and live in houses! I have so many questions..."
    mt "Maybe she just pitied me? I wish I could just ask her. But what would I even say, 'Hello Val, why aren't you evil? Also, is there a whole race of big people or is that just a you thing? "
    #house!
    m happy "My house!"
    mt "I'm still shocked I got the last owner to sell it to me. He was so eager to part with the land, he didn't care it wasn't totally legal to let me buy it."
    m sad "I'm so tired from that walk. I should really invest in a horse, shouldn't I?"

    scene black with fade
    "You go inside."
    m "I really am pleased with how I laid everything out. I was able to take most of things from my last practice, but it was hard getting everything in the new space."
    mt "Whenever I set up in a new area, I always try to work on the first floor and live upstairs. It's easier that way."
    m "I just hope these townsfolk are nicer than the last!"
    mt "The last town... Crayport? Crawport? All I remember was that my reputation preceded me there. Always felt like they were one misstep away from stoning me dead. Only reason they didn't was the fact they'd be out of a town doctor."
    mt "And there was that awful old man! God, what was his name?"

    ...

    m angry "O'Keefe, do you have anything actually wrong with you, or are you just going to complain about me?"
    o "I can do what I please, you witch! You may have some of these poor soul fooled, but not me!"
    m confused "What is this even about, sir? What'd I ever do to you? I was your daughter's midwife!"
    o "Oh, and she has heard from me on that! I can speak all day on all this magic around this place, but it's not that. It's the way you look down on us."
    m "Look {i}down{/i} on you?"
    o "Yes! You come from that college so relieved to be rid of the scandal of having a woman in their midst. And The King's College, damn them, actually gave you that piece of paper! And all you do is wave it at us!"
    m "You feel as if I'm waving it at you? All I ask is I be called Doctor!"
    o "You are no doctor, witch! You never will be!"

    ...

    mt "That guy hated me. I figured he was the town 'healer' before me and hated me for it, but I never asked. Last I heard, he was either dead or very close to it! I hope he didn't pass on so angry."
    m happy "Anyway, I think it's about time for breakfast."
    ###
    mt "You can't be serious! I wonder who's even here..."


    # This ends the game.

    return

