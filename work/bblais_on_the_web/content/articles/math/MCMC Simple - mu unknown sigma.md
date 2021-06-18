title: Stats 101 Examples with MCMC Part 2
subtitle: Estimating mean with unknown 𝜎
date: 4/28/2021
status: published
image: edge2edge-media-uKlneQRwaxY-unsplash.jpg

This is another in the series of "*Statistics 101*" examples solved with MCMC.  The previous in the series [can be found here](https://bblais.github.io/posts/2021/Apr/15/stats-101-examples-with-mcmc/).  In all of these posts I'm going to use a python library I make for my science-programming class, [stored on github](https://github.com/bblais/sci378), and the [emcee](https://emcee.readthedocs.io/en/stable/) library.  Install like:

```
pip install "git+git://github.com/bblais/sci378" --upgrade
pip install emcee
```


In this example, like [the last one](https://bblais.github.io/posts/2021/Apr/15/stats-101-examples-with-mcmc/), there is some true value, we call $\mu$.  The $N$ data points we have, $\{x_i\}$, consist of that true value with added independent, normally-distributed noise of *unknown* scale, $\sigma$.  


For a Bayesian solution, we need to specify the likelihood function -- how our model produces the data -- and the prior probability for the parameters.  The likelihood function is determined exactly as before,

$$
\begin{eqnarray}
x_i &\sim& \mu + \epsilon_i \\
P(x_i|\mu,\sigma) &\sim& \text{Normal}(x_i-\mu,\sigma) \\
P(\{x_i\}|\mu,\sigma) &\sim& \prod_i \text{Normal}(x_i-\mu,\sigma) 
\end{eqnarray}
$$
but with *unknown* scale, $\sigma$.

In the "*Statistics 101*" examples, the results are typically equivalent to *uniform* priors on the location parameters, but [Jeffreys](https://en.wikipedia.org/wiki/Jeffreys_prior) priors on *scale* parameters, so we'll assume uniform priors on $\mu$ and Jeffreys priors on $\sigma$


## Setting up the problem

In this example, like [the last one](https://bblais.github.io/posts/2021/Apr/15/stats-101-examples-with-mcmc/), there is some true value, we call $\mu$, with normally-distributed noise but this time with unknown scale, $\sigma$.  The likelihood function is determined identically as before, 

$$
\begin{eqnarray}
x_i &\sim& \mu + \epsilon_i \\
P(x_i|\mu,\sigma) &\sim& \text{Normal}(\mu,\sigma) 
\end{eqnarray}
$$
known $\sigma$

and we'll assume uniform priors on $\mu$.  The prior for $\sigma$, which we must now estimate, is taken to be a [Jeffreys prior](https://en.wikipedia.org/wiki/Jeffreys_prior).  This prior is uniform in $\log \sigma$ or, in other words, uniform in *scale*. 


```python
def lnlike(data,μ):
    # known σ
    x=data
    return lognormalpdf(x,μ,σ)

data=array([12.0,14,16])
model=MCMCModel(data,lnlike,
                μ=Uniform(-50,50),
                σ=Jeffreys(),
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


![]({static}/images/μσ chains.png)

```python
model.plot_distributions()
```


![]({static}/images/μt distribution.png)
![]({static}/images/σ distribution.png)

## Comparing to textbook examples


We compare to textbook solution for $\mu$ (i.e. Student t-distribution),

```python
x,y=model.get_distribution('μ')

plot(x,y,'-')
μ̂=mean(data)
N=len(data)

σμ=std(data,ddof=1)/sqrt(N)
y_pred=[exp(logtpdf(_,N-1,μ̂,σμ)) for _ in x]
plot(x,y_pred,'r--')

```

![]({static}/images/compare μ t.png)

and the textbook solution for $\sigma$ (i.e. Chi-square),

```python
x,y=model.get_distribution('σ',bins=800)
plot(x,y,'-')

V=((data-data.mean())**2).sum()
logp=-N*log(x)-V/2/x**2
y_pred=exp(logp)
dx=x[1]-x[0]
y_pred=y_pred/y_pred.sum()/dx

plot(x,y_pred,'r--')
xlim([0,20])
```

![]({static}/images/compare σ.png)


## Tail-area Probabilities


We can easily find the tail-area probability, the Bayesian equivalent to Student-t test, for $\mu$,

```python
model.P("μ>15")
```

```
0.037066666666666664
```

and for $\sigma$, the Bayesian equivalent to Chi-squared test, 

```python
model.P("σ<1")
```

```
0.01985
```

