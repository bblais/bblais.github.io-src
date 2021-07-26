Title: A teachable moment...lost
Date: 2010-01-07 19:47
Author: brianblais
Slug: a-teachable-moment-lost

So I just watched the Mythbusters episode where they recreate the bus
jump from the movie Speed. They do two things: a miniature version and
full-scale recreation. In their miniature version they scale down the
bus by a factor of 12, very carefully building the model bus as closely
as possible. Then they scale down the bridge by the same factor. They
then point out that they can't scale down gravity without going to the
moon. Technically, that would scale gravity by 1/6, not the required
1/12. You wouldn't even have to go nearly as far as the Moon to achieve
this. Since force gravity decreases as the square of the distance away
from the Earth (starting at 4000mi, the radius of the Earth), you would
only have to go up this high:

![7F25868D-9B38-47E5-904A-596DBCCE6242.jpg][]  

compared to the 240,000 mi, that's a real bargain! But this is about
10,000 mi above the Earth, whereas the Hubble is less than 600 mi above
the Earth, just to give some perspective.

So, without leaving the Earth, the NASA experts say that one can
compensate by going faster. Mythbusters [scrawls the analysis on the
side of the buss][] and says "basically, what these hieroglyphics mean
is to compensate for the physical impossibility of scaling gravity, the
speed of our 1/12 scale bus has to be just over 20 miles per hour". What
bothers me most about this is not that they don't really go through the
analysis, but that they refer to basic math as hieroglyphics and they
give no sense for **why** going a bit faster would compensate for
gravity. I am going to include the full analysis here, but below I will
also give a simpler explanation that they could have used, which only
includes a small amount of math that would have easily fit on the side
of the bus.

#### Analysis

Their analysis is equivalent to the following: the components of the
speed off of a ramped angle are

![9C04C024-2B71-4C35-9D45-12DD1CA648A6.jpg][]

and the *x* and *y* positions versus time are given by the standard
motion equations

![66BFBCE5-2574-4BB8-86F0-5D9DAC42F4E9.jpg][]  

Here is the critical step. We solve for time, *t*, and get rid of it in
the second equation. This way we have the shape of the entire trajectory
in space, without any dependance on time.

![E389C058-CB1F-4053-8BD4-CC077BA5F404.jpg][]

or:

![AC84A6F7-B5B8-4E18-8B38-988972FF279A.jpg][]

Now, what happens to this equation when we scale the distances down by a
certain amount?

![9C7D59E1-F0B8-4368-8B5A-317F7CB87CEE.jpg][]

which is *almost* the same, except for one factor of gamma over the
*v*^2^ term. Thus, if we replace the speed with

![AAECC237-7155-49A9-B8C3-66778D0955F2.jpg][]

the trajectory of the new version is identical to the old version. Now,
remember, that this doesn't include time: the scaled version, going a
faster, will reach the destination sooner.

#### A Clearer Way

I certainly wouldn't expect the television audience to follow that
analysis, although I wouldn't mind them showing it anyway (but more
explicitly). It's the sort of thing where many would ignore it, but the
ones who could understand it would get more out of the show. So let's
see if we can put it a bit more clearly. I'd start, first, by scaling
down the sizes by a factor of 16 not 12. That way I can take the square
root more easily. Then there'd be two more facts about gravity that I
would mention

1.  gravity doesn't affect motion horizontally
2.  vertically, if I throw something up at three times the speed, it
    will go up nine times the height (the square of the speed increase)

Scaling down just the size, but not the speed, by a factor of 16 would
decrease the time by the same factor of 16. If we scale the speed down
by a factor of 4, then three things happen: the height of the trajectory
reduces by 16 (item 2 above), the time of flight reduces by a factor of
4, and thus the horizontal distance covered (speed times time) is
reduced by a factor of 4x4=16. Notice that in doing so, the object
trajectory is scaled in both the vertical and horizontal directions by
16, which is the goal of the scaling.

I think that this is clearer than the way presented by Mythbusters, and
should have been covered in this way, or some similar way. It could have
have been a good teaching moment!

<div class="blogger-post-footer">
!<>

</div>

  [7F25868D-9B38-47E5-904A-596DBCCE6242.jpg]: http://lh4.ggpht.com/_VLTJPGH7Stw/S0Yv5WDsY3I/AAAAAAAAGEc/T7BuskACZ1s/7F25868D-9B38-47E5-904A-596DBCCE6242.jpg?imgmax=800
  [scrawls the analysis on the side of the buss]: http://www.youtube.com/watch?v=3All56NYdqI
  [9C04C024-2B71-4C35-9D45-12DD1CA648A6.jpg]: http://lh5.ggpht.com/_VLTJPGH7Stw/S0YxvGpWsRI/AAAAAAAAGEg/OIp1MHQivjg/9C04C024-2B71-4C35-9D45-12DD1CA648A6.jpg?imgmax=800
  [66BFBCE5-2574-4BB8-86F0-5D9DAC42F4E9.jpg]: http://lh5.ggpht.com/_VLTJPGH7Stw/S0YyMqywgYI/AAAAAAAAGEk/g15DfQWzwLs/66BFBCE5-2574-4BB8-86F0-5D9DAC42F4E9.jpg?imgmax=800
  [E389C058-CB1F-4053-8BD4-CC077BA5F404.jpg]: http://lh4.ggpht.com/_VLTJPGH7Stw/S0YzSkcnH7I/AAAAAAAAGEo/E3DauhFjYts/E389C058-CB1F-4053-8BD4-CC077BA5F404.jpg?imgmax=800
  [AC84A6F7-B5B8-4E18-8B38-988972FF279A.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/S0YzdCSM0TI/AAAAAAAAGEs/dVsAvPisvGg/AC84A6F7-B5B8-4E18-8B38-988972FF279A.jpg?imgmax=800
  [9C7D59E1-F0B8-4368-8B5A-317F7CB87CEE.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/S0Y0XAxIcKI/AAAAAAAAGEw/0xqHYgQa_ko/9C7D59E1-F0B8-4368-8B5A-317F7CB87CEE.jpg?imgmax=800
  [AAECC237-7155-49A9-B8C3-66778D0955F2.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/S0Y00Bzw7QI/AAAAAAAAGE0/nmmhbz3PBQU/AAECC237-7155-49A9-B8C3-66778D0955F2.jpg?imgmax=800
