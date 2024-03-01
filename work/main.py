# Start with loading all necessary libraries
import numpy as np
import pandas as pd
import spacy
import sys
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# Taking the cml argument
path = sys.argv[1]

# Inputed list of skills from the user
new_skills = ['leadership' , 'MS office', 'problem solving' ,'Analytical Skills',' Attention to Detail',' Financial Acumen',' Technical Proficiency', 'Communication Skills', 'Problem-Solving Skills', 'Risk Management', 'Compliance Knowledge', 'Cross-Functional Collaboration', 'Process Improvement', 'Audit Experience', 'Adaptability', 'Time Management', 'Critical Thinking', 'Ethical Integrity']

# Load in the dataframe
f = open(path, 'r')

# Taking the skills part
content = f.read()

data = {"IDX" : [] , "SCORE" : []}

# skills[] now has all the skills of all candidates for a specific job position
skills = content.split(',')

for i in range(len(new_skills)):
    # append the first item in the list to the skills list
    skills.insert(0,new_skills[i])
    # vector it to calculate the distance
    vectorizer = TfidfVectorizer()
    # vectorizing the skillset
    X = vectorizer.fit_transform(skills)
    # setting the threshold 
    threshold = 0.9
    #count = 0 #number of matches 
    for x in range(0,X.shape[0]): # loop through the vector itself 
        for y in range(x, X.shape[0]): # loop through the next vector
            if (x!=y): # do not compare it with itself
                cos_sim = cosine_similarity(X[x],X[y]) # apply the similarity calculation
                if cos_sim > threshold: # check the similarity value
                    print(cos_sim)
                    # append it to the data dictionary
                    data["IDX"] = i 
                    data["SCORE"] = cos_sim
    # remove the item that have been inserted to make the process faster and 
    # to avoid dubplication
    skills.pop(0)
print(data)

# Now we can predict the most common skills for each job
f.close()


