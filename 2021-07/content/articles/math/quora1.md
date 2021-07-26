title: If at first you don't succeed (for 50 times) you might reconsider
date: Jan 29, 2019
image: lea-bohm-576729-unsplash.jpg

Here's a [straightforward problem](https://www.quora.com/If-there-is-a-25-chance-of-something-what-is-the-probability-that-you-fail-to-succeed-50-times-in-a-row-before-you-finally-do-succeed/answer/Brian-Blais) from Quora - probably found in a textbook - but I try to find a new direction to make it more interesting.

> If there is a 25% chance of something, what is the probability that you fail to succeed 50 times in a row before you finally do succeed?

The problem, as stated, gives you a very small probability of 50 failures followed by a success.  As stated, this probability is simply

$P(S_{51}, F_{1,2,\cdots,50}) = 0.75^{50} \times 0.25 \sim 10^{-7}$

However, we rarely know that an event has *exactly* a probability of 25% - this is usually just a hunch.  Or possibly we *believe* the probability to be 25% but in fact it’s actually 0% or in other words (unknowingly) impossible - the claim itself can be wrong.  Further, the way the question is worded almost implies that you're trying to decide to abandon...or not...an action after 50 failures.  This is a different question than the original, I admit, but much closer to what one might expect in a more realistic scenario.

Pursuing this adjusted question, say we have the following two possibilities: the original claim that $p_{\rm event}=0.25$ or the claim is false and (for example) $p_{\rm event}=0$.  Let’s further assume that we are quite sure of the original claim, at level of 99.99%.  With the new question, we are interested in the probability of a success on try 51 after 50 previous failures, which is now a combination of the result of the claim possibly being true and the claim possibly being false.  I will outline the process for $m$ failures instead of 50, so that we can discuss it in a more interesting way.

$P(S_{51}| F_{1,2,\cdots,50}) = P(S_{51}| F_{1,2,\cdots,m}, {\rm True\ Claim})P({\rm True\ Claim}|F_{1,2,\cdots,m}) + P(S_{51}| F_{1,2,\cdots,m}, {\rm False\ Claim})P({\rm False\ Claim}|F_{1,2,\cdots,m})$

The key part of this calculation is the comparison of the two possibilities (i.e. the claim is true or the claim is false) after observing 50 failures. We can apply Bayes Rule, 

* $P({\rm True\ Claim}|F_{1,2,\cdots,m}) \sim P(F_{1,2,\cdots,m}| {\rm True\ Claim})\cdot P({\rm True\ Claim}) \sim 0.75^m \cdot 0.9999$
* $P({\rm False\ Claim}|F_{1,2,\cdots,m}) \sim P(F_{1,2,\cdots,m}| {\rm False\ Claim})\cdot P({\rm False\ Claim})\sim 1 \cdot 0.0001$

After only 32 failures these two probabilities are equal, or in other words, it's even money that the action is even *possible*.  After 50 failures, the odds for the original claim are around 180:1 against.  Clearly we are facing the definition of insanity[^1] at this point.

Essentially, because 50 failures is so unlikely for a 25% chance event or action, other possibilities intrude - such as "success *at all* is impossible".  There can, of course, be other possibilities that come to mind after many failures beyond the one I explore here.  However, the point that I want to stress is that one should think a little more deeply when faced even with such "simple" problems.


[^1]: doing the same thing over and over expecting a different result.