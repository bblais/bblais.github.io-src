title: Gravitational Attraction
date: 04/09/2021
tags: science
status: published
popular: false
image: muzammil-soorma-R11bppS4q8o-unsplash.jpg

What would happen if two people out in space a few meters apart, abandoned by their spacecraft, decided to wait until gravity pulled them together?  My initial thought was that it would take a really long time, longer than they would practically be able to wait.  The calculation (unless I've done something wrong) seems to indicate otherwise.

<img src="{static}/images/two people.png" width=200 align=center>

My first approach, which is approximate, is to determine the resulting kinetic energy when they come together and assume (badly) that it was a constant acceleration to determine the time.  This will low-ball the time but be easy to calculate. My second approach is to numerically simulate the system in [pyndamics3](https://github.com/bblais/pyndamics3).  If I feel like it, I might do the integral later, but after the first approximation I like to look at things numerically (mostly for fun).

Let's make the following assumptions:

- $m_1$ = $m_2$ = 100 kg
- $r_{\rm start}=3 {\rm m}$
- $r_{\rm end}=0.5 {\rm m}$

then we set up the calculation

$$
\begin{aligned}
-G \frac{m_1 m_2}{r_{\rm start}}  + 0 &= -G \frac{m_1 m_2}{r_{\rm end}} + \frac{1}{2} m_1 v^2 + \frac{1}{2} m_2 v^2  \\
 \frac{1}{2} (100 {\rm kg}+100 {\rm kg}) v^2 &= -6.7\times 10^{-11} \left[\frac{{\rm J}{\rm m}}{{\rm kg}^2}\right]\frac{100 {\rm kg} \cdot 100 {\rm kg}}{3 {\rm m}} - \left( -6.7\times 10^{-11} \left[\frac{{\rm J}{\rm m}}{{\rm kg}^2}\right]\frac{100 {\rm kg} \cdot 100 {\rm kg}}{0.5 {\rm m}}\right)
\end{aligned}
$$
```python
In [7]: G=6.7e-11

In [8]: m1=100

In [9]: m2=100

In [10]: r_start=3

In [11]: r_end=0.5

In [12]: -G*m1*m2/r_start-(-G*m1*m2/r_end)
Out[12]: 1.1166666666666668e-06
```

$$
\begin{aligned}
\frac{1}{2} (100 {\rm kg}+100 {\rm kg}) v^2 &=& 1.12 \times 10^{-6} {\rm J} \\
v&=&1.1\times 10^{-4} {\rm m}/{\rm s} 
\end{aligned}
$$


```python
In [13]: v=sqrt(2*1.12e-6/(m1+m2))

In [14]: v
Out[14]: 0.00010583005244258362
```

Assuming a constant acceleration, for each person to travel half of the 2.5 m distance separation, would be

$$
\begin{aligned}
\frac{v_{\rm final}}{2} &=& \frac{2.5 {\rm m}}{t} \\
t&=& 45000 {\rm s} = 12 {\rm hr}
\end{aligned}
$$

which is much shorter time than I was expecting!  

Not being satisfied, I implemented it in [pyndamics3]

```python
from pyndamics3 import *
sim=Simulation()
sim.add("x1' = v1",-1.5,plot=True)
sim.add("x2' = v2",1.5,plot=True)
sim.add("v1' = G*m1*m2/(x2-x1)**2/m1",0,plot=True)
sim.add("v2' = -G*m1*m2/(x2-x1)**2/m2",0,plot=True)
sim.params(G=6.7e-11,m1=100,m2=100)

second=1
minute=60*second
hour=60*minute
day=24*hour
t=13*hour+25*minute
sim.run(t)
```

<img src="{static}/images/x1x2.png" width=600 align=center>

which clearly shows them coming together in around 1/2 of a day, from their own gravity.  I guess I have to adjust my intuitions for such situations.