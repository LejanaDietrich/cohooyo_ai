Vorgehen: 
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


Installationen etc. finden sich in den jeweiligen Ordnern in preparations
