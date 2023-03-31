import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.

'''
It is interesting to see that spaCy thinks that a monkey is more related to a banana than a cat because both monkey and cat are animals
and banana is a type of food that monkey is seen eating in cartoons and photos, while most cats do not eat bananas.

Other example as follows: 
'''

tokens = nlp('elephant horse desert')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
It is interesting to see spaCy finds slightly more similarities between elephant and desert than horse and desert.  The most famous
type of elephants are african elephants and with the common misconception of Africa is mostly covered in desert, which I only found
out is not really true.  There are also the asian elephant in South East Asia but when people think about elephants, they think of Africa.
With horses, Arabian horses came to mind personally, from sub saharan / desert countries but there are also other horses in different continents.
'''


# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is 
# different from the model 'en_core_web_md'.

'''
The following shows up after running on en_core_web_sm:

UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, 
which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, 
or use one of the larger models instead if available.
  print(token.similarity(token_))

The difference between the models is in the accuracy of predictions and en_core_web_md (medium) is better than en_core_web_sm (small) hence the warning

'''