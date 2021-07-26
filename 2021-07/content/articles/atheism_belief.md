Title: We find God "not guilty" of existing
Date: 2015-05-18

I was listening to the [Unbelievable podcast] on the definition of atheism, whether it is "lack in a belief in God" or "believing that God does not exist" or something else, which got me thinking about how it maps to probability (as I always do).  Matt Dillahunty clearly defines atheism as a lack of belief, and in a court-room analogy says that he finds God "not guilty of existing".  In court, you find the plaintiff "guilty" or "not guilty", not "guilty" or "innocent".  The burden of proof lies squarely with the prosecution.  If they haven't met that burden, then the jury finds the plaintiff "not guilty".  They may, or may not, believe that the plaintiff is innocent.  Establishing *innocence* in the crime changes the burden of proof to the defendant.  The difference here comes down to priors, which we can see through some illustrative examples mapped to probability.

## Odd and Even Stars

Are there an odd number of stars in the universe or an even number?  Clearly, at any single point in time, there is a correct answer this question.  Given our lack of knowledge, we should have

$$
P(O)=P(E)=\frac{1}{2}
$$

If someone were to claim that there was very likely an odd number of stars, we'd ask for evidence.  If that evidence is not persuasive,

$$
P(O|{\rm evidence}) \sim P(O)
$$
 then we would certainly *lack* a belief in the odd-ness of the number of stars yet we would not say that we "believe there is not an odd number of stars".  It is up to the odd-number supporter to provide the evidence to raise our prior probability significantly above $P(O)=0.5$ - they have the burden of proof.  

## Different Data

If we imagine data that might actually affect this prior probability, the situation is a bit different.  Let's imagine that through the laws of physics we could demonstrate that

1. stars are nearly always formed in pairs
2. single stars are very short-lived

we may actually have an argument for an even-number of stars in the universe.  In this case, we have
$$
P(O|{\rm data}) \ll P(O)
$$
and thus
$$
P(E|{\rm data}) \gg P(E)
$$

Where one belief goes down, the other goes up.  For our belief in odd-ness to go down our belief in evenness must go up.  We no longer simply *lack* a belief in odd-ness, we now both *believe* in even-ness and *believe* in non-odd-ness.

## More than two outcomes

Something interesting happens when there are more than two outcomes.  

$$
P(H)=P(R)=P(Y)=\frac{1}{3}
$$

Some data that nearly rules out one hypothesis, say $R$, may not speak to either other hypothesis directly, so you get the equal redistribution like:
\begin{eqnarray}
\nonumber P(R)&\sim& 0 \\
\nonumber P(H)=P(Y)&\sim& 1/2 
\end{eqnarray}

or it might be the case that the data leaves unchanged the prior probability of one of the hypotheses, raising the probability of the other, like
\begin{eqnarray}
\nonumber P(R)&\sim& 0 \\
\nonumber P(H)&\sim& 1/3 \\
\nonumber P(Y)&\sim& 2/3 
\end{eqnarray}

Notice that it is possible to reduce the probability of one hypothesis (i.e. $R$) and not effect the probability of a separate hypothesis (i.e. $H$), when there are more than two outcomes.  It is also possible for the probability of that separate hypothesis (i.e. $H$) to go up, or even go down.  In other words, when there are more than one hypothesis, presenting evidence for (or against) one hypothesis does not always guarantee an adjustment in another hypothesis down (or up).

## Back to court

So, in court, the jury is tasked to decide "guilty" or "not-guilty", rather than "guilty" or "innocent".  Why are these not the same?  Because the *claim* is that the accused is "guilty" (like "oddness of stars"), so the evidence needs to be established for the claim.  A jury deciding "not-guilty" is saying that 
$$
P({\rm guilty}|{\rm evidence}) \sim P({\rm guilty})
$$
and the evidence is not convincing.

## Back to God

The atheist is just that person who is unconvinced by the evidence, 
$$
P({\rm God}|{\rm evidence}) \sim P({\rm God})
$$
not the person who believes there is no God,
$$
P({\rm God}|{\rm evidence}) \ll 0.5
$$

Atheists find God "not guilty" of existing

[Unbelievable Project]: http://web.bryant.edu/~bblais/unbelievable-project-a-non-believers-armchair-perspective-on-six-years-of-christian-debates.html
[Unbelievable podcast]: http://www.premierradio.org.uk/shows/saturday/unbelievable.aspx
[simple rules]: http://web.bryant.edu/~bblais/unbelievable-project-a-non-believers-armchair-perspective-on-six-years-of-christian-debates.html
[full RSS Feed of the podcasts]:  http://ondemand.premier.org.uk/unbelievable/AudioFeed.aspx
