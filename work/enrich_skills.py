# Start with loading all necessary libraries
import numpy as np
import pandas as pd
import sys
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt


# Taking the cml argument
path = sys.argv[1]

# Load in the dataframe
df = pd.read_csv(path, index_col=0)
# Taking the skills part

f = open("generated_skills.txt" , "r")

content = f.read()

content = content.split("\n")

i=0
for cont in content:
    if cont == "":
        content.pop(i)
    i += 1

print(content)

count = 0 
for i in range(1, len(content),2 ):
    print(content[i]+"\n")
    count += 1

print(count)

f.close()

