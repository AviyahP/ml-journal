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
This:
print(f"{i}: The word {top10[i][0]} appears {top10[i][1]} times.") for i in range(10)
also failed miserably. there is something I dont get. 

## 2026-08-19 - S5
1 - what is a vector?
a vector has multiple definitions that all work together - in geometry it is an arrow with direction and size starting at the origin. in computer science it can be represented by an ordered array of numbers (the coordinates). in mathematics the things that define a vector is that it can be added with other vertors and multiplied by scalars (??)
2 - what is span, and what does it mean for a vector to be "wasted"?
A span is the collection of all vectors that can be described as a linear combination (addtion of scalar multiplication) of the basis vectors. two non linearly dependent vectors span THE 2D plane if they are 2D vectors, A plane in 3D if they are 3D vectors. 3 2D vectors are for sure a redundant basis - at least one can be described as a lineaer combination of the others. 3 non linearly dependent 3D vectors span the 3D space. a wasted vector - a vector that is linearly dependent on the other vectors in the basis therefor does not expand the span. 
3 - what is still fuzzy - I must say that it is hard for my to visualize and grasp how any two 2D non lineraly dependetn vector span the entire plane. I can calcular what the scalars need be algerbraically but I have trouble grasping it geometrically especially if they are non perperdicular. Same thing when we move to 3D - hard for me to understand why two independent vectors will draw one plane and not another. whould love to reach a level where all these concepts sit intuitively in my head and I REALLY understand them and never forget again.... 

## 2026-08-19 - S6
Doing wordfreq2 was brutal.
Did not remember the "with open()" syntax properly. precisely that you should write "as f:" and that to read you do in indentation f.read(). 
took me time to realize that lower and strip won't work on the list
did not remember the syntax (remembers pieces of it, not enough to write it properly) for the sorting (key, reverse=True etc).
You had a nice clever way to unpack the loop variable for the final printing - didnt remember it and did it in a cumersome way. 
did not remember the whole store the punctiation string into PUNCT. 

