# lists of doctionaries, one per token
#match exavt token texts, lexical attributes, any token attributes

import spacy

from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

#initialize matcher with shared vocab
matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
pattern2 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern3 = [{"LEMMA": "buy"}, {"POS": "NOUN"}]

#add own pattern to the matcher
matcher.add("IPHONE_PATTERN", None, pattern)

#process some text
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")
#call matcher on the doc, it will retuen a list pf tuples
matches = matcher(doc)

#iterate
for match_id, start, end in matches:
        # get matched span
        matched_span = doc[start:end]
        print(matched_span.text)



patternX = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

doc2 = nlp("2018 FIFA World Cup: France won!")

for match_id, start, end in matches:
        # get matched span
        matched_span = doc2[start:end]
        print(matched_span.text)

matcher.add("IOS_VERSION_PATTERN", None, patternX)
matches2 = matcher(doc2)
print("Total matches found with patternX: ", len(matches))
for matches_id, start, end in matches2:
    print("Match found with patternX: ", doc[start:end].text)



patternY = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]

doc = nlp("I loved dogs but now I love cats more")

matcher.add("LOVE_PATTERN", None, patternY)
matches = matcher(doc)
print("Total matches found with patternY: ", len(matches))
for matches_id, start, end in matches:
    print("Match found with patternY: ", doc[start:end].text)




