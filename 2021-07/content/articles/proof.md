Title: Anyone using the term "scientific proof" doesn't know science
Date: 2014-01-31
Tags:  science, probability

In my introduction to probability in class this week, I was asked if proof and evidence really meant the same thing.  They don't.  To summarize,

> *Proof* does not exist in science, only in math an philosophy.

The only place you can have proof is where you have *axioms* (i.e. unprovable assertions), and can then *prove* a number of consequences of those axioms.  We can prove, for example, that the sum of the angles of a triangle is 180 degrees, if we start with the Euclidean axioms of geometry.  Science doesn't have axioms, and thus there are no proofs - there is only evidence.  We sometimes hear the term "proven scientifically", even from people who should know better (like Richard Carrier in his ["Is Philosophy Stupid" talk], his [books], and his [articles]).  Other treatments of this topic can be found on the [RationalWiki] and on [talkorigins].

The mapping to probability theory is quite easy: proofs involve probabilities which are either $P=1$ or $P=0$.  Another way of putting it is,

> All of the evidence in the world cannot bring the probability of a scientific claim to certainty.  

To see this with probability theory, imagine we have two hypotheses for the Earth - flat earth and round earth.  We can write Bayes' Rule for the probability of each given the data.  Note that this data includes things like the experience of airplane flight, Magellan's trip, pictures from space - all of which could be faked!  The flat earth hypothesis is not *logically* impossible. 

\begin{eqnarray}
P({\rm round}|{\rm data}) &=& \frac{P({\rm data}|{\rm round})P({\rm round})}{P({\rm data}|{\rm flat})P({\rm flat})+P({\rm data}|{\rm round})P({\rm round})}\\\\
P({\rm flat}|{\rm data}) &=& \frac{P({\rm data}|{\rm flat})P({\rm flat})}{P({\rm data}|{\rm flat})P({\rm flat})+P({\rm data}|{\rm round})P({\rm round})} 
\end{eqnarray}

Notice that, no matter how well the round earth hypothesis explains the data, 
$$P({\rm data}|{\rm round})\approx 1$$
and how unlikely you believe it is that the Earth is flat even *before* the data (a far too strong of an anti-flat Earth bias than is actually warranted),
 $$P({\rm flat})\ll 1$$
as long as there is some *possible* (even if seriously contrived) way to explain the data with the flat earth hypothesis, 
 $$P({\rm data}|{\rm flat}) \neq 0$$
it is *mathematically impossible* to make the round earth hypothesis certain,
$$P({\rm round}|{\rm data})\le 1$$

On the right-hand side of Bayes' Rule, the larger the round-earth terms and the flat-earth terms get to 1 and 0, respectively,  the closer the left-hand terms get to 1 and 0, but they never *equal* 1 and 0.  This does not mean that we can't be *confident* of claims, only that we cannot have *absolute certainty of anything* in science (and therefore, in life in general).  Anyone who doesn't understand that does not understand science.


["Is Philosophy Stupid" talk]: http://www.youtube.com/watch?v=YLvWz9GQ3PQ
[articles]: http://infidels.org/library/modern/richard_carrier/theory.html
[books]: http://www.amazon.com/Proving-History-Bayess-Theorem-Historical/dp/1616145595
[RationalWiki]: http://rationalwiki.org/wiki/Proof
[talkorigins]: http://www.talkorigins.org/faqs/comdesc/sciproof.html