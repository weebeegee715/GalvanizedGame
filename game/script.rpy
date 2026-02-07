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
define mcg = Character("Mira", callback=mira_beep, color="#329b15")
define mt = Character("Mira", image="nothing", color="#329b15", what_italic=True)
define kn = Character("Knight", callback=guylow_beep, color="#417ce4")
define o = Character("O'Keefe", callback=guylow_beep, color="#664011")
define l = Character("Lavinia", callback=girl_beep, color="#128f9aff")
define mag = Character("Magnus",callback=guy_beep, color="#c73c1cff" ) 
define k = Character("Kieran", callback=guylow_beep, color="#5e2d7eff")
define g = Character("Gale", callback=guy_beep,color ="#717815ff")
define a = Character("Asher", callback=guylow_beep, color="#417ce4")


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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black 
    with Dissolve (3.0)
    play music [ "fallingleaves.mp3", "piratesong.mp3", "Jonquil.mp3" , "piratesong2.mp3" ] fadeout 2.0 fadein 3.0 volume 0.4
    scene paper1
    with Fade (out_time=1.0, hold_time=1.0, in_time=3.0)

    # These display lines of dialogue.
    "{i}The Philosopher's Stone. The all-powerful stone said to grant untold powers to it's wielder.{i}"
    
    "{i}Most chase it for eternal youth, or Midas' golden touch. But those don't matter to you. What you seek is greater.{i}"

    scene paper2
    with dissolve

    "{i}The Panacea, A substance to cure all illness, lift all curses, and bring perferct health to the human form. The very pinnacle of medicine.{/i}"
    "{i}You have tried mixing sulfur and mercury in every fashion to no avail. But there is one thing you haven't tried...{/i}"

    scene paper3
    with dissolve

    "{i}The Darkheart, said to be the key to creating the mythical stone.{/i}"
    "{i}Said to be guarded by a terrible beast in a tall, dark wood, only showing itself in the dead of night.{/i}"
    "{i}But, you scarcely believe in monsters...{/i}"
  

    scene forestentrance 
    with Dissolve (3.0)

    show sprite test
    c "I won't be taking you any further, miss."
    m angry "What!? But I need to go {i}through{/i} the forest! Why are we stopping at its entrance?"
    c "The sun is nearly setting, and I'm not getting caught in this place at night. Wouldn't taake you much farther in the day, either."
    m angry "You couldn't have told me this earlier?! This is a matter of urgency!"
    c "I'm turning back now. Are you coming or not?"
    m angry "Most certainly not! You deny the coin of a customer because of a children's fairy tale? I will walk precisely through these woods on my own two feet and be better for it!"
    c "Suit yourself."
    m angry "I have!"
    hide sprite test with moveoutleft
    
    mt "He actually left me here!"
    m angry "This is absurd! how am I supposed to get through a place like this without a horse!? This is going to take ages."
    show sprite test with dissolve
    mt "And here I thought the locals were exaggerating about these woods! This explains why the property is so cheap around here, and why they'd even consider {i}my{/i} offer in the first place."
    mt "..."
    mt "It doesn't matter. I've already come all this way, and I'm not stopping now!"
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You make your way into the woods.{/i}"

    scene placeholderforest
    with fade
    m sad "I'm cold..."
    mt "I've been walking for hours, but haven't made any progress!" 
    mt "Not that I know what I'm even looking for... Maybe I should just go home."

    
    show small mira test with dissolve
    "You see someone coming! Maybe you could ask them for help?"
    hide small mira test
    show sprite test
    kn "Run! You must go!"

    m confused "Why? Are you alright?"
    mt "He doesn't seem to be threatening me. He looks scared of something."
    kn "We were fighting that {i}thing!{/i} I don't have time to explain, I need to get out of here!"
    m neutral "I'm a doctor! My name's Mira. At least let me help you!"
    "He calms down a bit."
    kn ". . . Alright. Think I've ran far enough. Please, be quick."
    m happy "Good. Sit down here."

    hide sprite test
    scene black
    with fade
    play sound 'audio/bag.mp3'
    "Laying your supplies out, you begin to work."
    scene healcg
    with Dissolve (2.0)

    
    
    m "What happened to you?"
    kn "There's something in these woods. We'd been paid by some men, men of high rank, to kill it! As soon as I saw it, I knew we'd made a mistake."
    kn "That thing bested us in seconds! I ran away before it got any worse."
    m "Surely you've faced this kind of animal before?"
    kn "No! Not an {i}animal{/i}, a {i}monster!{/i} a horrible, lumbering thing!"
    m "...what?"
    kn "{i}We must be going now!{/i} It's freezing!"

    scene placeholderforest at truecenter
    with fade 
    show sprite test with dissolve
    kn "{i}Thank you for all your help! Let's make haste!{/i}"
    mt "I can't go with him. Not only do I not know this man, I am not entirely sure he has his wits about him."
    m sad "I'm sorry, but I can't leave just yet."
    kn "{i}What?! Well, I'm not waiting around!{/i}"
    hide sprite test with moveoutright
    # run sfx
    mt "He ran off! Some knight he is!"

    mt "A madman, I'm sure. But his outfit looked official enough..."
    m angry "Come what may, I'm not leaving without the heart. I'm not."
    # pls draw progressively more upset sprites plzzz NO!!
    m sad "But I'm woefully underprepared. That man was armed to the teeth, and still made a run for it."
    mt "{i}...{/i}"
    # >:[ 
    m angry "I can't give up."
    
    hide sprite test with dissolve
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You go the direction the man you helped fled from.{/i}"

    scene placeholderforest at truecenter 
    with fade
    m confused "I don't hear anything. Maybe he really did make it up."
    m angry "That crazy fool really got me all scared for nothing?!"
    mt "I pray the town I've just moved into isn't full of people like him. Gone crazy with fairy tales."
    m scared "{w=0.3}Eek!" with sshake
    mt "Did a tree fall?! That was really loud... "
    mv "{sc=2}{size=25}U{w=0.2}g{w=0.2}h{w=0.2}h{w=0.2}.{w=0.2}.{w=0.2}.{/size}{/sc}"
    m confused "Huh? Is someone there?!"
    mt "Maybe someone who was with that man? Was he telling me the truth, after all?"

    scene black
    with dissolve
    m scared "...huh?"
    scene valreveal with fade
    m scared "..."
    "You're not sure what exactly lie in the ditch in front of you. A sea of dark black hair. Gold rings. Not fully concious, at least not yet. "
    mt "What do I do?! Do I help? Should I? {b}can{/b} I?"
    m scared "How am I even supposed to... Uh..."
    m scared "Hello? Can you hear me?! Are you alright?!"
    mv "..."
    mt "I don't think this is very smart..."
    mt "Maybe I should just leave? But how could I?"
    mv "{bt=2}Agh....{/bt}"
    scene miralookup with fade 
    "The world begins shift around you as whatever you shouted at comes to." with vpunch
    mcg "{sc=3}{size=27}.{w=0.1} .{w=0.1} . {/size}{/sc}"
    mt "Why can't I move? Why am I not moving?! I need to run!"
    ## i want this to be like an establishing like panning shot like a looking up
    scene madval with fade
    mv "{sc=2}{i}{size=45}Who are you?! What did you do to me?!{/size}{/i}{/sc}"
    m scared "{sc=3}{size=27}I didn't do anything! I just wanted to make sure you weren't hurt... {/size}{/sc}"
    mv "What difference does my wellbeing have on your life? Are you lying?"
    m angry "{sc=3}{size=35}What kind of person leaves someone on the ground like that?! Who do you take me for?{/size}{/sc}"
    scene gaspval
    mv "..."
    mt "That was stupid. Why can't I hold my tongue?"
    scene smirkval
    mv "It's quite refreshing for someone to speak so boldy with me. Most I interact with are the most craven of cowards."

   




    
    scene mehval
    "She pauses for quite a while."
    mv "You're very ill-dressed for the weather, miss. Do you intend to die in this cold?"
    m sad "{size=27}...{/size}"
    scene lessmadval
    mv "Oh, don't get all quiet now!"
    m scared "{size=27}No! No I dont!{/size}"
    scene mehval
    mv "Hm. And why are you poking around this place? I assume you know I don't take very kindly to it?"
    mt "How do I say this? I don't want to tell her I was planning to steal from her, but..."
    m angry "I came here to find the Darkheart. I hardly even know what it is, but, I seek it out. You have it, don't you?"
    scene smirkval
    mv "That's a funny question. Wouldn't I be dead without it?"
    m scared "Don't tell me it's your {i}actual{/i} heart!?"
    scene laughval
    mv "What on earth did you think it was?"
    mt "That's a good question."
    scene smirkval
    mv "Of course it's mine. And I don't think you're quite prepared to carve it out of me."
    m sad "How awful! My books talked about it like some kind of artifact. I would've never come here if I knew, believe me."
    mv "Well you didn't, and you did. Congrats on your wasted time."
    mv "I won't hurt you for it, if that's what you're so worked up about. No harm done."
    m sad "I'm truly sorry. You don't deserve to be treated that way. I'll search for a substitute immediately, And I hope it will get people to leave you be."
    scene gaspval
    mv "...!"
    m sad "I'll leave this very instant. My apologies, and goodbye."
    scene frownval
    ## more subtle less yuri. slowly slowly catching monkey
    mv "Wait!"
    m scared "Huh?!"
    scene mehval
    mv "I can't guarantee you'll be able to find a way out of here."
    m sad "Really?! Even if I head back the way I came?"
    mv "These woods shift by the second, especially at this hour. You'll be lost. And in such awful weather, too."
    m sad "...Oh no. I really am a fool..."
    m sad "{size=30}{bt=2}What do I do...{/bt}{/size}"
    mv"..."
    scene madval
    mv "Will you stop that? You win. I feel bad. You've managed to make me feel bad."
    scene mehval
    mv "I'll help you. But I can't guarantee you'll like it."
    mt "What is that supposed to mean? At least I'm being given a choice."
    m angry "I'll accept, on the condition no harm comes to me."
    mv "None will. I can swear to that."
    m angry "Then you have a deal."
    scene smirkval
    mv "Deal."
    scene handval
    ## spooky spellll O_O woo
    m scared "Huh?"
    "Some intracate golden pattern wraps around her finger."
    mv "I bet this'll do nicely."
    "You are the tiredest you've ever been..."
    scene black with fade
    ##fall sfx
    play sound "audio/oof.ogg"
    mcg "{w=0.7}.{w=0.2}.{w=0.2}."
    mv "Yeah, she's out cold."
    "..."

    play music [ "fallingleaves.mp3", "piratesong.mp3", "Jonquil.mp3" , "piratesong2.mp3" ] fadeout 2.0 fadein 3.0 volume 0.5

    scene black with fade
    "..."
    mcg "{w=0.7}.{w=0.2}.{w=0.2}."
    mcg "Huh?"

    ####

    scene librarydark1 at truecenter 
    with fade

    m confused "Where am I?"
    mt "This isn't my bed. I haven't slept this well in a while."

    "You try and throw the sheet off of you. It's much heavier than you expected it to be... "
    m confused "...huh?"

    
    "Early morning light shines through the room from an excessively large window behind you, but you cannot make out the walls. It's like this room goes on forever."
    m scared "Where's the door?!"

    scene librarydark2 at truecenter
    with dissolve

    
    "More light spills into the room, and it begins to yawn before you."
    m scared "What is this place?!"
    mt "It's huge! My head is starting to spin."

    "You hear something through the wall."

    # "I didn't want to wake you then." < :[
    mv "Hm? Is that her?"
    
    mt "It's her! From yesterday! That felt like it was just some dream, truly..."
    mt "I wouldn't have accepted if I'd known she was a witch! I'm just making awful choices, one after the next!"
    "You feel the ground, no doubt some shelf or table, shake beneath you as she looms closer." with sshake
    m sad "What do I do?"
    mv "..." with sshake
    ## wallking sfx
    mt "Hide!"
    scene darklairthrow
    # this needs a sound
    "You pull the heavy quilt back over your head. "
    scene black with dissolve
    mt "This was a horrible idea."
    #### door creak
    ## step stp step
    mt "She must be staring dead at me..."
    mv "I know you're up. I heard you."
    scene librarydark2
    with dissolve
    show val blue desk sleepy with dissolve
    m scared "...What do you want with me?"
    mv "Nothing. I assure you I've held to our deal."
    mv "..."
    mv "I supopse you find me detestable now? Doubly so?"
    m scared "You didn't tell me you were a {i}witch!{/i}"
    mv "I haven't even told you my name. I don't understand how you think? Some lumbering {i}thing{/i} is worthy of your help, but you draw the line when I have magic?"
    m confused "Of course you're worthy of help. Everyone is."
    m angry "I'm just weary of magic. I... haven't a clue how it works! Can you blame me?"
    mt "It is true I don't know the first thing about magic, and it is true I fear it. No doubt. But, I'm more afraid she'll find out I'm an alchemist! Witches hate us!"

    mv "... {i}Fine.{/i} If you're dead set on being so wary of me, let me just bring you home. Does that sound good?"
    m scared "Yes. It does."

    mv "Good. Here's how this is going to go. I'm going to apport us to the edge of the woods, you're going to go back to wherever you came from, and then we never have to see eachother again. Okay?"
    m "{sc=3}{size=27}{i}apport{/i} us? like, with magic?{/size}{/sc}"
    mv "What, you think I'm going to hike there? Yes, magic. Come now."
    scene handwalk with fade
    "She reaches her hand out to you. It's odd standing on the uneven surface."
    mv "Okay..."
    "She pulls something heavy from under the table with her off-hand."
    scene teleport1 with fade
    m scared "{sc=5}Why do you have an axe?!{/sc}"
    mv "God, stop yelling. It's my wand, and we're not going anywhere without it."
    m sad "{sc=3}Well...{/sc} okay."
    scene teleport2
    mv "This is going to take a while, I'm quite tired. Stay still."
    m confused "...{w=0.5}Why isn't anythimg happening?"
    mv "Apporting is {i}lazy{/i}, not quick. These kinds of things are best taken slowly."
    m "Why is that?"
    mv "We'd get nausea if we went any faster. Or we could just get stuck in-between forever."
    m sad "I thought you said this was safe!"
    mv "Lucky for you, I actually {i}know{/i} what I'm doing."
    m "I guess you do."
    m "So, you're okay from earlier? Did you sleep?"
    mv "Huh? No, I'm fine. I usually sleep during the day anyway. There's less people around at night."
    m "Oh no! I'm not keeping you awake, am I?"
    mv "{i}Oh, you are.{/i}"
    m "Sorry..."
    m "You're still all scraped. Can't you heal yourself with magic?"
    mv "{i}No.{/i} If people could heal with spells, wouldn't you be out of a job, {i}doctor?{/i}?"
    m "How'd you know that?"
    mv "It's obvious. And I heard you yesterday, too."
    m confused "When I was talking to that man? From that far away?"
    mv "Yeah."
    m gasp s"Really?"
    mv "Is that odd?"
    m happy "Honestly, this whole day has been odd. But I'm starting not to mind."
    mv "...hmm."
    m confused "Why'd you put me to sleep? What was that even for?"
    mv "I don't want you knowing the first thing about how I unlock my seals, not even with your eyes closed and not a clue how they work!. I can't risk that."
    m "But then why didn't you just do that with those men yesterday?"
    mv "That's not something to be taken lightly. If you fight with magic, you'll kill with magic, sooner or later. Nothing's worth that."
    m sad "I see."
    m confused "Are you alone here? You live all by yourself?"
    mv "Of course I do. Is that odd to you, too?"
    m "No, It's just..."
    m neutral "I'm Mira. Do you have a name?"
    mv "...I'm tired of answering questions."
    scene teleport3 with fade 
    m scared "Aah!"
    mt "That felt really, really weird! How is she used to that?!"
    scene teleport4
    mv "Well, we're here."
    mv "I think I have a question for you, though."
    m confused "What is it?"
    mv "Why on earth would {i}you{/i} want the Philosopher's Stone?"
    m scared "Ah!"
    mv "Most of the fools try their luck with me because they want power. They want to take things that aren't theirs. Is that what you want? You don't seem the type but..."
    mv "Looks can be decieving."
    m scared "It isn't! I swear!"
    mv "Why were you being so nice to me, hm? I won't be fooled. What do you {i}really{/i} want?"
    m angry "I need the Panacea! I've spent years of my life watching medecine lag farther and farther behind our problems, and that stupid {i}rock{/i} is the only way to fix it!"
    m angry "Do you {i}know{/i} how it feels when there is {i}nothing{/i} you can do for someone?"
    m sad "Someone you care about?"
    mv "..."
    m angry "That's what I really want. What I {i}wanted.{/i}"
    mv "..."
    m sad "Can you let me go?"
    mv "Oh..."
    scene black with dissolve
    "She sets you down, and you ungracefully climb out of her hand."
    scene forestentrance with fade
    mv "Mira?"
    "You cant see her now, but can hear her clear as day."
    m sad "Yes?"
    mv "I'm truly sorry, and..."
    v "My name is Val."
    m gasp "Oh!"
    "..."
    mt "I think she's gone."
    "Sunrise begins to give way into morning. It's time you go home."
    scene end1 with fade
    "{b}Part 1 'Catalyst' End.{/b}"

    # This ends the game.

    return

