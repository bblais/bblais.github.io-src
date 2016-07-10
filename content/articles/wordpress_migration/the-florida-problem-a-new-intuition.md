Title: The Florida problem - a new intuition
Date: 2011-10-30 13:35
Author: brianblais
Slug: the-florida-problem-a-new-intuition

**1. Introduction**

In a prior couple of posts [here][] and [here][1] I look into the
\`\`evil'' probability problem of the girl-named-Florida. This problem
compares the following two situations:

> Say you know a family has two children, and further that at least one
> of them is a girl. What is the probability that they have two girls?

and

> Say you know a family has two children, and further that at least one
> of them is a girl named Florida. What is the probability that they
> have two girls?

The former is easy to show is \$latex {p(2g|\\{L1g\\})=1/3}&fg=000000\$.
The latter is shown to be \$latex {p(2g|\\{L1g\\},F)=1/2}&fg=000000\$.
Intuition firmly insists that knowing the name shouldn't change the
probability, but the math and simulations insist otherwise. Thus, it is
our duty, to try to get our intuition around the problem. I was
motivated to look at this again when a commenter asked

> Can someone tell me what the relevance of the comparative
> rarity/commonness of the girl's name is? Suppose instead we knew that
> the girl's name was "Mary". The possibilities would still work out the
> same:
>
> B GM
>
> GM b
>
> GM GNM
>
> GM GM
>
> GNM GM

After much pondering, I think I have come up with another way to recast
the problem that adds to the intuition. I can't say that it makes it
completely obvious to me, like the [Monty Hall problem][] is for me now,
so I think there still is something missing in my understanding of *why
the problem is so unintuitive*. However, it does seem to push the idea a
bit farther forward. In the next section I introduce another problem,
with similar properties but is possibly more intuitive. I then describe
how it can be used to gain an intuition on the Florida problem, and why
the frequency of the name can make a difference.

**2. A Card Game**

Say I play a game with a very small deck (just so that we can work the
numbers well). The deck has 8 cards: Ace, two, three, and four of hearts
and the five, six, seven, and eight of spades. Two cards are dealt, and
you are given some modest information about the two cards, and asked to
determine the probability that the two cards are both hearts. Let's look
at three types of information given:

1.  *You're only told that there are two cards.* Thus, there the
    probability for two hearts is simply

    \$latex \\displaystyle p(2H) = \\frac{4}{8} \\times {3}{7} =
    \\frac{12}{56} \\ \\ \\ \\ \\ (1)&fg=000000\$

    This can be seen pictorially by listing every possible two-card hand
    and looking at those with two hearts, yielding 12 hands out of 56.

    ![]

    <p>
2.  *You're told that at least one of the cards is a heart*. Now we need
    to look at the first and second cards, and eliminate the possibility
    of two spades

    \$latex \\displaystyle p(2H|\\{L1H\\}) =
    \\frac{p(H\_1,H\_2)}{p(H\_1,S\_2)+p(S\_1,H\_2)+p(H\_1,H\_2)} \\ \  
   \\ \\ \\ (2)&fg=000000\$

    where \$latex {p(H\_1,S\_2)}&fg=000000\$ is that we drew a heart
    then a spade. We then have

    \$latex \\displaystyle \\begin{array}{rcl} p(2H|\\{L1H\\}) &=&
    \\frac{\\frac{4}{8}\\times\\frac{3}{7}}{\\frac{4}{8}\\times\\frac{4}{7}+\\frac{4}{8}\\times\\frac{4}{7}+\\frac{4}{8}\\times\\frac{3}{7}}\\\  
   &=&\\frac{12}{44} \\end{array} &fg=000000\$

    This can be seen pictorially by listing every possible two-card hand
    *with at least one heart* and looking at those with two hearts,
    yielding 12 hands out of 44.

    ![2]

3.  *You're told that at least one of the cards is an ace of hearts*.
    Notice how this changes things. Now, when we outline the
    possibilities, we get

    \$latex \\displaystyle p(2H|\\{L1H\\},A) =
    \\frac{p(H\_{1a},H\_{2n})+p(H\_{1n},H\_{2a})}{p(H\_{1a},H\_{2n})+p(H\_{1n},H\_{2a})+p(S\_{1},H\_{2a})+p(H\_{1a},S\_2)}
    \\ \\ \\ \\ \\ (3)&fg=000000\$

    Let's look at the numerator first.

    \$latex \\displaystyle p(H\_{1a},H\_{2n}) =
    p(H\_{2n}|H\_{1a})p(H\_{1a}) \\ \\ \\ \\ \\ (4)&fg=000000\$

    Written like this, it is like turning over card one, seeing it's an
    ace of hearts, and then turning over card 2. \$latex
    {p(H\_{1a})=1/8}&fg=000000\$, and seeing a heart that is not an ace
    is really the same as seeing any ol' heart, so it is \$latex
    {p(H\_{2n}|H\_{1a})=3/7}&fg=000000\$. This is not any different than
    the previous situation. However, the next term in the numerator

    \$latex \\displaystyle p(H\_{1n},H\_{2a}) =
    p(H\_{2a}|H\_{1n})p(H\_{1n}) \\ \\ \\ \\ \\ (5)&fg=000000\$

    *is* really different, because we are told that there is at least
    one ace. The probability of drawing a heart that is not an ace on
    the first card is still \$latex {p(H\_{1n})=3/8}&fg=000000\$.
    However, drawing an ace of hearts on the second card when we drew a
    non-ace of hearts on the first is *certain*, because we have
    knowledge that at least one is an ace. Thus, \$latex
    {p(H\_{2a}|H\_{1n})=1}&fg=000000\$. This gives, for the numerator,

    \$latex \\displaystyle
    p(H\_{1a},H\_{2n})+p(H\_{1n},H\_{2a})=\\frac{3}{7}\\cdot\\frac{1}{8}
    + 1\\cdot \\frac{3}{8} = \\frac{24}{56} \\ \\ \\ \\ \  
   (6)&fg=000000\$

    Notice that if \$latex {H\_{2a}}&fg=000000\$ had been independent of
    \$latex {H\_{1n}}&fg=000000\$ then we would have gotten the same
    12/56 term in the numerator as in the previous situation.
    Essentially, by giving the information that there is at least one
    ace, you are really making the value of one card dependent on the
    other, and thus knowledge of one gives you knowledge of the other
    and the probability for two hearts goes up. The same thing happens
    with \$latex {p(H\_{2a}|S\_1)}&fg=000000\$, but since we compare to
    the case where we know there is one heart anyway, this is not a
    difference.

    Following through with the rest gives us

    \$latex \\displaystyle \\begin{array}{rcl} p(2H|\\{L1H\\},A) &=&
    \\frac{p(H\_{1a},H\_{2n})+p(H\_{1n},H\_{2a})}{p(H\_{1a},H\_{2n})+p(H\_{1n},H\_{2a})+p(S\_{1},H\_{2a})+p(H\_{1a},S\_2)}
    \\\\ &=&\\frac{\\frac{3}{7}\\cdot\\frac{1}{8}+ 1 \\cdot
    \\frac{3}{8}}{\\frac{4}{7}\\cdot\\frac{1}{8}+1\\cdot
    \\frac{4}{8}+\\frac{24}{56}}\\\\ &=&\\frac{24}{56} = \\frac{6}{14}
    \\end{array} &fg=000000\$

    This can be seen pictorially by listing every possible two-card hand
    with an ace of hearts and looking at those with two hearts, yielding
    6 hands out of 14.

    ![3]

**3. Back to the Florida problem**

The ace-of-hearts problem is exactly like the Florida problem, if you
make the deck big enough. The key issue here seems to be that by giving
a rare name to one of the girl children, it correlates the two children
in a way that the independence assumptions in both the simpler problem
and one's intuition break down. If you were to \`\`draw'' a girl first
and not a Florida, then we *must* have a girl second named Florida. In
the same way, the game show host in Monty Hall is forced to give
information to the contestant through the rules of the game: 2/3 of the
time he is forced to give the contestant the door with the prize.

Another thing to notice is that the frequency of the \`\`aces'' (or
Floridas) in the problem definitely has an effect. You can confirm this
by changing the information in the card game to *You're told that at
least one of the cards has a rank less than three*. It is easy to see
how this would change the probabilities.

**3.1. Intuition**

So why is this problem so unintuitive? I think a lot of it is related to
the issues that Jeff J states in the comments.

> But suppose you learned what you know about this family because you
> meet the mother walking with her daughter, and asked her how many
> children she has. When she said “two,” this scenario fits the problem
> statement just as well as what Brian assumed. You know the family has
> two children, and that at least one is a girl. But, the probability is
> 1/2 that she has two daughters, not 1/3 (reference: Bar-Hillel and
> Falk, or look at Grinstead and Snell's on-line textbook).

There is a certain \`\`omniscience'' assumed in the card game (not so
unrealistically) and in the Florida problem (probably unrealistically)
that changes the scope of the problem. Most people's intuitions are
shaped by the cases like Jeff J, where we know of a specific child named
Florida, and asked about the chances of having another girl which is
1/2, or even know only that there is at least one girl, but a specific
one, so you get the 1/3 when thinking about it. The name, therefore,
doesn't affect anything...in most realistic situations. However, in this
card game it does affect the chances of having two hearts when you are
restricted to the hands with at least one ace of hearts. I find that it
doesn't seem to violate my intuition as badly in the card game as it
does in the Florida , and much more clearly and it doesn't seem to
violate our intuitions quite so badly.

  [here]: https://brianblais.wordpress.com/2010/01/05/there-once-was-a-girl-named-florida-a-k-a-evil-problems-in-probability/
  [1]: https://brianblais.wordpress.com/2010/02/22/coin-flips-and-names-evil-problems-in-probability-continued/
  [Monty Hall problem]: https://brianblais.wordpress.com/2009/09/16/probability-problems-and-simulation/
  []: http://brianblais.files.wordpress.com/2011/10/fig1.png
  [2]: http://brianblais.files.wordpress.com/2011/10/fig2.png
  [3]: http://brianblais.files.wordpress.com/2011/10/fig3.png
