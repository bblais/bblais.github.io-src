title: Stats 101 Examples with MCMC Part 3
subtitle: Estimating a proportion
date: 5/13/2021
status: published
image: edge2edge-media-uKlneQRwaxY-unsplash.jpg

This is another in the series of "*Statistics 101*" examples solved with MCMC.  Others in the series:

- [Estimating mean with known 𝜎](https://bblais.github.io/posts/2021/Apr/15/stats-101-examples-with-mcmc/)
- [Estimating mean with unknown 𝜎](https://bblais.github.io/posts/2021/Apr/28/stats-101-examples-with-mcmc-part-2/)

In all of these posts I'm going to use a python library I make for my science-programming class, [stored on github](https://github.com/bblais/sci378), and the [emcee](https://emcee.readthedocs.io/en/stable/) library.  Install like:

```
pip install "git+git://github.com/bblais/sci378" --upgrade
pip install emcee
```


In this example the data take the form of a number of "successes", $h$, in a total number of "trials", $N$, and we want to estimate the proportion, $\theta$.  This could be the number of heads observed in $N$ coin flips and we want to estimate the bias in the coin -- what is the probability that it flips heads.  In fact, the data I will use below is from [Lindley, 1976. "Inference for a Bernoulli Process (A Bayesian View)"](https://www.jstor.org/stable/2683855?seq=1#metadata_info_tab_contents), where he flips a thumbtack which might be able to produce two states pointing "up" or pointing "down", and gets the data UUUDUDUUUUUD (3 D, 9 U).

## Setting up the problem


For a Bayesian solution, we need to specify the likelihood function -- how our model produces the data -- and the prior probability for the parameters.  The likelihood function is determined from the Bernoulli function,

$$
P(h|N,\theta) \sim \text{Bernoulli}(N,\theta)
$$


In the "*Statistics 101*" examples, the results are typically equivalent to *uniform* priors on the location parameters.  This would translate to 
$$
P(\theta) \sim \text{Uniform}(0,1)
$$

However there are cases where we have more information.  Even flipping a biased coin, we know that both outcomes (heads and tails) are at least *possible* to happen.  Given this, the probabilities $P(\theta=0)$ and $P(\theta=1)$ should be zero and a different prior is justified (sidenote -- the maximum entropy solution to this is a Beta(2,2) distribution or, in other words, assume one heads and one tails have been observed before the data).  I'll continue with this example with uniform priors, because in [Lindley, 1976. "Inference for a Bernoulli Process (A Bayesian View)"](https://www.jstor.org/stable/2683855?seq=1#metadata_info_tab_contents) he is flipping a particular thumbtack for which it might not be possible for it to, say, flip "down".  His data turns out to be 3 down, 9 up, so we know after the data it was possible for both outcomes but not *before* the data.



```python
def lnlike(data,θ):
    h,N=data
    return logbernoullipdf(θ,h,N)

data=3,12
model=MCMCModel(data,lnlike,
                θ=Uniform(0,1),
                )

```

## Running MCMC, looking at the results

Now we run MCMC, plot the chains (so we can see it has converged) and look at distributions,

```python
model.run_mcmc(800,repeat=3)
model.plot_chains()
```

```
Sampling Prior...
Done.
0.27 s
Running MCMC 1/3...
Done.
2.63 s
Running MCMC 2/3...
Done.
2.79 s
Running MCMC 3/3...
Done.
2.47 s
```


![]({static}/images/proportion chains.png)

```python
model.plot_distributions()
```

![]({static}/images/proportion distribution.png)


Is this evidence for a biased coin at, say, 95% level?

```python
model.P("θ <0.5")
```

```
0.95485
```

yes, just as [Lindley, 1976 presents.](https://www.jstor.org/stable/2683855?seq=1#metadata_info_tab_contents) 


## Comparing to textbook examples

The textbook only considers large sample proportions, with the definition $f= h/N$. From the Beta distribution we get our estimate of the proportion 

\begin{eqnarray}
\hat{\theta} &\sim& f \\
\sigma^2 &\sim& \frac{f\cdot (1-f)}{N}
\end{eqnarray}
which matches the equations in the standard textbooks.  Comparing to our case, with $N=120$ we get good agreement,


![]({static}/images/compare proportion N=120.png)


However, we start seeing differences where the textbook treatment isn't as informative as the methods we're using here.  For small samples, say $N=12$, we see that the textbook approximation breaks down -- especially near the $f=0$ and $f=1$ boundaries, sometimes overestimating our certainty and sometimes underestimating it.  

![]({static}/images/compare proportion N=12.png)


Notice, however, that in the current approach we didn't need to change anything to get more robust answers.  Also notice that the current process for this problem is identical to the process for all of the other cases we've considered.  So what we are presenting, compared to the textbook treatments, is a more *unified* approach which *generalizes* to small samples giving a more *correct* analysis for our data.

