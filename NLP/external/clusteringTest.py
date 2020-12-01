#as specified by Alessandro
import requests
import json
from functools import reduce
import numpy as np
import string
from sklearn.feature_extraction import text as text_feature_extraction
from sklearn.feature_extraction import stop_words
import spacy
nlp = spacy.load("de_core_news_sm")

def pca(data):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca.transform(data)

#Feature Selection 
#mapped_jobs = list(map(lambda job: np.concatenate((nlp(job['jobTitle']).vector,[job['latitude'],job['longitude']])), jobs))

