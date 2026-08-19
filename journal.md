# ML journal

## 2026-08-17 - S1
Toolchain up. Why I'm doing this: trying to learn how to be technical native. know the environment, all the different commands and what they say...
Confused by: I still don't get what uv even is. And what is toolchain?

## 2026-08-17 - S2
This was pretty easy... but I am not sure my flow for the fizzbuzz programs is the most elegant one. I hate cumbersome repeated if statementes where you ask the same thing over and over, tried to avoid it. Also wasn't sure when the instruction said "for every number from 1 to 50" if that meant to include 50 or not, I assumed it should be included. not sure I'll remember the :.2f formating - need to repeat to rememver. Also need to see if we can set claude to check and rate my code for these execrcises going forward....

## 2026-08-17 - S3
Still good. The docstring thing is new. Make sense but I am not sure what the name stands for... Lambda is still not trivial to impelement and understand. 

## 2026-08-18 - S4
This one was more difficult. a lot of new commands and syntax to remember...
What I struggled with the most was to try and find a shorthand writing for:
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
I didn't find one. tried:
word_count = {w : word_count.get(w, 0)+ 1 for w in words}
but it failed miserably - gave every word the count 1.....