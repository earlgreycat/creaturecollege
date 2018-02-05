# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mc = ""

define u = Character(_("..."), color="#5F6A6A")
define mo = Character(_("Mom"), color="#212F3C")
define m = Character(_("Me"), color="#212F3C")
define player = Character("[mc]")

image bg foggyfield = "foggyfield.jpg"
image bg foggyforest = "foggyforest.jpg"
image mom = "mom.png"


##############################################################################
# Character Creation Screen - by Steamgirl
#
# A screen lets you distribute skill points.
# To use this screen initialise the various points
# Then use the following in your script:
# call screen character_creation
##############################################################################
# Example initialisation of points below. Move it where you want it.
init:
    #The number of maximum creation points
    $ init_creation_points = 10
    #The current number of creation points
    $ creation_points = init_creation_points

    #Skill 1 (in the example case, it's Charisma)
    $ skill1_max = 10
    $ skill1_points = 0

    #Skill 2 (in the example case, it's Strength)
    $ skill2_max = 10
    $ skill2_points = 0

    #Creating a style which sets the text size
    $ style.create('creation_points_style', 'default')
    $ style.creation_points_style_text.size = 30 #change this value for bigger/smaller text
    $ style.creation_points_style_button_text.size = 30 #change this value for bigger/smaller text on the buttom
    
screen character_creation:
    
    frame:
        style_group "creation_points_style"
        has vbox
        hbox:
            text "Points available: [creation_points]"
        hbox:
            if creation_points == 0:
                textbutton ("Charisma") xminimum 200 action None
            else:
                textbutton ("Charisma") xminimum 200 action [SetVariable("skill1_points", skill1_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill1_max value skill1_points xmaximum 200 #ymaximum 36
        hbox:
            if creation_points == 0:
                textbutton ("Strength") xminimum 200 action None
            else:
                textbutton ("Strength") xminimum 200 action [SetVariable("skill2_points", skill2_points + 1), SetVariable("creation_points", creation_points - 1)]
            bar range skill2_max value skill2_points xmaximum 200 #ymaximum 36
        hbox:
            textbutton ("Start Over") action [SetVariable("skill1_points", 0), SetVariable("skill2_points", 0), SetVariable("creation_points", init_creation_points)]
            if creation_points == 0:
                textbutton ("Finished") action Return()
            else:
                textbutton ("Finished") action None

# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.

# We'll comment it out for now.

label splashscreen:
    scene black
    show text "Canaan Piddy Paws presents..." with fade
    $ renpy.pause(2.0)
    hide text with fade

return
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
    
    mo "Did you label your suitcase? What if it gets lost?"
    
label name:
    while not mc:
        $ mc = renpy.input("What is your name? It must be 2-10 characters long.", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=10)
        $ mc = mc.strip()
        if len(mc) < 2:
            "You must name your character a minimum of 2 letters."
            $ mc = ""
    $ mc = mc.title()
    
menu:
    "[mc] is the correct name?"
    
    "No":
        jump name
        
    "Yes":
        "You write [mc] clearly on the label."
        
label afterNameMenu:        
        
    mo "Okay, okay, I’ll leave you be. You’re an adult now. Give me a call as soon as you're settled!"
    
    player "I will, Mom. Please don’t worry."
    
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
    player "\“I know right from wrong.”\ You feel a boost in morality as you say these words."
    jump blackscreen

label love:
    player "\“No matter what, there is always love.”\ You feel your heart swell with love and passion as you say these words."
    jump blackscreen
    
label energy:    
    player "\“Live each day as if it’s your last.”\ You feel your energy rise as you say these words."
    jump blackscreen

label money:
    player "\“Save your money, and everything will be alright.”\ You take pride in the savings you’ve accumulated as you say these words."
    jump blackscreen

label intelligence:
    player "\“A clear intellect will solve any problem.”\ You swell with pride at the academic achievements you’ve accomplished as you say these words."
    jump blackscreen

call screen character_creation

label blackscreen:
    scene black
    with dissolve
    
    "You take a moment to appreciate the small token given to you by your family. That feeling lasts for a moment before you realize that the fog has made it impossible to see the path ahead of you."


    # This ends the game.

    return
