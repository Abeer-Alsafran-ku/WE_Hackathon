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



def compute_cosine_similarity(string, string_list):
    # Combine the input string and the list of strings
    all_strings = [string] + string_list

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_strings)

    # Compute cosine similarity between the input string and the list of strings
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    return cosine_similarities



# Taking the cml argument
path = sys.argv[1]

# Load in the dataframe
df = pd.read_csv(path, index_col=0, keep_default_na=False)
# Taking the skills part
data = {"JOB" : [] , "COURSE" : []}

data["JOB"] = df["CURRENT_JOB_TITLE"]
data["COURSE"] = df["COURSE"]

jobs = []
courses = []
for job in data["JOB"]:
    jobs.append(job)

for course in data["COURSE"]:
    courses.append(course)


job = input("Enter a job postion : ")

similarities = compute_cosine_similarity(job, jobs)

# Print similarity scores
for i, sim in enumerate(similarities):
    if sim >= 0.6:
        print(f"Similarity between '{job}' and '{jobs[i]}': {sim} and course is'{courses[i]}'")


