Title: Why pseudoscientists like the chi-square test (and why it shouldn't be taught)
Date: 2010-09-01 17:10
Author: brianblais
Slug: why-pseudoscientists-like-the-chi-square-test-and-why-it-shouldnt-be-taught

In a [prior post][] I outlined how orthodox statistics can lead to the
[either-or logical fallacies][] common in pseudoscience, like astrology
and ufo-ology.

In this post I focus on the &chi^2^ test, it's pathologies, and why it
is so useful for a pseudoscientist. The example is lifted from [E. T.
Jaynes' book "Probability Theory"][]

The two problems with &chi^2^ are:

1.  it violates your strong intuition in some simple cases
2.  it can lead to different results with the exact same data, binned in
    a different way

Both of these properties are useful to the pseudoscientist.

Intuition and Chi-square: The Three-sided coin
----------------------------------------------

In each of this case we will have some data, and two models to compare
which try to explain the data. Intuition strongly favors one, and
&chi^2^ favors the other. One of my favorite problems is the
[three-sided coin][]: where the coin can fall heads, tails, or on the
edge. Imagine we have two models for a relatively thick coin:

-   Model A: p~heads~=p~tails~=0.499, p~edge~=0.002
-   Model B: p~heads~=p~tails~=p~edge~=1/3

And we have the following data:

-   N=29: n~heads~=14, n~tails~=14, n~edge~=1

Which model are you more confident in? Model A of course! If we use the
&psi-measure for goodness of fit with these two models, as defined in
[my prior post][prior post], then we have (remember: smaller &psi means
more confident in the fit, just like smaller &chi^2^):

![E7E94805-9E10-451E-9B95-C8EB2BA875C7.jpg][]

![7AFD29D5-C801-416E-82AC-F9B363147B22.jpg][]

with &psi~B~-&psi~A~=26.85 which makes model A more then 100 times more
likely than model B (a &psi difference of 20 would be exactly 100
times). Perfectly reasonable. What about &chi^2^?

![31844A12-1F3E-4D51-B2D0-EFAE00BE66A7.jpg][]

which makes model B slightly preferable to model A! Amazing! Where is
this coming from? Apparently it is coming from the somewhat rare event
of an edge-landing. If our data had been instead

-   N=29: n~heads~=15, n~tails~=14, n~edge~=0

then we'd have

-   &psi~A~=0.3
-   &psi~B~=51.2

and

-   &chi^2^~A~=0.093
-   &chi^2^~B~=14.55

where now both measures agree that model A is superior.

<table align="center" width="50%">
<tr>
<td>
**Why do pseudoscientists love the &chi^2^ test?**

</td>
</tr>
<p>
<tr>
<td>
*Answer 1: Because all they need to do is wait for that inevitable,
somewhat rare but still possible, data point and &chi^2^ yields a
pathologically high value*

</td>
</tr>
<p>
</table>
The &psi-measure and log-likelihood
-----------------------------------

To understand the other problem with the &chi^2^ test we need to
understand what the &psi-measure is doing. As above, imagine we have a
set of observations O~i~. We define the total number of observed points
and the relative frequency of each observation,

![23229268-8820-42F8-BF8C-C984679DCB51.jpg][]

The maximum likelihood solution for the probabilities of observing O~i~
for each class, i, is just the relative frequency of each observation.
This is the "just-so" solution, where we estimate the probability of
seeing 14 heads in 29 flips as p=14/29. This "just-so" solution will
have the closest match, and the highest likelihood (by definition). If
we have a model which specifies a different set of probabilities for
each class, then it's likelihood is simply

![71272C22-E8B6-4497-82DF-FBDD89729630.jpg][]

The &psi measure can be rewritten as

![B363F3D7-1964-421A-A8E2-B19020D0117A.jpg][]

So you can think of the &psi-measure as comparing a model with the
"just-so" solution (which has maximum likelihood). Further, subtracting
one value of &psi with another (for different models) performs the
log-likelihood ratio between the models. A proper analysis should
include prior information, which can be [done almost as easily][].

An almost equivalent problem
----------------------------

Imagine that we have a coin with 6 faces, and we are comparing the
following models:

-   Model A: p = [0.499/2, 0.499/2, 0.499/2, 0.499/2, 0.002/2,0.002/2]
-   Model B: p = [1/6,1/6,1/6,1/6,1/6,1/6]

And we have the following data:

-   N=29: O=[7,7,7,7,0,1]

where I have listed the probabilities and the outcomes for each face.
Notice that, grouping them together in pairs we retrieve the same as the
first example. Thus when comparing the two models, with this equivalent
problem, we should get the same value. Because the size of the problem
changed, the individual &psi values will be different (larger) because
there are more terms in the "just-so" solution. However, the difference
between the models should be the same. The results are:

-   &psi~A~=11.35 (old value 8.34)
-   &psi~B~=38.2 (old value 35.19)

with &psi~B~-&psi~A~=26.85 (old value 26.85...the same!), and

-   &chi^2^~A~=32.6 (old value 15.33)
-   &chi^2^~B~=11.76 (old value 11.66)

The &chi^2^ for one of the models (Model A) has been inflated quite a
lot relative to the other model. This means that, depending on how you
bin the data, you can make whichever model that you are looking at more
or less significantly different, without changing the data at all.

<table align="center" width="50%">
<tr>
<td>
**Why do pseudoscientists love the &chi^2^ test?**

</td>
</tr>
<p>
<tr>
<td>
*Answer 2: Because all they need to do is bin their data in different
ways to affect the level of significance of their model over the model
to which they are comparing*

</td>
</tr>
<p>
</table>
Still taught?
-------------

So, why is the &chi^2^ test still taught? I don't know. It has
pathological behavior in simple systems, where somewhat rare events
artificially inflate its value, and it can be easily used to prop up an
unreasonable model simply by rearranging the data. Why not teach
something, like the &psi-measure, which is grounded theoretically in the
likelihood principle and does not have such pathological behavior? If
you prefer to use the log-likelihood instead, then that would be fine
(and equivalent).

I think it is about time to purge the &chi^2^ test from our textbooks,
and replace it with something correct.

<div class="blogger-post-footer">
![]

</div>

  [prior post]: http://bblais.blogspot.com/2010/08/orthodox-statistics-conducive-to-pseudo.html
  [either-or logical fallacies]: http://en.wikipedia.org/wiki/False_dilemma
  [E. T. Jaynes' book "Probability Theory"]: http://www.amazon.com/Probability-Theory-Logic-Science-Vol/dp/0521592712/ref=sr_1_1?ie=UTF8&s=books&qid=1283295597&sr=8-1
  [three-sided coin]: http://pubs.amstat.org/doi/abs/10.1198/000313007X222497
  [E7E94805-9E10-451E-9B95-C8EB2BA875C7.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/TH2VC6WKxkI/AAAAAAAAGiQ/YjW0NbJ0SsI/E7E94805-9E10-451E-9B95-C8EB2BA875C7.jpg?imgmax=800
  [7AFD29D5-C801-416E-82AC-F9B363147B22.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/TH4gCkRSb0I/AAAAAAAAGiY/8M8QyPr1vlM/7AFD29D5-C801-416E-82AC-F9B363147B22.jpg?imgmax=800
  [31844A12-1F3E-4D51-B2D0-EFAE00BE66A7.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/TH2QNPSVmjI/AAAAAAAAGiI/CP3fa-MJ7Vc/31844A12-1F3E-4D51-B2D0-EFAE00BE66A7.jpg?imgmax=800
  [23229268-8820-42F8-BF8C-C984679DCB51.jpg]: http://lh6.ggpht.com/_VLTJPGH7Stw/TH58MuJZOPI/AAAAAAAAGig/FET0c4rhfxg/23229268-8820-42F8-BF8C-C984679DCB51.jpg?imgmax=800
  [71272C22-E8B6-4497-82DF-FBDD89729630.jpg]: http://lh4.ggpht.com/_VLTJPGH7Stw/TH59WfaMs4I/AAAAAAAAGio/YErvCX24kpc/71272C22-E8B6-4497-82DF-FBDD89729630.jpg?imgmax=800
  [B363F3D7-1964-421A-A8E2-B19020D0117A.jpg]: http://lh5.ggpht.com/_VLTJPGH7Stw/TH6KOVWBbAI/AAAAAAAAGi4/nM4i1qXTzHM/B363F3D7-1964-421A-A8E2-B19020D0117A.jpg?imgmax=800
  [done almost as easily]: http://bblais.blogspot.com/2010/08/non-psychic-octopus.html
  []: https://blogger.googleusercontent.com/tracker/6965073194684424505-4580898654910908885?l=bblais.blogspot.com
