import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')

stopwords_list = stopwords.words('english')

def clean(sentence):
    re_general_pattern = r"https?:\/\/.*[\r\n]*|#\w+|@\w+|\.{2,}"
    re_punctuation_pattern = r"[^\w\s]"
    re_repeating_character_pattern = r"(\w)\1{2,}"
    
    # 1- Removing whitespaces at the beginning and ending of texts
    sentence = sentence.strip()
    # 2- Removing new lines
    sentence = re.sub("\n", "", sentence)
    # 3- Removing URLs, Hashtags, Mentions, and repeating dots
    sentence = re.sub(re_general_pattern, "", sentence)
    # 4- Removing punctuations
    sentence = re.sub(re_punctuation_pattern, "", sentence)
    # 5- Removing repeating characters that occur more than twice
    sentence = re.sub(re_repeating_character_pattern, r"\1", sentence)
    # 6- Removing English stop words
    sentence = " ".join(word for word in sentence.split() if word not in stopwords_list)

    return sentence


# df["SKILLS"] = df["SKILLS"].apply(clean)
