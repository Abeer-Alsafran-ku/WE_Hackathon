import numpy as np
import pandas as pd
import sys
from collections import Counter

def count_words(lst):
    word_count = {}  # Dictionary to store word counts

    # Count occurrences of each word in the list
    for word in lst:
        word = word.lower()
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Create a 2D array to store word and its count
    word_count_array = []
    for word, count in word_count.items():
        word_count_array.append([word, count])

    return word_count_array


def rank_occurrences(lst):
    # Count occurrences of each item in the list
    count = Counter(lst)
    
    # Rank items based on their occurrences
    ranked_items = count.most_common()
    
    return ranked_items


path = sys.argv[1]

# Load in the dataframe
f = open(path , 'r')

skill_list = f.read()

skill_list = skill_list.split(',')

f.close()


ranked = rank_occurrences(skill_list)

print(ranked)
'''

# Count words and their occurrences
word_count_array = count_words(skill_list)

# Display the 2D array
i = 0 
max = 0
idx = 0

for item in word_count_array:
    if item[1] > max :
        max = item[1]
        idx = i
    i += 1

print("maximum " , max , " index " , idx, " len ", len(word_count_array))
j = 0
for item in word_count_array:
    if j == idx:
        print(item[0], " occur " , item[1])
    j += 1
'''
