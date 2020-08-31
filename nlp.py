import sys, os


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


blockPrint()
from nltk.corpus import wordnet
from PyDictionary import PyDictionary
#from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

import string
from Aardvark import *
dictionary = PyDictionary()
lemma = WordNetLemmatizer()
#Aardvark.library
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)



@Aardvark.function("clean_text")
def clean_text(name, doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


@Aardvark.function("GetWordInfo")
def GetWordInfo(name, word):
    synonyms = [word]
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return {
        'synonyms': synonyms,
        'antonyms': antonyms,
        'definition': dictionary.meaning(word, disable_errors=True)
    }


@Aardvark.function("ProcessList")
def processlist(name, li):
    newlist = {}
    for i in li:
        x = li[i]
        for item in i:
            newlist[item] = x
    return newlist


@Aardvark.function("GetTopics")
def gettopics(name, doc_complete, number_topics=5, num_words=5,
              passes=50):  #Gets the topic of a conversation
    doc_clean = [clean_text("", doc).split() for doc in doc_complete]

    # Importing Gensim
    import gensim
    from gensim import corpora

    # Creating the term dictionary of our courpus, where every unique term is assigned an index.
    dictionary = corpora.Dictionary(doc_clean)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel

    # Running and Trainign LDA model on the document term matrix.
    ldamodel = Lda(
        doc_term_matrix,
        num_topics=number_topics,
        id2word=dictionary,
        passes=passes)
    return (ldamodel.print_topics(
        num_topics=number_topics, num_words=num_words))
enablePrint()