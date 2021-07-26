title: Probability Does Extend Logic
date: Nov 17, 2016
image:horsehead1.png

In the article [*Probability theory does not extend logic*](https://meaningness.com/probability-and-logic) David Chapman, the author, criticizes the claim that probability theory generalizes logic to cases with uncertainty.  He is particularly scornful of [E. T. Jaynes'](https://en.wikipedia.org/wiki/Edwin_Thompson_Jaynes) [treatment of this](http://bayes.wustl.edu/etj/prob/book.pdf).  As far as I can see, his criticisms are misplaced.  I have broken the critcisms up into into a couple of categories, and explained the problem with each.  In summary, I couldn't find a *specific* problem where a logical conclusion was outside the domain of probability, or a *specific* problem where probability theory resulted in an incorrect conclusion that could be demonstrated independently.  Mostly, it seemed to be a criticism of notation and the ambiguity of English.

## Abuse of notation

> Suppose you roll a die, and you believe it is fair. Then you believe that the probability it will come up as a three is 1/6. You could write this as P(3) = 1/6.
> 
> People write things like that all the time, and it is totally legitimate. It might make you slightly uneasy, however. 3 is a number. It’s abstract. Do numbers have probabilities? Not as such. You assign 3 a probability, in this particular context. In a different context—for example, rolling an icosahedral die—it would have a different probability.
> 

He goes on to use a more abstract example,

> the logician C. L. Dodgson demonstrated that some snarks—not all—are boojums. A probabilist may write this generalization as a conditional probability:
> 
> $P(boojum|snark) = 0.4$
> 
> The vertical bar | is read “given”. The statement is understood as something like “if you see a snark, the probability that it is a boojum is 0.4.” Or, “the probability of boojumness given snarkness is 0.4.”
> 
> Mathematicians would call this “an abuse of notation”; but if it is interpreted intelligently in context, it’s unproblematic. Still, it’s rather queer. What exactly are “snark” and “boojum” supposed to mean here?
> 

If you actually read Jaynes, he stresses pedantically that *all* probabilities are conditional - there is an $I$ on the right-hand side in *all* of his equations.  Most of us (lazily) drop this, but there are some paradoxes that can arise when ignored.  For example, David Chapman's first example 

$$
P(3)=1/6
$$

should be changed to

$$
P(3|I)=1/6
$$

where the $I$ contains the interpretation (e.g. six-sided vs four-sided die, rolling procedure, *any* other knowledge we bring to the table).  So the bulk of this discussion seems to be much ado about nothing.

## Relationships vs propositions

David Chapman points out the benefits of using predicate logic to express relationships explicitly, such as 

> Back to the cave:
> 
> ∀x: ∀y: P(∃z: grue(z) ∧ near(z,x) | person(x) ∧ cave(y) ∧ in(x, y)) = 0.8
> 
> “If a person (x) is in a cave (y), then the probability that there’s a grue (z) near the person is 0.8.” Most of what is going on this statement is predicate logic, not probability. Remember that for probability theory, propositions are opaque and atomic. As far as it is concerned, “person(x) ∧ cave(y) ∧ in(x, y)” is just a long name for an event that is either observed or not; and so likewise “∃z: grue(z) ∧ near(z,x).” It can’t “look inside” to see that we’re talking about three different things and their relationships.
> In practice, probability theory is often combined with other mathematical methods (such as predicate logic in this case). Probabilists mostly don’t even notice they are doing this. When they use logic, they do so informally and intuitively.

I am no philosopher, nor mathematician, but as far as I can tell the only "work" that is being done by the predicate calculus is a compact, unambiguous  summary of what is expressed in English adequately.  Of course, we'll often (lazily) short-hand even this to 

$$
P({\rm grue}|{\rm cave},I) = 0.8
$$

where again, the $I$ includes the more verbose description.  There is a balance between explicitness and economy of symbols.  I still don't see the conflict - the predicate logic seems to offer nothing more in these cases.

## Specifics to Generalities

> Suppose we sequence DNA from some monsters and find that it sure looks like Arthur and Harold are both fathers of Edward:
> 
> P(father(Arthur, Edward) | experiment) = 0.99
> 
> P(father(Harold, Edward) | experiment) = 0.99
> 
> P(Arthur = Harold | observations) = 0.01
> 
> This should update our belief that every vertebrate has only one father. How?
> Here we would be reasoning from specifics to generalities (whereas the implicit instantiation trick of Bayesian networks allows us to reason from generalities to specifics). This is outside the scope of probability theory.
> 

This is definitely wrong.  What we have are experiments (i.e. data) and we have models.  We could easily have models like:

\begin{eqnarray*}
M_1 &=& \mbox{every vertebrate has only one father} \\
M_2 &=& \mbox{every vertebrate has either one or two fathers} \\
\end{eqnarray*}

and we'd want to know,

\begin{eqnarray*}
P(M_1|{\rm data},I) &=&  \cdots \\
P(M_2|{\rm data},I) &=&  \cdots \\
\end{eqnarray*}

where the data are above.  Although it could get messy, it certainly is not "outside the scope of probability theory".  It comes down to the models.

## Models and Rationality

David Chapman includes:

>Formal systems (such as logic and probability theory) are also only useful once you have a model. Where do those come from? I think it’s important to go about finding models in a rational way—but formal rationality has nothing to offer.

Here I agree - your inference is only as good as your models.  Where did the structure of General Relativity come from, originally?  From the creative process of Einstein.   Models are not derived, but are created.

I don't think we spend enough time celebrating the creative enterprise that is the scientific process. 

