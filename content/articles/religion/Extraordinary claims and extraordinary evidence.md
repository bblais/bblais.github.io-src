Title: Extraordinary claims require extraordinary evidence
subtitle: a probabilistic analysis
Date: 2023-05-02
status: published
image: robert-lukeman-_RBcxo9AU-U-unsplash.jpg

> Extraordinary claims require extraordinary evidence - Carl Sagan

I think no pithy quote has caused so much angst with apologists than this one from Carl Sagan, directed in particular to religious miracle claims.  Before looking into it a bit more specifically, I want to point out that the word "claim" here refers to "explanation" or "proposition" and not to testimony (which would include a form of evidence).  I'll have more to say about this in another post.  If we are talking about testimony as the evidence, then we need to break the "claim" into the "explanation" part and the "evidence" part (see [my ramble on claims and evidence here]({filename}Claims versus Evidence.md)).  

To see an overly technical treatment of this by an apologist, we can look to Tim McGrew's treatment on Erik Manning's channel, as well as one of his own on the related topic of Hume.

- McGrew's Sagan video:   https://youtu.be/LD2hQFTJsK0
- McGrew's Hume video: https://www.youtube.com/watch?v=H7Gv8Fw_fFE&list=WL&index=12

I'll give more detailed responses to these videos later, but here I just want to map the Sagan quote to probabilities.

## The analysis

For me, it seems straightforward to set up.  We start with some notation.

- $D$ = data, or the evidence
- $M_i$ = the various models, or explanations, or claims.  We'll treat $M_o$ as the extraordinary explanation and $M_1, M_2, \ldots$ as the mundane explanations

Bayes theorem then has


$$
\begin{aligned}
P(M_o|D) &= \frac{P(D|M_o)P(M_o)}{P(D|M_o)P(M_o)+P(D|M_1)P(M_1)+P(D|M_2)P(M_2)+\cdots} \\
&=\frac{P(D|M_o)P(M_o)}{P(D|M_o)P(M_o)+\sum_{i=1}^{N}P(D|M_i)P(M_i)}
\end{aligned}
$$
We can simplify this by merging all of the mundane explanations together into $M_1$, which is also equivalent to $\sim M_o$
$$
\begin{aligned}
P(M_o|D) &= \frac{P(D|M_o)P(M_o)}{P(D|M_o)P(M_o)+P(D|M_1)P(M_1)}
\end{aligned}
$$
which leads to
$$
\begin{aligned}
P(M_o|D) &= \frac{P(D|M_o)P(M_o)}{P(D|M_o)P(M_o)+P(D|M_1)P(M_1)} \\
&=\frac{P(D|M_o)P(M_o)}{P(D|M_o)P(M_o)}\left(\frac{1}{1+\frac{P(D|M_1)P(M_1)}{P(D|M_o)P(M_o)}}\right)\\
&\equiv \frac{1}{1+r}
\end{aligned}
$$
where $r=P(D|M_1)P(M_1)/P(D|M_o)/P(M_o)$ which was a long-winded way of getting to the odds form of Bayes theorem.  

In order for the posterior for the extraordinary claim to rise above $P(M_o|D) >0.5$ then $r<1$. 
To map the phrase to values we have,

- extraordinary claim $\equiv$ low prior:  $P(M_o)\ll 1$
- mundane claim $\equiv$ high prior:  $P(M_1) \sim 1$

This means that $P(M_1)/P(M_o)\gg 1$ which immediately implies for $r<1$ that $P(D|M_o) \gg P(D|M_1)$.  

Now, let's assume that the extraordinary claim perfectly fits the observed data, so that we have $P(D|M_o)\sim 1$. What the last statement implies is that to justify your extraordinary claim, you must have 
$$
P(D|M_1)\ll 1
$$
or every other mundane claim must be nearly ruled out, not just unlikely.  This is exactly what science does -- construct situations (i.e. controlled experiments) to make any mundane explanation nearly impossible.  The level of "nearly impossible" depends of course on the extraordinariness of the primary claim.  

I find this consequence so straightforward, that I find it baffling that it is at all contentious.  
