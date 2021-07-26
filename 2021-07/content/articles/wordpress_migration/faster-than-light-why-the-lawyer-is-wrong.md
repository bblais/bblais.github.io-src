Title: Faster than light...why the lawyer is wrong
Date: 2011-10-14 15:11
Author: brianblais
Slug: faster-than-light-why-the-lawyer-is-wrong

In a post [well outside of his expertise][], lawyer Michael D. Cicchini
weighs in on the recent observation that some neutrinos have been
observed [traveling faster than the speed of light][]. In his own words
"I try to stick to law-related topics, but every once in a while I'll
delve into matters that are way over my head, like college sports and
even physics." He should stick to law.

His post makes the following two claims:

1.  physicists created the concept of "dark matter" simply to keep
    Einstein's theory of general relativity alive
2.  The speed of light, Einstein had said, was the fastest speed at
    which anything could move. If an object could move faster than that,
    then Einstein's theories would be proved incorrect.

He concludes with

> Hopefully scientists won't continue to cling to Einstein's theories if
> it's not warranted. The hallmark of science has always been its
> willingness to discard what no longer works when new evidence comes
> along. And toward that end, here's an admittedly uneducated
> suggestion: abandon Einstein's quest of unifying the quantum with the
> cosmic. [...] it appears that such an attempt is doomed to failure
> because one of the theories they're attempting to unify is wrong.
>
> Back to the drawing board.

This post is ill-informed for many reasons. Let me try to address a few.

**Dark Matter**

The concept of [dark matter][] was not invented to keep Einstein's
theory alive, it was invented to keep *Newton's* theory alive (which
Einstein's General Theory of Relativity is consistent with, and extends
to new areas). Essentially, given the form of Newton's law, we can
estimate the mass of a galaxy from its spinning. It turns out that this
method of measuring the mass yields 10 times the mass that we get by
estimating it from the directly observed mass (i.e. from counting up the
the light emitted by the mass). We then have several choices:

1.  the counting up the light method underestimates mass by a factor of
    10...this is highly unlikely, because the method has been consistent
    with many other measurements, and is a direct consequence of
    fundamental laws of physics
2.  Newton's laws are wrong
3.  there is more mass than we can actually see...we give it a name,
    "dark matter", just as a place-holder until we could determine what
    it is.

Guess what? Scientists have explored all these possibilities! The most
relevant ones to this post have to do with [MOND (Modified Newtonian
Dynamics)][]. For example, Newton's law of gravity is of the form

$$ 
F=\frac{GMm}{r^2} = ma 
$$

The consequences of this have been checked out many decimal places, and
explains things as diverse as the tides, the formation of planetary
rings, and the development of galaxies. What would it take to displace
this? You'd have to modify it in such a way as to be consistent with all
of the things that it predicts well, as accurately as it currently
predicts, and have your modifications be consistent with some other set
of observations which are inconsistent with the current theory. This is
why it took 200 years to significantly modify Newton's Theory of
Gravity, with Einsteins General Theory of Relativity. An example of MOND
could be something like

$$
F=\frac{GMm}{r^2}\times \mu\left(\frac{a}{a_o}\right) 
$$

where $\mu(a/a_o)$ is a function that needs to be
close to 1 for normal situations (and thus look like Newton's laws), but
be different for the case of spinning galaxies. In this case there is a
single parameter, $a_o$, which is a critical
acceleration far above which the situation is "normal". Typical values
are around $ 10^{-10} {\rm m/s^2}$, and one
possible form for $\mu()$ is

$$ \mu(x) = 1-e^{-x}
$$

Near the Earth, this translates to

$$ \mu(x) =0.\underbrace{99999999\cdots}_{10^{10} {\rm nines!}} 
$$

On the big scale, on the outskirts of galaxies, the accelerations are
comparable to $a_o$ and the predictions can lead to
consistent mass curves without introducing more mass.

The dark matter postulate has also been, and continues to be, explored.
There are some theoretical reasons to suggest that dark matter exists in
the form of new fundamental particles, and there are attempts now to
directly measure them.

The point here is that the original post was *completely wrong* about
the motivation to include dark matter. Further, it was wrong in implying
that scientists don't examine and try to replace well-established ideas.
I tell my students that it is a good day if you can demonstrate that one
of your colleagues is wrong. It is an even better day if you can
overturn a well-established idea (you get phone calls from Sweden for
this). However, the burden is on the scientist trying to overturn a
well-established idea to put forward something that is both consistent
with all of the observations of the previous theory, and to demonstrate
consistency on new tests that yield a different (and thus wrong) result
from the old theory. Thus, it gets harder and harder to overturn an idea
that is well established in science.

**The Speed of Light**

First, let me point out that Einstein doesn't say in his 1905 paper on
Special Relativity that the speed of light is the maximum speed (note,
this is different than General Relativity, which handles gravity...a
distinction that Michael Cicchini doesn't seem to grasp). He merely
asserts that the speed of light is measured to be constant in all
inertial reference frames (i.e. measurements made in situations of
constant speed). The derivation of the maximum speed is a consequence of
this, and results in the Lorentz transformation. What we see in these
equations is a factor entering in throughout of the form

$$
\gamma = \frac{1}{\sqrt{1-v^2/c^2}} 
$$

where $c$ is the speed of light, and $v$ is the speed of an object. This factor goes to infinity
as $v\rightarrow c$, which places the speed limit.
However, in certain circumstances, it might be that the factor takes a
different form and, say, looks like

$$
\gamma = \frac{1}{\sqrt{1-v^2/c^2 +10^{-20}}} 
$$


which would allow speeds greater than the speed of light. This
simplistic hack will break other parts of the theory, and so a more
subtle modification would be needed, but it could certainly be
done...and it wouldn't require overturning Einstein's theory. We must be
particularly observant of the following two facts:

1.  relativistic quantum mechanics (QED) makes predictions so accurate,
    it would be like predicting the width of North America to the width
    of a human hair...*any* replacement theory would need to do as well
2.  one other significant observation of neutrinos comes from supernova
    explosions, many light years away. It is observed that the neutrinos
    reaches us at the time, or very slightly below the time that the
    light from the explosion reaches us. Thus, over far longer spans of
    space there is no observed violation of the speed of light limit.

Although the neutrino story is intriguing, it does not entail the
overthrow of Einstein even if it turns out to be true. More likely it
will not be true, however. The biggest lesson of this is that lawyers
should not speak about physics (although to be fair, Edwin Hubble, the
discoverer of the expansion of the universe, was a lawyer before he
became an astronomer). My bet is still on Einstein, no matter what the
result of the experiment is. This isn't because I am dogmatically
attached to Einstein's ideas, but that his ideas have been tested to an
astonishing degree, and any replacement will have to do just as well.

  [well outside of his expertise]: http://thelegalwatchdog.blogspot.com/2011/09/legal-watchdog-faster-than-speed-of.html
  [traveling faster than the speed of light]: http://news.sciencemag.org/sciencenow/2011/09/neutrinos-travel-faster-than-lig.html
  [dark matter]: http://en.wikipedia.org/wiki/Dark_matter
  [MOND (Modified Newtonian Dynamics)]: http://en.wikipedia.org/wiki/Modified_Newtonian_dynamics
