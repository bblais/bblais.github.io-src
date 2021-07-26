Title: Probability Problems and Simulation
Date: 2009-09-16 12:36
Author: brianblais
Slug: probability-problems-and-simulation

There are a number of classic probability problems that challenge the
intuition, both for students and for teachers. I have found that one way
to overcome this intuition block is to write a quick simulation. A good
example is the classic evil probability [problem of the Monty Hall][].
The derivation of the solution is straightforward, but it is easy to
convince yourself of the wrong answer. A quick simulation, like the one
below, makes it clear: 1/3 of the time the host gets a choice with which
door to open, and 2/3 of the time the host has no choice - with the
other door having the prize. I find a numerical simulation helps to
bolster my confidence in a mathematical analysis, especially when it is
particularly unintuitive.

    from random import randint
    import random
    turn=0
    win=0
    human=False

    while turn<500:
        
        prize=randint(1,3)
        door_choices=[1,2,3]
        
        if human:
            your_first_answer=input('Which door %s? ' % str(door_choices))
        else:   # automatic
            your_first_answer=random.choice(door_choices)
        
        if prize==your_first_answer:  # happens 1/3 of the time
            door_choices.remove(your_first_answer)  # get the other two
            door_choices=sorted([your_first_answer,
                                 random.choice(door_choices)])
        else:
            door_choices=sorted([prize,your_first_answer])

        if human:
            your_second_answer=input('Which door %s? ' % str(door_choices))
        else:   # automatic
        
            # always switch
            if door_choices[0]==your_first_answer:
                your_second_answer=door_choices[1]
            else:
                your_second_answer=door_choices[0]
            
        if your_second_answer==prize:
            print "You win!"
            win+=1
        else:
            print "You Lose!"
        
        turn+=1


    print "Winning percentage: ",float(win)/turn*100



[problem of the Monty Hall]: http://en.wikipedia.org/wiki/Monty_Hall_problem
