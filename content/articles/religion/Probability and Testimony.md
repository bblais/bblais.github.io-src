Title: Sometimes more testimony is worse.
subtitle: Scientific methods impact source reliability
Date: 2022-06-14
status: published
image: zwaddi-YvYBOSiBJE8-unsplash.jpg

When asked the question raised by McLatchie, 

![[Pasted image 20220614074246.png]]

I would have to say that new testimony does not raise my probability for a miracle, mostly because all prior attempts to do so have been debunked or at best shown to be profoundly unreliable.   This lowers my credence in the sources, even if I don't have time to investigate in detail the next new claim.  Am I being hyper-skeptical?  I don't think so -- I'm simply adjusting my beliefs to the evidence, and that evidence is that miracle claims have not met their burden of proof.  How could this problem be addressed for me?   In modern settings, having randomized-controlled studies of miracles would be the best  -- because those claims that use this process have shown themselves to be reliable, and thus $a\rightarrow 0$ in the model described below.  Given modern miracle claims, and their issues, I don't think that any ancient source could convince me of miracles -- their reliability on matters of the physical, chemical, and biological world has been shown to be terrible, thus $a\rightarrow 1$ in the model below.  

Although this model is a simplification, it is useful to see that the adjustment of probabilities needs to be taken with care and that unintuitive and non-monotonic effects can easily occur (you can see another non-monotonic effect with the high-low-nines deck example [shown here]({filename}../religion/Bad Apologetics - miscellaneous topics from Jonathan McLatchie.md)).  Even if for a single data point, the probability of a model increases, the same can't be said of an accumulation of data points unless one is sure that all of the simplifying assumptions are correct -- and they never are.

## Introduction

In response to Paulogia's tweet:

![[Pasted image 20220614074210.png]]

Jonathan McLatchie has a reply that got me thinking:

![[Pasted image 20220614074246.png]]


It relates to an idea about testimonies I've heard around, but [clearly stated by Timothy McGrew](https://youtu.be/GH11Ur8cjwM?t=931):

 
![[Pasted image 20220614073547.png]]
> What the Math Means - A sufficient number of *independent* testimonies, each of which has *at least a certain minimum amount of force*, will overcome any finite presumption against a miracle.  Hume's "everlasting check" fails; a cumulative case can, in principle, make any miracle claim credible. 

It's a mathematical fact that if we have all of the following...

1. several data points, $D_1, D_2, \ldots, D_n$ 
2. for each, the probability of the miracle, $M$, is greater than it's negation, $\bar{M}$: $P(M|D_i)/P(\bar{M}|D_i)>1$
3. the data are logically independent, $P(D_i|M,D_j)=P(D_i|M)$

then we can look at the posterior odds for the miracle,

$$
\begin{aligned}
 O &\equiv \frac{P(M|D_1, D_2, \ldots, D_n)}{P(\bar{M}|D_1, D_2, \ldots, D_n)} \\
 &=\frac{P(D_1, D_2, \ldots, D_n|M)P(M)}{P(D_1, D_2, \ldots, D_n|\bar{M})P(\bar{M})} \\
 &=\underbrace{\frac{P(D_1|M)\cdot P(D_2|M) \cdots P(D_n|M)}{P(D_1|\bar{M})\cdot P(D_2|\bar{M}) \cdots P(D_n|\bar{M})}}_{\text{cumulative testimony}}\times \underbrace{\frac{P(M)}{P(\bar{M})}}_{\text{prior odds}} \\
 \end{aligned}
$$
and the cumulative testimony can, in principle (for sufficiently large $n$), overwhelm *any* small prior odds.  The McGrews use this fact in their article [The Argument from Miracles: A Cumulative Case for the Resurrection of Jesus of Nazareth](https://onlinelibrary.wiley.com/doi/10.1002/9781444308334.ch11), but definitely check out the [9-hour analysis of the problems with this article]({filename}../media/bad_apologetics_2021.md).  ([Part 1 of a summary can be found here]({filename}../religion/bad_apologetics_2021_summary_part_1.md)).

Typical (and perfectly reasonable) responses to this are:

1. the independence of the data are not established
2. the data themselves are not what are often claimed -- the McGrews will often say that, for example, a data point is $D_W = \text{the women found the tomb}$ when in fact that data point should be $D_{TW} = \text{there is a text that says that the women found the tomb}$. 
3. the priors are overestimated, or ignored, and the likelihoods are overestimated
4. there is no way to corroborate the data

In this post, I want to explore point 2 above, that we do not have a claim itself, but instead we have someone *making* a claim.  This provides one extra level of indirectness to the evidence.  I want to discuss this, because I think this fact alone accounts for most of my own reticence in accepting extraordinary claims, why the methods of science work so well, and seems to show a naïveté in the apologists use of evidence.   I also think this point is rarely addressed.

## Setting up the problem

In [E.T. Jaynes](https://bayes.wustl.edu/etj/etj.html) book on [Probability Theory](https://www.amazon.com/Probability-Theory-Science-T-Jaynes/dp/0521592712) in Chapter 5 on peculiar uses of probability theory, he explores the idea of diverging probability assignments due to ones perspective on the source of the information.  This idea motivated my particular approach here.  

We have the proposition, $M\equiv \text{a miracle occurred}$, for which we have a prior, 
$$\begin{aligned}
P(M) &\equiv m\\
P(\bar{M}) &\equiv 1-m\\
\end{aligned}$$
Note, that for *miracle* here you can substitute any extraordinary claim.  Our data consists not of extraordinary observations of the world but of a series of *claims* about such observations.  This can include sources such as

- statements from people who made the observations
- texts, in this case ancient texts, which include the claims
- second- and third-hand accounts of observations

For the sake of concreteness, I'll say that the data is $C \equiv \text{person X has made a claim of } M$.

For the sake of charity, we will assume that if a miracle has occurred, then the person would make that claim with certainty, 
$$
P(C|M)=1
$$
Also for charity, we will ignore data that we'd expect under $M$ but do not observe.  

If the miracle did not occur, we might expect someone to make the claim that there was a miracle anyway.  This could be from a simple mistake, someone who interprets the world, in general, in terms of divine-action (e.g. rain is caused by the Gods, etc...).  It could be from outright lying.  It could be from lack of proper observational controls, or lack of information.  Any of these could lead someone to make a claim of $M$ even if its negation, $\bar{M}$, is actually true.  I simplify this to some constant probability,
$$
P(C|\bar{M})=a
$$
We can now write down with this simple model, the probability of a miracle given this data,
$$
\begin{aligned}
P(M|C) &= \frac{P(C|M)P(M)}{P(C|M)P(M)+P(C|\bar{M})P(\bar{M})} \\
&=\frac{1\cdot m}{1\cdot m + a\cdot (1-m)} = \frac{m}{m+a\cdot(1-m)}
\end{aligned}
$$
It's good to pause to see if this form makes sense.  If $a=0$, which means that if there is no miracle, person $X$ will never make the claim that there is one.  This leads to $P(M|C)_{a=0} = 1$ which is what is expected -- the claim of a miracle can't be mistaken.   What if person $X$ always reports a miracle, even if there isn't one?  In that case $a=1$ and we get $P(M|C)_{a=1} = m$ which is our prior probability for a miracle.  Essentially, this person with $a=1$ gives no useful information -- they are the proverbial boy who cried miracle.  No new information means that our probabilities do not change and we are left with our original prior probability.

We can think of $a$ as a measure of the reliability (or rather unreliability) of the source, with $a=0$ being completely reliable and $a=1$ being (nearly) unreliable.  I say "nearly" because we are still assuming that person $X$ reliably communicates a miracle if it does occur.  

One thing to note about our charitable choices in this model is that that the probability can never go lower than the initial prior.  This is clearly wrong, because one can potentially have disconfirming evidence for a miracle, but we are not considering this here.  Thus, at the outset, this model has a pro-miracle bias built in.  Even with this bias it will become clear how we can counter miracle claims by exploring the scientific process in a bit more detail below.  First, we reproduce the McGrew observation above using this model, by accumulating multiple independent claims, $C_0, C_1, C_2, \ldots, C_n$.  Following the process above ([checking with WolframAlpha](https://www.wolframalpha.com/input?i=w%3Dm%2F%28m%2Ba*%281-m%29%29%3B+x%3Dw%2F%28w%2Ba*%281-w%29%29%3B+y%3Dx%2F%28x%2Ba*%281-x%29%29%3B+z%3Dy%2F%28y%2Ba*%281-y%29%29%3B+)) we get

$$
\begin{aligned}
P(M|C_0, C_1, C_2, \ldots, C_n) &= \frac{m}{m+a^n\cdot(1-m)}
\end{aligned}
$$
A couple of examples would look like

![[Pasted image 20220614091756.png]]


One can show that, with a high enough $n$, even a very low prior ($m \ll 1$) and a really unreliable source ($a \sim 1$) you can recover the probability of the miracle.  In the example above, I show for a slightly low prior for miracle ($m=0.1$) and a marginally unreliable source ($a=0.8$) we recover the probability of a miracle ($P(M|C_0, \ldots, C_n)>0.5$) in about 10 data points whereas with a lower prior by a factor of 100 and a more unreliable source, it takes $n=66$ points.   One can question whether the claims-data used to support miracles rise to this number (I don't think it does), but that will not be my main point here.  

## Enter the methods of science

The process of data and model comparison doesn't exist in a vacuum.  It's against a backdrop of science demonstrating that many (all?) of the claims for miracles and most extraordinary claims (e.g. UFOs, alien abductions, homeopathy, etc...) have been shown to be false or at best unsubstantiated.  It is my personal experience that none of the [miracle claims that have been presented to me](https://bblais.github.io/search.html?q=miracles) withstand even the slightest level of scrutiny.  There's a [very long discussion on the best cases here]({filename}../media/bad_apologetics_feb_2022.md) with the same result -- one problem after another.  How does this affect the model above?   Imagine the following process:

- Claim 1 $\rightarrow$ debunking of Claim 1 $\rightarrow$ Claim 2 $\rightarrow$ debunking of Claim 2 $\rightarrow$ Claim 3 $\rightarrow$ debunking of Claim 3 $\rightarrow \cdots$ 

which pretty much describes my personal experience with the evidence for miracles (and most extraordinary claims).  Each time a claim is put up, and I investigate it, I find it lacking -- usually in pretty mundane and straightforward ways.  Either the claim is completely debunked or at a minimum shown to be not reliable.  What this process does is change how *reliable* the sources are, so that next time, similar claims might be less likely. In the model, $a$ is pushed toward the value of $1$ each time a claim is dispensed with.  Mathematically, a simple way to accomplish this is to add to $a$ some fraction, $\gamma$, of the remaining distance between $1$ and the current value of $a$.  In this way, $a$ is pushed toward $1$ but will never reach or exceed it.  

$$
a \rightarrow a+\gamma\cdot (1-a)
$$
thus the source-reliability, $a$, is no longer a constant but depends on how many ($n$) claims have been presented (and dispensed with).  We can [find $a$ as a function of $n$](https://www.wolframalpha.com/input?i=a_n%3Da_n-1+%2B+gamma*%281-a_n-1%29), 

$$
a(n) = (a_0 + \gamma -1)\cdot (1-\gamma)^{n-1}+1
$$
where $a_0$ is the initial assessment of the reliability of the source of the claims.  A quick pause to see that this makes sense:  if $\gamma=0$ there is no change to the reliability of the claims, and we have our original value $a(n)=a_0$.  If $\gamma=1$ then even after the first claim, the source becomes completely unreliable, $a=1$.   

This new process gives us a messier posterior for the miracle,

$$
\begin{aligned}
P(M|C_0, C_1, C_2, \ldots, C_n) &= \frac{m}{m+\left((a_0 + \gamma -1)\cdot (1-\gamma)^{n-1}+1\right)^n\cdot(1-m)}
\end{aligned}
$$
But easy to look at numerically,

![[Pasted image 20220614100045.png]]

We can see the effect of claims being shown to be unreliable can make further testimony *less reliable*, even in a model which has a definitively pro-miracle bias.  One can see in the curves on the left that the initial claims increase the probability of a miracle, but as they get debunked that initial increase in confidence is erased, and further testimony reduces the probability of claims back to the prior. 

## Conclusion

When asked the question raised by McLatchie, 

![[Pasted image 20220614074246.png]]


I would have to say that new testimony does not raise my probability for a miracle, mostly because all prior attempts to do so have been debunked or at best shown to be profoundly unreliable.   This lowers my credence in the sources, even if I don't have time to investigate in detail the next new claim.  Am I being hyper-skeptical?  I don't think so -- I'm simply adjusting my beliefs to the evidence, and that evidence is that miracle claims have not met their burden of proof.  How could this problem be addressed for me?   In modern settings, having randomized-controlled studies of miracles would be the best  -- because those claims that use this process have shown themselves to be reliable, and thus $a\rightarrow 0$ in the model above.  Given modern miracle claims, and their issues, I don't think that any ancient source could convince me of miracles -- their reliability on matters of the physical, chemical, and biological world has been shown to be terrible, thus $a\rightarrow 1$.  

Although this model is a simplification, it is useful to see that the adjustment of probabilities needs to be taken with care and that unintuitive and non-monotonic effects can easily occur (you can see another non-monotonic effect with the high-low-nines deck example [shown here]({filename}../religion/Bad Apologetics - miscellaneous topics from Jonathan McLatchie.md)).  Even if for a single data point, the probability of a model increases, the same can't be said of an accumulation of data points unless one is sure that the simplifying assumptions are correct -- and they never are.