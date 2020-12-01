Es wird ein Spacy-Modell erweitert.

Spacy-Features:
https://www.skcript.com/svr/how-to-easily-extract-text-from-anything-using-spacy/

Standard-Modelle fuer die deutsche Sprache (trainiert auf Wikipedia):
https://spacy.io/models/de

Machine-Learning Toolbox:
https://amitness.com/toolbox/

Keyword extraction Beispiel (andere Python library):
https://www.kdnuggets.com/2019/11/content-based-recommender-using-natural-language-processing-nlp.html

Spacy-Training
https://spacy.io/usage/training
https://spacy.io/usage/vectors-similarity

Beim Updaten von existierenden Modellen koennen Kategorien wir "PPERSON" fuer das
Einsatzgebiet verbessert werden.
Um neue Kategorien zu erstellen muss laenger mit mehr Daten trainiert werden, sowie
darauf geachtet, dass alte Kategorien nicht teilweise vergessen werden.
Fuer Cohooyo koennten eigene Kategorien wir "BRANCHE" trotzdem nuetzlich sein.

Eigene Pipeline-Komponenten wie ein Text classifier koennen falls noetig
ebenfalls eingefuegt werden

Moeglicher Ansatz (vgl Spacy-Features):
Tokenizing
Part-of-Speech Tagging: nur Nomen, Verben, Adjektive beachten
Lemmatization: Basisform von Woertern bilden, die die KI besser vergleichen kann
(Named-Entity-Recignition: 
    Koennte ueberfluessig sein, wenn Basisdaten wie Name, Alter in extra Feldern stehen)
Similarity: Vergleich (Auf Doc, Span oder Tokenebene moeglich)
(Training, falls Basismodell abgeaendert wird)

TODO: 
Recherchieren, ob die deutschen Modelle fuer unser Feld ausreichend viele Vektoren
    haben, mit denen ein ML-Algorithmus, der sich auf numbers verlaesst arbeiten kann
Wenn nicht, muss ein word2vec gefunden werden, der dies noch macht
    => Wahrscheinlich, nach Alessandro so vorgesehen
Recherchieren, wie Vord2Vec eingesetzt werden kann, um schon existierendes
spacy-Modell zu modifizieren