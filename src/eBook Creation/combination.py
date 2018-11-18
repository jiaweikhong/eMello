# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:36:30 2018

@author: Jin
"""

'''
1. Change epub file format to a zipped file
2. Extract the zipped contents into a new folder
3. Parse all html pages in the folder and extract text


4a. Run extracted text through tone analyzer
5a. Match tone of text with database of labelled songs
6a. Output text file with page-song pairing


4b. Run extracted text through syllable counter, Part of Speech tagger, and find word meaning
6b. Edit html files to add in pop ups corresponding to dictionary words
'''

import os
import zipfile
import extract_text as et
import sort_words as sw
import noOEBPS as no

file = [i for i in os.listdir() if ("epub" in i)][0]
#file = "finding_a_friend_-_aurora_productions.epub"
base = os.path.splitext(file)[0]
os.rename(file, base + ".zip")


zip_ref = zipfile.ZipFile(base + ".zip", 'r')

bookname = "newbook"
newbook = "newbookedited"
#create a new empty folder
if not os.path.exists(bookname):
    os.makedirs(bookname)
    
zip_ref.extractall(bookname)
zip_ref.close()


# find book name, number of pages
pages = 14
et.extract(bookname, base, pages, "booktext.txt")
sw.sortwords('booktext.txt')
no.edithtml("dictwords.txt", bookname, newbook)


#tonebooktext.txt
#booktext.txt















