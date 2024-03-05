# Start with loading all necessary libraries
import numpy as np
import pandas as pd
import sys
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
# Taking the cml argument
path = sys.argv[1]

# Load in the dataframe
df = pd.read_csv(path, index_col=0)
# Taking the skills part
df['SKILLS'] = df['SKILLS'].apply(clean)
# Save the path as same as the arg name
path = path[39:] 
# Split the path into 2 parts
token = path.split('/')
# Create the customized filename
filename = token[0] + 'Skills.txt'
# Open a file to append to it the skills 
f = open(filename, "w")

# Array of skills, that we want to analys
skills = []
# Extract the skills and append them to a file with the same name
for skill in df['SKILLS']:
	content = skill.split(',')
	for cont in content:
		skills.append(cont)
	f.write(str(skill)+',')	
f.close()
# skills[] now has all the skills of all candidates for a specific job position
# Now we can predict the most common skills for each job
# and plot it 
'''
skill_series = pd.Series(skills)

skill_count = skill_series.value_counts()

print(len(skill_count),'\n')
i =0 
for i in range(len(skill_count)):
	if skill_count.index[i] != " ":
		if skill_count.index[i].isnumeric():
			pass
		else:
			print(skill_count.index[i])
'''
