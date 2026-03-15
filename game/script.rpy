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
    $ medshake = Shake((0, 0, 0, 0), 2.0, dist=8)
    $ bigshake = Shake((0, 0, 0, 0), 7.0, dist=8)


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
define v = Character("Valencia", image = "val",callback=val_beep, color="#de9c01", what_size = 37)
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

image coach:
    "coach.png"
    pause 2
    "coach blink.png"
    pause 0.4
    "coach.png"
    pause 0.5
    "coach blink.png"
    pause 0.4
    repeat

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
    play music [ "fallingleaves.mp3", "Jonquil.mp3"  ] fadeout 2.0 fadein 3.0 volume 0.4
    scene paper1
    with Fade (out_time=1.0, hold_time=1.0, in_time=3.0)

    # These display lines of dialogue.
    "{i}The Philosopher's Stone. The all-powerful stone said to grant untold powers to it's wielder.{i}"

    scene paper2
    with dissolve

    "{i}The Panacea, A substance to cure all illness, lift all curses, and bring perferct health to the human form. The very pinnacle of medicine.{/i}"
    "{i}You have done everything in your power to make this. There is only a single thing you haven't tried...{/i}"

    scene paper3
    with dissolve

    "{i}The Darkheart, said to be the key to creating the mythical stone.{/i}"

    scene forestentrance 
    with Dissolve (3.0)
    m angry "Only problem is that it's in the middle of these woods! This'll take all ages to find..."
    c "Good luck with that."
    m confused "Huh?"
    show coach with dissolve
    mt "I paid this man enough for the whole way through! Is he gonna leave me here?"
    m angry "Don't tell me you intend to stop right here, sir!"
    c "I won't be taking you any further, miss."
    m angry "What!? But I need to go {i}through{/i} the forest! Why are we stopping at its entrance?"
    c "The sun is nearly setting, and I'm not getting caught in this place at night. Wouldn't take you much farther in the day, either."
    m angry "You couldn't have told me this earlier?! This is a matter of urgency!"
    c "I'm turning back now. Are you coming or not?"
    m angry "Most certainly not! I will walk precisely through these woods on my own two feet and be better for it!"
    c "Suit yourself."
    m angry "I have!"
    hide coach with moveoutleft
    
    mt "He actually left me here? You can't be serious!"
    m angry "This is absurd! how am I supposed to get through this place without a horse!?"
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

    "Someones coming!"
    show asher with dissolve
    mt "Who is this guy? He doesn't look right."
    kn "Run! You have to get out of here!"

    m confused "Huh? Are you alright, sir?"
    mt "He doesn't seem to be threatening me. He looks scared of something."
    kn "We were fighting that {i}thing!{/i} I don't have time to explain, I need to get out of here!"
    m confused "I'm a doctor! My name's Mira. At least let me help you!"
    "He calms down a bit."
    kn ". . . Alright. Think I've ran far enough. Please, be quick."
    m happy "Good. I will."

    hide asher
    scene black
    with fade
    play sound 'audio/bag.mp3'
    "Laying your supplies out, you begin to work."
    scene healcg
    with Dissolve (2.0)

    
    
    m confused "What happened to you?"
    kn "There's something in these woods. We'd been paid by some men, men of high rank, to kill it! It has this thing, the Darkheart! All those alchemists want it. As soon as I saw it, I knew we'd made a mistake."
    mt "The Darkheart?! Something has the Darkheart?"
    kn "That thing bested us in seconds! I ran away before it got any worse."
    m confused "Surely you've faced this kind of animal before?"
    kn "No! Not an {i}animal{/i}, a {i}monster!{/i} a horrible, lumbering thing!"
    m "...huh? You aren't serious. There's no such thing."
    kn "{i}Oh, yes there is!{/i} And we have to leave now, if we want to leave at all!"

    scene placeholderforest at truecenter
    with fade 
    show asher with dissolve
    kn "{i}Thank you for your help, but we have to go! Now! {/i}"
    mt "I can't go with him. Not only do I not know this man, I am not entirely sure he has his wits about him."
    m sad "I'm sorry, but I can't leave just yet."
    kn "{i}What?! I- I must be going!{/i}"
    hide asher with moveoutright
    # run sfx
    mt "He ran off! Who knew a knight could be so craven?"

    mt "He's a madman, I'm sure. But his armor looked official enough to me..."
    m angry "Come what may, I'm not leaving without the heart. I'm not."
    m sad "But there must have been at least {i}some{/i} truth to his words..."
    mt "..."
    # >:[ 
    m angry "I can't give up."
    
    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "{i}You go the direction the man you helped fled from.{/i}"

    scene placeholderforest at truecenter 
    with fade
    m confused "I don't hear anything. Maybe he really did make it up."
    m angry "That crazy guy really got me all scared for nothing?!"
    mt "First the coach I hired, and now that knight, both acting so odd..."
    m neutral "...hmm."
    mt "I've been here too long... I'm starting to get a bad feeling."
    m angry "Okay, maybe this place {i}is{/i} a bit creepy. But, I'm not afraid!"
    mt "{w=0.4}!!!" with bigshake
    m scared "What was {i}that?!{/i} I almost fell!"
    mt "Did a tree fall?! That was really loud... "
    mv "{sc=2}{size=25}U{w=0.2}g{w=0.2}h{w=0.2}h{w=0.2}.{w=0.2}.{w=0.2}.{/size}{/sc}"
    m confused "Huh? Is someone there?!"
    mt "Maybe someone who was with that man? Hopefully they aren't hurt worse than he was!"

    scene black
    with dissolve
    play sound 'audio/DirtSteps.mp3'
    "..."
    m scared "{w=0.2}...What on {i}earth{/i}?"
    scene cliffvalreveal with fade
    m scared "..."
    mt "A monster? No, a person! This is a {i}person!{/i}"
    mt "What do I do?! Do I help? How {i}can{/i} I even help?"
    m scared "How am I even supposed to... Uh..."
    m scared "Hello? Can you hear me?! Are you alright?!"
    mv "...?"
    mt "I don't think this is very smart of me..."
    mt "Maybe I should just leave? But how could I leave a person like this? But if those stories are true, I'm really not safe-"
    mv "{bt=2}Agh....{/bt}"
    scene cliffmiracooked at truecenter
    with fade
    "The world begins shift around you as whatever you shouted at comes to." with vpunch
    mcg "{sc=3}{size=27}.{w=0.1} .{w=0.1} . {/size}{/sc}"
    mt "Why can't I move? Why am I not moving?! I need to run!"
    ## i want this to be like an establishing like panning shot like a looking up
    scene cliffvalmad with fade
    mv "{sc=2}Who on earth are you?! What do you want from me?{/sc}"
    m scared "{sc=2}I don't want anything! I just wanted to make sure you weren't hurt...{/sc}"
    mt "This has got to be the worst day of my life!"
    mv "{i}Hurt?{/i} Why on earth would you care? You must be lying."
    m angry "{sc=2}What kind of person leaves someone on the ground like that?! Who do you take me for?{/sc}"
    scene cliffvalgasp
    mv "...?"
    mt "That was stupid! Why can't I just hold my tongue? "
    scene cliffvallaugh
    mt "Huh? Was that {i}funny{/i}"
    mv "That was rather brave of you, no?"
    mt "That was really loud... My are ears are starting to ring."
    scene cliffvalsmirk
    mv "It's quite refreshing for someone to speak so boldy with me... maybe you aren't lying."

   




    
    scene cliffvalmeh
    "..."
    mv "You're very ill-dressed for the weather, miss. Do you intend to die in this cold?"
    m sad "{size=27}...{/size}"
    scene cliffvalmad
    mv "Don't tell me you're going to go quiet {i}now.{/i}"
    m scared "I don't intend to, no."
    scene cliffvalmeh
    mv "Hm. And why are you poking around this place? I assume you know I don't take very kindly to it?"
    mt "How do I say this? I don't want to say I was planning to steal..."
    m angry "I came here to find the Darkheart. I hardly even know what it is, but, I seek it out. You have it, don't you?"
    scene cliffvalsmirk
    mv "That's a funny question. Wouldn't I be dead without it?"
    m scared "Don't tell me it's your {i}actual{/i} heart!?"
    scene cliffvallaugh
    mv "What on earth did you think it was? What a silly question!"
    mt "Come to think of it, I wasn't actually sure..."
    scene cliffvalsmirk
    mv "Of course it's mine. And I'm guessing you didn't come prepared to carve it out of me?"
    m sad "How awful! My books talked about it like some kind of artifact. I would've never come here if I knew, believe me."
    scene cliffvalmeh
    mv "Well you didn't, and you did. Congrats on all your wasted time."
    m sad "Oh no..."
    mv "I won't hurt you, if that's what you're all worked up about. No harm done, okay? "
    m sad "...I'm really sorry. No one deserves to be treated that way."
    scene cliffvalgasp
    mv "...!"
    m sad "I'll leave this very instant. My apologies, and goodbye."
    ## more subtle less yuri. slowly slowly catching monkey
    mv "Wait."
    m scared "Huh?!"
    scene cliffvalmeh
    mv "You won't be able to find your way out of here."
    m confused "Really?! Even if I head back the way I came?"
    mv "The paths in these woods... shift, especially at this hour. I'm sure you'll get lost."
    m sad "Really?"
    m sad "{bt=2}What am I supposed to do?...{/bt}"
    mv "..."
    m sad "..."
    scene cliffvalmad
    mv "Are you {i}trying{/i} to get to feel bad for you? Are you just going to sit there frowning at me?"
    m scared "Ah! No, I- I'm not! Uh..."
    scene cliffvalmeh
    mv "...Oh, {i}fine.{/i}"
    mv "I'll help you. But I can't guarantee you'll like it. I'm serious."
    mt "What is that supposed to mean?... At least I'm being given a choice?"
    m angry "Fine."
    scene cliffvalreach
    m scared "Huh?"
    mv "Come on, then. There's a storm coming and I intend to be indoors for it."
    m "Do I really have to...?"
    mv "I told you that you wouldn't like it. This was supposed to be the easy part."
    m "{sc=2}Okay...{/sc}"
    mv ""
    scene magictime
    mt "Huh? Don't tell me this is-"
    mv "This'll send us right back inside."
    "Every sense of where you are is ripped away. You feel..."

    scene black with fade
    mv "Aw, no. Are you still awake? Can you hear me? Wake up!"

    play music [ "fallingleaves.mp3", "Jonquil.mp3"] fadeout 2.0 fadein 3.0 volume 0.5

    scene black with fade
    "..."
    mcg "{w=0.7}.{w=0.2}.{w=0.2}."
    mv "Ah! Are you awake now?"
    mcg "..."
    mv "{i}Hello?{/i}"

    scene librarydark at truecenter
    with dissolve
    mcg "Huh?"
    mv "Morning."
    m scared "Aah!"
    mv "Am I such an awful thing to wake up to?"
    m scared "...What do you want with me?"
    mv "Nothing. That whole getting knocked out thing was all you. Guess you're just not used to magic."
    m "..."
    mv "I almost forgot. Do you find me detestable now? You can condone a monster, but not the use of magic."
    m scared "You didn't tell me you were a witch! How was I supposed to know?"
    mv "I didn't even tell you my {i}name{/i}. Also, try not to call me a witch, either."
    m sad "I didn't mean to offend you. Sorry."
    mv "You didn't. I'm just not a witch. Doesn't matter, either way."
    m angry "I'm just weary of magic. I... haven't a clue how it works! Can you blame me?"
    mt "And why on earth would she help an alchemist? Every alchemist I know hates magic! Doesn't it go the other way?"
    m scared "..."
    mv "... {i}Fine.{/i} If you're dead set on being so wary of me, let me just take you home. Does that sound good?"
    m scared "Yes. It does."

    mv "Good. Here's how this is going to go. I'm going to apport us to the edge of the woods, you're going to go back to wherever you came from, and then we never have to see eachother again. Okay?"
    m "{sc=3}Apport? Like last time? With magic?{/sc}"
    mv "Yes, like last time. I'll take it slower, okay?"
    m angry "Okay. Just once more."
    scene black with fade
    mcg "Eek!"
    mv "You're {i}fine.{/i}"
    mt "Not with being grabbed like housekeys, I'm not!"
    mv "Let me get my things..."
    scene teleport1 with fade
    m scared "{sc=4}Why do you have an axe?!{/sc}"
    mv "God, stop yelling. It's my wand, and we're not going anywhere without it."
    m sad "{sc=3}Well...{/sc} okay."
    scene teleport2
    mv "This is going to take a while. Stay very still."
    m confused "...{w=0.5}Why isn't anything happening?"
    mv "Apporting is supposed to be slow. I'm just used to zipping around where I please, but, you're obviously not."
    m "And it knocked me out?"
    mv "Guess so."
    m sad "It won't happen again, though?"
    mv "No, no. I know what I'm doing."
    m "I guess so..."
    m "Where are we?"
    mv "A library. A very large one."
    m "You live here?"
    mv "You could say."
    m "So, you're okay from earlier? Did you sleep?"
    mv "Huh? No. I'm fine. I usually sleep during the day. There's less people to deal with at night."
    m "Oh no! I'm not keeping you awake, am I?"
    mv "{i}Oh, believe me, you are.{/i}"
    m "Sorry..."
    m "You're still all scraped. Can't you heal yourself with magic?"
    mv "{i}No.{/i} If people could heal with spells, wouldn't you be out of a job, {i}doctor?{/i}"
    m confused "How'd you know that?"
    mv "It's obvious. And I heard you yesterday, too."
    m confused "When I was talking to that man? From that far away?"
    mv "Yeah."
    m confused "Really?"
    mv "Is that odd?"
    m "Honestly, this whole day has been odd. But I'm starting not to mind."
    mv "...hmm."
    m confused "Why are you helping me?"
    mv "Huh?"
    m confused "It's just that I've heard so many bad things about you, and, you're going out of your way for me."
    mv "You hardly know me. You don't even know my name, and now you think you're fit to judge my character?"
    m sad "No, It's just..."
    m confused "{i}Do{/i} you have a name? Mine is Mira."
    mv "...I'm bored of answering questions."
    scene teleport3 with fade
    m scared "Aah! How did we do that?!"
    mv "Magic. Quit yelling."
    mt "That felt really, really weird! I could never get used to that!"
    scene teleport4
    mv "Well, we're here."
    mv "...I think I have a question for you, though."
    m confused "What is it?"
    mv "What are you getting out of this?"
    m confused "I don't think I understand...?"
    mv "Most alchemists try their luck with me because they want power. They want to take things that aren't theirs. Isn't that what you want?"
    m scared "Ah!"
    mt "I never said I wasn't an alchemist outright, but I didn't say so, either... "
    m scared "I..."
    mv "No, no, I get it. It's only natural to crave power when you are powerless, but..."
    mv "Why are you being so {i}nice{/i} about it?"
    m scared "I don't understand..."
    mv "Why are you pretending to care about {i}me{/i}? You care about my {i}Heart.{/i}"
    mv "As soon as you leave, you'll probably begin to do everything in your power to find someone strong enough to kill me. So why can't you just drop the act?"
    mt "..."
    m angry "You're wrong about that."
    mv "What?"
    m angry "I learned alchemy for the same reason I learned medicine. I wanted to help people."
    m sad "And if I get that stone, I can help everyone. {i}Cure{/i} everyone of anything and everything!."
    m angry "I don't care if your Heart is the easiest way in the world to get the Stone. I {i}know{i} there is another way. I'll find one."
    mv "...I see."
    m angry "You do?"
    mv "...I'll let you down, now."


    scene black with dissolve
    mv "Be careful, now."
    m "I will."

    scene forestentrance with fade
    mv "Mira?"
    m confused "Hm."
    mv "If you're serious about this, you can come use my library whenever you need."
    m happy "You mean that?"
    mv "Yes, I do. You're quite annoying, but I feel you know what you're doing."
    mt "I'm annoying?"
    v "And my name is Valencia. Goodbye now."
    mt ""

    scene black with fade
    "Part 1 'Catalyst' End."


    # This ends the game.


    return


