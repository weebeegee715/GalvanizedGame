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
    
    m "This is absurd! how am I supposed to get through a place like this without a horse!? This is going to take ages."
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
    mt "I'd figured the Heart would've been some kind of odd flower, but there is {i}nothing{/i} here!"

    
    show small mira test with dissolve
    "You see someone coming! Maybe you could ask them for help?"
    hide small mira test
    show sprite test
    kn "Get away from here! Go!"

    m confused "Why? What's going on? Are you ok?"
    mt "He doesn't seem to be threatening me. He looks scared of something."
    kn "We were fighting that {i}thing! {/i} I don't have time to explain, I need to get out of here!"
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

    
    
    m "What happened to you? What on earth were you fighting?"
    kn "There's a m-monster in these woods. We'd been paid by some men, men of high rank, to kill it! As soon as I saw it, I knew we'd made a mistake."
    kn "That thing bested us in seconds! I ran away before it got any worse."
    m "Surely you've faced this kind beast before?"
    kn "No! This wasn't some typical monster, it was something else entirely! And by God, it was huge! it blocked out the moon!"
    m "Really? That's terrifying!"
    kn "Yes, but, {i} we must be going now!{/i} It's freezing!"

    scene placeholderforest at truecenter
    with fade 
    show sprite test with dissolve
    kn "{i}Thank you for all your help! Let's make haste!{/i}"
    "Should I go with him? I'm scared to continue, but, I may never have a chance like this to get the Heart again!"
    m sad "I'm sorry, but I can't leave just yet."
    kn "{i}What?! Well, I'm not waiting around!{/i}"
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

    scene placeholderforest at truecenter
    m confused "I don't hear any fighting... maybe it went away?"
    m scared "Eek!" with sshake
    mt "Did a tree fall?! That was really loud... "
    mv "{bt=3}{size=45}Ugh...{/size}{/bt}"
    m confused "Huh? Is someone there?"
    mt "Maybe some of that man's friends are here? I need to help them!"

    scene black
    with dissolve
    m scared "Ah!"
    scene valreveal with fade
    m scared "..."
    "You're not sure what exactly lie in the ditch in front of you. A sea of dark black hair. Gold rings. It isn't concious, at least not yet. "
    mt "What do I do?! I think she took a fall! Did she hit her head?"
    mt "How am I even supposed to help? Uh..."
    m scared "Hello? Can you hear me?! Are you alright?!"
    mv "..."
    mt "Am I even supposed to be helping...? This isn't just some human-looking monster, right?!"
    mt "Maybe I should just leave, I might not-{w=.15}}{nw}"
    mv "Huh?"
    scene miralookup with fade 
    "The world begins shift around you as whatever you shouted at comes to."
    mcg "{sc=3}{size=27}oh no... {/size}{/sc}"
    mt "Why can't I move? Why am I not moving?! I need to run!"
    ## i want this to be like an establishing like panning shot like a looking up
    scene madval with fade
    mv "{size=45}{sc=1}{b}{i}Who are you?! What did you do to me?!{/i}{/b}{/sc}{/size}"
    m scared "{sc=3}{size=27}I didn't do anything! I just wanted to make sure you weren't hurt... {/size}{/sc}"
    mv "What difference does my wellbeing have on your life? Are you lying?"
    m angry "{sc=3}{size=27}What kind of person leaves someone on the ground like that?! Who do you take me for?{/size}{/sc}"
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
    mv "Oh, don't clam up now!"
    "She seems to have taken offense to the lack of an answer."
    m scared "{size=27}No! No I dont!{/size}"
    mv "Hm. And why are you poking around this place? I assume you know I don't take very kindly to visitors?"
    mt "How do I say this? I don't want to tell her I was planning to steal from her, but..."
    m angry "I came here to find the Darkheart. I hardly even know what it is, but, I seek it out. You have it, don't you?"
    scene smirkval
    mv "That's a funny question. Wouldn't I be dead without it?"
    m scared "Don't tell me it's your {i}actual{/i} heart!?"
    scene laughval
    mv "What on earth did you think it was?"
    scene smirkval
    mv "Of course it's mine. And I don't think you're prepared to cut it out."
    m sad "How awful... They talked about it like some artifact. I would've never come here if I knew. Such disrepect..."
    scene gaspval
    mv "..."
    "She seems to be shocked at your concern for her."
    m sad "I'm very sorry. I'll- I'll go now. Goodbye."
    scene frownval
    mv "Wait!"
    m scared "Huh?!"
    ### <:c
    mv "I can't guarantee you'll be able to find a way out of here."
    m sad "Really?! Even if I head back the way I came?"
    mv "This place shifts by the second. You'll be lost. And in such awful weather, too."
    m sad "..."
    scene mehval
    mv "{i}{size=17}I guess this is my problem now...{/size}{/i}"
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
    mv "Yup..."



    scene black with fade
    mcg "Huh?"

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
    mv "{size=45}Hm? Is that her?{/size}"

    mt "Damn it! I didn't know she had magic! I'm just making horrible choices, one after the next!"
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
    m scared "You're a witch..."
    mv "I told you that you wouldn't like it. I even asked first! I never ask for anything."
    mv "..."
    mv "I supopse you find me detestable now? Moreso than before?"
    m scared "..."
    mv "Didn't I say I wouldn't hurt you?"
    m scared "How am I supposed to trust you?"
    mv "Oh, {i}fine.{/i} If you're dead set on being so wary of me, let me just bring you home. Does that sound good?"
    m scared "Yes. It does."

    mv "Good. Here's how this is going to go. I'm going to apport us to the edge of the woods, you're going to go back to wherever you came from, and then we never have to see eachother again. Okay?"
    m "{sc=3}{size=27}{i}apport{/i} us? like, with magic?{/size}{/sc}"
    mv "What, you think I'm going to hike there? Yes, magic. Come now."
    scene handwalk with fade
    "She reaches her hand out to you. It's odd, standing on it."
    mv "Okay..."
    "She pulls something heavy from under the table with her off-hand."
    scene teleport1 with fade
    m scared "{sc=5}Why do you have an axe?!{/sc}"
    mv "God, stop yelling. It's my wand, and we're not going anywhere without it."
    m sad "{sc=3}Well...{/sc} okay."
    scene teleport2
    mv "This is going to take a bit. I'm quite tired."
    m "So, you're okay from earlier? Did you sleep?"
    mv "Huh? No, I'm fine. I usually sleep during the day. Less people at night."
    m "You're still all scraped. You can't heal yourself with magic?"
    mv "{i}No.{/i} If people could heal with spells, wouldn't you be out of a job, {i}doctor?{/i}?"
    m "How'd you know that?"
    mv "It's obvious. And I heard you yesterday."
    m "When I was talking to. that man? From that far away?"
    mv "..."
    m "..."
    m "Why'd you put me to sleep? What was that for?"
    mv "I don't want you knowing the first thing about how I unlock my seals, not even with your eyes closed. Cant risk that."
    m "Why didn't you just do that with those men yesterday?"
    mv "I asked you first, didn't I?"
    m "I guess that is true... Do you live alone?"
    mv "Of course I do. Do you see anyone else here?"
    m "No, It's just..."
    m neutral "I'm Mira. Do you have a name?"
    mv "Not that you need to know."
    scene teleport3 with fade 
    m scared "Aah!"
    mt "That felt really, really weird! How is she used to that?!"
    scene teleport4
    mv "Well, we're here. What were you even going to do with my heart, if you got it?"
    m sad "I needed it for a drug. A cure-all, essentially. But now, I'm right back where I started. I don't know what I'll do."
    mv "Oh..."
    # chased from last town?
    m sad "I bought a property right by here, too! I planned to work and live here until it was completed, but it seems it was all a waste."
    mt "I don't think she cares very much, but it's nice to talk to someone."
    mv "I see."
    scene black with dissolve
    "She sets you down, and you ungracefully climb out of her hand."
    scene forestentrance with fade
    mt "I wonder what I'll do now."
    mv "Mira?"
    "You cant see her now, but can hear her clear as day."
    m sad "Yes?"
    mv "Don't come back. Please."
    m confused "{i}What?{/i} Why?"
    "..."
    mt ""
    "You see the sunrise."
    mt "I don't know what to make of this..."

    scene end1 with fade
    "{b}Part 1 'Catalyst' End.{/b}" 

    scene black with fade
    "Part 2 '"

   
    



        



    # This ends the game.

    return

