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

skills = pd.read_csv("skills.csv")
courses = pd.read_csv("Courses.csv")
job_roles = pd.read_csv("JobRoles.csv")
user_profile = pd.read_csv("UserProfiles.csv")

'''
print(skills["SkillID"])
print(skills["SkillName"])
print(skills["Category"])
print(skills["Description"])


print(courses["CourseID"])
print(courses["CourseName"])
print(courses["SkillsTaughtIDs"])


print(job_roles["JobID"])
print(job_roles["JobTitle"])
print(job_roles["RequiredSkillsIDs"])
print(job_roles["Description"])

print(user_profile["Name"])
print(user_profile["Degree"])
print(user_profile["FieldofStudy"])
print(user_profile["DateofBirth"])
print(user_profile["AppliedPosition"])

'''
def find_similar_string(input_string, string_list):
    # Add the input string to the string list
    string_list.append(input_string)

    # Convert the strings to a matrix of token counts
    vectorizer = CountVectorizer().fit_transform(string_list)

    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(vectorizer[-1], vectorizer[:-1])

    # Get the index of the most similar string
    most_similar_index = cosine_similarities.argmax()

    # Remove the input string from the string list
    string_list.pop()

    return most_similar_index

# take the job 

job = input("Enter a job position: ")

# ranked people based on some factors such as max number of skills 
# it will have a the names of candidates

ranked = []

# take the similar job title from job roles

similar_index = find_similar_string(job, job_roles['JobTitle'])

print(similar_index)



