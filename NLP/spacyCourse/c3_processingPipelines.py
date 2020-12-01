import spacy
# pipeline:
# passing text to an nlp tokenizes it into a DOM object but thealso
# tags tokens
# parses dependencies
# recognizes named entities (component called ner)
# classifies the text => textcat, has to be included manually, is rather specific

nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)
print(nlp.pipeline)

#custom pipeline components for:
#   Computing your own values based on tokens and their attributes
#   Adding named entities, for example based on a dictionary
def length_component(doc):
    # Get the doc's length
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Return the doc
    return doc


# Add the component first in the pipeline and print the pipe names
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# Process a text
doc = nlp("This is a sentence.")