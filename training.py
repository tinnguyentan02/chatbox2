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

intents = json.load(open("intents.json").read())
 