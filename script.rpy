define d = Character('Dayana', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

label start:

    "So after \"the incident\" at my last school you move to east boston and end up having to switch schools."

    "Your mom thinks its in your best intrest to go to a \"good school\" so she makes you go to Excel Academy a charter school by your house."

    "The morning of you first day starts and you get ready, and head off." 

    scene bg exceloutside
    with dissolve

    "After a short while, we reach excel, the school that we both go to."

    "It's a kinda rundown and fancy at the same time, it looks out of place from where ."

    "I look around to find the guide thats supposed to go show me around the school."

    "Then out of the corner of my eyes i see this short girl walking over to me, I first thought that she was a middle schooler since theres one to the right of the school."

    "But as it turns out shes the tour guide."

    show sylvie green smile
    with dissolve

    "She she waves and intoduces her self."

    d "Hi im dayana, i'll be the one showing you around today."

menu optional_name:
    "what do you say?"
    "Be Rude":
        jump angry
    "Be Nice":
        jump happy

    


label angry:

    m "*sigh*"

    m "What do you want?"

    show sylvie green smile
    
    d "umm..."

    d "I was supposed to be your tour guide but not any more."

    d "so rude and for what"

    hide sylvie green smile
    with dissolve

    "..."
    jump leaving_mad





label happy:

    m "*sigh*"

    m "Hey, im the new kid"

    d "I know the principle gave me a photo of what you look like."

    m "Oh did he. or where you just stalking me"

    
    "you both laugh" 


    jump leaving_happy

label leaving_happy:

    d "Ok lets get this started "

    hide sylvie

    "dayana walks away"
    
    "..."

    m "Here we go ig"



    

label leaving_mad:

    "Well uh that didnt go as planed"

    "Looks like im going to have to explore the school on my own"

    "This couldnt possibly go bad"

    "..."
   
    "Right?"

    scene bg xlfront

    "..."

    "so where should i go first?"



