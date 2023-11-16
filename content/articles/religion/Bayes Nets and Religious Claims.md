Title: Bayes Can Also Be Used to Obscure a Topic
status: draft
image: david-clode-wygfGUqOmqs-unsplash.jpg


I was recently made aware of a series on Christian apologetics by [author Nick Meader](https://medium.com/@nick-meader) which uses Bayes Nets to explore the probabilities of the claims.  Two of the articles in these series give a good picture of his approach.  

- [How Likely is it that Jesus is the Messiah (Part IV)?](https://medium.com/interfaith-now/how-likely-is-it-that-jesus-is-the-messiah-part-iv-9a8bc820c801)
- [Does Evidence for Jesus’ Resurrection Meet Hume’s Criteria for Miracles?](https://medium.com/interfaith-now/does-evidence-for-jesus-resurrection-meet-hume-s-criteria-for-miracles-b23b069dd2e7)

My first approach with such work is to reproduce it quantitatively, so that I can be sure I understand the claims being made and how the analysis is done.  Personally, I find I don't understand an analytic approach unless I can reproduce it in detail.  In Meader's work, he uses a package called [Genie](https://www.bayesfusion.com/genie/) for doing his Bayes Nets.  I'm more of an open-source proponent, so I used [my own bayes_net package](https://github.com/bblais/bayes_net) but also reproduced it in [another package](https://github.com/MaxHalford/sorobn)  just to be sure my code didn't have errors.  You can see my code for the [first article here](https://github.com/bblais/bayes_net/blob/main/examples/2023-01-15%20-%20Bayes%20Nets%20and%20Religion.ipynb) and for the [second article here](https://github.com/bblais/bayes_net/blob/main/examples/2023-04-16%20-%20Bayes%20Nets%20and%20Hume%20and%20Resurrection.ipynb).  In going through this work, I made several observations.

### The notation is sloppy

Sometimes the post refers to a prior as $P(T)$ and sometimes as $P(M|K)$, where $K$ is background knowledge.  This should be $P(T|K)$ with the "$|K$" through the entire analysis (as [ET Jaynes](https://bayes.wustl.edu/etj/node1.html) does).  If you want to be lazy (as I usually do 😀) then drop it everywhere and have $P(M)$ as your prior.  

###  The probability values are not well laid out.  

Sometimes the probabilities are written as equations, and sometimes like "probability of a Messiah if God does not exist is 0".  This should have been written $P(M|\sim\! T)=0$.  The same with "the probability of theism updates from an agnostic prior (50%) to near certainty that theism is true (96%)", where a simple $P(T|E)=0.96$ would have shown explicitly what was being calculated. As such it is hard to read, and you have to hunt and peck for the values being used, especially given that the code is not provided.  For completeness I put the entire Bayes Net structure and probabilities for both papers below, making it easier to obtain all of the values for replication on whatever platform you'd like.


### The probability structure is simplistic in the extreme.  

This is where the content really lies, and shows that the entire approach seems to both bake in the solution the author wants and at the same time obscure it for others, making it sound far fancier than it really is.  



### Bayes Net for the Messiah Post

- [How Likely is it that Jesus is the Messiah (Part IV)?](https://medium.com/interfaith-now/how-likely-is-it-that-jesus-is-the-messiah-part-iv-9a8bc820c801)

	P(Theism,Messiah,Evidence)=P(Theism)P(Messiah|Theism)P(Evidence|Messiah)
	
	P(Theism):
	
	  Theism       p      
	  ======       =      
	   True     0.500000  
	  False     0.500000  
	============
	
	P(Messiah|Theism):
	
	  Theism    Messiah       p      
	  ======    =======       =      
	   True       True     0.250000  
	   True      False     0.750000  
	  False       True     0.000000  
	  False      False     1.000000  
	============
	
	P(Evidence|Messiah):
	
	 Messiah    Evidence      p      
	 =======    ========      =      
	   True       True     0.100000  
	   True      False     0.900000  
	  False       True     0.001000  
	  False      False     0.999000  
	============

### Bayes Net for the Resurrection Post

- [Does Evidence for Jesus’ Resurrection Meet Hume’s Criteria for Miracles?](https://medium.com/interfaith-now/does-evidence-for-jesus-resurrection-meet-hume-s-criteria-for-miracles-b23b069dd2e7)

	`P(Theism,Messiah,Resurrection,EvidenceM,EvidenceR)=P(Theism)P(Messiah|Theism)P(Resurrection|Messiah)P(EvidenceM|Messiah)P(EvidenceR|Resurrection)
	
	P(Theism):
	
	  Theism       p      
	  ======       =      
	   True     0.500000  
	  False     0.500000  
	============
	
	P(Messiah|Theism):
	
	  Theism    Messiah       p      
	  ======    =======       =      
	   True       True     0.250000  
	   True      False     0.750000  
	  False       True     0.000000  
	  False      False     1.000000  
	============
	
	P(Resurrection|Messiah):
	
	 Messiah   Resurrection     p      
	 =======   ============     =      
	   True       True     0.250000  
	   True      False     0.750000  
	  False       True     0.000000  
	  False      False     1.000000  
	============
	
	P(EvidenceM|Messiah):
	
	 Messiah   EvidenceM      p      
	 =======   =========      =      
	   True       True     0.100000  
	   True      False     0.900000  
	  False       True     0.001000  
	  False      False     0.999000  
	============
	
	P(EvidenceR|Resurrection):
	
	Resurrection EvidenceR      p      
	============ =========      =      
	   True       True     0.100000  
	   True      False     0.900000  
	  False       True     0.001000  
	  False      False     0.999000  
	============


