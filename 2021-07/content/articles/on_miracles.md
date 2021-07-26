title: On Miracles
subtitle: Hume was right all along
date: 2015-05-13

After my [post about the misquoting Hume] and the miraculous, I was recommended to read the Stanford Encyclopedia of Philosophy [article on miracles] where it supposedly explains why "Hume was toast" before any misquoting of him.  In this post, I hope to sketch the relevant parts of the encyclopedia article, and demonstrate how it does not establish any significant deficiency of Hume.  I use the same headings as the [article on miracles] to make it easier to follow.

# Concepts and Definitions

The article begins by discussing one of Hume's definitions of a miracle as "a violation of the laws of nature".  From what I can tell, their main critique is they don't like the connotations of the word "law", a perspective I share - it is a bit loose terminology, with too many alternate meanings to be the foundation of a well-defined argument.  Their revised definition is the following:

> A miracle is an event that exceeds the productive power of nature

Perhaps this is the scientist in me, and why I am not a philosopher, but I don't see a striking difference between these two definitions in at least how they are used.  So it seems reasonable to adopt this as a good working definition.

They go on to clarify a subset of miracle,

> a religiously significant miracle is a detectable miracle that has a supernatural cause.

This clarification is to deal with the following problem, and I'd agree with at least the sentiment.

> An insignificant shift in a few grains of sand in the lonesome desert might, if it exceeded the productive powers of nature, qualify as a miracle in some thin sense, but it would manifestly lack religious significance and count not be used as the fulcrum for any interesting argument.

I am not sure how, in practice, one would be able to determine a "supernatural cause", let alone establish how an event could be beyond the "productive power of nature" without committing a fallacy of *argument from ignorance*, but let's leave that for now.
 
# Arguments for Miracle Claims

This section starts with a quick list of the types of evidence and arguments made for miracles.

> Many arguments for miracles adduce the testimony of sincere and able eyewitnesses as the key piece of evidence on which the force of the argument depends. But other factors are also cited in favor of miracle claims: the existence of commemorative ceremonies from earliest times, for example, or the transformation of the eyewitnesses from fearful cowards into defiant proclaimers of the resurrection, or the conversion of St. Paul, or the growth of the early church under extremely adverse conditions and without any of the normal conditions of success such as wealth, patronage, or the use of force. These considerations are often used jointly in a cumulative argument. It is therefore difficult to isolate a single canonical argument for most miracle claims. The various arguments must be handled on a case-by-case basis.

All of these pieces of so-called evidence are the worst kind of evidence, for which there are countless examples of the same, or similar evidence use to shore up the claims of other (presumably false) beliefs.  You can think "Mormonism" or "Alien Abductions" for nearly every point listed.

They then outline two types of inductive arguments:

> 1. the conclusion (in this case that the miracle in question has actually occurred) is probable to some specific degree, or at least more probable than not
> 2. the conclusion is more probable given the evidence presented than it is considered independently of that evidence

Point (1) is just either specifying either $P({\rm miracle}|{\rm data})$ directly or establishing only that $P({\rm miracle}|{\rm data})>0.5$.  Point (2) is $P({\rm miracle}|{\rm data})>P({\rm miracle})$.  Point (2) is nearly useless.  For example, you could have
\begin{eqnarray*}
P({\rm miracle})&=&0.00001 \\
P({\rm miracle}|{\rm data})&=&0.001
\end{eqnarray*}
and still have a seriously unlikely hypothesis, even given a factor of 100 increase in probability of a miracle given the data.  Thus the *only* thing that matters must be the actual value of $P({\rm miracle}|{\rm data})$.

One such argument for miracles specifies the type of evidence needed to make one confident that one is talking about a miracle.  The article calls this a "criteriological" argument, but all of the arguments dealt with are probabilistic.  What are the criteria, for example?  This one is from Charles Leslie:

>
1. That the matters of fact be such, as that men's outward senses, their eyes and ears, may be judges of it.
2. That it be done publicly in the face of the world.
3. That not only public monuments be kept up in memory of it, but some outward actions to be performed.
4. That such monuments, and such actions or observances, be instituted, and do commence from the time that the matter of fact was done.

One can easily site both the golden plates of Joseph Smith, and also the events surrounding Roswell, that satisfy all of these.  Clearly, there is an issue with them.

Another common argument is called the "minimal facts" approach.  The best summary, and take-down of this argument is on [Matthew Ferguson's blog].  One essential missing part of the minimal facts approach is that it only includes *likelihoods* and not *priors*, and thus fails a basic probabilistic analysis.

## Probabilistic arguments

The first form here deals with *testimony*, with the following assumptions and conventions:

1. $T_i\equiv$ the proposition "Witness $i$ testifies to $M$"
2. $P(T_i,T_j) = P(T_i)\times P(T_j)$: independence
3. $P(T_i|M)=P(T_j|M)$ for all $i$ and $j$: all testimony is equally informative

We then easily derive:
$$
\frac{P(M|T_1,T_2,\cdots,T_n)}{P(\sim\!M|T_1,T_2,\cdots,T_n)} = \left(\frac{P(T_1|M)}{P(T_1|\sim\!M)}\right)^n \times \frac{P(M)}{P(\sim\!M)}
$$

The article then spins this in a positive way toward miracles:
>[I]f independent witnesses can be found, who speak truth more frequently than falsehood, *it is ALWAYS possible to assign a number of independent witnesses, the improbability of the falsehood of whose concurring testimony shall be greater than the improbability of the alleged miracle.* (Babbage 1837: 202, emphasis original; cf. Holder 1998 and Earman 2000)

However, comparing with Hume, it becomes obvious why this spin fails:
> When anyone tells me, that he saw a dead man restored to life, I immediately consider with myself, whether it be more probable, that this person should either deceive or be deceived, or that the fact, which he relates, should have really happened. I weigh the one miracle against the other; and according to the superiority, which I discover, I pronounce my decision, and always reject the greater miracle. If the falsehood of the testimony would be more miraculous, than the event which he relates; then, and not till then, can he pretend to command my belief or opinion. (Hume)

The first quote implies that the terms $P(T_1|M)$ and $P(T_1|\sim\!M)$ refer to speaking truth vs falsehoods (i.e. lying), as opposed to speaking correctly vs being mistaken.  In the latter, it is very easy to see why, for certain types of extraordinary events, we would expect fallible observers to have $P(T_1|\sim\!M)>P(T_1|M)$ and further that even *if* witnesses were in general slightly more reliable than not, we can't expect the observations to be *independent* in general.  In the specific case of the (anonymous) Gospel writers, there is strong evidence of *dependence* in the accounts to make this entire calculation (except in its gross qualitative features) irrelevant.

# Arguments against miracles

Quoting Hume again,

> The plain consequence is (and it is a general maxim worthy of our attention), “That no testimony is sufficient to establish a miracle, unless the testimony be of such a kind, that its falsehood would be more miraculous, than the fact, which it endeavors to establish: And even in that case, there is a mutual destruction of arguments, and the superior only gives us an assurance suitable to that degree of force, which remains, after deducting the inferior.”

This is correct, and is a direct statement of Bayesian reasoning
$$
\frac{P(M|E)}{P(\sim\!M|E)} =\frac{P(E|M)}{P(E|\sim\!M)} \times\frac{P(M)}{P(\sim\!M)}
$$
where we can use the approximations $P(E|M)\approx 1$ and $P(\sim\!M)\approx 1$ and achieve
$$
\frac{P(M|E)}{P(\sim\!M|E)} \approx \frac{P(M)}{P(E|\sim\!M)}
$$

The [article on miracles] continues to try to map this to a philosophical structure (needlessly, I'd say), with the following "simple version" of the argument:

>  A very simple version of the argument, leaving out the comparison to the laws of nature and focusing on the alleged infirmities of testimony, can be laid out deductively (following Whately, in Paley 1859: 33):
>
> 1) Testimony is a kind of evidence very likely to be false.
> 
> 2) The evidence for the Christian miracles is testimony.
>
> Therefore,
>
> 3) The evidence for the Christian miracles is likely to be false.
>
>This is, however, much too crude an argument to carry any weight, since it turns on a simple ambiguity between all testimony and some testimony. Whately offers an amusing parody that makes the fallacy obvious: Some books are mere trash; Hume's Works are [some] books; therefore, etc.

It's remarkable that such a silly parallel is seriously made.  The structure isn't really parallel at all, so let's make it explicit:

1. Books are likely to be trash. (in other words, most books are trash)
2. Hume wrote some books
3. therefore, Hume's books are likely to be trash.

This is a correct argument, given the premises.  If all we knew was that "some guy named Hume" wrote "some book", then with all probability (if premise 1. is correct) that book would be trash.  The issue is that, unconsciously, we are inserting extra information - Hume was a famous philosopher, he had a particular education, etc...  With this extra information, we would have a hard time supporting a similar premise as 1. above.  

The fact that this is so trivially dispensed with makes one wonder - why would anyone be convinced by this?  Why couldn't the author of the article see it?  It smacks of grasping at straws to try to dispel Hume's main arguments.  

The article continues with some odd re-phrasings of Hume, where the mathematics is just the single line above.  I don't understand all the work.  A strange one is then critiqued with an even stranger statement:
>The presumptive case against the resurrection from universal testimony would be as strong as Hume supposes only if, *per impossible*, all mankind throughout all ages had been watching the tomb of Jesus on the morning of the third day and testified that nothing occurred. Even aside from the problems of time travel, there is not a *single piece* of direct testimonial evidence to Jesus' non-resurrection.

Does anyone seriously think that the case against a claim always (or even usually) takes the form of direct testimony against that claim?  Where is the testimony that Zeus didn't exist?  Anyone who can explain this odd line of reasoning, please chime in.

# Particular Arguments

According to the article, Hume lists a set of conditions needed to make testimony carry maximum weight:

>[T]here is not to be found, in all history, any miracle attested by a sufficient number of men, of such unquestioned good sense, education, and learning, as to secure us against all delusion in themselves; of such undoubted integrity, as to place them beyond all suspicion of any design to deceive others; of such credit and reputation in the eyes of mankind, as to have a great deal to lose in case of their being detected in any falsehood; and at the same time attesting facts, performed in such a public manner, and in so celebrated a part of the world, as to render the detection unavoidable: All which circumstances are requisite to give us a full assurance in the testimony of men. (Hume 1748/2000: 88)

Essentially, he is saying that the methods of science have never confirmed a miracle.  The methods of science help "secure us against all delusion in themselves", remove "suspicion of any design to deceive others", with processes "performed in a public manner" that "render the detection unavoidable".

It is criticized by noting that some of these conditions can cut the other way, such as the condition of "credit and reputation",

>It might have been said with some shew of plausibility, that such persons by their knowledge and abilities, their reputation and interest, might have it in their power to countenance and propagate an imposture among the people, and give it some credit in the world. (Leland 1755: 90–91; cf. Beckett 1883: 29–37)

This is, essentially, pointing out fallacy of authority - a good critique.  Science, by its processes, attempts to avoid that as well.  Of course, Hume predates modern science, so I think we can forgive him some sloppiness or poor choice of terminology.

Hume continues to suggest that the religious context of the miracle claime makes the telling of the miracle story even more likely.  This would increase the probability of obtaining the testimony even if no miracle happened - $P(E|\sim\!M)$ increases - making the probability of a miracle go down.  The criticism here?  The effect could happen in the other direction:

> But as George Campbell points out (1762/1839: 48–49), this consideration cuts both ways; the religious nature of the claim may also operate to make it less readily received:
> 
>>[T]he prejudice resulting from the religious affection, may just as readily obstruct as promote our faith in a religious miracle. What things in nature are more contrary, than one religion is to another religion? They are just as contrary as light and darkness, truth and error. The affections with which they are contemplated by the same person, are just as opposite as desire and aversion, love and hatred. The same religious zeal which gives the mind of a Christian a propensity to the belief of a miracle in support of Christianity, will inspire him with an aversion from the belief of a miracle in support of Mahometanism. The same principle which will make him acquiesce in evidence less than sufficient in one case, will make him require evidence more than sufficient in the other….

I disagree quite strongly with this line of thinking.  One of the big problems with pseudoscience is that it promotes poor thinking in other domains.  Someone who believes in miracles will not find it hard to believe that the miracle claims of other religions are at least possible.  If you believe in unseen agents, then to move from Christianity to New Age to Scientology isn't that large of a stretch.  Often, when ones religion is undermined, the typical response is to switch to another religion!  Thus, they are not as opposite as "light and darkness".  Poor thinking is poor thinking, regardless of the context.

## Argument from Parity

Hume brings up miracles in other religions.  In a fit of special pleading, the [article on miracles] retorts,

>All attempts to draw an evidential parallel between the miracles of the New Testament and the miracle stories of later ecclesiastical history are therefore dubious. There are simply more resources for explaining how the ecclesiastical stories, which were promoted to an established and favorably disposed audience, could have arisen and been believed without there being any truth to the reports.

The argument is quite simple - if there are known cases of miracle claims where no miracle actually occurred, that increase $P(E|\sim\!M)$, making the probability of a miracle go down given testimony.  It doesn't matter whether you have good reasons to believe there was no miracle for these cases - it undermines testimony of miracles in general.

# In conclusion

So, as far as I can tell, there is no substantive critique to Hume's statements about miracles.  He lacks the rigor of the mathematics of probability, but his wording is so straightforwardly translated to it that I find it difficult to see what the problem is.  I also found it ironic that the entire article, which has been pro-miracle the entire time, ends with this:

>For the evidence for a miracle claim, being public and empirical, is never strictly demonstrative, either as to the fact of the event or as to the supernatural cause of the event. It remains possible, though the facts in the case may in principle render it wildly improbable, that the testifier is either a deceiver or himself deceived; and so long as those possibilities exist, there will be logical space for other forms of evidence to bear on the conclusion. Arguments about miracles therefore take their place as one piece—a fascinating piece—in a larger and more important puzzle.

This is pretty much exactly what Hume was saying.  Given that there is always a non-zero probability of the testifier either lying or being mistaken, one has to establish the evidence for a miracle strong enough to overcome both the negligibly small prior probability and this non-zero probability of the testimony being wrong.  Since mistakes are a common human trait, and distortions are also common on testimony, evidence for miracles according to probability theory, Hume, and all rational thought have always been found lacking.

Of course, if you could demonstrate it otherwise, please let me know!  I'd love to believe in miracles.  I just have never seen anything even remotely convincing.  

For some other items I've written about miracles, see:

1. [http://web.bryant.edu/~bblais/do-healing-miracles-happen.html](http://web.bryant.edu/~bblais/do-healing-miracles-happen.html)
2. [http://web.bryant.edu/~bblais/a-little-about-miracles.html](http://web.bryant.edu/~bblais/a-little-about-miracles.html)
3. [http://web.bryant.edu/~bblais/unbelievable-project-miracles-and-healing-is-it-evidence-for-the-truth-of-christianity.html](http://web.bryant.edu/~bblais/unbelievable-project-miracles-and-healing-is-it-evidence-for-the-truth-of-christianity.html)



[post about the misquoting Hume]: http://web.bryant.edu/~bblais/misquoting-hume.html
[article on miracles]: http://plato.stanford.edu/entries/miracles/
[Matthew Ferguson's blog]:https://adversusapologetica.wordpress.com/2013/06/29/knocking-out-the-pillars-of-the-minimal-facts-apologetic/


