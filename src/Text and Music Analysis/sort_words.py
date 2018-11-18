# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:09:13 2018

@author: Jin
"""

import string
import syllable_counter as sc

#booktext = 'mermaid.txt'


def sortwords(booktext):
    
    h = open('5000words.txt','r') #opens and reads list of 5000 most common English words
    wordlist = [i.strip() for i in h.readlines() if len(i.strip())<=8] #eliminate all words with 9 or more letters from the list
    c = open('conjunctions.txt','r') #opens and reads list of English conjunctions 
    for i in c.readlines():
        wordlist.append((i.strip()).lower())
    l = open('gradeword.txt','r')
    for i in l.readlines():
        i = ''.join([j for j in i if j.isalpha()])
        wordlist.append((i.strip()).lower())
    l.close()
    h.close()
    c.close()
    
    
    
    
    f = open(booktext, 'r')
    text = f.read() # stores the text of the book
    words = text.split(' ')
    words = [''.join(c for c in i if c not in string.punctuation) for i in words] #stores all words in a text and eliminates punctuation
    words = [i.lower() for i in words if (i and (i not in wordlist) and (i.lower()==i))] # eliminates all words that are in the list of most common words
    #print(words)
    f.close()
    
    
    # counts the number of occurances of words within the text, and puts it in dictionary
    # keys are the words and values are the number of occurances
    d = {}
    for i in [i for i in set(words)]:
        d[i] = d.get(i, words.count(i))
    
    print(d)
    
    
    word = ' '.join(set(words)) #joins the set of unique words in a block of text
    print(word)
    
    comp_words = sc.find_syllables(word) # uses the syllable counter function to filter through the list
    print(comp_words)
    
    writewords = sc.get_word_info(comp_words) # creates the dictionary of words and their meanings
    print(writewords)
    
    # writes the word dictionary into a text file
    g = open('dictwords.txt','w')
    g.write('{}'.format(writewords))
    g.close()
