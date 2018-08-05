print "give me a digit and I will turn it into a word."
n=int(raw_input('enter your digit'))
if n<=5: # Is it five or less?
    if n<=2: # Is it two or less?
        if n==2: # end for 2
            print 'Two'
        else: # Is it one or zero?
            if n==1: # end for 1
                print 'One'
            else: # end for 0
                print 'Zero'
    else: # Is it three, four, or five?
        if n==3: # end for 3
            print 'Three'
        else: # Is it four or five?
            if n==4: # end for 4
                print 'four'
            else: # end for 5
                print 'five'
else: # Is it six or more?
    if n>=8: # Is it eight or nine?
        if n==8: # end for 8
            print 'eight'
        else: # end for 9
            print 'nine'
    else: # Is it six or seven?
        if n==7: # end for 7
            print 'seven'
        else: # end for 6
            print 'six'
        
        
    
