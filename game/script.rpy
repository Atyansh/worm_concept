# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Taylor")

define l = Character("Lisa")

image taylor:
    "Taylor.png"
    zoom 0.75
    #yalign 0.5

image bg cafeteria:
    "cafeteria.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafeteria

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    l "Today is my first day of school at Winslow High."
    l "Why am I here?"
    l "Life of a supervillain can be pretty stressful so I decided to cool off and give normal life a try."
    l "I don't really need to study in school."
    l "Exams are a breeze for me, and I already got my high school certification online."
    l "But this might be a good opportunity to meet new people and maybe even make some friends."


    show taylor
    with dissolve

    # These display lines of dialogue.

    t "Hello"

    t "I haven't seen you before, are you new here?"

    "Something about this girl seemed different."
    "I've been trying to not use my power to analyze people and give them a real shot."
    "But even without the use of my powers, I could tell something was up."

    # This ends the game.

    return
