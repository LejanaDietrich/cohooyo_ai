# making predictions in context, trained on large example datasets
# they can be updated to make better predictions, especially on own specific data
#the models are loaded without their training data
import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp("She ate the pizza.")

for token in doc:
    print(token.text, token.pos_)

doc2 = nlp("Apple is looking at buying U.K. startup for $1 billion")
# iterate over the predicted entities
for ent in doc2.ents:
    print(ent.text, ent.label_)



text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"
# Process the text
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # This is for formatting only
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")


text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Process the text
doc = nlp(text)

# Iterate over the entities
for ent in doc.ents:
    # Print the entity text and label
    print(ent.text, ent.label_)

# Get the span for "iPhone X" since the model didn't recognize it
iphone_x = doc[1:3]

# Print the span text
print("Missing entity:", iphone_x.text)
