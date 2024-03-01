import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.DataFrame(columns=["ID","DESCRIPTION"], data=np.matrix([[10,"iPhone 13 Mini, 128GB, Starlight - Unlocked (Renewed Premium)"],
                                                                [11,"Apple iPhone 13, 128GB, Blue - Unlocked (Renewed)"],
                                                                [12,"Apple iPhone 13 Mini, 128GB, Blue - Unlocked (Renewed)"],
                                                                [13,"iPhone 13 Pro Max, 128GB, Graphite - Unlocked (Renewed Premium)"],
                                                                [14,"iPhone 13 Pro, 256GB, Graphite - Unlocked (Renewed Premium)"],
                                                                [15,"Apple iPhone 13 Pro Max, 512GB, Sierra Blue - Unlocked (Renewed)"],
                                                                [16,"SAMSUNG Galaxy Z Fold 4 Cell Phone, Factory Unlocked Android Smartphone, 512GB, Flex Mode, Hands Free Video, Multi Window View, Foldable Display, S Pen Compatible, US Version, Gray Green"],
                                                                [17,"Apple iPhone 12 Pro, 512GB, Pacific Blue - Unlocked (Renewed Premium)"],
                                                                [18,"Apple iPhone 12 Pro, 128GB, Graphite - Unlocked (Renewed Premium)"]
                                                                ]))
# print(df)
corpus = list(df["DESCRIPTION"].values)
print(f'the corpus = {corpus}')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

threshold = 0.8
coutn = 0
for x in range(0,X.shape[0]):
    for y in range(x,X.shape[0]):
        if(x!=y):
            if cosine_similarity(X[x], X[y]) > threshold:
                coutn += 1
                print("Cosine similarity:", cosine_similarity(X[x], X[y]))
                print(df["ID"][x],":",corpus[x])
                print(df["ID"][y],":",corpus[y])

print(coutn)



data = {"ID" : [] , "REV" : []}

for i in range(6):
    data['ID'].append(i)
    data["REV"].append(i+1)
    
print(data)



