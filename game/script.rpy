label start:
    scene bg classroom with fade
    play music "audio/laying low.mp3" fadeout 1.0 fadein 1.0
    pause
    instructor "...and though capes rarely trigger at the same time, when that does happen,
    they tend to share a similar powerset..."
    "*lecture continues*"
    me "Why am I stuck in this class?"
    me "I already know this material."
    me "Anyone who is a cape nerd like me learned this stuff years ago through Parahumans Online"
    me "Sure I'm learning the theory behind all this."
    me "But that stuff is useless since we don't really understand powers anyway."
    me "Besides, the instructor barely explained the kiss/kill syndrome."
    me "You could learn more about it by reading fanfics about powers."
    instructor "...agent refines itself by communicating with others in its vic..."
    me "*yawns*"
    play sound "audio/school bell.mov"
    pause
    instructor "Alright class, same time tomorrow."
    instructor "Read chapter 2 of \"Cape Life\" beforehand."
    instructor "And make sure to bring in your clickers, there will be a quiz!"

    show lisa 1 at center with dissolve
    girl "Whew... that was a loooong class!"
    girl "I noticed you weren't paying much attention."
    girl "Something tells me you're pretty familiar with this stuff. I wonder why."

    me "Err... who are you?"

    girl "I'm Lisa."

    me "Hey Lisa, you're right I wasn't really focused on the lecture. How'd you know?"

    lisa "I tend to figure stuff out like that."
    lisa "You were zoned out for most of the lecture. I saw you yawn many times too."
    lisa "It's not like I need superpowers to notice the obvious."

    me "It's kinda weird you were paying so much attention on me."

    lisa "Well there's this other reason too."
    lisa "You see, I've been scouting around this school for capes, and you seem to have caught my eye."

    "Shit... does she know about my secret?"
    "How would she know??? I haven't used my powers at all and for good reason."
    "What should I do?"

    menu:
        "Tell her you're just a cape nerd":
            jump nerd
        "Admit you're a cape":
            jump cape
        "Flirt with her":
            jump flirt


label nerd:
    me "I was zoned cuz I already know this stuff."
    me "Not because I have any powers, I just spend a lot of time reading about them online."
    me "If anything, I'm a super-fan"
    lisa "Uh-huh"
    lisa "Alright then have a good day!"
    hide lisa with fade
    "I don't think she bought my excuse. I'm gonna have to watch out for her."
    "Does she have powers too? How else would she know that I'm a cape?"
    "Either way, I'll worry about her later. I've got other things to focus on at the moment"
    "Out of sight, out of mind."
    window hide
    show screen neutral_end with dissolve
    pause
    return

label flirt:
    me "Let's just I was a cape, would you go out with me?"
    lisa "Cut the games out jackass, I already know you're a cape. I'm one too."
    me "You're a cape, I'm a cape, wanna make some cape babies?"
    lisa "*sighs*"
    lisa "I don't have time to deal with this."
    lisa "Taylor, get him!"
    show taylor 4 at right with fade
    "This girl shows up and she looks like she definitely doesn't want to be here."
    me "Ouch!"
    "I feel a sudden pain on my palm."
    "I look down at my hand to find that a spider bit me."
    taylor "That's a brown recluse spider."
    taylor "You're going to have a pretty painful time soon."
    "I suddenly see a swarm of bugs approaching me."
    me "Okay stop! I was just messing around!"
    lisa "It's too late. We don't mess around!"
    "Several of the bugs start biting me all over."
    "IT... BURNS!!!"
    window hide
    show screen bad_end with dissolve
    pause
    return

label cape:
    me "You got me! But please don't tell anyone!"
    lisa "That's up to me to decide."
    lisa "Mind telling me about your powers?"
    me "I don't think that's a good idea. My powers are weird and hard to explain."
    lisa "Try anyway!"
    me "How about we go somewhere else first?"
    lisa "If you say so."

    scene bg shopping with fade
    play music "audio/resonance.mp3" fadeout 1.0 fadein 1.0
    show lisa 1 at center
    lisa "Let me introduce you to a couple of my friends."
    show alec 1 at left with dissolve
    show taylor 4 at right with dissolve
    alec "Hey there mysterious cape."
    taylor "..."
    me "I thought you weren't going to tell anyone!"
    lisa "They're just my friends and they're cool."
    lisa "You can trust them!"
    me "That girl doesn't look very trustworthy."
    me "She looks like she might attack me any second."
    show taylor 1
    taylor "Watch what you say or you're gonna regret it."
    "I can sense that she isn't kidding around."
    "Gotta be cautious with her."
    alec "I'm hungry, let's head over to Fugly Bob's."
    show screen taylor_dance
    with dissolve
    taylor "Yay dinner!"
    hide screen taylor_dance
    show taylor 2
    "Wtf was that?"
    "She seems so gloomy but then someone mentions food and she was dancing??"
    me "Now that I think of it, I could use some dinner"
    "Anything to delay talking about my powers..."
    window hide
    show screen good_end with dissolve
    pause
    return
