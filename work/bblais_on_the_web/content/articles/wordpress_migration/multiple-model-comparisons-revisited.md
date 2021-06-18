Title: Multiple Model Comparisons Revisited
Date: 2010-09-25 17:51
Author: brianblais
Slug: multiple-model-comparisons-revisited

Introduction
------------

In a [previous post][], I hinted at how to do multiple hypotheses
testing, using the ψ-measure. It turns out to be much clearer just using
the posterior probabilities. The ψ-measure has a nice intuitive feel for
the two-hypothesis case, but becomes convoluted in the multiple
hyptheses case. Further, when introducing the application of Bayes
theorem for students, I have found it to be clearer to follow the
following procedure. We first look at Bayes theorem directly, for N
hypotheses:

﻿![NewImage.jpg][]

We then calculate the numerator only, for every possible hypothesis:

 

﻿![NewImage.jpg][1]

 

calculate the sum of all of these values,

![NewImage.jpg][2]

￼and then normalize

![NewImage.jpg][3]

﻿The Octopus, Again {style="font-size:1.5em;"}
-------------------

 

From the [Wikipedia article][], we have the following data:, which gave
us correct=12 out of N=14:

￼ ￼ ￼![NewImage.jpg][4]

![NewImage.jpg][5]

![NewImage.jpg][6]

The hypotheses that we consider are the following:

H = “Octopus is psychic, and can predict future (sports) events with 90%
accuracy” R = “Octopus makes random choices” Y = “chooses flags with big
yellow stripes 90% of the time” G = “chooses Germany 90% of the time”

Notice that both models Y and G, give us correct=12 for N=14 (if the
“choosing Germany” chooses Spain in the Netherlands match, because of
the similarity). The prior for the psychic octopus is, again, the very
generous p(H) = 1/100. The two other non-random models should be more
likely, before any data, so I take them to be p(Y)=p(G)=1/20. The random
model, being the most likely, has the rest of the prior probability,
p(R)=0.89.

Now we calculate the numerators:

﻿￼![NewImage.jpg][7]

Sum the values,

￼![NewImage.jpg][8]

and divide. achieving

￼![NewImage.jpg][9]

Thus, the two flag models went from being rare compared to random to
being much more likely than random, and certainly much more likely than
psychic. Bayes theorem, properly applied, is a quantitative embodiment
of Carl Sagan’s famous quote “extraordinary claims require extraordinary
evidence”. It is not just that the evidence must be extraordinary (like
999 correct out of 1000), but the evidence must be extraordinary to
address all of the, somewhat rare but possible, hypotheses that would
come up as much more likely given the initial result. The process of
science is to perform experiments to address these alternative
hypotheses.

<div class="blogger-post-footer">
!<>

</div>

  [previous post]: http://bblais.blogspot.com/2010/08/non-psychic-octopus.html
  [NewImage.jpg]: http://lh5.ggpht.com/_VLTJPGH7Stw/TJ5YNmoEK4I/AAAAAAAAHfo/gKieBjr683c/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [1]: http://lh5.ggpht.com/_VLTJPGH7Stw/TJ5YOPUek-I/AAAAAAAAHfs/wSasTJWi2Bg/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [2]: http://lh3.ggpht.com/_VLTJPGH7Stw/TJ5YOoIiclI/AAAAAAAAHfw/HQG0j1F485s/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [3]: http://lh6.ggpht.com/_VLTJPGH7Stw/TJ5YPYViTVI/AAAAAAAAHf0/6nw8HOnTST0/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [Wikipedia article]: http://en.wikipedia.org/wiki/Paul_the_Octopus
  [4]: http://lh4.ggpht.com/_VLTJPGH7Stw/TJ6HJQDMLoI/AAAAAAAAHgU/7s7pJo6yOLM/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [5]: http://lh4.ggpht.com/_VLTJPGH7Stw/TJ6HKXtkmxI/AAAAAAAAHgY/eUYF0y0zaPg/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [6]: http://lh3.ggpht.com/_VLTJPGH7Stw/TJ6HK6T5AAI/AAAAAAAAHgc/IL4X8FZuPME/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [7]: http://lh6.ggpht.com/_VLTJPGH7Stw/TJ6IJdKKCZI/AAAAAAAAHgo/SByKieJwf64/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [8]: http://lh6.ggpht.com/_VLTJPGH7Stw/TJ6IKDPTUxI/AAAAAAAAHgs/_waIBc1-gQQ/NewImage.jpg?imgmax=800
    "NewImage.jpg"
  [9]: http://lh5.ggpht.com/_VLTJPGH7Stw/TJ6IKtoEjnI/AAAAAAAAHgw/DACIjf9GoiI/NewImage.jpg?imgmax=800
    "NewImage.jpg"
