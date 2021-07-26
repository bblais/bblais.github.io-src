title: Superseding the $t$ test
Date: 2015-04-23
subtitle: A Bayesian comparison of means

There's a very nice paper, [Bayesian estimation supersedes the t test](http://www.indiana.edu/~kruschke/articles/Kruschke2013JEPG.pdf). John K. Kruschke, Journal of Experimental Psychology: General, 2013, v.142(2), pp.573-603. The methods described provide at once posterior probabilities not just for the means of two groups, but their standard deviations, their normality, and effect size.  The [supporting website](http://www.indiana.edu/~kruschke/BEST/) has a lot of useful resources, including a number of implementations.  The original implementation is in R, but there is a [Python implementation using PyMC](https://github.com/strawlab/best).

I decided to implement the same thing using the [emcee package](http://dan.iel.fm/emcee/current/).  The full implementation is [viewable here](http://nbviewer.ipython.org/gist/bblais/7a1c6ec3b4c8d1b0465f).  My implementation is pretty general, and can handle some arbitrary tests of the variables, like:

    #!python
    model.P('(mu1>101) & (mu1<102.1)')

    0.85502222222222224

and

    #!python
    model.P('sigma1<sigma2')

    0.0060111111111111112

and

    #!python
    model.plot_distribution('Effect Size=(mu1-mu2)/sqrt((sigma1**2+sigma2**2)/2)')

![effectsize](images/effect_size.png)

Hopefully the code will be useful to someone, perhaps just me as I explore similar problems.


