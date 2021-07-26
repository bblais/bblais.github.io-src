Title: Coin flips and names (Evil problems in probability continued)
Date: 2010-02-22 12:22
Author: brianblais
Slug: coin-flips-and-names-evil-problems-in-probability-continued

In my [post about the girl-named-Florida problem][], there is a factor
in the analysis looking at the probability of having a girl named
Florida given that you have two girls: *P(F|2g)*.

This term is easily calculated as

<div style="text-align:center;">
![97AB81E4-08B6-4C53-8129-5432094EE211.jpg][]

</div>

which I used in the analysis.

Someone raised the question, "What would happen if (as we know) people
don't tend to name two children the same (unless you're George
Foreman)?" At first, this seems exactly like a coin flip problem: what
is the probability of, in two coin flips, flipping heads on the first
flip or flipping heads on the second but not both? It turns out that
this is a different problem, and the result is surprising (at least to
me). We have to be very careful what information we condition on,
knowing that the English language is a little more fluid than we like
when dealing with such problems. In the coin flip case we define

<div style="text-align:center;">
![5AA78167-FEF6-4DBE-BA47-8CE19D8CC0F4.jpg][]

</div>
:

and it follows, given the probability of flipping heads is *h*,

<div style="text-align:center;">
![B305BC0D-48EB-4BCB-929F-0C7BE8F53B21.jpg][]

</div>
</p>
which is just the standard result, subtracting off the possibility of
having both heads. For h=0.5, this yields the standard result of P(h) =
0.5. As h gets close to 1, the probability of a heads goes way up, and
thus the *probability of both being heads goes way up*. As a result, the
probability of just having 1 heads goes to zero.

The situation with names is nearly the opposite: as the frequency of a
name increases, the name is much more common. This makes it more and
more likely that you will have someone with that name. The difference is
in the conditioning information:

<div style="text-align:center;">
![EBA08560-A8CA-4B0A-94FB-3279139A9848.jpg][]

</div>

The analysis then goes:

<div style="text-align:center;">
![B10C9CE9-BECE-42D9-A17E-5214D5134406.jpg][]

</div>

which is exactly the same result as the case where one can name both of
the children Florida! I was a little surprised by this result, but a
quick simulation confirmed it as well.

### Simulation

    from pylab import *from numpy import *f=0.1N=10000r1=rand(N)r2=rand(N)N1=list(r1&lt f)N2=list(r2&lt f)case1=[n1 or n2 for n1,n2 in zip(N1,N2)]print "Fraction allowing duplicate names: ",case1.count(True)/float(len(case1))print "Theoretical Value: ",f+f-f**2nn=[]for n1,n2 in zip(N1,N2):    if n1:        nn.append(False)    else:        nn.append(n2)        N2=nncase2=[n1 or n2 for n1,n2 in zip(N1,N2)]print "Fraction not allowing duplicate names: ",case2.count(True)/float(len(case2))

### Simulation Result

Fraction allowing duplicate names: 0.1853  
Theoretical Value: 0.19  
Fraction not allowing duplicate names: 0.1853

<div class="blogger-post-footer">
!<>

</div>

  [post about the girl-named-Florida problem]: http://bblais.blogspot.com/2010/01/there-once-was-girl-named-florida-aka.html
  [97AB81E4-08B6-4C53-8129-5432094EE211.jpg]: http://lh3.ggpht.com/_VLTJPGH7Stw/S4Jx1rj-4wI/AAAAAAAAGN4/u4sMDWEq0y4/97AB81E4-08B6-4C53-8129-5432094EE211.jpg?imgmax=800
  [5AA78167-FEF6-4DBE-BA47-8CE19D8CC0F4.jpg]: http://lh4.ggpht.com/_VLTJPGH7Stw/S4JzKq7joYI/AAAAAAAAGOA/fyAfRau4UrA/5AA78167-FEF6-4DBE-BA47-8CE19D8CC0F4.jpg?imgmax=800
  [B305BC0D-48EB-4BCB-929F-0C7BE8F53B21.jpg]: http://lh6.ggpht.com/_VLTJPGH7Stw/S4J0OmC1EPI/AAAAAAAAGOI/8w2ZdwcWgn4/B305BC0D-48EB-4BCB-929F-0C7BE8F53B21.jpg?imgmax=800
  [EBA08560-A8CA-4B0A-94FB-3279139A9848.jpg]: http://lh5.ggpht.com/_VLTJPGH7Stw/S4J1sa1NCyI/AAAAAAAAGOQ/_WB3zDnMoss/EBA08560-A8CA-4B0A-94FB-3279139A9848.jpg?imgmax=800
  [B10C9CE9-BECE-42D9-A17E-5214D5134406.jpg]: http://lh4.ggpht.com/_VLTJPGH7Stw/S4J2p2E6wmI/AAAAAAAAGOY/QVCf0OBV6CA/B10C9CE9-BECE-42D9-A17E-5214D5134406.jpg?imgmax=800
