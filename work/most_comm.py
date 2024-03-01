import numpy as np
import pandas as pd
import sys



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


path = sys.argv[1]

# Load in the dataframe

f = open(path , 'r')

skill_list = f.read()

skill_list = skill_list.split(',')

f.close()
# Count words and their occurrences
word_count_array = count_words(skill_list)

# Display the 2D array
for item in word_count_array:
    print(item)

