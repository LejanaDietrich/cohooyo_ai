import spacy

# matching things in finite categories - like country names - works fast with strings
# may be a good idea for job fields

import json
from spacy.lang.en import English
# Import the PhraseMatcher and initialize it
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

nlp = English()
doc = nlp("Czech Republic may help Slovakia protect its airspace")



matcher = PhraseMatcher(nlp.vocab)

# Create pattern Doc objects and add them to the matcher
# This is the faster version of: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Call the matcher on the test document and print the result
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])


#extracting countries and relationships
with open("exercises/en/country_text.txt") as f:
    TEXT = f.read()

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Create a doc and reset existing entities
doc = nlp(TEXT)
doc.ents = []

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE"
    span = ____(____, ____, ____, label=____)

    # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [____]

    # Get the span's root head token
    span_root_head = ____.____.____
    # Print the text of the span root's head token and the span text
    print(span_root_head.____, "-->", span.text)

# Print the entities in the document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])