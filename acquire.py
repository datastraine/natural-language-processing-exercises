from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd
import numpy as np

def get_blog_articles():
    '''
    Retruns a list of dictionaries of the below list of aticles where title is the title
    of the article and content is the text of the article

    'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    'https://codeup.com/data-science-myths/'
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/'
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/'
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/'
    '''
    # Assigns each article to a art object
    art1 = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    art2 = 'https://codeup.com/data-science-myths/'
    art3 = 'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/'
    art4 = 'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/'
    art5 = 'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/'

    # places the art objects into a list to iterate over
    articles = [art1, art2, art3, art4, art5]
    # create an empty list to store the dictionaries
    blog_articles = []
    headers = {'User-Agent': 'Codeup Data Science'}
    # use a for loop to go through the list of articles
    for article in articles:
        url = article
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        # create the soup object of html parser
        soup = BeautifulSoup(response.content, 'html.parser')
        # grab the title from the post-title class of the blog post
        title = soup.find('h1', class_='jupiterx-post-title')
        # grab the article text from the content class of the blog post
        body = soup.find('div', class_='jupiterx-post-content')
        #store the results in a dictionary object
        dicob = {"title":title.text, "content":body.text}
        # apeend the dictionary object to the blog_articles list
        blog_articles.append(dicob)
    #return the final results
    return blog_articles

def get_inshorts():
    '''
    Retruns a list of dictionaries of the below list of aticles category sections from the
    inshorts website where title is the title of an article, content is the text of the article,
    and the category is what section of the site the article came from

    business = 'https://inshorts.com/en/read/business'
    sports = 'https://inshorts.com/en/read/sports'
    technology = 'https://inshorts.com/en/read/technology'
    entertainment = 'https://inshorts.com/en/read/entertainment'

    '''
    # Assign each category's urls to corresponding objects
    business = 'https://inshorts.com/en/read/business'
    sports = 'https://inshorts.com/en/read/sports'
    technology = 'https://inshorts.com/en/read/technology'
    entertainment = 'https://inshorts.com/en/read/entertainment'
    # create an empty list object to store the dictonaries in
    inshorts=[]   
    # put each category object into a list to iterate over
    articles = [business, sports, technology, entertainment]
    # use a for loop to iterate over each cateatogry to get into the URL
    for article in articles:
        body_list = []
        title_list = []
        url = article
        # assign the url to response
        response = get(url)
        # create a soup object to use html.parser
        soup = BeautifulSoup(response.content, 'html.parser')
        # find the titles of all the articles on the first page and put the results into a list
        titles = soup.findAll('span', itemprop="headline")
        # find the body content of all the articles on the first page and put the results into a list
        bodies = soup.findAll('div', itemprop="articleBody")
        # use a for loop to get into the list of titles and
        for title in titles:
            # extract the text from the each title
            title_list.append(title.extract().text)
            # then for do the same thing for the body of each article while staying inside the 
            # title loop to ensure they are done in order
            for body in bodies:
                body_list.append(body.extract().text)
                # store the results in a dictonary object that properly lables the key value pairs
                # category is derivied from the url as each url's using string slicing
            dicob = {"title":title.text, "content":body.text, "category":article[29:]}
        # append each dicob to the list
            inshorts.append(dicob)
# Return the article dictionary list
    return inshorts