import acquire
import pandas as pd 
import numpy as np
import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


def basic_clean(somestring):
    '''
    Take in a string and performs a basic clean by converting it to all lower case letters,
    and then normalizes the encoding and removes an character that isn't a letter, number, and a space.
    Returns the result.
    '''
    basic = somestring.lower()
    basic = unicodedata.normalize('NFKD', basic).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    basic = re.sub(r"[^a-z0-9'\s]", '', basic)
    return basic

def tokenize(somestring):
    '''
    Creates a tokenizer object to tokenize the given string and then returns the tokenized string
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    tokened = tokenizer.tokenize(somestring, return_str=True)    
    return tokened

def stem(somestring):
    '''
    Creates a stemming object and then uses it to stem the provided string. Returns the string stemmed
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in somestring.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed

def lemmatize(somestring):
    '''
    Creates a lemmatize object and then uses it to lemmatize the provided string. Returns the string stemmed
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in somestring.split()]
    article_lemmatized = ' '.join(lemmas)
    return article_lemmatized

def remove_stopwords(somestring):
    '''
    Downloads the 'stopwords' library from nltk
    Downloads the wordnet library from nltk
    Uses the standard stop words english from the stopwords library minus not and no
    ensures the string is in all lower case
    removes all the words in the stopwords list
    '''
    nltk.download('stopwords')
    nltk.download('wordnet')
    stopword_list = stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    somestring = somestring.lower()
    words = somestring.split()
    filtered_words = [w for w in words if w not in stopword_list]
    article_without_stopwords = ' '.join(filtered_words)
    return article_without_stopwords

def prep_news():
    news_df = pd.DataFrame(acquire.get_inshorts())
    news_df = news_df[['title', 'content']]
    news_df.columns=['title', 'original']
    news_df['clean'] = news_df['original'].apply(basic_clean).apply(tokenize).apply(remove_stopwords)
    news_df['stemmed'] = news_df['original'].apply(stem)
    news_df['lemmatized'] = news_df['original'].apply(lemmatize)
    return news_df

def prep_blogs():
    codeup_df = pd.DataFrame(acquire.get_blog_articles())
    codeup_df.columns=['title', 'original']
    codeup_df['clean'] = codeup_df['original'].apply(basic_clean).apply(tokenize).apply(remove_stopwords)
    codeup_df['stemmed'] = codeup_df['original'].apply(stem)
    codeup_df['lemmatized'] = codeup_df['original'].apply(lemmatize)
    return codeup_df