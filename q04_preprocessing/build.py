import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re
import string
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q03_recognize_pattern.build import q03_recognize_pattern

p_stemmer = PorterStemmer()
tokenizer = TreebankWordTokenizer()
stop_words = set(stopwords.words('english'))


def q04_preprocessing(corpus, punc=True, stem=True, rm_words=[]):
    "write your solution here"
    rm_words_set = set(rm_words)

    for word in rm_words_set:
        stop_words.add(word)

    new_stop_words = set(stop_words)
    corpus = q03_recognize_pattern(corpus)

    # Remove text between curly braces as they may not be present in actual data
    corpus = [re.sub('{.+}', '', text) for text in corpus]

    # Replace punctuation with space
    corpus = [re.sub('[{}]'.format(re.escape(string.punctuation)), ' ', text) for text in corpus] if punc else corpus

    # Tokenize
    corpus = [row.lower() for row in corpus]
    corpus = [tokenizer.tokenize(row) for row in corpus]

    # Remove Stopwords and custom defined words
    corpus = [[word for word in text if word not in new_stop_words] for text in corpus]

    # Stemmer
    corpus = [[p_stemmer.stem(word) for word in text] for text in corpus] if stem else corpus

    return corpus