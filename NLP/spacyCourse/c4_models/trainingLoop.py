#1 Loop a number of times
    #2 Shuffle the training data (to avoid model getting stuck in suboptimal solution)
    #3 Divide data into batches (minibatching - increases reliability of gradient estimates)
        #4 Update model for each batch + start the loop again
        #5 Save the updated model after final iteration
import spacy
import random
import json

with open("NLP\external\course\c4_models\gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

# Setting up pipeline from scratch
    # Starting with blank model
nlp = spacy.blank("de")
    # Create blank entity recognizer and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
    # New label for the entity recognizer
ner.add_label("GADGET")

# Start training
nlp.begin_training()
# Loop for 10 iterations for maximal accuracy
for itn in range(20):
    random.shuffle(TRAINING_DATA)
    # Losses to measure how many mistakes are still being made
    losses={}
    # Divide examples into batches
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]
        # Update the model
        nlp.update(texts, annotations, losses=losses)
    print(losses)

