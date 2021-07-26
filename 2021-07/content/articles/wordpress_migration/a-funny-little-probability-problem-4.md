Title: A funny little probability problem
Date: 2013-03-23 12:21
Author: brianblais
Slug: a-funny-little-probability-problem-4

**(Note: this problem has an error...can you find it? I will post the
correction ~~soon~~ [here][], which itself has some interesting
properties)**

We often make the important distinction between drawing cards with or
without replacement when determining the results of card games. Clearly,
if you draw a Jack, then the probability of drawing another Jack is
different whether you replace and shuffle, or you leave the drawn Jack
out. In an extreme case, imagine a deck with only one Jack.

After going through an example in class, and applying replacement, a
student asked about the same example without replacement. I didn't have
time to go over the example in class, but I sketched how the calculation
would be different, and would yield a different answer. After class,
going through the calculation, I was in for a surprise.

## The problem


You draw two cards from a deck, and ask what is the probability that the
first is a black card, and the second is a jack. In math notation, we
want:

$$  
P(B1,J2)  
$$

## With replacement


In replacement, we replace the first card after drawing it, reshuffle,
and then draw the second. Thus the two events are independent.

$$  
\begin{array}{rcl}  
P(B1,J2|{\rm replace}) &=& P(B1) \times P(J2) \\  
&=&\frac{26}{52} \times \frac{4}{52} = 0.0385  
\end{array}  
$$

##Without replacement


Without replacement is a little trickier to set up, because the second
draw depends on the first.

$$  
\begin{array}{rcl}  
P(B1,J2|{\rm no-replace}) &=& P(B1) \times P(J2|B1) \\  
&=&\frac{26}{52} \times
\left(P(J2|B1,J1)P(J1)+P(J2|B1,\overline{J1})P(\overline{J1})
\right)\\  
&=&\frac{26}{52} \times \left(\frac{3}{51} \cdot
\frac{4}{52}+\frac{4}{51} \cdot \frac{48}{52} \right)\\  
&=&\frac{26}{52} \times \left(\frac{204}{51\cdot 52} \right)\\  
&=&0.0385  
\end{array}  
$$

**the same answer!!**

**(Note: this problem has an error...can you find it? I will post the
correction ~~soon~~ [here][], which itself has some interesting
properties)**

## Conclusion


The only conclusions are

1.  My intuition fails me sometimes, on even simple problems
2.  Drawing a black card on the first draw tells you no more information
    about drawing a jack on the second (or any other number, for that
    matter).  

Cool!

**(Note: this problem has an error...can you find it? I will post the
correction ~~soon~~ [here][], which itself has some interesting
properties)**

  [here]: a-funny-little-probability-problem-correct
