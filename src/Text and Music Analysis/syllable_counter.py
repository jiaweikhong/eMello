# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:28:33 2018
"""

import pyphen
from wordster import wordster
from vocabulary.vocabulary import Vocabulary as vb
from pprint import pprint
import requests
import json


# function that identifies the number of syllables of words in a block of text
def find_syllables(text):
    dic = pyphen.Pyphen(lang='en') #uses the pyphen library
    words = [i.lower() if i.isalpha() else i.split('.')[0] for i in text.split()]
    words = [i if i.isalpha() else i.split(',')[0] for i in words]
    #print(words)
    l = []
    for i in words:
        if len(dic.inserted(i).split('-')) >= 2: #accepts all words with two or more syllables
            if i.isalpha():
                l.append(i)
    
    finalList = set(l)
    return(finalList)

# function that takes in a list of words and returns a dictionary with the word as a key and the corresponding meaning as a value 
def get_word_info(wordlist):
    d = {}
    for i in wordlist:
        d[i] = (findPOS(i), oxfordMeaning(i))
    #pprint(d)
    return(d)


# function to identify the part of speech that the word belongs to
def findPOS(word):
    try:
        return((vb.part_of_speech("difficult").split(',')[1]).split('"text": ')[1])
    except:
        return None



# function that utilises the Oxford API to identify the meaning of a certain word
def oxfordMeaning(word_id):
    app_id = '556ae1e3'
    app_key = '01b384c1ceba47745592fd9112e88f86'
    
    language = 'en' #defines language used as English
    
    try:
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()       
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        i = r.json()["results"]
        
        # parses the json result from the API call to extract the meaning of the word
        definition = (i[0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
        return(definition)
    except:
        #returns None if no meaning for the particular word is found
        return None
    