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

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string, optional extra_words and exclude_words, default none for both 
    and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))
    # Split words in string.
    words = string.split()
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    return string_without_stopwords

def prep_news():
    '''
    Uses the above helper on the inshorts news data to creates following new columns
    clean - applies basic_clean, tokenizatize, and removes stop words on the article contents
    stemmed - applies stemming to the original contents
    lemmatized - applies the lemmatize function to the original content
    '''
    news_df = pd.DataFrame(acquire.get_inshorts())
    news_df['clean'] = news_df['content'].apply(basic_clean).apply(tokenize).apply(remove_stopwords)
    news_df['stemmed'] = news_df['content'].apply(stem)
    news_df['lemmatized'] = news_df['content'].apply(basic_clean).apply(lemmatize)
    return news_df

def prep_blogs():
    '''
    Uses the above helper on the CodeUp blog data to creates following new columns
    clean - applies basic_clean, tokenizatize, and remove stop words on the article contents
    stemmed - applies stemming to the original contents
    lemmatized - applies the lemmatize function to the original content
    '''
    codeup_df = pd.DataFrame(acquire.get_blog_articles())
    codeup_df['clean'] = codeup_df['content'].apply(basic_clean).apply(tokenize).apply(remove_stopwords)
    codeup_df['stemmed'] = codeup_df['content'].apply(stem)
    codeup_df['lemmatized'] = codeup_df['content'].apply(basic_clean).apply(lemmatize)
    return codeup_df