print "Welcome to the game!"
d= int(raw_input('Type the desiered difficulty (numbers only)')) # d is difficulty
p=0 # used to break the while loop
a=0 # number of attempts made so far
g=0 # the player's current guess, guessing 0 is giving up
import random
n= random.randint(1, d) # n is the random number that is generated 
print "A random number has been generated"
print 'guess 0 to give up'
while p==0:
    g= int(raw_input('Guess what the number is, the number of attemps you use will be recorded'))
    if g!=0:
        a= a+1
    if g==n:
        p=1
        print 'you have guessed correctly'
    else:
        if g==0:
            print "Oh you have given up. You are such a worthless human!"
            print "Anyway, the random number is...", n
            print "The number of attempts you made...", a
            print "Your score is negative infinety"
            p=1
        else:
            print "You are wrong, try again!"
if g==n:
    print "Here's the number of attempts you have used..."
    print a
    s= d-a # s is the score
    print "Here's your score..."
    print s
    
