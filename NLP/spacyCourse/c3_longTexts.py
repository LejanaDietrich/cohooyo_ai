#nlp.pipe method instead of calling nlp on each tests
#data can be passed as tuples of text and context, yields (doc, context)
import spacy
from spacy.tokens import Doc
from spacy.lang.en import English

nlp = spacy.load("en_core_web_md")

data = [
    ("This is a text.", {"id:": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16})
]

#using extension components with .pipe

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

for doc, context in nlp.pipe(data, as_tuples = True):
    #doc._.id = context["id"]
    print(doc.text, context["page_number"])


#Only use tokenizer
doc = nlp.make_doc("Hello there")


#Temporarily disable unused pipes (only in context of the with block)
with nlp.disable_pipes("tagger", "parser"):
    doc = nlp("Some text for you, Apple, Galaxy")
    print(doc.ents)