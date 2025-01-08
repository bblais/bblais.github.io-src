Title: A funny little probability problem - some closure
Date: 2013-03-25 09:48
Author: brianblais
Slug: a-funny-little-probability-problem-some-closure

## Introduction

This weekend I got hooked on a [funny little probability puzzle][], and
have finally found some closure. It started with an off-hand comment by
a student, which led me to think more deeply about the problem once I
actually worked it out. The problem was simple enough:

> You draw two cards from a deck, and ask what is the probability that
> the first is a black card, and the second is a jack. In math notation,
> we want:
>
> $$
>  P(B1,J2)  
> $$
>
> </p>

I compared *with replacement* to *without replacement*, and got the same
answer, much to my surprise. After satisfying my surprise with a
numerical simulation, I thought, "there are clearly cases where it
*does* make a difference between replacement and no replacement (drawing
two jacks, for example), so where does it matter?"

##Another case

So I did another case:

> You draw two cards from a deck, and ask what is the probability that
> the first is a *face* card, and the second is a jack. In math
> notation, we want:
>
> 
> $$
>  P(F1,J2)  
>  $$
>
>
> </p>

### With replacement:

$$
\begin{aligned} 
P(F1,J2|{\rm replace}) &= P(F1) \times P(J2) \\
&=\frac{12}{52} \times \frac{4}{52} = \frac{48}{2704}=0.0178  
\end{aligned} 
$$
</p>
### Without replacement

$$
\begin{array}{rcl}  
P(F1,J2|{\rm no-replace}) &=& P(F1) \times P(J2|F1) \\  
&=&\frac{12}{52} \times
\left(P(J2|F1,J1)P(J1|F1)+P(J2|F1,\overline{J1})P(\overline{J1}|F1)\right)\\
&=&\frac{12}{52} \times \left(\frac{3}{51} \cdot
\frac{4}{12}+\frac{4}{51} \cdot \frac{8}{12} \right)\\ 
&=&\frac{44}{2652}\\  
&=&0.0166  
\end{array}  
$$

## The General Case

It appeared to me that there was a pattern - some relationship between
the number of jacks, the number of cards, and the number of the
sub-population (color, face, etc...) such that the replacement and the
no-replacement cases would come out the same, because *most* cases
don't. So I looked at it in general, where I define:

$$
\begin{array}{rcl}  
N_C &=& \mbox{number of cards} \\  
N_J &=& \mbox{number of jacks} \\  
N_F &=& \mbox{number of the sub-population (faces, color,
etc...)}\\  
N_{JF} &=& \mbox{number of jacks in the sub-population}  
\end{array}  
$$

### With replacement: {#with-replacement_1}

$$
\begin{array}{rcl}  
P(F1,J2|{\rm replace}) &=& \frac{N_F}{N_C} \cdot
\frac{N_J}{N_C}  
\end{array}  
$$

### Without replacement {#without-replacement_1}

$$
\begin{array}{rcl}  
P(F1,J2|{\rm no-replace}) &=& P(F1) \times P(J2|F1) \\  
&=&\frac{N_F}{N_C} \times
\left(P(J2|F1,J1)P(J1|F1)+P(J2|F1,\overline{J1})P(\overline{J1}|F1)\right)\\  
&=&\frac{N_F}{N_C} \times \left( \frac{N_J-1}{N_C-1}\cdot
\frac{N_{JF}}{N_F} + \frac{N_J}{N_C-1}\cdot
\frac{N_F-N_{JF}}{N_F} \right)  
\end{array}  
$$

### Solving

When these two expressions are the same, we have:

$$
\begin{array}{rcl}  
\frac{N_F}{N_C} \cdot \frac{N_J}{N_C}&=&\frac{N_F}{N_C}
\times \left( \frac{N_J-1}{N_C-1}\cdot \frac{N_{JF}}{N_F} +
\frac{N_J}{N_C-1}\cdot \frac{N_F-N_{JF}}{N_F} \right)  
\end{array}  
$$

which, believe it or not, simplifies to

$$
\begin{array}{rcl}  
N_F/N_C &=& N_{JF}/N_J  
\end{array}  
$$

or, in other words, for the replacement and non-replacement
probabilities to be the same in this simple game, the fraction of the
subpopulation to the deck has to be the same fraction as the jacks in
that subpopulation to the number of jacks. In the case of color, 1/2 the
deck is black and 1/2 the jacks are black. However, 3/13 of the deck are
face cards and 4/4 of the jacks are face cards. An interesting symmetry.

Essentially, when there exists this symmetry, knowledge of the first
draw gives you no information about the second. I imagine there is some
fancy math theorem to this effect, but it is still pretty cool.

  [funny little probability puzzle]: a-funny-little-probability-problem-correct.html
