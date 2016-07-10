title: Will the Sun Rise Tomorrow?
Date: 2014-09-22
subtitle: Hume, Laplace, and Bayes

On a recent [Unbelievable podcast] there is a discussion between  [Calum Miller and James Croft] on the topic "is our universe more likely on atheism or theism?", where Calum introduces probabilistic arguments throughout.  At one point he brings up evidence for the sun coming up, as an example of knowledge claims and models.

## Calum describes Hume
Calum - "Hume basically noted that we don't have any non-circular justification for thinking that the universe will be regular, that it will continue to be regular in the future. [...] He doesn't just say that we have to be a bit unsure that the sun will rise tomorrow, he says that we have no good reason at all for thinking the sun will rise tomorrow.  The most common justification that the sun will rise tomorrow is that it has risen every day  in the past.  But then if you compare two theories, one says that the sun rises everyday in the past and in the future and the other theory says that the sun rises everyday in the past but won't rise tomorrow.  Both those theories predict the observations we already have, both those theories lead us to expect the observations, and so the observations we currently have don't distinguish between these two theories.  And yet one of those theories predicts the sun will rise tomorrow and one of them predicts that the sun won't rise tomorrow.  So, even though we have those observations, they don't really do an obviously good job of determining which of these theories is true.  [...]  He is saying that the past observations don't give us that good reason for thinking that the sun will rise tomorrow.  This is the Problem of Induction and has perplexed philosophers for centuries."{.tq}

## What does Hume *actually* say about the Sun rising?

[Hume writes]: 

> Matters of fact, which are the second objects of human reason, are not ascertained in the same manner; nor is our evidence of their truth, however great, of a like nature with the foregoing. The contrary of every matter of fact is still possible, because it can never imply a contradiction, and is conceived by the mind with the same facility and distinctness, as if ever so conformable to reality. That the sun will not rise tomorrow is no less intelligible a proposition, and implies no more contradiction, than the affirmation, that it will rise. We should in vain, therefore, attempt to demonstrate its falsehood. Were it demonstratively false, it would imply a contradiction, and could never be distinctly conceived by the mind. An Enquiry Concerning Human Understanding (1772). Hackett Publ Co. 1993; Chapter on Cause and Effect.

Here Hume is essentially stating that all propositions have a non-zero probability (however small they might be) unless they are *logically* impossible.  This is not saying, at all, that we have no good reason to believe the sun will rise tomorrow.

> The bread, which I formerly ate, nourished me: that is, a body of such sensible qualities was, at that time, endued with such secret powers; but does it follow, that other bread must also nourish me at another time, and that like sensible qualities must always be attended with like secret powers? The consequence seems nowise necessary. 

Again, although Hume predates probability theory, this is essentially what he is saying - the consequence is not logically *necessary* (i.e. $P({\rm consequence}|{\rm observations})<1$).  We see this as a direct application of probability theory,  a totally uncontroversial application at that.  

I fail to see that the "problem" of induction is really a problem.  I also fail to see Hume claiming that there is no good reason to see the consequence following from the the observations, just that he doesn't see one:

> The connection between these propositions is not intuitive. There is required a medium, which may enable the mind to draw such an inference, if indeed it be drawn by reasoning and argument. What that medium is, I must confess, passes my comprehension, and it is incumbent on those to produce it, who assert that it really exists, and is the origin of all our conclusions concerning matter of fact.


The medium Hume refers to is simply the calculus of probability, something which post-dates Hume's writings.  Hume was being honest that he didn't see a way, and he did not claim that there was no possible way - that would be an argument from ignorance.  


## What does Laplace say about the Sun rising?

Once we have probability theory, then we can actually do some simple calculations concerning the probability of the sun rising tomorrow.  Of course these calculations are not a complete description of the problem, but give the flavor of it.  Laplace used the sunrise problem as an example application of his Rule of Succession, which itself is derived from the rules of probability.  The calculation goes something like this.

* Our model is that the sun rises with unknown probability $p$
* Given complete ignorance of $p$ we assume an initial uniform probability
* The sun has risen every day for the written record, say, 10000 years
* the probability for rising tomorrow, which is also the mean value of $p$ over the posterior, is given by the [Rule of Succession] (also known as the "assume one success and one failure"):
\begin{eqnarray}
P(r_{\rm tomorrow}|r_{\rm today}, r_{\rm yesterday}, r_{\rm day before}, \ldots, r_{0}) 
&=& \frac{10000 {\rm yr}\times 365 {\rm d}/{\rm yr}+1}{10000 {\rm yr}\times 365 {\rm d}/{\rm yr}+2}\\\\
&=&0.9999997
\end{eqnarray}

It [gets messier] when you can't even assume that both a failure and a success are possible, but it [can still be done] without any change to the qualitative result.

Clearly we have quite good reasons to believe the that sun will rise tomorrow.


## Two theories

We go back to Calum's two theories: 

> If you compare two theories, one says that the sun rises everyday in the past and in the future and the other theory says that the sun rises everyday in the past but won't rise tomorrow.  Both those theories predict the observations we already have, both those theories lead us to expect the observations, and so the observations we currently have don't distinguish between these two theories.{.tq}


The situation for arguing a high probability of tomorrow's sun rise is far more compelling, however, because our information is not simply that the sun has risen in the past, but includes observations of the patterns of the seasons, the predictions of the phases of the moon and Venus, and a whole host of other factors which significantly increase the chance the sun will rise.  Laplace knew this well, and was using this example not as a serious calculation, but as a pedagogical example.

As a consequence, both of Calum's so-called theories do *not* predict the observations we already have - only one of them does.  Even if we accept just the observations for which both theories are consistent in the past, one has to view this two-theory perspective from the point of prediction.  It's now tomorrow, and "Theory B" doesn't work - so we modify it to say the sun won't rise *tomorrow* (the new tomorrow).  That next day comes with a sunrise, and this "Theory B 2.0" is wrong (again) and has to be modified (again).  It is clear that "Theory B" fails, and we should be less confident in it.  That's why, in science, it isn't nearly enough to be consistent with past data - one must make predictions, not just post-dictions, and test it.  It is often trivial to come up with "explanations" for data we already have.

## Conclusions

It seems to me that the so-called "Problem of Induction" was solved centuries ago, with the advent of probability theory, and all such hand-wringing seems to be only for philosophers.  In the sciences, these challenges to induction just aren't taken seriously.   I'll sleep soundly tonight with the confident knowledge that the sun will rise again tomorrow, despite the protestations of philosophers.



[Hume writes]: http://www.marxists.org/reference/subject/philosophy/works/en/hume.htm
[Unbelievable podcast]: http://www.premierchristianradio.com/shows/saturday/unbelievable.aspx

[Calum Miller and James Croft]: http://www.premierchristianradio.com/Shows/Saturday/Unbelievable/Episodes/Unbelievable-Is-our-universe-more-likely-on-atheism-or-theism-Calum-Miller-vs-James-Croft
[Rule of Succession]: http://en.wikipedia.org/wiki/Rule_of_succession
[gets messier]: http://en.wikipedia.org/wiki/Rule_of_succession#Mathematical_details
[can still be done]: http://en.wikipedia.org/wiki/Rule_of_succession#Mathematical_details