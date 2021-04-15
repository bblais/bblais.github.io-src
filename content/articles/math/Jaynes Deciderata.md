title: Probability - It's Not Just about the Math
date: 6/16/2019
status: published
image: andrew-ridley-76547-unsplash-0686333.jpg

When I first learned probability, I thought it was all about math and counting.  Then [E. T. Jaynes](https://bayes.wustl.edu/etj/etj.html) showed me that probability forms the foundation of rationality itself.  Remarkably very few axioms are needed to constrain the mathematical forms necessary for rational thought and the outcome turns out to be [Laplace's original formulation](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace#Analytic_theory_of_probabilities).  What follows are the axioms so that you can appreciate them as much as I.  The paper *[From Laplace to Supernova SN1987A: Bayesian Inference In Astrophysics](https://bayes.wustl.edu/gregory/articles.pdf)* by Tom Loredo is an excellent and complete guide to this, including quantitative examples.  

Jaynes prefers the word *desiderata* for this list - a collection of things needed or wanted - but they function the same as *axioms* of the analysis - unproven foundational statements as a basis for a derived system - and I prefer to use that terminology.  Whatever you'd like to name them, here they are:

1. **Degrees of plausibility are represented by real numbers**.  This is a choice of practicality.  Perhaps there is some value in probability represented with *complex numbers*, but so far no useful generalization has been found to my knowledge.
2.  **Qualitative consistency with common sense**.  Specifically, the system must be consistent with standard Boolean logic - the logic of syllogisms and deductive logic.  This is not a generic call to "*common sense*" to base the system on, but rather the short-hand informal speech that Jaynes likes to use.
3. **Internal consistency**. If a conclusion can be reasoned out in more than one way then every possible way must yield the same result.
4. **Propriety**.  We must take into account all of the information provided that is relevant to the question.
5. **Equivalent states consistency**.  Equivalent states of knowledge must be represented by equivalent plausibility assignments.

To quote Jaynes: 

> At this point, most students are surprised to learn that our search for desiderata is at an end. The above conditions, it turns out, uniquely determine the rules by which [we] must reason; i.e. there is only one set of mathematical operations for manipulating plausibilities which has all these properties.

From these axioms, we can derive,

* the sum and product rules of probability, which describe the process of combining bits of knowledge
* Bayes Rule, which describes the structure of learning from evidence
* the marginalization rule, where model simplicity is attributed to fewer adjustable parameters
* deductive logic, the limit as the probabilities go to 0 and 1
* the dangers of either/or thinking
* and much more!

An important consequence of the derivation is that *any* system which disagrees with it must violate one or more of the axioms listed.  The entire approach shows that probability theory is far more fundamental than is typically appreciated.