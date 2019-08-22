import time
print "                                               HANGMAN"
print ""                              
print "    "
time.sleep(0.1)
print "                              G",
time.sleep(0.1)
print "E",
time.sleep(0.1)
print "N",
time.sleep(0.1)
print "E",
time.sleep(0.1)
print "R",
time.sleep(0.1)
print "A",
time.sleep(0.1)
print "L ",
time.sleep(0.1)
print "I",
time.sleep(0.1)
print "N",
time.sleep(0.1)
print "S",
time.sleep(0.1)
print "T",
time.sleep(0.1)
print "R",
time.sleep(0.1)
print "U",
time.sleep(0.1)
print "C",
time.sleep(0.1)
print "T",
time.sleep(0.1)
print "I",
time.sleep(0.1)
print "O",
time.sleep(0.1)
print "N",
time.sleep(0.1)
print "'S",
time.sleep(0)
print ".",
time.sleep(0)
print ".",
time.sleep(0)
print "."
time.sleep(1)
print "    "
time.sleep(0.5)
print ""
print "                   Each candidate will have to guess the word till all body parts hunged."
time.sleep(0.5)
print "                              With each right guess score will multiple of 10."
time.sleep(0.5)
print "                             With each wrong attempt a body part will be hung."
time.sleep(0.5)
print "                         Game will run till words to be guessed or body parts are left."
time.sleep(0.5)
print "                 Game will terminate when all body parts hung or words not to be guessed."
print "    "
time.sleep(1)
print "                                             HERE",
time.sleep(1)
print "WE",
time.sleep(1)
print "GO!!!",
time.sleep(1)
print ".",
time.sleep(0.5)
print ".",
time.sleep(0.5)
print ".",
time.sleep(0.5)
print ".",
time.sleep(0.5)
print ".",
print "    "
print ""
print ""
name=raw_input("    INPUT NAME:")
print ""
print "                          Hello ",name,", it's time to play hangman..."
print ""
for z in range(0,10):
    print ""
    hangmanparts=6
    k=""
    f="1"
    j="2"
    l="3"
    c=""
    point=1
    import random
    print "     LEVEL 1"
    print "     LEVEL 2"
    print "     LEVEL 3"
    choice2=raw_input("     Choose level:")
    print ""
    print "                             ",name,", you have opted for level",choice2
    print ""
    print "                                   GUESS THE ALPHABET's "
    print ""
    if choice2==f:
        x=random.randint(0,3)
        if x==0:
            a="aggeressively"
            b=["_","g","g","_","r","e","_","_","i","v","e","l","_"]
            o="_ _ li _ _ o _"
            print o
            print "     HINT - WITH ANGER"
            y1,y2,y3,y4,y5,=0,3,6,7,11
        if x==1:
            a="impoverished"
            b=["i","_","_","o","_","e","r","i","_","h","_","d"]
            o="i _ _ o _ eri _ h _ d"
            print o
            print "     HINT - POOR"
            y1,y2,y3,y4,y5,=1,2,4,8,10
        if x==2:
            a="acquaintance"
            b=["_","c","q","u","_","_","n","_","a","n","c","_"]
            o="_ cqu _ _ n _ anc _"
            print o
            print "     HINT - A PERSON WHOM YOU KNOW"
            y1,y2,y3,y4,y5,=0,4,5,7,11
    if choice2==j:
        x=random.randint(0,3)
        if x==0:
            a="overpower"
            b=["_","v","_","_","p","o","_","e","_"]
            o="_ v _ _ po _ e _"
            print o
            print "     HINT - TO DEFEAT SOMEONE"
            y1,y2,y3,y4,y5,=0,2,3,6,8
        if x==1:
            a="expensive"
            b=["_","_","p","e","_","s","_","_","e"]
            o="_ _ pe _ s _ _ e"
            print o
            print "     HINT - COSTLY"
            y1,y2,y3,y4,y5,=0,1,4,6,7
        if x==2:
            a="nightmare"
            b=["n","i","_","h","_","_","a","_","e"]
            o="ni _ h _ _ a _ e"
            print o
            print "     HINT - UNPLEASENT DREAM"
            y1,y2,y3,y4,y5,=2,4,5,7,8
    if choice2==l:
        x=random.randint(0,3)
        if x==0:
            a="gleamed"
            b=["_","l","_","_","m","_","_"]
            o="_ _ mp _ _ e _"
            print o
            print "     HINT - SHOWN"
            y1,y2,y3,y4,y5,=0,2,4,5,6
        if x==1:
            a="rapping"
            b=["_","_","p","_","i","_","_"]
            o="_ _ te _ _ e _"
            print o
            print "     HINT - HITTING"
            y1,y2,y3,y4,y5,=0,1,3,5,6
        if x==2:
            a="frilled"
            b=["_","r","_","_","l","_","_"]
            o="_ _ im _ _ n _"
            print o
            print "     HINT - FOLDS"
            y1,y2,y3,y4,y5,=0,2,3,5,6
    while "_" in b and hangmanparts>0:
        guess=str.lower(raw_input("     Guess a character :"))
        length=len(guess)
        if length>1:
            print "     You must have ONE character"
            continue
        if length<1:
            print "     At least you guess a character"
            continue
        if guess.isdigit():
            print "     NUMBERS are not allowed"
            continue
        if guess in b[y1]:
            print "     Same character not allowed"
            continue
        if guess in b[y2]:
            print "     Same character not allowed"
            continue
        if guess in b[y3]:
            print "     Same character not allowed"
            continue
        if guess in b[y4]:
            print "     Same character not allowed"
            continue
        if guess in b[y5]:
            print "     Same character not allowed"
            continue
        if guess in a[y1]:
            b[y1]=guess
            for f in b:
                c+=f
            print c
            c*=0
            point*=10
            print "     Guess was RIGHT,",
            print "     Score was,",point
            print "     Chances left are",hangmanparts
            print ""
        if guess in a[y2]:
            b[y2]=guess
            for f in b:
                c+=f
            print c
            c*=0
            point*=10
            print "     Guess was RIGHT,",
            print "     Score was,",point
            print "     Chances left are",hangmanparts
            print ""
        if guess in a[y3]:
            b[y3]=guess
            for f in b:
                c+=f
            print c
            c*=0
            point*=10
            print "     Guess was RIGHT,",
            print "     Score was,",point
            print "     Chances left are",hangmanparts
            print ""
        if guess in a[y4]:
            b[y4]=guess
            for f in b:
                c+=f
            print c
            c*=0
            point*=10
            print "     Guess was RIGHT,",
            print "     Score was,",point
            print "     Chances left are,",hangmanparts
            print ""
        if guess in a[y5]:
            b[y5]=guess
            for f in b:
                c+=f
            print c
            c*=0
            point*=10
            print "     Guess was CORRECT,",
            print "     Score was,",point
            print "     Chances left are,",hangmanparts
            print ""
        if (guess not in a[y1]) and (guess not in a[y2]) and (guess not in a[y3]) and (guess not in a[y4]) and (guess not in a[5]):
            hangmanparts-=1
            if hangmanparts==5:
                for f in b:
                    c+=f
                print c
                c*=0
                print ""
                print """     ___
    |   ||
    |   @
    |
    |
    |
"""
                print "     Chances left are,",hangmanparts
            if hangmanparts==4:
                for f in b:
                    c+=f
                print c
                c*=0
                print ""
                print """     ___
    |   ||
    |   @
    |   /
    |
    |
"""
                print "     Chances left are,",hangmanparts
            if hangmanparts==3:
                for f in b:
                    c+=f
                print c
                c*=0
                print ""
                print """     ___
    |   ||
    |   @
    |  /|
    |
    |
"""
                print "     Chances left are,",hangmanparts
            if hangmanparts==2:
                for f in b:
                    c+=f
                print c
                c*=0
                print ""
                print """     ___
    |   ||
    |   @
    |  /|/
    |
    |
"""
                print "     Chances left are,",hangmanparts
            if hangmanparts==1:
                for f in b:
                    c+=f
                print c
                c*=0
                print ""
                print """     ___
    |   ||
    |   @
    |  /|/
    |  /
    |
"""
                print "     Chances left are,",hangmanparts
    if "_" not in b and hangmanparts>0:
        time.sleep(1)
        print "     GAME WON",
        print ", Yiiiiiiiiipeeeeeeeeeeee!!!!!!!!"
        print ""
    if "_" in b and hangmanparts<0:
        time.sleep(1)
        print "     GAME LOOSE"
        print ""
    if (guess not in a[y1]) or (guess not in a[y2]) or (guess not in a[y3]) or (guess not in a[y4]) or (guess not in a[y5]):
        print "     GAME OVER!!!"
        print ""
        if hangmanparts==0:
            print ""
            print """     ___
    |   ||
    |   @
    |  /|/
    |  / /
    |
"""
        d=str.upper(raw_input("     Want to REPLAY (Y/N):"))
        if d=="Y":
            print ""
            print ""
            time.sleep(0.5)
            continue
        if d=="N":
            print ""
            break
        if d!="Y" or "N":
            print "     Invalid choice"
            break
print ""
print ""
print ""
print "                                                             MADE BY: ",
time.sleep(0.1)
print "S",
time.sleep(0.1)
print "a",
time.sleep(0.1)
print "u",
time.sleep(0.1)
print "r",
time.sleep(0.1)
print "a",
time.sleep(0.1)
print "v",

time.sleep(0.1)
print " ",
time.sleep(0.1)
print "S",
time.sleep(0.1)
print "i",
time.sleep(0.1)
print "n",
time.sleep(0.1)
print "g",
time.sleep(0.1)
print "h"
time.sleep(0.2)
