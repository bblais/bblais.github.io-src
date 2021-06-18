title: Laplace and Twins
subtitle: Why Bayes is still right
date: 3/28/2016

From this paper,

[http://statweb.stanford.edu/~ckirby/brad/other/2013Perspective.pdf](http://statweb.stanford.edu/~ckirby/brad/other/2013Perspective.pdf)

we have the following text:

>“Controversial theorem” sounds like an oxymoron, but Bayes’ Rule has played this
part for two and a half centuries. Twice it has soared to scientific celebrity, twice it has crashed,
and it is currently enjoying another boom. The Theorem itself is a landmark of logical reasoning
and the first serious triumph of statistical inference, yet is still treated with suspicion by a
majority of statisticians. There are reasons to believe in the staying power of its current
popularity, but also some worrisome signs of trouble ahead.

>Here is a simple but genuine example of the Rule in action (1). A physicist couple I know
learned, from sonograms, that they were due to be parents of twin boys. “What is the probability
our twins will be Identical rather than Fraternal?” was their question. There are two pieces of
relevant evidence: only one-third of twins are Identical; on the other hand, Identicals are twice as
likely to yield twin boy sonograms, since they are always same-sex while Fraternals are 50/50.
Putting this together, the Rule correctly concludes that in this case the two pieces balance out,
and that the odds of Identical are even. Note: the twins were fraternal.

>...

>The trouble and the
subsequent busts came from overenthusiastic application of the Theorem in the absence of
genuine prior information, with Laplace as a prime violator. Suppose that in the twins example
we lacked the “one-third Identicals” prior knowledge. Laplace would have casually assumed a
uniform distribution between zero and one for the unknown prior probability of Identical
(yielding 2/3 rather than 1/2 as the answer to the physicists’ question.) In modern parlance,
Laplace would be trying to assign an “uninformative prior,” one having only neutral effects on
the output of Bayes’ rule (3).

## The original calculation, with knowledge

So, let's start with the following knowledge and some notation.

* we've observed twin boy sonograms, a proposition denoted as $S$
* 1/3 of twins are identical, thus $P(I) \equiv q = 1/3$.  You'll see why I use $q$ later.

We are interested in $P(I|S)$.  We can derive a few related probabilities, like

* $P(S|I) = 1/2$.  This comes from the notion that identical twins must be either BB or GG, and only half of them would give twin *boy* sonograms.
* $P(S|\sim I) = 1/4$. This comes from the notion that fraternal twins must be BB, BG, GB or GG, and only 1/4 of them would give twin *boy* sonograms.

Setting the calculation in terms of odds ratios (which I don't like as much as direct probabilities), we get

\begin{eqnarray}
\frac{P(I|S)}{P(\sim I|S)} &=& \frac{P(S|I)P(I)}{P(S|\sim I)P(\sim I)} \\
&=& \frac{1/2 \times 1/3}{1/4 \times (1-1/3)} = 1
\end{eqnarray}
or 1:1 odds, and thus

$$P(I|S)=1/2$$

## What would Laplace do?

The text refers to an "uninformative prior", in a derogatory way, and then proceeds to mistakenly use an *informative*, incorrect prior and attribute it to Laplace.  Laplace, [like Hume](http://web.bryant.edu/~bblais/misquoting-hume.html), is mischaracterized so often it really is remarkable.  Let's follow through how the text gets the $P(S|I)=2/3$ presumably what Laplace would do.  To get this, we assume that there are two states (identical and fraternal) and that uninformative means equal probability to these states.  Thus the prior is $P(I)=1/2$, and the same calculation proceeds as 

\begin{eqnarray}
\frac{P(I|S)}{P(\sim I|S)} &=& \frac{P(S|I)P(I)}{P(S|\sim I)P(\sim I)} \\
&=& \frac{1/2 \times 1/2}{1/4 \times (1-1/2)} = 2
\end{eqnarray}
or 2:1 odds and thus

$$P(I|S)=2/3$$

The author then implies that this is clearly wrong, even though it does make sense that different knowledge *should* lead to different probability assignments.  Regardless, the author calls Laplace the "prime violator" of the "overenthusiastic application" of Bayes Theorem, where Laplace "casually assumed a uniform distribution" for the probability of getting identical twins. However I would say that this is the *correct* thing to do when one has no information - to do otherwise *inserts* unjustified information into the system.

## What would Laplace *really* do?

Let's assume Laplace is really starting from scratch, and can't even estimate the number of twins well, so he does use a uniform distribution on $q$ above.  The proper calculation then is to *marginalize* over this uniform distribution.  Applying Bayes Theorem, we get

\begin{eqnarray}
P(I|S) &=& \int_0^1 \frac{P(S|I) \cdot q}{P(S|I)\cdot q + P(S|\sim I)\cdot (1-q)} P(q) dq
\end{eqnarray}

As above we have

* $P(S|I) = 1/2$
* $P(S|\sim I) = 1/4$
* $P(q) =$ uniform from 0 to 1

and so we get (with some [Wolfram Alpha magic](http://www.wolframalpha.com/input/?i=integrate+1%2F2*q%2F%5B1%2F4*q%2B1%2F4%5D+for+q+from+0+to+1) )

\begin{eqnarray}
P(I|S) &=& \int_0^1 \frac{1/2 \cdot q}{1/2\cdot q + 1/4\cdot (1-q)} dq = 2-\log 4 \approx 0.614
\end{eqnarray}

again, different than our informed probability, but also different than assuming that identical twins must occur 50% of the time.  Essentially, by not knowing that identical twins are actually as rare as 1/3 of all twins, we will overestimate the probability that a pair of boy sonograms would be identical - this is a *good* thing, not a bad one.  To do otherwise would be assuming knowledge we don't have (at the time).

## What would Laplace do *next*?


Like a good scientist, Laplace would probably follow this line of logic with some data taking.  Imagine he observes $h$ identical twins in $N$ twins, he would change his uniform distribution to a Beta distribution - just like a coin flip.  The calculation now looks like:

\begin{eqnarray}
P(I|S) &=& \int_0^1 \frac{1/2 \cdot q}{1/2\cdot q + 1/4\cdot (1-q)} {\rm Beta}(h+1,N+1) dq 
\end{eqnarray}

which is easiest done numerically.  Using the sie library from [my book](http://web.bryant.edu/~bblais/statistical-inference-for-everyone-sie.html) I have for $h=0$, $N=0$, 

```python
h=0
N=0

d=beta(h,N)
q=linspace(0,1,1000)
dq=q[1]-q[0]
pq=d.pdf(q)

f=sum(0.5*q/(.5*q+.25*(1-q))*pq*dq)
print f
```

> f = 0.614

matching our analytical calculation.  Now, with a modest 30 sets of twins, 10 of which are identical (consistent with our modern observations), we have

```python
h=10
N=30

d=beta(h,N)
q=linspace(0,1,1000)
dq=q[1]-q[0]
pq=d.pdf(q)

f=sum(0.5*q/(.5*q+.25*(1-q))*pq*dq)
print f
```

> f = 0.506

or within 1% of the modern value.  So Laplace would have arrived at a perfectly reasonable answer prior to looking at the data and a well-informed answer within one visit to a French hospital.  

So, what is the objection to Bayes' Theorem again?
