Title: Reproducing Richard Carrier's Calculations
date: Sep 9, 2024
status: published
image: patrick-fore-0gkw_9fy0eQ-unsplash.jpg

It is said that a published work without the code is little more than an advertisement.  It is for this reason that I try to make sure that I publish all of the code needed reproduce any work that I do, and encourage all researchers to do the same.  

I recently had to go through Richard Carrier's In Richard Carrier’s  _On the Historicity of Jesus_[@carrier2014historicity] the author calculates the probability of the historicity of Jesus, $P(h)$, and Jesus mythicism, $P(\neg h)$. Although his numbers are sometimes based on quantitative estimates, many are not.  His probability is contained in the summary tables in his book.[@carrier2014historicity, p. 597]. Unfortunately, the tables are all scattered through the book and he doesn't explicitly lay out the equations for the final calculation.  Here, as an exercise, I show his full calculation and in the process developed some Python code to make such calculations and their presentation easier.  

Note that the term ‘prior probability’ here depends on what one calls evidence – the posterior of one calculation becomes the prior for the next – because it is ‘prior’ to new evidence. Unlike Carrier, we prefer to make explicit the evidence used at all steps, even from the start.
  
## Summary of Carrier's Prior

Carrier’s prior probability is based on a reference class consisting of two defining features,

- $e_1$ - the reference class member is a person from Mediterranean Antiquity,
- $e_2$ - the reference class member is a Rank-Raglan hero.

Here Carrier uses a set of 14 Rank-Raglan heroes and proceeds to calculate the probability of historicity in two ways: a charitable-to-historicity calculation (*a fortiori*) with 4 out of the 14 historical and a non-charitable calculation (*a judicantiori*) with 0 out of the 14 historical. The data Carrier uses for these cases is shown in the following table:

|               | *a fortiori*    | *a judicantiori* |
|-------------:|:-------------:|:-------------:|
| Historical    | $N_h=4$       | $N_h=0$       |
| Non-historical| $N_m=10$      | $N_m=14$      |
| Total         | $N=14$        | $N=14$        |

Carrier then applies Laplace's Rule of Succession[@Jaynes2003] to calculate the relevant probabilities.  Laplace's Rule of Succession arises from the process of estimating a proportion, $\theta$, given $s$ "successes" out of $N$ total samples (e.g. flipping $s$ heads out of a total $N$ flips of a coin).  The mean value of the proportion, $\theta$, assuming a uniform distribution for $\theta$ is 

$$
\begin{aligned}
\bar{\theta}= \frac{s+1}{N+2}
\end{aligned}
$$

Intuitively, this is the fraction of successes one would observe if, in addition to the actual data, we have one extra "success" and one extra "failure".  

Applied to Carrier’s own calculations, we get a charitable-to-historicity (_a fortiori_) calculation:
  $$P(h|e_1,e_2) = \frac{N_h+1}{N+2}=\frac{4+1}{14+2}=0.31 \sim 1/3\text{ (rounded up)}$$ 
  We also get a non-charitable (_a judicantiori_) calculation:
  $$P(h|e_1,e_2) = \frac{N_h+1}{N+2}=\frac{0+1}{14+2}=0.06$$

### An alternate method

Another way to do the same calculation (giving the same result, as expected) is to write out a full Bayes' theorem formulation for $P(h|e_1,e_2)$, and using an uninformative prior on $h$ given that we're talking about people from Mediterranean antiquity, $P(h|e_1)=P(\neg h|e_1)=0.5$.  In this formulation, the Rank-Raglan feature ($e_2$) is now evidence and Carrier's "prior" is a posterior on that evidence.  This has the advantage of being able to handle some data that is independent of $e_2$ and some that is dependent on $e_2$ which we will see below.  

As a matter of process, we choose to calculate Bayes' Theorem in three steps as described in [@Blais:2014aa]: 

1. calculate just the numerators for all models 
2. calculate the total probability (i.e. denominator) from the sum of the numerators
3. divide each numerator by the total probability, yielding the final posterior probabilities

We find this makes the layout of the calculation more consistent and clear, and as a bonus, we rely less on posterior ratios.

1. $$\begin{aligned}
P(h|e_1,e_2)&\sim \underbrace{P(e_2|h,e_1)}_{\left(\frac{N_h+1}{N+2}\right)} \cdot \underbrace{P(h|e_1)}_{1/2}\\
P(\neg h|e_1,e_2)&\sim \underbrace{P(e_2|\neg h,e_1)}_{\left(\frac{N_m+1}{N+2}\right)} \cdot \underbrace{P(\neg h|e_1)}_{1/2}\\
\end{aligned}$$
$$\begin{aligned}
P(h|e_1,e_2)&\sim \left(\frac{N_h+1}{N+2}\right) \cdot 1/2\\
 & \sim \left(\frac{4+1}{14+2}\right) \cdot 1/2 = 0.1562\\
P(\neg h|e_1,e_2)&\sim \left(\frac{N_m+1}{N+2}\right) \cdot 1/2\\
 & \sim \left(\frac{10+1}{14+2}\right) \cdot 1/2 = 0.3438\\
\end{aligned}$$
2. $$\begin{aligned}
T_{\text{denominator}}&=0.1562 + 0.3438 = 0.5000\end{aligned}$$
3. $$\begin{aligned}
P(h|e_1,e_2)& =0.1562/0.5000=0.3125\\
P(\neg h|e_1,e_2)& =0.3438/0.5000=0.6875\\
\end{aligned}$$

This approach yields identical results -- as it should.^[E.T. Jaynes refers to this as "equivalent states of knowledge must have equivalent probability assignments."]

## Carrier's Original Posterior Calculation

For completeness we show the result of Carrier's original posterior calculation, using evidence he presents in [@carrier2014historicity], which we denote as $\{c_i\}$.  While Carrier's prior probability calculation was based on counts of texts, the rest of his calculations come from his personal judgments on specific aspects of the texts.  His calculations involve looking at *Extrabiblical* texts, *Acts of the Apostles*, the *Gospels*, and the *Epistles of Paul*.  He further assumes the statistical independence of all of these individual judgments, which may be questionable.  We won't explore these problems here, but proceed to reproduce his calculation as-is.  The procedure is then

- list off each individual likelihood ratio $P(c_i|h)/P(c_i|\neg h)$, for each piece of Carrier's judgments $c_i$,
- multiply them all, assuming independence
- multiply by the prior odds ratio to get the posterior odds ratio
- convert to the probability of historicity, $P(h|e_1,e_2,\left\{c_i\right\})$

The following table shows each prior or likelihood ratio for this entire process, both for the charitable and the uncharitable calculations.

|                                                  | *a fortiori*   | *a judicantiori*   | Source        |
|:-------------------------------------------------|:-------------|:-----------------|:--------------|
| $c_{1} :=$ prior ($e_1$,$e_2$)                   | 1/2          | 1/15             | Prior         |
| $c_{2} :=$ Twin traditions                       | 4/5          | 1/2              | Extrabiblical |
| $c_{3} :=$ Documentary silence                   | 1            | 1                | Extrabiblical |
| $c_{4} :=$ 1 Clement                             | 4/5          | 1/2              | Extrabiblical |
| $c_{5} :=$ Ignatius and Ascension of Isaiah      | 4/5          | 1/2              | Extrabiblical |
| $c_{6} :=$ Papias                                | 1            | 1                | Extrabiblical |
| $c_{7} :=$ Hegesippus                            | 9/10         | 4/5              | Extrabiblical |
| $c_{8} :=$ Josephus                              | 1            | 1                | Extrabiblical |
| $c_{9} :=$ Pliny                                 | 1            | 1                | Extrabiblical |
| $c_{10} :=$ Tacitus                              | 1            | 1                | Extrabiblical |
| $c_{11} :=$ Suetonius                            | 1            | 1                | Extrabiblical |
| $c_{12} :=$ Thallus                              | 1            | 1                | Extrabiblical |
| $c_{13} :=$ Lack of gainsaying witnesses         | 1            | 1                | Extrabiblical |
| $c_{14} :=$ Vanishing family et al.              | 4/5          | 2/5              | Acts          |
| $c_{15} :=$ Omissions in Paul's trials           | 9/10         | 1/2              | Acts          |
| $c_{16} :=$ Remainder of Acts                    | 1            | 1                | Acts          |
| $c_{17} :=$ Reasons                              | 1            | 1                | Gospels       |
| $c_{18} :=$ Other canonical Epistles             | 4/5          | 3/5              | Epistles      |
| $c_{19} :=$ Gospels in Paul, Hebrews, Colossians | 3/5          | 2/5              | Epistles      |
| $c_{20} :=$ Things Jesus said                    | 1            | 1                | Epistles      |
| $c_{21} :=$ The Eucharist (1 Cor. 11.23-26)      | 1            | 1                | Epistles      |
| $c_{22} :=$ Things Jesus did                     | 3/4          | 1/2              | Epistles      |
| $c_{23} :=$ Made from sperm                      | 2            | 1                | Epistles      |
| $c_{24} :=$ Made from a woman                    | 2            | 1                | Epistles      |
| $c_{25} :=$ Brothers of the Lord                 | 2            | 1/2              | Epistles      |

### *a fortiori* calculation,

- Posterior ratio $$
\frac{P(h|e_1,e_2,\left\{c_i\right\})}{P(\neg h|e_1,e_2,\left\{c_i\right\})}=\frac{186624}{390625}
$$
- Posterior probabilities $$\begin{aligned}
P(h|e_1,e_2,\left\{c_i\right\})&=\frac{186624}{577249}=0.323\\
P(\neg h|e_1,e_2,\left\{c_i\right\})&=\frac{390625}{577249}=0.677\\
\end{aligned}
$$

### *a judicantiori* calculation


- Posterior ratio $$
\frac{P(h|e_1,e_2,\left\{c_i\right\})}{P(\neg h|e_1,e_2,\left\{c_i\right\})}=\frac{1}{12500}
$$
- Posterior probabilities $$\begin{aligned}
P(h|e_1,e_2,\left\{c_i\right\})&=\frac{1}{12501}=0.000080\\
P(\neg h|e_1,e_2,\left\{c_i\right\})&=\frac{12500}{12501}=0.999920\\
\end{aligned}
$$
This reproduces the numbers Carrier presents.
## The Python code

One thing about this calculation is that it is fairly long and quite tedious.  There are a number of places it can go wrong.  Updating with new data becomes a challenge of bookkeeping, and it is a challenge to make sure that the equations written match the data and the numerical results without typos or missing terms.  This is the sort of thing that computers do quite well - tedious and systematic calculations and presentations. 

I put all the code here:  [https://github.com/bblais/Reproduce-Richard-Carrier-Calculations](https://github.com/bblais/Reproduce-Richard-Carrier-Calculations)

The code allows me to do:

```python
PP={'h|e_1,e_2':[ ['e_2|h,e_1',LS(N_h,N),['N_h','N']],
                  ['h|e_1',F(1,2),'1/2']],
    '\\neg h|e_1,e_2':[ 
            ['e_2|\\neg h,e_1',LS(N_m,N),['N_m','N']],
            ['\\neg h|e_1',F(1,2),'1/2']
       ],
      }

vals,S=P_to_display2(PP)
```

to generate Markdown with all of the steps written out, and the calculations done:

	1. $$\begin{aligned}
	P(h|e_1,e_2)&\sim \underbrace{P(e_2|h,e_1)}_{\left(\frac{N_h+1}{N+2}\right)} \cdot \underbrace{P(h|e_1)}_{1/2}\\
	P(\neg h|e_1,e_2)&\sim \underbrace{P(e_2|\neg h,e_1)}_{\left(\frac{N_m+1}{N+2}\right)} \cdot \underbrace{P(\neg h|e_1)}_{1/2}\\
	\end{aligned}$$
	$$\begin{aligned}
	P(h|e_1,e_2)&\sim \left(\frac{N_h+1}{N+2}\right) \cdot 1/2\\
	 & \sim \left(\frac{4+1}{14+2}\right) \cdot 1/2 = 0.1562\\
	P(\neg h|e_1,e_2)&\sim \left(\frac{N_m+1}{N+2}\right) \cdot 1/2\\
	 & \sim \left(\frac{10+1}{14+2}\right) \cdot 1/2 = 0.3438\\
	\end{aligned}$$
	2. $$\begin{aligned}
	T_{\text{denominator}}&=0.1562 + 0.3438 = 0.5000\end{aligned}$$
	3. $$\begin{aligned}
	P(h|e_1,e_2)& =0.1562/0.5000=0.3125\\
	P(\neg h|e_1,e_2)& =0.3438/0.5000=0.6875\\
	\end{aligned}$$

which looks like

1. $$\begin{aligned}
P(h|e_1,e_2)&\sim \underbrace{P(e_2|h,e_1)}_{\left(\frac{N_h+1}{N+2}\right)} \cdot \underbrace{P(h|e_1)}_{1/2}\\
P(\neg h|e_1,e_2)&\sim \underbrace{P(e_2|\neg h,e_1)}_{\left(\frac{N_m+1}{N+2}\right)} \cdot \underbrace{P(\neg h|e_1)}_{1/2}\\
\end{aligned}$$
$$\begin{aligned}
P(h|e_1,e_2)&\sim \left(\frac{N_h+1}{N+2}\right) \cdot 1/2\\
 & \sim \left(\frac{4+1}{14+2}\right) \cdot 1/2 = 0.1562\\
P(\neg h|e_1,e_2)&\sim \left(\frac{N_m+1}{N+2}\right) \cdot 1/2\\
 & \sim \left(\frac{10+1}{14+2}\right) \cdot 1/2 = 0.3438\\
\end{aligned}$$
2. $$\begin{aligned}
T_{\text{denominator}}&=0.1562 + 0.3438 = 0.5000\end{aligned}$$
3. $$\begin{aligned}
P(h|e_1,e_2)& =0.1562/0.5000=0.3125\\
P(\neg h|e_1,e_2)& =0.3438/0.5000=0.6875\\
\end{aligned}$$
Enjoy!