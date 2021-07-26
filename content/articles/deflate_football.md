title: How to Deflate a Football Deflating Story
Date: 2015-01-23
subtitle: Why Science Should Trump Personal Opinion
image: football.jpg

So, it's all over the news, the [Patriots cheated] with deflating the football by 1-2 psi, and are [lying about not knowing anything about it].  There are even claims that there are [scientific reasons for this being an advantage].  What seems to be lacking at this point is:

1. any actual evidence of wrongdoing - no video, no eyewitnesses, nothing
2. any actual *data* concerning the footballs in question, i.e. their actual pressures at various times
3. any actual *data* concerning all of the footballs in the game, i.e. their actual pressures at various times

The only data we have is that the balls were measured later in the game, with an observed drop from the beginning of the game, and a possible way to benefit from that.  The first thing we have to ask is, are there any mundane explanations of this observation?  The second thing we have to ask is if there is a way to distinguish between the mundane explanations and the possible nefarious ones.  Let's tackle the first.  

## Can Temperature Change Account for the Data?  Yes!

When measuring the pressure in a football, we measure the *difference* between the pressure inside of the football and the atmospheric pressure.  Atmospheric pressure is about 14.7 psi, so when the reading of the football pressure is, say, 13 psi then the absolute pressure is 

\begin{equation}
14.7 \,{\rm psi} + 13 \,{\rm psi} = 27.7 \,{\rm psi}
\end{equation}

From the ideal gas law we also have the relationship between pressure and temperature,
\begin{eqnarray}
PV&=&nkT \\\\
P&\propto& T \\\\
\frac{P_1}{P_2}&=&\frac{T_1}{T_2}
\end{eqnarray}

So a change of temperature from 70 F (294 K) down to 40 F (278 K) leads to a drop in football pressure from 27.7 psi down to

\begin{eqnarray}
\frac{27.7\,{\rm psi}}{P_2}&=&\frac{294 K}{278 K}\\\\
P_2&=& 26.2 \,{\rm psi}
\end{eqnarray}

or a football pressure reading of

\begin{equation}
26.2 \,{\rm psi}- 14.7 \,{\rm psi} = 11.5 \,{\rm psi}
\end{equation}

Perfectly within the range of data that we have access to.  If the amount were much more (4 psi, for example) then we might get suspicious, but this does not seem to be the case.

## Well, that's nice in theory, but...

Sure, it seems to work in theory, but we should test it.  Well, [someone has].  He inflated two balls to 13 psi, one in the room and one in the refrigerator.  It went down to 11.7 psi.  He added that someone falling on the ball could also make the ball lose air.  Nice and tidy.  Hearing this, my mind was instantly made up - unless someone can provide actual evidence to the contrary.  Was the interviewer convinced?  Nope - 

> "Ok, disclaimer time.  Yes, the professor is a Patriots fan, and these sound like a lot of excuses to let the Patriots off the hook.  But he says that this is real scientific stuff."  

Yes, it is - and it's not rocket science either.  It's not *"excuses"*, it's the most plausible explanation until someone can actually provide evidence contrary to it.


## What do we do with mundane explanations?

Now that we have a mundane explanation, what do we do?  We need to require of any other explanation a much more rigourous and strong case - the evidence has to be much stronger than otherwise, because the mundane explanation has a very high prior probability.  Do we have that evidence?  Not that I've seen.  So, until someone shows me the video of a person letting out air from the football, or provides a credible witness, I'm chalking this one up to the typical hysteria Americans like in their news stories and go on with more important things.  Let's hope the NFL listens to the science, and does the same.



[lying about not knowing anything about it]: http://bleacherreport.com/articles/2339195-is-the-nfl-going-to-let-brady-and-belichick-play-it-for-a-fool
[Patriots cheated]: http://www.bostonglobe.com/sports/2015/01/20/nfl-says-patriots-used-under-inflated-footballs/7UlPZI3eotRTBadM89saeO/story.html
[scientific reasons for this being an advantage]:http://www.foxnews.com/science/2015/01/23/deflate-gate-science-underinflated-footballs/
[someone has]: http://www.wcsh6.com/story/news/local/2015/01/22/deflategate-patriots-football-pressure-inflated/22174475/
