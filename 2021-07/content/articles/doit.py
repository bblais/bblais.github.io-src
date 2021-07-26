import os,sys

fnames="""back.md
bayes_god.md
best_test.md
bias_probability.md
chicken_egg.md
deflate_football.md
demo_vs_experiment.md
evidence_philosophical.md
football_physics.md
hume_miracles.md
latex_vs_word.md
longest_night.md
morality_evolution.md
neil_on_interstellar.md
not_a_denier.md
obj_morality_reduc.md
on_pluto.md
priors_vs_likelihood.md
python_language.md
reductionism_art_neuroscience.md
simple_questions.md
supernatural_dark_matter.md
unanswerable.md
presentations/what_is_science.md
Unbelievable Project/[0024] Unbelievable? 24 Nov 2007 - The atheist who sold his soul on ebay - 24 November 2007.md
Unbelievable Project/[0028] Unbelievable? 22 Dec 2007 - Did Christians steal Christmas? - 22 December 2007.md
Unbelievable Project/[0033] Unbelievable? 26 Jan 2008 Morality - do we need God to be Good? - 26 January 2008.md
Unbelievable Project/[0034] Unbelievable? 2 Feb 2008 Positive atheism? - 02 February 2008.md
Unbelievable Project/[0036] Unbelievable? 16 Feb 2008 Noah and the Flood - did it happen? - 16 February 2008.md
Unbelievable Project/[0043] Unbelievable? 5 Apr 2008 12 Apr 2008 "Why I became an atheist" Part 1 and Part 2 - John Loftus & Peter May - 05 April 2008.md
Unbelievable Project/[0274] Did Jesus Exist? Bart Ehrman Q&A - Unbelievable? - 18 August 2012.md
Unbelievable Project/[0308] How did life begin? Adam Rutherford & Fuz Rana - Unbelievable? - 09 April 2013.md
Unbelievable Project/faith_and_trust.md
Unbelievable Project/faith_empirical.md
Unbelievable Project/probability_theism_vs_atheism.md
Unbelievable Project/sun_rise_tomorrow.md"""

for fname in fnames.split("\n"):
    if not fname:
        continue

    cmd="./datestamp.py '%s'" % fname
    print(cmd)
    os.system(cmd)

