from random import shuffle
from sklearn.feature_extraction.text import CountVectorizer
from cleaner import clean
from sklearn.model_selection import train_test_split as tts
import numpy as np

def chunkify(lst, n): return [lst[i::n] for i in range(n)]

def preprocess():
    vec = CountVectorizer()

    data = clean('lyrics.txt')
    vec.fit_transform([i[1] for i in data])
    shuffle(data)
    data, d2 = tts(data, test_size=0.1)
    data = chunkify(data, 10)

    lyrics = []
    for d in data:
        temp = [[], []]
        for item in d:
            temp[0].append(item[1])
            temp[1].append(item[0])
        temp[0] = vec.transform(temp[0]).toarray().tolist()
        lyrics.append(temp)
    test = [[], []]
    for item in d2:
        test[0].append(item[1])
        test[1].append(item[0])
    test[0] = vec.transform(test[0]).toarray().tolist()

    return [lyrics, test]