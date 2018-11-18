# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:57:18 2018

@author: Jin
"""

import codecs
import shutil
import os


new_book = "mermaid_40"
old_book = "mermaid_copy"

#creating a new folder to copy the ebook
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


copyDirectory(old_book, new_book)


def edithtml(dictwords, old_book, new_book):
    # initialising variables required in the script
    enum = -1
    done = []
    
    
    for file in os.listdir("{}".format(old_book)):
        if "html" in file: #searching for all html files within the book folder
            
            #initialising variables that need to be reset every iteration
            enum += 1
            new_page = []
            moreword = []
            moremeaning =[]
            punctuation = "" #creates variable to store any punctuations
            
            
            g = open(dictwords,'r') #opens text file containing dictionary of difficult words and their corresponding meanings
            complicated_words = eval(g.read()) #puts the contents of the text file into a python dictionary
    
            f = codecs.open('{}\\{}'.format(new_book,file), 'r', 'utf-8') #reading the html file and decoding as utf-8      
            page = f.read()
            l = [i for i in page.split(" ")] #this fragments the code based on the spaces
    
            
            for i in l: #iterating through every single code fragment (including the text of the book)
                
                # creating an inline css stylesheet to format page and create modals
                # unable to comment within the css code as it is written directly into the page        
                if "<head>" in i: #this looks for the head <head> tag and adds the css stylesheet
                    i += ' <style type = "text/css"> \
                    body {\
                            color:black;\
                            margin:0;\
                            width:90% !important;\
                            height:100% !important;\
                            padding-left:5% !important;\
                            font-family:Times New Roman,Georgia,Arial;\
                            font-size:30px !important;}\
                    img {\
                        	max-width:100%;\
                        	height:auto;\
                        }\
                    .modal-container{\
                            text-align: middle !important;\
                            horizontal-align: middle;\
        			        position:absolute;\
        			        background-color:#ffe7d3;\
                            top: 50%\
        			        left:10%;\
        			        width: 280px;\
        			        max-width:100%;\
                            font-family: "Trebuchet MS", Helvetica, sans-serif;\
        			        padding-right: 20px;\
                            padding-left: 20px;\
                            font-size: 24px;\
        			        border-radius:20px;\
                            border-style: solid;\
                            border: 3px solid rgba(30, 30, 30, 0.6);\
                            offset-path:none;\
                            display: block;\
        			        -webkit-transform: translate(85%, -1300px);\
        			        -ms-transform: translate(85%, -1300px);\
        			        transform: translate(85%, -1300x);\
                            z-index: 100;\
        			        transition: transform 300ms ease-out;}\
                            -webkit-transition: -webkit-transform 300ms ease-out;\
                        .boxshadow{ \
                            -moz-box-shadow: 6px 6px 6px #535353;\
                            -webkit-box-shadow: 6px 6px 6px #535353;\
                            box-shadow: 6px 6px 10px;\
                            }\
                    .roundbox{\
                            -moz-border-radius: 10px 10px 10px 10px;\
                            -webkit-border-radius: 10px;  \
                            border-radius: 10px 10px 10px 10px;\
                            }\
                    #modalclose{};\
    	            .modal:before{\
                            display: inline-block;\
                            vertical-align: middle;\
                            horizontal-align: middle;\
                            text-align: middle !important;\
            			    content: "";\
            			    position:static ;\
            		        background-color: rgba(0,0,0,0.3);\
    			            top:0;\
            			    left:50%;\
        			        height:100%;\
                            }\
    		          .modal:target:before{\
    			       }\
    		          .modal:target .modal-container{\
                            display:block;\
            			    -webkit-transform: translate(85%, -400px);\
            			    -ms-transform: translate(85%, -400px);\
            			    transform: translate(85%, -400px);}\
                            z-index: 100;\
                            text-align: middle;\
                            font: Helvetica, Verdana, sans-serif;\
                    .boxshadow{ \
                            -moz-box-shadow: 1px 1px 2px #535353;\
                            -webkit-box-shadow: 3px 3px 5px #535353;\
                            box-shadow: 3px 3px 5px;\
                            }\
                    .roundbox{\
                            -moz-border-radius: 20px 20px 20px 20px;\
                            -webkit-border-radius: 20px;  \
                            border-radius: 20px 20px 20px 20px;\
                            }\
                    .modal-close{\
                            color: #7f5b60;\
                            position: absolute;\
                            font-size: 140%;\
                            font-weight: bold;\
                            right: 3%;\
                            top:0%;\
                            }\
                    .modal-close:hover{\
                            color: #fff;\
                            }\
                    .modal-window h1 {\
                            font-size: 150%;\
                            margin: 0px 0px 10px;\
                            text-align: middle;\
                            }\
                    .fade {\
                            opacity: 1;\
                            -webkit-transition: opacity .15s linear;\
                            -o-transition: opacity .15s linear;\
                            transition: opacity .15s linear;\
                            }\
                    .background {\
                            position: absolute;\
                        	top: 0;\
                        	left: 0;\
                        	z-index: 90;\
                        	width: 100%;\
                        	height: 500px;\
                        	background-color: #000;\
                        	filter:alpha(opacity=60);\
                        	-moz-opacity: 0.6;\
                        	opacity: 0.6;\
                        	}\
                    </style>'
                    
                    new = i
       
                    
                if i:
                    #remove any punctuations from the end of words
                    if not i[-1].isalpha():
                        punctuation = i[-1]
                        i = i[:-1]
    
                if ((i.lower() in complicated_words.keys()) and (i.lower() not in done)):
                    #checking if the word is in the dictionary
                    values = complicated_words[i.lower()]
                    #adding= True #switches to a state in which a modal will be added to the page
    
                    if values[1] == None:
                        new = i
                    #if the word does not contain any proper meaning in the Oxford dictionary, skip over it
                        
                    else:
                        new =  '<a href="#{}">{}</a>'.format(i.lower(),i) #create a hyperlink on the word
                        word = i #assign the word to the variable word
                        
                        # clean up the text containing the meaning of the word
                        meaning = (values[1].split('.'))[0]
                        meaning = meaning.split(' ')
                        meaning[0] = meaning[0].title()
                        meaning = ' '.join(meaning)
                        
                        #appending the word and its respective meaning to lists
                        moreword.append(word)
                        moremeaning.append(meaning)
                        
                        done.append(word.lower()) #adds it to the list of words already done, so there are no repeated popups in the book
                        print(done)
                
                
                
                # both the paragraph tags and the divider tags are needed because some epub3 books use the two tags
                # exchangably to format their books. This allows us to add the modals regardless of the type of book
                
                
                #searching for a paragraph <p> tag in the html code
                elif ("</p>" in i) and (len(moreword)>0):
                    j = i.split('</p>')
                    #print(j)
                    if j[1]:
                        new = j[0] + '</p>'
                        for mean,i in enumerate(moreword):
                            new += '<div class="modal" id = "{}"> <div class="modal-container fade"><h2 align="center">{}</h2>\
                            <a href="#modalclose" class="modal-close" style="text-decoration:none;">{}</a><p>{}</p>\
                            </div></div>'.format(i.lower(),i.title(), "x", moremeaning[mean]) 
                        new += j[1]
                    else:
                        new = j[0] + '</p>' 
                        for mean,i in enumerate(moreword):
                            new += '<div class="modal" id = "{}"> <div class="modal-container fade"><h2 align="center">{}</h2>\
                        <a href="#modalclose" class="modal-close" style="text-decoration:none;">{}</a><p>{}</p>\
                        </div></div>'.format(i.lower(),i.title(), "x", moremeaning[mean])
                    
                    
                    #resetting variables once modal is added
                    word = ''
                    meaning = ''
                    moreword = []
                    moremeaning = []
                
                
                
                #searching for a divider <div> tag in the html code
                elif ("</div>" in i) and (len(moreword)>0):
                    
                    j = i.split('</div>')
                    #print(j)
                    if j[1]:
                        new = j[0] 
                        for mean,i in enumerate(moreword):
                            new += '<div class="modal" id = "{}"> <div class="modal-container fade"><h2 align="center">{}</h2>\
                            <a href="#modalclose" class="modal-close" style="text-decoration:none;">{}</a><p>{}</p>\
                            </div></div>'.format(i.lower(),i.title(), "x", moremeaning[mean]) 
                        new += '</div>' + j[1]
                    else:
                        new = j[0] 
                        for mean,i in enumerate(moreword):
                            new += '<div class="modal" id = "{}"> <div class="modal-container fade"><h2 align="center">{}</h2>\
                            <a href="#modalclose" class="modal-close" style="text-decoration:none;">{}</a><p>{}</p>\
                            </div></div>'.format(i.lower(),i.title(), "x", moremeaning[mean]) 
                        new += '</div>'
                    
                    
                    #resetting variables once modal is added
                    word = ''
                    meaning = ''
                    moreword = []
                    moremeaning = []
                    
                 
                
                else:
                    new = i
                  
                
                new_page.append(new+punctuation) #combining the code fragment back with its punctuation       
                punctuation = "" #resetting the punctuation variable
                
       
            final = ' '.join(new_page) #combining all the cpde fragments back into the same page
            f.close()
            
    
            #write the new code into a html page
            #formatting name of new html script for easy classification
            if "title" in file:
                g = codecs.open("{}\\{}.html".format(new_book,0), 'w', "utf-8")
                g.write(final)
                g.close()
            else:                 
                num = ''.join([i for i in file if i.isdigit()])
                num = num.lstrip("0")
                if not num:
                    num = 0
                num = int(num)+1
                g = codecs.open("{}\\{}.html".format(new_book,num), 'w', "utf-8")
                g.write(final)
                g.close()
            










