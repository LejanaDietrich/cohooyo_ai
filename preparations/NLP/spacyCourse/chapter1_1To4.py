#includes processing pipeline/ language-specific tokenization rules etc
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Created by processing a string of text with the nlp object
doc = nlp("Hello World!")

# iterate over tokens in a Doc
for token in doc:
    print(token.text)

# single one
token = doc[1]
print ("token 1: " + token.text)

# a slice from the doc consisting of several tokens 
# (slice notation is universal in py)
span = doc[1:3]
print("span 1-3: " + span.text)

#Lexical attributes:
doc2 = nlp("It costs $5.")
print("Index:   ", [token.i for token in doc2])
print("Text:   ", [token.text for token in doc2])

print("is_alpha:    ", [token.is_alpha for token in doc2])
print("is_punct:    ", [token.is_punct for token in doc2])
print("like_num:    ", [token.like_num for token in doc2])

doc3 = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Iterate over the tokens in the doc
for token in doc3:
    # Check if the token resembles a number
    if token.like_num:
        # Get the next token in the document
        next_token = doc3[token.i + 1]
        # Check if the next token's text equals "%"
        if next_token.text == "%":
            print("Percentage found:", token.text)

