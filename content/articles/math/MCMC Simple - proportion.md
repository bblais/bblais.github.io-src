title: Stats 101 Examples with MCMC Part 3
subtitle: Estimating proportion
date: 4/19/2021
status: draft
image: edge2edge-media-uKlneQRwaxY-unsplash.jpg

I'd like to walk through some of the "*Statistics 101*" examples (e.g. estimating $\mu$ with known $\sigma$, estimating a proportion, etc...) for which we have simple analytical solutions, but explore them with [MCMC].  The reason I want to do that is to introduce MCMC on simple cases, which are not much different than more complicated cases, but are better understood.  The second reason is to explore some cases which are nearly as easy, but are never covered in introductory textbooks.  In all of these, for now, I'm going to use a python library I make for my science-programming class, [stored on github](https://github.com/bblais/sci378), and the [emcee] library.  Install like:

```
pip install "git+git://github.com/bblais/sci378" --upgrade
pip install emcee
```


We'll start with the easiest example:  there is some true value, we call $\mu$, with normally-distributed noise of known scale, $\sigma$.  The likelihood function is determined like

$$
\begin{eqnarray}
x_i &\sim& \mu + \epsilon_i \\
P(x_i|\mu,\sigma) &\sim& \text{Normal}(\mu,\sigma) 
\end{eqnarray}
$$
known $\sigma$

and we'll assume uniform priors on $\mu$.  


```python
def lnlike(data,μ):
    # known σ
    x=data
    return lognormalpdf(x,μ,σ)

data=array([12.0,14,16])
σ=1
model=MCMCModel(data,lnlike,
                μ=Uniform(-50,50),
                )
```

now we run MCMC, plot the chains (so we can see it has converged) and look at distributions,

```python
model.run_mcmc(800,repeat=3)
model.plot_chains()
```

```
Sampling Prior...
Done.
0.21 s
Running MCMC 1/3...
Done.
2.23 s
Running MCMC 2/3...
Done.
2.24 s
Running MCMC 3/3...
Done.
2.51 s
```


![]({static}/images/μ chains.png)

```python
model.plot_distributions()
```


![]({static}/images/μ distribution.png)

compare to textbook solution (i.e. Normal with deviation $\sigma/\sqrt{N}$),

```python
x,y=model.get_distribution('μ')
plot(x,y,'-')
μ̂=mean(data)
N=len(data)
σμ=σ/sqrt(N)
y_pred=[exp(lognormalpdf(_,μ̂,σμ)) for _ in x]
plot(x,y_pred,'r--')
```

![]({static}/images/compare μ.png)


and finally do a Z-test

```python
model.P('μ>15')
```

```
0.037066666666666664
```

This simple example can be a template for more complex problems, which I will explore other times.  What do you think?