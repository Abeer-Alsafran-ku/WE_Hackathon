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

    #print("all strings " , all_strings, "\n")
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_strings)

    # Compute cosine similarity between the input string and the list of strings
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    #print(cosine_similarities)

    #print("\n")
    return cosine_similarities



# Taking the cml argument
path = sys.argv[1]

# Load in the dataframe
df = pd.read_csv(path, index_col=0, keep_default_na=False)
# Taking the skills part
data = {"C_JOB" : [] , "COURSE" : [], "P_JOB" : []}

data["P_JOB"] = df["PREVIOUS_JOB_TITLE"]
data["C_JOB"] = df["CURRENT_JOB_TITLE"]
data["COURSE"] = df["COURSE"]

c_jobs = []
p_jobs = []
courses = []
uni_jobs = []
skills = []
# skills generated by AI based on job position and courses has been taken

f = open("generated_skills.txt" , "r")

content = f.read()

content = content.split("\n")
f.close()

i=0
for cont in content:
    if cont == "":
        content.pop(i)
    i += 1

fd = open("pure_skills.txt", "w")

count = 0 
for i in range(1, len(content),2 ):
    # write to a file the skills 
    fd.write(content[i]+'\n')
    count += 1
fd.close()

# open file to read skills that has been generated from AI
fd = open("pure_skills.txt","r")
skills = fd.read()
# skills now are seted
skills = skills.split("\n")
fd.close()

# previous jobs
for job in data["P_JOB"]:
    p_jobs.append(job)

# current jobs
for job in data["C_JOB"]:
    c_jobs.append(job)

# courses 
for course in data["COURSE"]:
    courses.append(course)

# uni_jobs is for unified jobs 
# if the current job is not defined then the previous job will fill in as current job
i = 0 
for job in c_jobs:
    # job is empty 
    if job == '':
        job = p_jobs[i]
    # check if the job is already exists 
    uni_jobs.append(job)
    i += 1

#for i in range(len(uni_jobs)):
#    print(f"{i}- job held:'{uni_jobs[i]}'| courses:'{courses[i]}'\n")

job = input("Enter a job postion : ")

similarities = compute_cosine_similarity(job, uni_jobs)

# Print similarity scores
for i, sim in enumerate(similarities):
    if sim >= 0.6:
        print(f"job similar to {job} is {uni_jobs[i]}'\nand course is:\n'{courses[i]}\nand skills:\n {skills[i]}'\n")
    elif sim <= 0.1 :
        print(f"Sorry! no job was fined\n")
        break