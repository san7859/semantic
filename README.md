# semantic
This is for tasks in T38 consisting of semantic.py and watch_next.py 


semantic.py includes

● a note about what I found interesting about the similarities
between cat, monkey and banana and an example of my own.

● Comment on the difference between the simpler language model ‘en_core_web_sm’
and the model 'en_core_web_md'.



watch_next.py

● consists of a system that will tell you what to watch next based on the word
vector similarity of the description of movies.

● Read in the movies.txt file. Each separate line is a description of a different
movie.
● Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
● The function should take in the description as a parameter and return the
title of the most similar movie
