Title: Climate and the Moon
Date: 2011-07-28 09:45
Author: brianblais
Slug: climate-and-the-moon

In a [prior post][] I criticize an article on climate which states that
current climate models ignore the effect of conduction (i.e. direct
contact) and convection, and focus exclusively on the greenhouse gas
radiative effect. A comment to that post needs a full response. The
comment in full is here:

“I almost bought your discussion until you provided the diagram from
Kiehl and Trenberth which is ludicrous. The whole construct here is to
create the illusion that the sun cannot heat the earth above minus 18
which is absolute nonsense based on assuming it is valid on geometric
grounds to reduce the solar insolation by a factor of 4 then again by
the albedo.

If this is valid how then does the surface temperature of the moon reach
\~123 C - quoted by NASA.

And how do you explain daytime temperatures on Earth in excess of 50 C
as has been recorded ?”

I will focus on the Moon part, just because it is the easiest, but it
will be natural to see how to approach this for the Earth as well.
First, I must point out the irony of the comment. In trying to defend
the claim that the climate models ignore conduction and convection, and
focus exclusively on radiation, the comment refers to a system (the
Moon) where there is no atmosphere and thus no conduction (except within
the ground itself) or convection! Second I have to wonder about how
stupid the commenter thinks NASA is. Do they really think that
scientists would consider models that are flagrantly in conflict with
the most basic observation about the Moon’s surface (i.e. its
temperature extremes)? Do they really think that scientists would come
up with a calculation that Moon can’t achieve temperatures above, say,
-18 C and then stare at 100 C temperature measurements and just leave
the calculation as is for decades? Let’s consider how one would develop
a model of the surface temperature of the Moon, and it will answer the
objections raised in the comment, as well as outline how real science
actually progresses.

<span style="font-size:15pt;">**The Average Blackbody Model**</span>

We start with a very simple model of a spherical body out in space
receiving input from the Sun to the tune of 1400
W/m<span style="vertical-align:super;">2</span>. At the same time, the
spherical body emits radiation with a power per square meter dependent
on T<span style="vertical-align:super;">4</span> (i.e. the blackbody
law).

![Untitled-2011-07-28-05-45.png][]

Notice that in this very simple model we are assuming several things:

1.  that the conduction *within* the body is instantaneous, thus the
    temperature of the body is uniform, and the output energy is
    uniform.
2.  the body is not rotating, so the radiation it is receiving is
    constant
3.  there is no atmosphere, thus no conduction or convection outside of
    the solid body
4.  the albedo is the *average* albedo of the Moon, or a=0.14. Thus this
    object absorbs 86% of the radiation coming in

I’m not saying this is a *good* model, but it is a simple one that helps
one understand *some* of the concepts at hand. We will see shortly that
it has a number of shortcomings, but for now we’ll see how far we can
push it. This is a traditional procedure in science. You start with the
simplest model you can write down, push out all the consequences you can
until the model breaks, and then introduce the needed complexities to
address those consequences (and no more!). Thus, you always have the
simplest model that is consistent with as many of the observations that
you can.

The total energy out of the body would be the blackbody term shown,
multiplied by the total surface area of the sphere: the radiation is
outward in all directions. The incoming radiation, however, strikes only
one side. Further, it strikes at different angles. Applying calculus one
finds that the effective area is simply the cross-sectional area of the
sphere, or the area of a circle the same size as the sphere.

![PastedGraphic-2011-07-28-05-45.jpg][]

We can then write down the change in the temperature, which depends on
the material (the mass and specific heat), given the net energy input to
the body. I’ll call this dependency K...its exact value, although
calculable, will not be important in the model except qualitatively. We
then have

![PastedGraphic1-2011-07-28-05-45.jpg][]

When the “energy in” is greater than “energy out”, the temperature
increases. When “energy in” is *less than* “energy out” the temperature
*decreases*. Once it reaches equilibrium, temperature remains constant.
What constant? That would be when dT/dt=0, or...

![PastedGraphic2-2011-07-28-05-45.jpg][]

If we look up the values for the actual Moon we get the following:

![PastedGraphic3-2011-07-28-05-45.jpg][]

So our model is not too bad, for the average value, but it could
probably be improved. So, now back to the comment which motivated this
all:

“If this is valid how then does the surface temperature of the moon
reach \~123 C - quoted by NASA.”

The bottom line here is that, if there is an observation that is in
conflict with a model, one of the assumptions of the model is probably
incorrect, or perhaps you’re comparing the wrong observations to the
model. We assumed that the object has a uniform temperature but we
*know* from the 3 data points above (the min, max and mean temperatures)
that this is not true! Essentially our model didn’t even *attempt* to
describe temperature variations on the surface, so it comes as no
surprise that it is not consistent with them. Many times theorists will
use a model, with known deficiencies, because they are interested in
different questions: perhaps we are only interested in the average
value, and what happens from that average value? In that case, it
doesn’t make a lot of sense to include complexities that will be
averaged out anyway when we want to answer our question.

To miss this point is to miss the entire process of comparing theory
with experiment. It turns out, however, in this case we can make a few
simple modifications to explore some of the temperature variation.

<span style="font-size:15pt;">**The Infinitely Slow Surface-Conduction
Model**</span>

We use the same assumptions as before, with one modification (in bold):

1.  that the conduction *within* the body **takes an infinite amount of
    time (i.e. no surface conduction at all)**. Thus, each patch of
    surface acts as its own independent object
2.  the body is not rotating, so the radiation it is receiving is
    constant
3.  there is no atmosphere, thus no conduction or convection outside of
    the solid body
4.  the albedo is the *average* albedo of the Moon, or a=0.14. Thus this
    object absorbs 86% of the radiation coming in

We consider two types of patches: one on the near side and one on the
far side.

**Near-side patch**

Imagine a patch of surface 1 square meter, with the same albedo as the
Moon (i.e. absorbing 86%), and a combined mass and specific heat
summarized by a constant K’. The energy equation then becomes

![PastedGraphic4-2011-07-28-05-45.jpg][]

at equilibrium we thus have

![PastedGraphic5-2011-07-28-05-45.jpg][]

![PastedGraphic6-2011-07-28-05-45.jpg][]

which again, is reasonably close to the real value. Notice that all we
had to do is change the conduction assumption to get surface temperature
variation. If you’re concerned that the maximum temperature predicted is
lower than the observed, notice that I am using the *average* albedo of
the Moon. There are parts of the Moon’s surface with a lower albedo, and
will thus get hotter as a result.

**Far-side patch**

Now imagine a patch of surface 1 square meter, with the same albedo as
the Moon (i.e. absorbing 86%), and a combined mass and specific heat
summarized by a constant K’ but with *no sunlight at all coming in*. The
energy equation then becomes

![PastedGraphic7-2011-07-28-05-45.jpg][]

The only equilibrium value for this is T=0. If no energy is coming in,
and we have energy going out, the object will keep cooling. So in this
model we have the near side T=380 K and the far side T=0 K, at
equilibrium.

Although the model is clearly wrong, it demonstrates one thing: you can
easily get temperatures above and below the average-model calculation
simply by having not all parts of the surface heated equally, and some
non-zero time of energy “communication” (i.e. surface conduction or, if
you have an atmosphere, conduction and convection with the atmosphere)
between the parts. The extreme version calculated here simply
demonstrates the effect and is not meant to be realistic.

<span style="font-size:15pt;">**Adding a Few More Complexities -
Qualitative Discussion**</span>

We now modify the assumptions as follows

1.  that the conduction *within* the body **takes a finite, non-zero,
    amount of time**
2.  the body **rotates once every 28 days, like the Moon**
3.  there is no atmosphere, thus no conduction or convection outside of
    the solid body
4.  the albedo is the *average* albedo of the Moon, or a=0.14. Thus this
    object absorbs 86% of the radiation coming in

Although one could set up a simple calculation, or numerical model, to
handle this case I am not going to go through the exercise. However,
there are two effects that will happen when adding these two changes:

1.  the maximum temperature predicted will be a bit lower than the
    no-conduction model. This is primarily because the moon rotates the
    near-side patch out of the the most direct sunlight relatively
    quickly. If the surface conduction is on the order of minutes, this
    will make little or no difference. If it is around hours to days
    then it will. In fact, one could use this difference to help
    determine the time constant (related to the constant K’) for the
    surface of the Moon
2.  the minimum temperature predicted will be higher than the T=0
    predicted from the no-conduction model. This is both because the
    moon rotates the far-side patch out of the dark, and that energy
    from the previously warmed surface will conduct to the far-side
    patch.

It is fairly straightforward to get a model that is nearly consistent
with the observed temperature range, and is consistent with the thermal
properties of the surface of the Moon. One can get even more careful by
modifying assumption (4), and use the local albedo of the various
patches. In addition, one would need to look at all patches on the
near-side, taking into account the varying angle of inclination of the
radiation. This will not modify the qualitative results.

<span style="font-size:15pt;">**Conclusions**</span>

This all started when I criticized someone’s commentary on climate
models, where they claimed that the models exclude thermal conduction
and convection, and thus the focus on greenhouse gasses was entirely
inappropriate. A further comment claimed that these models put an
explicit maximum temperature achievable when they calculate the surface
temperature of an object from blackbody equations. The comment further
criticized my use of the *average model* summary for the Earth for this
reason.

Notice the procedure we employed to model the system, and address these
concerns. We started with a very simple globally averaged model, and got
an interesting temperature value similar to the data. We then added a
few complexities, such a differential heating, and noticed how this
gives a range of temperatures on the surface. We also noticed that the
range was half right (half wrong?): the maximum was good, but the
minimum was terrible. Adding rotation and non-zero conduction time gives
some dynamics and can achieve reasonably close agreement. A more
detailed implementation of the local albedo fixes the small errors,
especially on the top end. By using this procedure, we can see exactly
which parts of our model give which parts of the result. It also shows
which parts of the model give the biggest effect, and which are there
for small adjustments.

All that is needed to go beyond the average model, and achieve
temperature well above the average, is to include differential heating
of the surface and some non-zero time of energy “communication”. Once
you heat different parts in different ways, and add rotations and
time-delays of conductions, you get some interesting dynamics *around
the average*, going both above and below the average. The average
calculation is still useful, if you’re not interested in short-term
dynamics. It is further useful as a pedagogical tool, because it is a
lot simpler. Thus it is not “ludicrous” to use the diagram from Kiehl
and Trenberth, as long as one is aware that this is a *globally averaged
model*. If you attempt to infer things well beyond the point of the
model, then do not criticize the model - criticize your comparison, and
look for a more detailed model that addresses the questions that you’re
interested in.

<div class="blogger-post-footer">
!<>

</div>

  [prior post]: http://bblais.blogspot.com/2010/02/not-so-hidden-flaw-in-this-climate.html
  [Untitled-2011-07-28-05-45.png]: http://lh3.ggpht.com/-vYTzgPcRcyo/TjHqHeo8lTI/AAAAAAAAJWk/YWfC7X_Xmuc/Untitled-2011-07-28-05-45.png
  [PastedGraphic-2011-07-28-05-45.jpg]: http://lh5.ggpht.com/-DFpwP3AbRBY/TjHqHva9NgI/AAAAAAAAJWo/9WZzozkdfrI/PastedGraphic-2011-07-28-05-45.jpg
  [PastedGraphic1-2011-07-28-05-45.jpg]: http://lh5.ggpht.com/-SouO2yBsJMI/TjHqHr0RCiI/AAAAAAAAJWs/Wan5GRey3ik/PastedGraphic1-2011-07-28-05-45.jpg
  [PastedGraphic2-2011-07-28-05-45.jpg]: http://lh4.ggpht.com/-gL6eKMccMXk/TjHqH95v6YI/AAAAAAAAJWw/mFUatrZWc3g/PastedGraphic2-2011-07-28-05-45.jpg
  [PastedGraphic3-2011-07-28-05-45.jpg]: http://lh4.ggpht.com/-Ploy44ZPyrw/TjHqIBOaI0I/AAAAAAAAJW0/orpTzEhRZmM/PastedGraphic3-2011-07-28-05-45.jpg
  [PastedGraphic4-2011-07-28-05-45.jpg]: http://lh4.ggpht.com/-ETELFjeOiIc/TjHqIUstGGI/AAAAAAAAJW4/cee8InVHVaw/PastedGraphic4-2011-07-28-05-45.jpg
  [PastedGraphic5-2011-07-28-05-45.jpg]: http://lh6.ggpht.com/-msH1r34w0D0/TjHqIpGWduI/AAAAAAAAJW8/JjfihtD0trA/PastedGraphic5-2011-07-28-05-45.jpg
  [PastedGraphic6-2011-07-28-05-45.jpg]: http://lh5.ggpht.com/-jMOJzKfly3Q/TjHqIsVVMSI/AAAAAAAAJXA/bDAj3wEuM04/PastedGraphic6-2011-07-28-05-45.jpg
  [PastedGraphic7-2011-07-28-05-45.jpg]: http://lh4.ggpht.com/-_e7zevzi8B0/TjHqI63DYqI/AAAAAAAAJXE/8eisv6XbIZ0/PastedGraphic7-2011-07-28-05-45.jpg
