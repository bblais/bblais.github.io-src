Title: Fine Tuning
subtitle: -- A Bayesian Approach (Part 2 of 2)
date: Sep 7, 2023
status: draft
tags: statistics, Bayesian
image: jon-flobrant-_r19nfvS3wY-unsplash 1.jpg

In a [previous post]({filename}../religion/Fine Tuning - Not convincing.md) I outline the fine tuning argument, and some of the reasons I find it unconvincing.  In this post I walk through the same material but use probability theory to describe it, translating the math to pictures wherever I can.  In some cases I think this approach makes the argument clearer, perhaps in other cases it make it more opaque -- your mileage may vary.  At any rate, it should help a reader go through some of Luke Barnes's work like [*"A Reasonable Little Question: A Formulation of the Fine-Tuning Argument"*](https://quod.lib.umich.edu/e/ergo/12405314.0006.042/--reasonable-little-question-a-formulation-of-the-fine-tuning?rgn=main;view=fulltext) which I read after doing the work for this post.

## The setup

First, some notation:
$$
\begin{aligned}
N&\equiv \text{not designed (i.e. naturalism)} \\
T&\equiv \text{designed (i.e. theism)} \\
\phi&\equiv \text{a parameter in the theory} \\
\phi^\ast&\equiv \text{the optimium value of a parameter in the theory} \\
\end{aligned}
$$
In the argument, we are trying to compare the two hypotheses, $N$ and $T$, given the data.  What is the data?  There are two pieces: the existence of life and the value of the parameter of a theory, $\phi$.  This parameter represents the collection of parameters that are supposedly fine-tuned, listed in the [previous post]({filename}../religion/Fine Tuning - Not convincing.md).   Without loss of generality, we can collect the entire weight of the fine tuning to one fine-tuned uber-parameter, $\phi$.

The comparison of the hypotheses can now be written as
$$
\begin{aligned}
P(N|\text{life},\phi)&\sim P(\text{life},\phi|N)P(N) \\
P(T|\text{life},\phi)&\sim P(\text{life},\phi|T)P(T)
\end{aligned}
$$
where I've written only the numerator of Bayes Theorem using the same conventions used in my book ["Statistical Inference for Everyone"]({filename}../books/sfe.md).  

Marginalizing over the parameter $\phi$ we get

$$
\begin{aligned}
P(N|\text{life})&\sim \int_\phi P(\text{life}|\phi,N)P(\phi|N)P(N) d\phi \\
P(T|\text{life})&\sim \int_\phi P(\text{life}|\phi,T)P(\phi|T)P(T) d\phi 
\end{aligned}
$$
If we can take the priors to be equal, $P(N)=P(T)=0.5$ for the moment it  is equivalent to ignoring the priors -- something apologists always do.  The argument then becomes that the likelihood ratios are so skewed that no reasonable difference in priors could overcome it.  This will come up again in the objections.

## The argument

We have a number of terms in the equation above that factor into the argument.  

- priors are not relevant, and are taken to be equal, $P(N)=P(T)=0.5$
- non-design (i.e. naturalism) has no preference for the parameter, $\phi$ over a wide or infinite range: $P(\phi|N)$
- we derive from current theories that a very narrow range for the parameter $\phi \sim \phi^\ast$ is needed to produce life: both $P(\text{life}|\phi,N)$ and $P(\text{life}|\phi,T)$
- design (i.e. theism) predicts that the parameter can be set externally to the universe by a designer at creation, and that life is a goal of creation, so it is likely to be set to a value conducive to life: $P(\phi|T)$

We show how the terms in the equation above map to these statements of the argument, using rough pictures of the probability functions.  I use the [XKCD](https://xkcd.com) [style for the plots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html).  

#### non-design (i.e. naturalism) has no preference for the parameter, $\phi$ over a wide or infinite range: $P(\phi|N)$

![[Pasted image 20230619082643.png]]

### we derive from current theories that a very narrow range for the parameter $\phi \sim \phi^\ast$ is needed to produce life: both $P(\text{life}|\phi,N)$ and $P(\text{life}|\phi,T)$


![[Pasted image 20230619083003.png]]


### design (i.e. theism) predicts that the parameter can be set externally to the universe by a designer at creation, and that life is a goal of creation, so it is likely to be set to a value conducive to life: $P(\phi|T)$


![[Pasted image 20230619083432.png]]


### A short digression on the integral

The marginalization step we introduced to "get rid of" the parameter, $\phi$, is the way to take into account the uncertainty of the parameter in a rigorous way.  Mathematically it is expressed as an integral,
$$
\begin{aligned}
\int_\phi P(\text{life}|\phi,N)P(\phi|N) d\phi 
\end{aligned}
$$
As a picture it is easy to see it as the percent overlap of the two functions, as shown here:

![[Pasted image 20230619084043.png]]

### back to the argument 

So, the fine tuning argument boils down to the idea that the percent overlap in the two probability functions related to the design is much larger than the percent overlap in the two probability functions related to not-design.   You can see this is the case with the following two figures,

![[Pasted image 20230619084853.png]]

![[Pasted image 20230619085149.png]]


## Objections

### The priors are not negligible nor are they equal


### $P(\phi|N)$ might be narrow

### $P(\phi|T)$ not defined

### $P(\text{life}|\phi,N)$ not narrow

- forms of life with different $\phi$

### $P(\text{life}|\phi,T)$ independent of $\phi$

- $T$ could design life irrespective of $\phi$




## Notes


https://plato.stanford.edu/entries/fine-tuning/

https://www3.nd.edu/~jspeaks/courses/2021-22/10106-fall/index.html




![[Pasted image 20230615095547.png]]


![[Pasted image 20230615095641.png]]


## The setup of the problem using probability

The fine-tuning argument is set up as a straightforward model selection problem.  Let's define the models:

- $R$ - random
- $N$ - necessity
- $G$ - design (this is essentially God)

So the comparison is between $P(R|\rm data)$, $P(N|\rm data)$, and $P(G|\rm data)$.

$P(R|\rm life, tuning) \sim P(\rm life,tuning|R)P(R) = P(\rm life|\rm tuning,R)P(\rm tuning|R)P(R)$

The three equations would then be

$$
\begin{aligned}
P(R|\rm life, tuning) &\sim P(\rm life|\rm tuning,R)P(\rm tuning|R)P(R) \\
P(N|\rm life, tuning) &\sim P(\rm life|\rm tuning,N)P(\rm tuning|N)P(N) \\
P(G|\rm life, tuning) &\sim P(\rm life|\rm tuning,G)P(\rm tuning|G)P(G) \\
\end{aligned}
$$

Note: need to have a probability of tuning given our understanding, need to write this out on paper first.




## Probability of the constant being necessary

## Divine simplicity when compared  to fine tuning

## Objection to multiverse as being not verified scientifically compared to theism

## Look up Sean Carroll response

