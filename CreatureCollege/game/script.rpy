# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character(_("..."), color="#5F6A6A")
define mo = Character(_("Mom"), color="#212F3C")
define m = Character(_("Me"), color="##212F3C")

image bg foggyfield = "foggyfield.jpg"
image bg foggyforest = "foggyforest.jpg"
image mom = "mom.png"

# The game starts here.

label start:
    
    scene bg foggyfield
    with fade
    
    "You stand in an empty field. It is pitch black outside, with no stars or moon to light the landscape. The headlights of a sedan illuminate the edges of a path leading into sinister woods."
    
    "You hear the crunching of gravel against shoe, and suddenly are folded into a tight embrace."
    
    u "I’m going to miss you so much!"
    
    m "It’ll be okay, Mom!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mom
    with dissolve

    # These display lines of dialogue.

    mo "Do you have everything you need? You didn’t forget your toothbrush? Cellphone? Socks?!"

    m "Mommmm… yes, I have all those things!"
    
    mo "Okay, okay, I’ll leave you be. You’re an adult now."
    
    mo "Give me a call as soon as you’re settled!"
    
    m "I will, Mom. Please don’t worry."
    
    scene foggyforest
    with fade
    
    "You pick up your suitcase, and walk onto the path. As soon as you enter the forest, the fog surrounds you. You begin to worry whether you’ll find your destination after all. Distantly, you hear your mother’s voice."
    
    mo "I’m proud of you! And always remember what we’ve taught you!"
    
    "Although your mom can no longer hear you, you reflexively recite the mantra that your family has instilled in you since birth..."
    
menu:
    "I know right from wrong":
        jump morality

    "No matter what, there is always love":
        jump love

    "Live each day as if it’s your last":
        jump energy
         
    "Save your money, and everything will be alright":
        jump money

    "A clear intellect will solve any problem":
        jump intelligence
    
label morality:    
    m "\“I know right from wrong.”\ You feel a boost in morality as you say these words."
    jump blackscreen

label love:
    m "\“No matter what, there is always love.”\ You feel your heart swell with love and passion as you say these words."
    jump blackscreen
    
label energy:    
    m "\“Live each day as if it’s your last.”\ You feel your energy rise as you say these words."
    jump blackscreen

label money:
    m "\“Save your money, and everything will be alright.”\ You take pride in the savings you’ve accumulated as you say these words."
    jump blackscreen

label intelligence:
    m "\“A clear intellect will solve any problem.”\ You swell with pride at the academic achievements you’ve accomplished as you say these words."
    jump blackscreen

label blackscreen:
    scene black
    with dissolve
    
    "You take a moment to appreciate the small token given to you by your family. That feeling lasts for a moment before you realize that the fog has made it impossible to see the path ahead of you."

    # This ends the game.

    return
