import spacy
# spacy can compare doc, span and token objects, returns similarity score between 0 to 1
# ! it needs a model with word vectors included => usually _md (medium) or _lg (large)
nlp = spacy.load("en_core_web_md")

doc1 = nlp("I like fast food")
doc2 = nlp ("I like pizza and pasta")
span = doc2[2:5]
#docs
print(doc1.similarity(doc2))
#tokens
print(doc2[2].similarity(doc2[4]))
#span and doc
print(span.similarity(doc1))

#vectors:
doc = nlp("Two bananas in pyjamas")

# Get the vector for the token "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)
