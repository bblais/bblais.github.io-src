Title: Four Types of Bayesian-Frequentist Comparisons
Date: 2017-04-10
summary: It is important when discussing different perspectives to keep clear what the vocabulary is. If you expand the problem set to include limited $N$ problems, with non-Normal distributions (such as Beta and Cauchy), then the differences start to become apparent.  
image: ocean-water-1149661_960_720.jpg



In my conversations with some of my statistics colleagues who are less familiar with Bayes methods, I came up with four categories of problems that come up in Bayesian-Frequentist comparisons.

## Conditional probability problems

An example of this is

>A patient goes to see a doctor. The doctor performs a test with 99 percent reliability--that is, 99 percent of people who are sick test positive and 99 percent of the healthy people test negative. The doctor knows that only 1 percent of the people in the country are sick. Now the question is: if the patient tests positive, what are the chances the patient is sick?

There are a million of these sorts of questions, and I did about 5-10 of the questions from the actuarial P test.  Clearly the use of Bayes Theorem is essential in all of this, and is uncontroversial on these problems - there really isn’t an alternative.  If you dislike the term "Bayesian" here, as some textbooks seem to, you can refer to these as conditional probability problems but we're talking about the same thing.  So, the difference between so-called Orthodox or Frequentist approaches and so-called Bayesian approaches to problems must lie in other types of problems.  I'll note that intro stats books of all stripes include these problems, and from a Bayesian perspective they are typically limited to these types of problems.

## Sampling distribution of the mean

My first encounter with the difference between Frequentist and Bayesian perspectives was in the "sampling distribution of the mean” chapter.  The problem, say, is given a series of measurements of something (i.e. the mass of Saturn, the lengths of flower petals, etc…) what is the best estimate for the underlying quantity - e.g. what is the best estimate of the mass of Saturn and how confident are we in that measurement?  Say, from orbital data, we get the following 10 data points for the mass of Saturn (in Earth-masses):

102,  95,  85,  86,  93, 105,  96,  91, 104, 115

What is the best estimate for the mass of Saturn, and our uncertainty in that estimate?

Both Frequentist and Bayesian methods come up with
\begin{eqnarray}
\mu&=&\bar{x} \pm \frac{S}{\sqrt{N}} \\
\bar{x}&=& \frac{1}{N} \sum_{k=1}^{N} x_k \\
S^2&=& \frac{1}{(N-1)}\sum_{k=1}^{N} (x_k-\bar{x})^2
\end{eqnarray}

The Bayesian and Frequentist approaches will come up with - numerically - the same answer to this question, but the vocabulary will be different.  One speaks about the probability of the mean value, the other about the properties of the sampling distribution with respect to $N$ data points.  In either case, it makes no difference *practically*.

## Jaynes-type Galilean problems

Where the rubber meets the road is a problem like the one proposed by Lindley, where he flipped a thumbtack and noted that sometimes it lands "point up" and others “point down”. His actual data was:

>U U U D U D U U U U U D  (9 Ups, and 3 Downs)

And the question is, *can we be 95% sure of this tack being an unfair tack?*  Given the physical properties of thumbtacks, we really don’t have any expectation that it *should* be fair (unlike a coin, where we have a symmetry argument).  We come up with different answers - quantitatively and possible qualitatively - on this one (see page 54 of the [presentation on the three-sided coin I gave](http://web.bryant.edu/~bblais/pdf/pres_011407.pdf))

## Anything with the Cauchy distribution

There is one final category of problems in the comparison with Bayesian and Frequentist methods. 

  Imagine we have a lighthouse which is off shore some known distance, B, and is located along the shore at some unknown location $x=a$:

             (lighthouse)
                   *          ---
                               ^
                               |
                               B
                               |
                               V
    ————shore——————+——————————————————————>  x
                  x=a

we want to estimate the location (“a”) from a series of locations of flashes on the shore - the lighthouse is spinning around and flashing at random times.  We can only observe where the flash lands on the shore, not the direction it came from.   The data is, for example, the locations of these 10 flashes:

-4.89,  1.03,  1.64,  1.17,  0.74,  1.46,  0.76,  -7.16,  0.31,  2.48

One can show that the location of a single flash should follow a Cauchy distribution:  $p(x|a,B) = B/(B^2 + (x-a)^2)$.  This is due to the angular geometry of the problem.

The question is, what is the best estimate of “a”?  What is the uncertainty in this estimate? What methods would you employ?  The Bayesian treatment for this problem is in D.S. Sivia’s, *Data Analysis: a Bayesian Tutorial, Second Edition* (Oxford, 2006).  A very similar problem is given in [Think Bayes](http://www.greenteapress.com/thinkbayes/html/thinkbayes010.html) and another nice treatment is on [João Pedro Neto's blog](http://www.di.fc.ul.pt/~jpn/r/bugs/lighthouse.html).

I'm pretty sure this problem is resistant to any procedure relying on sampling distributions (as all Frequentist procedures are) due to the [peculiar properties of the Cauchy Distribution](https://en.wikipedia.org/wiki/Cauchy_distribution).

## Conclusions

It is important when discussing different perspectives to keep clear what the vocabulary is - what are we actually talking about?  If you limit the problems to simple conditional probability problems, there isn't any difference between the Bayesian and Frequentist perspectives and one might wonder what the big deal is?  However, if you expand the problem set to include limited $N$ problems, with non-Normal distributions (such as Beta and Cauchy), then the differences start to become apparent.  

