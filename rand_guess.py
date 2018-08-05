print 

import random
import os

#----------- this is VASU VERSION -----------------------#
os.system('clear')
print "\n\n --------- Welcome to the GUESS THE NUMBER game! --------- \n\n"
d= int(raw_input('Type the max number N for the range 1..N :'))
p=0
a=0
g=0
n= random.randint(1, d)
print "A random number has been generated"
while True:
    g= int(raw_input('Guess what the number is, the number of attemps you use will be recorded'))
    a= a+1
    if g==n:
       print 'you have guessed correctly'
       break
    if g==0:
       print 'you lose, unable to try more..ha..ha'
       break
    if g!=n:
        print "You are wrong, try again!"

print "\n\n\n ---- RESULT ------ \n\n"        
print "        Number of attempts :", a, "RANDOM NUMBER..", g

s= d-a
print "        Here's your score...", s, 

    
    
