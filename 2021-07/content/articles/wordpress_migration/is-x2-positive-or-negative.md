Title: Is -x^2 positive or negative?
Date: 2010-11-22 01:29
Author: brianblais
Slug: is-x2-positive-or-negative

So, is -x^2^ a positive, negative, or undefined quantity for real-valued
x?  Ask any physicist or mathematician and they will say that it is a
negative number for real valued x making things like: exp(-x^2^) between
0 and 1.  That is why it came as a **BIG** surprise to me that computer
scientists don't think that, and a program like Excel will interpret:

=-5\^2

as ***positive*** 25!  After taking quite a while debugging a student
problem calculating the normal distribution in Excel, it got me on a
quest (and an argument with a colleague) to figure out who else thought
this way.  I checked Matlab, Mathematica, Python, and Google as well as
a calculator on the computer.  All interpreted -5\^2 (properly) as -25.
 To do otherwise, I believe, is perverse for any application that is
doing mathematical applications.  I was directed to [this page][], which
outlines many languages.  Pretty much just Excel, COBOL, Chipmunk BASIC
and a few small scripting languages take the "unary minus" approach,
which makes "unary minus" have precedence over exponentiation.

I am not sure why anyone would consider this a good idea, for working
with actual math equations.  Of course one could add parentheses, but
which is clearer:

y=exp(-x\^2)

or

y=exp(-(x\^2))

The second is obviously not ambiguous, but less clear.  Anyway, that is
the entire reason why we have order of operations, so we don't have to
do:

5+(3\*4)-(2\*3)+(2\*(3\^3))

So, Excel, come into at least the 20th century and figure out that
exponentiation trumps "minus", whatever you want to call it.

 

<div class="blogger-post-footer">
![]

</div>

  [this page]: http://www.macnauchtan.com/pub/precedence.html
  []: https://blogger.googleusercontent.com/tracker/6965073194684424505-3329800788246678449?l=bblais.blogspot.com
