import spacy
from spacy.lang.en import English
nlp = English()

# create doc manually:
from spacy.tokens import Doc

words = ["Hello", "world", "!"]
spaces = [ True, False, False]
#don't forget to also pass in the shared vocab
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# manually creating span
from spacy.tokens import Span
span = Span(doc, 0, 2)
span_w_label = Span(doc, 0, 2, label="GREETING")
#add to doc entities
doc.ents = [span_w_label]
print([(ent.text, ent.label_) for ent in doc.ents])

#Always convert results to strings as late as possible, information will be lost

# style:
doc2 = nlp("Berlin looks like a nice city")

# Get all tokens and part-of-speech tags
token_texts = [token.text for token in doc2]
pos_tags = [token.pos_ for token in doc2]

for index, pos in enumerate(pos_tags):
    # Check if the current token is a proper noun
    if pos == "PROPN":
        # Check if the next token is a verb
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)