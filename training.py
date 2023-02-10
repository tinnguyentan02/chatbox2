import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer  # to reduce words to the stem

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


lemmatizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())

words = []
classes = []
documents = []
ignore_letter = ['!', '?', '.', ',']

for intent in intents['intents']:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append(word_list)
        

print(words, '\n', documents)

 