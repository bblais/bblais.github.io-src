Title: A funny little probability problem - correct
Date: 2013-03-23 23:23
Author: brianblais
Slug: a-funny-little-probability-problem-correct

## Introduction

In a [previous post][] I made a calculation error, which arrived at an
unintuitive result - a result that still stands. I got side-tracked
with, what I thought, was an arithmetic error. I wasn't satisfied,
because my intuition still thought that the without-replacement
probability should be a smidge higher, because of the reduction in the
number of cards. Because of this, I kept thinking about the problem to
see where it went wrong. I asked another faculty member the same
question, and although I didn't receive a full answer, it was enough to
figure out that I was on the right track initially, but was just a
little sloppy. So what went wrong, and why? Let me reproduce the
problem, and the *correct* calculation this time, and then go on to see
the implications of the error.

##The problem

You draw two cards from a deck, and ask what is the probability that the
first is a black card, and the second is a jack. In math notation, we
want:

$$  
P(B1,J2)  
$$


## The right answer, and how I know

The easiest way to be absolutely sure I had the right answer is to
simply outline every possible two-hand deal, and count the number of
cards in each case.

### With replacement:

    from Game import *
    deals=[]
    deck=makedeck()
    for card1 in deck:
        deck2=makedeck()
        for card2 in deck2:
            deals.append([card1,card2])

    found=[x for x in deals if x[0].color=='Black' and x[1].rank==11]

The length of "found" is 104, and the length of the "deals" is 2704 (52
x 52).

### Without replacement:

    from Game import *
    deals=[]
    deck=makedeck()
    for card1 in deck:
        deck2=makedeck()
        deck2.remove(card1)   # <------ remove the card
        for card2 in deck2:
            deals.append([card1,card2])

    found=[x for x in deals if x[0].color=='Black' and x[1].rank==11]

The length of "found" is 102, and the length of the "deals" is 2652 (52
x 51), which is the *same* fraction.

### With replacement {#with-replacement_1}

*This part was correct, and just repeated here.*

In replacement, we replace the first card after drawing it, reshuffle,
and then draw the second. Thus the two events are independent.

$$  
\begin{array}{rcl}  
P(B1,J2|{\rm replace}) &=& P(B1) \times P(J2) \\  
&=&\frac{26}{52} \times \frac{4}{52} = \frac{104}{2704}=0.0385  
\end{array}  
$$


###Without replacement {#without-replacement_1}

$$  
\begin{array}{rcl}  
P(B1,J2|{\rm no-replace}) &=& P(B1) \times P(J2|B1) \\  
&=&\frac{26}{52} \times
\left(P(J2|B1,J1)\underline{P(J1|B1)}+P(J2|B1,\overline{J1})\underline{P(\overline{J1}|B1)}\right)\\  
&=&\frac{26}{52} \times \left(\frac{3}{51} \cdot
\underline{\frac{2}{26}}+\frac{4}{51} \cdot
\underline{\frac{24}{26}} \right)\\  
&=&\frac{26}{52} \times \underline{\left(\frac{102}{51\cdot 26}
\right)}\\  
&=&\frac{102}{2652}\\  
&=&0.0385  
\end{array}  
$$


where I have put boxes, or underline, around where I differ from the
previous calculation.  

###The difference

The difference comes from the term like:

$$  
P(J2|B1,J1)P(J1|B1)  
$$


In the *incorrect* version, we had

$$  
P(J2|B1,J1)P(J1)  
$$


Essentially, I was being sloppy, and forgot to copy the right-hand side
of the conditional, without the *B1*.

What I find interesting, which is why I've gone to such a detail, are
the following:

1.  how easy it is to make simple arithmetic mistakes in these sorts of
    problems
2.  how easy it is to have a subtle rewrite of a problem, and get a
    different answer
3.  how a simulation gives a lot of confidence in a result

I've found, over time, that I don't tend to trust mathematical results
without a numerical result to support it.  

Still, it is a cool result, and still somewhat unintuitive - at least at
first. Thinking in terms of information, it makes sense - knowing that
the first card is black tells you nothing about the rank of the second
card.  

  [previous post]: a-funny-little-probability-problem-4
