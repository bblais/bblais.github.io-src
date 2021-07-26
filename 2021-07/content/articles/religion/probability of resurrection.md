title: Probability of the Resurrection
subtitle: Discussion through Calculation
date: 9/3/2019
status: Published
image: patrick-schneider-wczrs3Unfnk-unsplash.jpg


In a recent discussion about the use of probability in a religious context I saw another poor job of a calculation of the Resurrection (I had read several others that had serious problems).  I then felt that it would be good to sketch out how it *should* be done.  The goal here is not to come up with a single number, but to have a structure which invites discussion.  

## A smaller problem

We are restricting the problem to the smallest possible case to most easily see the form that the calculation takes when done properly.  The problem is 

> A friend of yours flipped a coin three times and got heads three times in a row.  Would this be good evidence for your friend having a coin with two heads compared to, say, a typical coin with 1 heads and 1 tails?  Here we have 2 models ($M_1$, say, is for the 1-headed coin model and $M_2$ is for the 2-headed coin model), and some observed data (heads, heads, heads in 3 flips).

We want to know the probability of each of the models given the data.  In math notation we use the vertical bar,$|$, as the symbol for "given".  The "data" is summarized as "H H H" for three observed heads flips.  So we want to obtain,
$$
P(M_1 | \text{H H H})  \text{ and } P(M_2 | \text{H H H})
$$
following Bayes theorem, we write the top of Bayes equation as 
$$
P(M_1 | \text{H H H}) \sim P(\text{H H H}| M_1) \times P(M_1)
$$
and
$$
P(M_2 | \text{H H H}) \sim P(\text{H H H}| M_2) \times P(M_2)
$$
Before continuing, let me point out a few things.  First, I'm not using equals here, but the $\sim$ sign to denote that I'm writing just the top part of the equation first.  I'll add these two things up to get the bottom of Bayes in the next step.  I do it as a two-step process to make it easier to write down (i.e. it formats better in text) and to help when we generalize to more than 2 models, where Bayes can get a bit unwieldy. 

The term $P(\text{H H H}| M_1)$ is the probability we'd see the data if we knew (i.e. we're given) that model 1 is true.  Since $M_1$ is from a fair coin, we get 1/2 probability for each head independently and we don't have any extra counting term, so we'd get the $P(\text{H H H}| M_1)=\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}$.  The term $P(\text{H H H}| M_2)$ is the probability we'd see the data if we knew (i.e. we're given) that model 2 is true.  Since $M_2$ is from a rigged two-headed coin, we get a probability of 1 for each head so we'd get the $P(\text{H H H}| M_2)=1\times 1\times 1$.  

The terms $P(M_1)$ and $P(M_2)$ are the prior probabilities of the model - how much we should believe them before we saw the data.  This is probably the most contentious point, and worth dwelling on.  It's not 50%, just because there are two possibilities.  Do we even know if a two-headed coin exists?  Have you ever seen one?  The two models are not symmetric.  Turns out I have seen one!  There's one in my desk, which I love to bring out to fool my students.  :-)  It was found by accident with my daughter going through all of our loose change.  I have never seen one since, but if we just took my house as an example, it's no bigger than a 1/100 of all the quarters.  This can inform the prior as $P(M_1) = 0.99$ and $P(M_2) = 0.01$.  I would guess that this is a huge *over estimate* for the $P(M_2)$ but it's good to run with.  

Getting back to our probabilities, we calculate the top terms of Bayes, add them up, and then go back to divide each by that total.  Thus we get:
$$
\begin{align}
P(M_1 | \text{H H H}) &\sim P(\text{H H H}| M_1) \times P(M_1) = \frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times 0.99 = 0.124 \\
P(M_2 | \text{H H H}) &\sim P(\text{H H H}| M_2) \times P(M_2) = 1\times 1\times 1\times 0.01 = 0.01
\end{align}
$$
(adding them up) $T=0.124 + 0.01 = 0.134$

finally getting (notice the equals now)
$$
\begin{align}
P(M_1 | \text{H H H}) &=0.124/T = 0.124/0.134=0.925 \\
P(M_2 | \text{H H H}) &=0.01/T=0.01/0.134 = 0.075
\end{align}
$$
So, finally, we can have good reason -- by a long shot -- to *not believe* that the person has a 2-headed coin.   Although we  have a nearly $8\times$ increase in the probability of that model, $M_2$, given the observed data of 3 heads, this doesn't bring our confidence up to the level of belief - you'd need more data for that.  

This problem has exactly the same structure as the problem under consideration, trying to find the probability of the resurrection given the data we have and the number of possible models.

## The problem at hand - the probability of the Resurrection

The proper way to set the problem up, like the coin, is the following.  First, we start with the different models:

* $R$ = Resurrection happened
* $M$ = Resurrection story made up entirely
* $V$ = Resurrection story incited by visions from early apostles and embellished
* etc...

and then the math follows just like the example above,

* data = texts of gospels and Paul (and their history)

* $P(R | \text{data}) \sim P(\text{data} | R) \times P(R)$
* $P(M | \text{data}) \sim P(\text{data} | M) \times P(M)$
* $P(V | \text{data}) \sim P(\text{data} | V) \times P(V)$
* .... [insert more models if you'd like]

then add up to $T = \ldots$, and divide all terms, just like the coin.  

Arguments over priors can ensue, but I think it would  be fair to say that $P(M)>P(V) \gg P(R)$. Although one might question this order (e.g.  arguing that visions are more common than story construction) it is certainly true that resurrections are far less common than stories or visions.  How often do we see resurrections?  How often do we see God raising someone from the dead?  How often have we heard claims of people being raised from the dead, from God or otherwise?  These very simple questions bring the prior for the Resurrection *way* down.  The theist will typically counter with something like "I agree that resurrections through *natural* processes are extremely unlikely, but if there is a God he could easily make resurrections through *supernatural* causes likely."  I'll deal specifically with this objection in detail below but at this point the term $P(R)$ doesn't presuppose any mechanisms - it is just the probability of a resurrection before seeing any data and it should be agreed that this is much lower than visions or stories.

Beyond the prior, we note that terms like $P(\text{data} | R)$ have to balance both the positive claims and negative claims.  For example, we might say that this term is quite high from the positive claims -- if the Resurrection actually happened then it easily explains the stories of seeing Jesus afterward.  However, there are things that we probably should have seen -- but don't -- if the Resurrection actually happened.  Some includes the lack of an account of Roman stolen-body litigation (as would have been done to the disciples), the fact that Paul doesn't mention the empty tomb, and the guards at the tomb are only mentioned in Matthew are not mentioned in Mark, Luke, John, or even Paul.  These negative claims are easily explained with the other two models but are not easily explained from the Resurrection model making $P(\text{data} | R)$ much lower than is generally communicated.

### Supernatural causation

Now, what about the claim that the low priors are mitigated by the issue of God *supernaturally* raising Jesus?  Here is where it gets interesting.  If you want to add the possibility of God raising Jesus *supernaturally* from the dead we can do this with a process called *marginalization*, which is a fancy term for adding up all of the possibilities.  Mathematically it looks like the following,

First define some symbols,

* $+G$ = God
* $+S$ = Supernatural action
* $-G$ = no God
* $-S$ = natural action

We can then draw out the probability terms (which don't mention any specific methods of resurrections) into several terms, each for a different method, and then apply Bayes' rule yielding
$$
\begin{align}
P(R | \text{data}) =& P(R, +G,+S | \text{data}) + P(R, -G,+S| \text{data}) + P(R, +G,-S| \text{data}) + P(R, -G,-S| \text{data})\\
\sim & P(\text{data}|R,+G,+S)P(R|+G,+S)P(+S|+G)P(+G) + \\ \nonumber
&P(\text{data}|R,-G,+S)P(R|-G,+S)P(+S|-G)P(-G) + \\ \nonumber
&P(\text{data}|R,+G,-S)P(R|+G,-S)P(-S|+G)P(+G) + \\ \nonumber
&P(\text{data}|R,-G,-S)P(R|-G,-S)P(-S|-G)P(-G) 
\end{align}
$$
This messy result lets us look at individual terms to see where we might have to examine the data more closely.  Theists state that terms like $P(R|-G,-S)$ are small (unlikely resurrection given no God and only natural action), and I'll grant you that.  How about $P( R | +G, -S)$ or, in words,  why couldn't God have done the resurrection naturally?  How about  $P( R | -G, +S) $ or, in words, couldn't Satan or Stephen Fry's evil God have done the resurrection supernaturally?  How have theists ruled these out?  

 Suddenly, by opening up some specific alternatives, one needs to follow all of those alternatives -- and their inverses -- through the entire calculation.  You then have to provide evidence for God's supposed actions ($P(+S|+G)$ and $P(-S|+G)$) reading his inscrutable plan.  You also have to demonstrate that there are not other supernatural agents at play, and that it is likely that God is the one acting. Given that theists have yet to provide *any way* of testing supernatural claims *at all* it seems like a big feat.  In short, by introducing supernatural causation into the mix, theists have made their life harder -- not easier.