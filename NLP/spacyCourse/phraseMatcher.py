import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_md')

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", None, pattern)
doc = nlp("I have a Golden Retriever")

#matches = matcher(doc)
for match_id, start, end in matcher(doc):
    #get matched span
    span = doc[start:end]
    print("Matched span: ", span.text)