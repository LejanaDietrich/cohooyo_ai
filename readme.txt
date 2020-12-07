Vorgehen: 
Zuerst theoretisches Modell entwickeln, indem 8 Teilaugaben von Alessandro 
umgesetzt werden. Ggf bereits in TensorFlow einarbeiten
Dann wirkliche Implementierung beginnen.
    NLP optimieren, dann daraus ML entwickeln
    Model Assessments jeder implementierung, um die Qualität zu bestimmen 
        (die fuer unser Szenarion hoeher, als die externer Modelle sein sollte)
        Mindestens fuer jede eine confusion Matrix erstellen
    Wird ein großer Teil des Algorithmus selbst geschrieben,
     Unit tests fuer Funktionen

Technologien und Frameworks: 
    ML:
        TensorFlow (tensorflow recommenders)
        Keras als High-Lvl abstraction von TensorFlow, Zeit sparend
        skLearn als Bibliothek
    Training:
        Google Server
        Spacy
    NLP:
        Spacy
        Brat oder besser Prodigy, zur Daten-Annotierung
    Daten:
        sklearn
    Visualisierung:
        matplotlip (Python Bibliothek)
        seaborn (basiert auf matplotlib)
    Validierung/Evaluation:
    (Vergleich:)

Falls weiteres noetig - Machine-Learning Toolbox:
https://amitness.com/toolbox/

!aktueller Prototyp:
models\leastEffort\prototype.py

TODO:
Der aktuelle Prototyp soll vervollstaendigt, angebunden und dann Stueck fuer Stueck erweitert werden
0) Herausfinden, in welcher Reihenfolge diese Schritte am besten sind (vor allem ab 3))
1) Konzept zu Erstellen von Empfehlungen/Listen und Weitergeben dieser ans Backend
 -> Internetrecherche + Backend fragen
 -> Wie IDs der naechsten Matches aus Clustering holen?
 -> Wie oft gibt die KI die naechsten Matches und wie viele?
 -> Muss immer aktuelle Map + aktuelles Clustering speichern, 
     wird mit jedem Swipe geupdated?
 -> Gibt das Backend nach festen Kriterien gefilterte Matchmoeglichkeiten an die KI
    und diese sortiert sie weiter? Oder sortiert die KI und das Backend filtert 
    nochmal aus?
 -> Wer greift wann auf DB und API zu?
2) Mapping verbessern
  -> Entscheiden, welche Attribute gemappt werden!
  -> Wie wird gewichtet
3) NLP
 -> Vektoren und Similarities zu den Jobfeldern untersuchen
4) ML
 -> Content-Based Filtering
 -> Herausfinden, ob sklearn Algorithmus weiter trainiert werden kann / wird wenn man ihn einsetzt
 -> Sichergehen, dass Cold Recommender System mit KMeans machbar ist
 -> Verschiedene sklearn Algorithmen ausprobieren
   -> https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html
   -> https://scikit-learn-extra.readthedocs.io/en/latest/generated/sklearn_extra.cluster.KMedoids.html
5) Backend-Anbindung

word2vec - 
    preparations\NLP\internal\readme.txt
Beispiel durcharbeiten, z.B.
    https://www.analyticsvidhya.com/blog/2020/08/recommendation-system-k-nearest-neighbors/

Recommender-System-Aufbau verstehen:
https://github.com/jfkirk/tensorrec
https://github.com/caserec/CaseRecommender
Analyzing:
http://surpriselib.com/


!Installationen und Erklaerungen finden sich in den jeweiligen Ordnern in preparations
