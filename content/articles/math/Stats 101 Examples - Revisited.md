title: Stats 101 Examples - Revisited
date: 9/10/2024
image: edge2edge-media-uKlneQRwaxY-unsplash.jpg
status: draft
tags: MCMC, Bayesian


In some previous posts I've explored an easy Python implementation of some elementary "Stats 101 Examples" using MCMC instead of the standard statistical tests. 

- [Best Estimate with Known Variation]({filename}MCMC Simple - mu known sigma.md) (i.e. z-test)
- [Best Estimate with Unknown Variation]({filename}MCMC Simple - mu unknown sigma.md) (i.e. Student-T test)
- [Proportion]({filename}MCMC Simple - proportion.md) (i.e. proportion test)
- [Cauchy distribution]({filename}MCMC Simple - Cauchy.md) (i.e. no known frequentist test)

 Since the original posts I've rewritten the code to be more flexible and closer to the calculations than the original implementation.

In all of these posts I'm going to use a python library I make for my science-programming class, [stored on github](https://github.com/bblais/sci378), and the [emcee](https://emcee.readthedocs.io/en/stable/) library.  Install like:

```
pip install "git+git://github.com/bblais/sci378" --upgrade
pip install emcee
```

