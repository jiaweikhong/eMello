# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:25:16 2018

@author: Jin
"""

import os
import codecs
from bs4 import BeautifulSoup
import IBM_text_Analysis as analysis


#pages = 15
#book = "mermaid_copy"
#txtname = "mermaid.txt"
#title = "«Grand-père Jacques"

# creating a function 
def extract(read_book, title, pages, txtname):
    enum = -1
    #for file in os.listdir("{}\\{}".format(read_book, "OEBPS")):
    for file in os.listdir("{}".format(read_book)): #iterates through  the book
        
        if "html" in file: #searches for all html files
            if "title" not in file:
                enum += 1
                if enum >= pages-1:
                    break
                print(file)
                #f = codecs.open('{}\\{}\\{}'.format(read_book,"OEBPS",file), 'r', 'utf-8') 
                f = codecs.open('{}\\{}'.format(read_book,file), 'r', 'utf-8')                
                page = f.read()
                
                # using the beautifulsoup library to parse the html file to access the text
                soup = BeautifulSoup(page, "html5lib")
                text = (soup.text)
                
                # formatting the text to make it more readable 
                text = text.strip()
                text = ' '.join([i.strip() for i in text.split('  ')])
                #text = '. '.join([i.strip() for i in text.split('.')])
                text = text.replace(title,'')
                #print(text)
                
                # using the tone analyser script to identify the tone of every page
                tone = analysis.findTone(text)
                
                #write into text files
                f = open("tone{}".format(txtname), "a")
                f.write("{} \n".format(file))
                f.write("{}\n".format(text))
                f.write("{} \n\n\n".format(tone))
                f.close()
                
                g = open(txtname, 'a')
                g.write(text)
                g.close()
                num = ''.join([i for i in file if i.isdigit()])
                num = num.lstrip("0")
                if not num:
                    num = 0
                num = int(num)+1
                h = open("toneonly.txt", "a")
                h.write("{}, {}, {} \n".format(num, tone["tone_id"], tone["score"]))
                h.close()
            
#extract(book,title,pages,txtname)
