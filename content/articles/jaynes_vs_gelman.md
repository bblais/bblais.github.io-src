title: Jaynes vs Gelman
subtitle: Bayes for Messy Data
date: Nov 24 2016
image: landscape-54998_640.jpg

I copied a [comment on my old site](https://brianblais.wordpress.com/2016/08/20/is-science-a-self-sealing-process/#comment-1306), and am replying to it here.  It is a *fantastically interesting question*, which I have been enjoying thinking about.

It refers to [a critique of E. T. Jaynes by Andrew Gelman](http://www.stat.columbia.edu/~gelman/research/published/philosophy.pdf) which I comment on below.  


>I’m working through a hard copy of your book and I stumbled upon Gelman’s criticism that Jayne’s for more messy datasets (people vs physics) without objective parameters might not work well.
>
>Gelman seems to take issue with Jayne’s in that:
>
>1. The prior or model cannot be falsified and there isn’t enough model checking. He is more falsificationist
>2. Gelman has a more frequentist definition of probability
>3. Cannot change, adjust or add new priors.
>4. Often impossible to know true prior…then is it ok to have a subjective one?
>
>5. All models are wrong in social science, but some are less wrong or more useful, so important to cycle through models.
>
Jayne’s seems to be purist and justified, whereas gelman has pragmatic approach from practice and incorporation of other philosophies.
>
Since you have cited Gelman’s book, what are your thoughts on these points? The practical implication is that I’m going to be analyzing social science data, and Gelman per those dimensions seems to make more sense, but Jayne’s is more philosophically grounded.
>
Is your book Pure Jayne’s or would it work for a social scientist? I’m particularly interested in the idea of subjective priors incorporating theory or other non statistical experiments like ABM, falsifying and cycling through models etc

I'm not sure Gelman is a frequentist, but he is definitely a pragmatist.  He's also working with messy data.  

Gelman seems to be against *model comparison*, admitting that all of the models are in fact wrong.  This reminds me of a comment Jaynes made that Ronald Fisher (the King of Frequentism) was motivated by the types of problems he was an expert in - genetics - where frequencies *were* the data, and populations actually existed.  Gelman prefers model *checking* because the models he considers cannot be derived from first-principles or come from estabished quantitative theories.  Compare this to Tom Loredo's paper [*From Laplace to Supernova SN 1987A: Bayesian Inference in Astrophysics*](http://bayes.wustl.edu/gregory/articles.pdf), an article that was formative for myself.  Loredo's model comparison example "Measuring a Weak Counting Signal" is an icon of what Gelman calls the, 

> view of Bayesian inference as inductive reasoning (what we call here ‘the usual story’)

In Loredo's case, there are a number of characteristics of the problems he's investigating which are fundamentally different than the problems Gelman faces.

1. There is a theoretical justification for the existence of, and the mathematical form of, the "background" effect
2. There is a theoretical justification for the existence of, and the mathematical form of, the "signal" he is working with
3. There is a reasonable justification for the prior probability
4. The result would probably not be very sensitive to the choice of prior
5. Many of the parameters estimated can be independently measured

These characteristics of the *problem* have profound effects on the *models* and the methods for verifying them.  In Gelman's case, with social science data, there are no theoretical models - he's interested only in establishing the existence of relationships.  The parameters cannot be independently verified, and there are no theoretical justifications for priors.  The social scientist must use qualitative correspondence with expert knowledge, knowing that it will be debatable.  The parameters estimated cannot be explored directly.  So, what is the social scientist to do?  Spin out consequences, and compare with observations, the "hypothetico-deductive Bayesian modelling process".

Gelman makes a big deal about induction.  Perhaps I am not understanding something, but I don't see the big deal.  Gelman says 

> The common core of various conceptions of induction is some form of inference
from particulars to the general – in the statistical context, presumably, inference from the observations $y$ to parameters $\theta$ describing the data-generating process. But if that
were all that was meant, then not only is ‘frequentist statistics a theory of inductive inference’ (Mayo & Cox, 2006), but the whole range of guess-and-test behaviors engaged in by animals (Holland, Holyoak, Nisbett, & Thagard, 1986), including those formalized in
the hypothetico-deductive method, are also inductive. Even the unpromising-sounding procedure, ‘pick a model at random and keep it until its accumulated error gets too big, then pick another model completely at random’, would qualify (and could work surprisingly well under some circumstances – cf. Ashby, 1960; Foster & Young, 2003). So would utterly irrational procedures (‘pick a new random ! when the sum of the least significant digits in $y$ is 13’). Clearly something more is required, or at least implied, by
those claiming that Bayesian updating is inductive.

Contrary to what Gelman is inferring here, I actually believe that the guess-and-test is in fact inductive, in addition to frequentism being inductive.  What's the "something more" that Bayesian updating has that the others don't?  It has a theoretical justification - any and all other methods that disagree with Bayesian conclusions must violate one of the listed "deciderata" of Jaynes.  This doesn't seem to me to be a controversial statement. There are many methods of induction, but only probability theory properly followed is optimal.  

Bayesian approaches can also be *deductive*, as Gelman prefers.  Deductive logic is a subset of probability theory, and that's all we're talking about here.  



As far as I can tell, Jaynes and Gelman are not really in disagreement.  







