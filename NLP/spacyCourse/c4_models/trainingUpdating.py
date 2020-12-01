#helps with accuracy, right classification schemes for problems
import spacy
from spacy.lang.de import German
nlp = German()

#1 initialize model wights randomly
nlp.begin_training
#2 predict a few examples with current weights
nlp.update
#3 compare prediction with true labels
#4 calculate how to change weights to improve predictions
#5 update weights slightly
#6 back to #2

#where to get enough training data?
    #usually created manually or semi-automated, for example using spacy's Matcher
#Updating an existing model requires houndreds to thousands of examples
#Training a new category: thousands to a million


#Example: Training entity recognizer, teaching model to generalize:
#Each token can only be part of one entity, examples need to come w/ context
    #("iPhone X is coming", "entities": [(0, 8, "GADGET")])
    #("I need a new phone! Any tips?", {"entities": []})

#! See other files here for actual examples