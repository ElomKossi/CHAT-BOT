import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenize_sentencre, all_words):
    pass

a = "How long does shipping take?"
print(a)
a = tokenize(a)
print(a)

words = ["organize", "organizes", "organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)