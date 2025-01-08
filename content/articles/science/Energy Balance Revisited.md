Title: Energy Balance Revisited
Date: 2024-11-04
status: published
image: photoholgic-kKWcOwioewA-unsplash.jpg

Going back a few years I published an article simplifying the calculations for atmospheric greenhouse gas effects for undergraduate non-science majors,

> [Blais, B. (2003). Teaching energy balance using round numbers. _Physics education_, _38_(6), 519.](https://iopscience.iop.org/article/10.1088/0031-9120/38/6/004/meta)

I recently came across another article which does a similar thing, but using slightly different notation and terminology,

>[LoPresto, M. C. (2013). Adding albedo and atmospheres. _The Physics Teacher_, _51_(3), 152-153.](https://pubs.aip.org/aapt/pte/article/51/3/152/276578)

In the spirit of reproducibility I wanted to see if I could connect LoPresto's results with mine. 

## Round Number Method

In my method, the amount of energy entering the Earth system is the round number $S=100/r^2$ where $r$ is the distance from the sun in astronomical units (AU).  In these units, $r=1$ for the Earth.  The temperature of the surface, or any atmospheric layer, is related to the energy output of that layer, derived to be 
$$
\begin{equation}
\left(\frac{T}{88.5 \text{K}}\right)^4 = E
\end{equation}
$$
We look at a simple 1-layer model, where the short-wavelength albedo is $a$ and the atmosphere absorbs some fraction, $\gamma$, of the long-wavelength radiation.

![[Energy Balance.drawio.svg]]

we get energy balance equations of

$$
\begin{aligned}
+(1-a)\cdot S -E_s + E_1 &=0 \\
+\gamma E_s - E_1 - E_1 &=0
\end{aligned}
$$

which leads to solutions for the energy emitted from the surface and the layer 1, as well as the corresponding temperatures,

$$
\begin{aligned}
E_1&=\frac{\gamma S \cdot (1-a)}{2-\gamma} \\
E_s&=\frac{2E_1}{\gamma}=\frac{2 S \cdot (1-a)}{2-\gamma}\\
T_1&=88.5\text{ K}\cdot \left(\frac{\gamma S \cdot (1-a)}{2-\gamma}\right)^{1/4} \\
T_s&=88.5\text{ K}\cdot \left(\frac{2 S \cdot (1-a)}{2-\gamma}\right)^{1/4} = T_1 \cdot 2^{1/4}\cdot (2-\gamma)^{-1/4}
\end{aligned}
$$

We can check a few extreme cases, like $\gamma=0$ (no atmosphere),
$$
\begin{aligned}
E_1&=0 \\
E_s&=S \cdot (1-a) \\
T_s&=88.5\text{ K}\cdot \left(S \cdot (1-a)\right)^{1/4}
\end{aligned}
$$
and an infrared-opaque atmosphere, $\gamma=1$,

$$
\begin{aligned}
E_1&=S \cdot (1-a) \\
E_s&=2 S \cdot (1-a)\\
T_1&=88.5\text{ K}\cdot \left(S \cdot (1-a)\right)^{1/4} \\
T_s&=88.5\text{ K}\cdot \left(2S \cdot (1-a)\right)^{1/4} \\
\end{aligned}
$$
Using the numbers from [LoPresto, M. C. (2013)](https://pubs.aip.org/aapt/pte/article/51/3/152/276578), where the albedo ($a$) is measured but the long-wavelength radiation fraction of absorption ($\gamma$) is inferred^[LoPresto uses values for the properties of the atmosphere in their table, but admits there is a lot of variation.  I prefer to infer the values from the temperatures, and discuss whether it makes sense.], we get

|         |   Albedo |   T Obs. [K] |   Distance from Sun [AU] |   T (no atm) [K] |   T (γ=0.3) [K] |   γ (best fit) |
|:--------|---------:|-------------:|-------------------------:|-----------------:|----------------:|---------------:|
| Mercury |    0.119 |          400 |                     0.39 |            434.2 |           452.2 |         -0.776 |
| Venus   |    0.75  |          737 |                     0.72 |            233.2 |           242.9 |          1.98  |
| Earth   |    0.306 |          288 |                     1    |            255.4 |           266   |          0.762 |
| Mars    |    0.25  |          225 |                     1.52 |            211.2 |           220   |          0.446 |
| Jupiter |    0.343 |          124 |                     5.2  |            110.5 |           115.1 |          0.739 |
| Saturn  |    0.342 |           97 |                     9.58 |             81.4 |            84.8 |          1.006 |
| Uranus  |    0.3   |           58 |                    19.22 |             58.4 |            60.8 |         -0.054 |
| Neptune |    0.29  |           59 |                    30.07 |             46.8 |            48.8 |          1.205 |

There are several things to note here.   If we interpret $\gamma$ as the fraction absorbed, both $\gamma<0$ and $\gamma>1$ are physically impossible.  The former indicates that there is no atmosphere and we must be within uncertainties in the albedo or observed temperature.  The latter is something we can address, by modifying the model.  This is done by deriving the equations used in  [LoPresto, M. C. (2013)](https://pubs.aip.org/aapt/pte/article/51/3/152/276578).

## Adding Albedo and Atmosphere

From the paper,

>[LoPresto, M. C. (2013). Adding albedo and atmospheres. _The Physics Teacher_, _51_(3), 152-153.](https://pubs.aip.org/aapt/pte/article/51/3/152/276578)

we are given the result from a multi-layer model atmosphere.  Their result for the case without an atmosphere is
$$
T_e=(1-a)^{1/4}\left(\frac{279}{r^{1/2}}\right)\text{ K}
$$
which we call $T_e$ for effective radiative temperature.^[LoPresto calls it simply $T$ which we find unclear.]. This is the same as our $\gamma=0$ case,
$$
\begin{aligned}
T_s&=88.5\text{ K}\cdot \left(S \cdot (1-a)\right)^{1/4}\\
T_s&=88.5\text{ K}\cdot \left(\frac{100}{r^2} \cdot (1-a)\right)^{1/4}\\
&=279\text{ K} \cdot \frac{1}{r^{1/2}}\cdot \left(1-a\right)^{1/4}
\end{aligned}
$$
They then include a greenhouse, and derive the temperature to be
$$
T_g = 2^{1/4}\cdot T_e
$$
which is equivalent to our case above with $\gamma=1$.  They then quote a result,
$$
T_g = (1+\tau)^{1/4}\cdot T_e
$$
without derivation, of which their previous result is a special case ($\tau=1$).  The value $\tau$ is called the "total extinction thickness" and is the number of layers that completely absorb infrared radiation (i.e. long wavelength).  So there must be some connection between my $\gamma$ and their $\tau$.  

## Deriving the total extinction thickness, $\tau$

To derive their result, we add more layers to the original model, and assume that every layer absorbs 100% of the radiation entering it from other layers.

![[Energy Balance2.drawio.svg]]

The energy balance equations for $n$ such layers is,

$$
\begin{aligned}
+(1-a)\cdot S -E_s + E_1 &=0 \\
+E_s - E_1 - E_1 + E_2&=0 \\
+E_1 - E_2 - E_2 + E_3&=0 \\
&\vdots\\
+E_{n-3} - E_{n-2} - E_{n-2} + E_{n-1}&=0 \\
+E_{n-2} - E_{n-1} - E_{n-1} + E_n&=0 \\
+E_{n-1} - E_{n} - E_{n}&=0
\end{aligned}
$$
You can confirm that this works for the $n=3$ model shown.  Notice that there is an asymmetry in the equations, with the surface-layer and the top-layer equations a little different from the others.

Solving from the top layer (last equation) down to the surface we get
$$
\begin{aligned}
E_{n-1}&=2E_n \\
E_{n-2}&=2E_{n-1}-E_n = 3E_n \\
E_{n-3}&=2E_{n-2}-E_{n-1} = 4E_n \\
&\vdots\\
E_{2}&=(1+n-2)\cdot E_n\\
E_{1}&=(1+n-1)\cdot E_n\\
E_{s}&=(1+n)\cdot E_n
\end{aligned}
$$
From the first balance equation we 
$$
\begin{aligned}
+(1-a)\cdot S -E_s + E_1 &=0 \\
(1-a)\cdot S - (1+n)\cdot E_n + (1+n-1)\cdot E_n&=0 \\
(1-a)\cdot S-E_n&=0 \\
E_n&=(1-a)\cdot S
\end{aligned}
$$

Our final result for the energy output of the surface in the multi-layer model is,

$$
\begin{aligned}
E_{s}&=(1+n)\cdot (1-a)\cdot S \\
T_s &=88.5 \text{ K}\cdot (1+n)^{1/4}\cdot \left((1-a)\cdot S\right)^{1/4} \\
&=(1+n)^{1/4} \cdot T_e \\
&=(1+\tau)^{1/4} \cdot T_e \\
\end{aligned}
$$
Where the last step is the result from LoPresto, where it is clear that the number of layers, $n$, is equivalent to their "total extinction thickness", $\tau$.  

## Connecting our $\gamma$ to LoPresto's $\tau$

Connecting my $\gamma$ to LoPresto's $\tau$ we get

$$
\frac{2}{2-\gamma}=1+\tau
$$
or 
$$
\gamma=\frac{2\tau}{1+\tau}
$$
We can then reproduce the table above

|         | Albedo | T Obs. [K] | Distance from Sun [AU] | T (no atm) [K] | γ (best fit) | τ (best fit) | T (best fit) |
| :------ | -----: | ---------: | ---------------------: | -------------: | -----------: | -----------: | -----------: |
| Mercury |  0.119 |        400 |                   0.39 |          434.2 |       -0.776 |        -0.28 |          400 |
| Venus   |   0.75 |        737 |                   0.72 |          233.2 |         1.98 |       98.729 |        736.9 |
| Earth   |  0.306 |        288 |                      1 |          255.4 |        0.762 |        0.616 |          288 |
| Mars    |   0.25 |        225 |                   1.52 |          211.2 |        0.446 |        0.287 |          225 |
| Jupiter |  0.343 |        124 |                    5.2 |          110.5 |        0.739 |        0.586 |          124 |
| Saturn  |  0.342 |         97 |                   9.58 |           81.4 |        1.006 |        1.013 |           97 |
| Uranus  |    0.3 |         58 |                  19.22 |           58.4 |       -0.054 |       -0.026 |           58 |
| Neptune |   0.29 |         59 |                  30.07 |           46.8 |        1.205 |        1.516 |         58.9 |

The interpretation of, say, Venus's $\tau=98$ (100 effective layers!) is much easier using this result rather than the physically unreasonable $\gamma=1.98$.  In teaching this concept to students again, I may sketch the derivation, and then quote the result:

$$
\begin{aligned}
E_{s}&=(1+n)\cdot (1-a)\cdot S
\end{aligned}
$$
which has a reasonably intuitive simple form.  I imagine there may be other useful comparisons to make.

