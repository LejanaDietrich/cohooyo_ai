NLP Model: External
Untersuchung diverser externer NLP-Methoden und vortrainierter Modelle
mit Hile von Spacy

(Moegliches Problem: Keine sentiment analysis in Spacy
PyNLP als Moeglichkeit, ungewoehnlichere Algorithmen zu nutzen, nur wenn noetig)

Standard-Modelle fuer die deutsche Sprache (trainiert auf Wikipedia):
https://spacy.io/models/de

Install/Update Spacy:
    Python Version 3.7 ist unterstuetzt, neuere Versionen nicht
    in beliebigem Ordner, z.B. Installationsort von Python per Konsole:
        pip install -U spacy
    Sprachpakete downloaden:
        npm install kann ausprobiert werden, reicht vielleicht
        small:
            (python -m spacy download en_core_web_sm)
            python -m spacy download de_core_news_sm
        medium:
            (python -m spacy download en_core_web_md)
            python -m spacy download de_core_news_md
        large:
            (python -m spacy download en_core_web_lg)
            python -m spacy download de_core_news_lg

Zur Visualisierung wird die Python Bibliothek matplotlibrary genutzt:
    python -m pip install -U matplotlib
Sowie die darauf basierende Bib seaborn:
    pip install seaborn

Im course Unterordner finden sich der Link zu einem empfehlenswerten spacy-Tutorial,
    sowie Files mit bearbeiteten Uebungen, die zur Referenz dienen koennen

spacy can define it's common tags and labels:
print(spacy.explain("NPP"))

Spacy kann den Arbeitsschritt uebernehmen, Beschreibungen zu Vektoren zu verarbeiten.
Eigene Word2Vec (Trainingsalgorithmen) koennen zu spacys statistischen Modellen hinzugefuegt werden.
Irrelevante Woerter zu streichen funktioniert nicht sehr gut, es wird die durchschnittliche 
 Aehnlichkeit der Tokens verwendet => Similyrity ist bei kurzen Texten idR hoeher.
Die Vektoren haben idR 300 Dimensionen

Werden Matcher genutzt, sollen bei langen Datensätzen PhraseMatcher genutzt werden => Effizienz

TODO: Vergleichen des deutschen _sm _md und _lg Modells
        clusteringTest (von Kunde gestellt) zum Laufen bringen
