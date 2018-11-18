# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:57:18 2018

@author: Jin
"""

import codecs
import shutil
import os


new_book = "epub_book_new84"

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


copyDirectory("dragon_copy", new_book)


enum = -1
word = ''
adding = False
meaning = ''


for file in os.listdir("{}\\{}".format(new_book, "OEBPS")):
    if ".xhtml" in file:
        enum += 1
        #print(file)

        f = codecs.open('{}\\{}\\{}'.format(new_book,"OEBPS",file), 'r', 'utf-8') 
        new_page = []
        g = open('dictwords.txt','r')
        complicated_words = eval(g.read())
        #print(complicated_words)
        #print(complicated_words["glittering"])
    
        punc = ["\"","." , "!", "?", "'"]
        punctuation = ""
        done = []
        
        
        page = f.read()
        #print(page)
        #pprint(page)
        #page= BeautifulSoup(f.read(), "html5lib").get_text()
        l = [i for i in page.split(" ")]
        
        for i in l:
            music = "music.mp3"
            
            if '<345html' in i:
                #print(i)
                new = '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" >'
                #print(new)
            
            
            if "<head>" in i:

                i += ' <style type = "text/css"> \
                body {color:black;\
                margin:0;\
                width:768px !important;\
                height:904px !important;\
                font-family:Times New Roman,Georgia,Arial;\
                font-size:22px !important;}\
                .modal-container{\
                   text-align: middle;\
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
			       -webkit-transform: translate(0%, -1300px);\
			       -ms-transform: translate(0%, -1300px);\
			       transform: translate(0%, -1300x);\
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
                  text-align: middle;\
			       content: "";\
			       position:static ;\
			       background-color: rgba(0,0,0,0.3);\
			       top:0;\
			       left:50%;\
			       height:100%;\
			       width:100%;}\
		          .modal:target:before{\
			       }\
		          .modal:target .modal-container{\
                  display:block;\
			     -webkit-transform: translate(0%, -200px);\
			       -ms-transform: translate(0%, -200px);\
			       transform: translate(0%, -200px);}\
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
                if not i[-1].isalpha():
                    punctuation = i[-1]
                    i = i[:-1]

            if i.lower() in complicated_words.keys():
                values = complicated_words[i.lower()]
                adding= True
                if "jpg" in values or "png" in values:
                    new = i
                    #done.append(i.lower())
                    
                elif values[1] == None:
                    new = i
                    
                else:
                    new =  '<a href="#{}">{}</a>'.format(i.lower(),i)
                    #new = '<a class=reference epub:type="noteref" href="#{}">{}</a>'.format(i.lower(), i)
                    #new = '<a epub:type="noteref" href="footnote.html#note1">{}</a>'.format(i)
                    #new = '<a epub:type="noteref" href="#fn-1" id="fnref-1">{}</a>'.format(i)

                    word = i
                    meaning = (values[1].split('.'))[0]
                    meaning = meaning.split(' ')
                    meaning[0] = meaning[0].title()
                    meaning = ' '.join(meaning)
                    #done.append(i.lower())
                    adding = True
                    #print(new)
            
           
            elif ("</p>" in i) and (adding == True):
                j = i.split('</p>')
                print(j)
                new = j[0] + '</p>' + '<div class="modal" id = "{}"> <div class="modal-container fade"><h2>{}</h2><a href="#modalclose" class="modal-close">{}</a><p>{}</p>\
                </div></div>'.format(word.lower(),word.title(), "x", meaning)
                #new = j[0] + '</p>' + '<p class="footnotes"><a href="ch001.html">1</a> \
                    #<span epub:type="footnote" id="note1">Schindler’s List (Steven Spielberg, 1993)</span></p>' + j[1]
                #new = j[0] + '</p>' + '<aside id="{}" epub:type="footnote" >"This is a note"<aside>'.format(word.lower()) + j[1]
                #new = j[0] + '</p>' + '<ol class="footnotes"><li id="fn-1" epub:type="footnote"><p>Schindler’s List (Steven Spielberg, 1993)\
                #<a href="#fnref-1" class="reversefootnote" hidden="hidden">&#8617;</a></p></li></ol>' + j[1]
                adding = False
                word = ''
                meaning = ''
            
            elif ("</div>" in i) and (adding == True):
                
                j = i.split('</div>')
                #print(j)
                if j[1]:
                    new = j[0] + '<div class="modal" id = "{}"> <div class="modal-container fade"><h2>{}</h2><a href="#modalclose" class="modal-close">{}</a><p>{}</p>\
                    </div></div>'.format(word.lower(),word.title(), "x", meaning) + '</div>' + j[1]
                else:
                    new = j[0] + '<div class="modal" id = "{}"> <div class="modal-container fade"><h2>{}</h2><a href="#modalclose" class="modal-close">{}</a><p>{}</p>\
                    </div></div>'.format(word.lower(),word.title(), "x", meaning) + '</div>'
                #new = j[0] + '</p>' + '<p class="footnotes"><a href="ch001.html">1</a> \
                    #<span epub:type="footnote" id="note1">Schindler’s List (Steven Spielberg, 1993)</span></p>' + j[1]
                #new = j[0] + '</p>' + '<aside id="{}" epub:type="footnote" >"This is a note"<aside>'.format(word.lower()) + j[1]
                #new = j[0] + '</p>' + '<ol class="footnotes"><li id="fn-1" epub:type="footnote"><p>Schindler’s List (Steven Spielberg, 1993)\
                #<a href="#fnref-1" class="reversefootnote" hidden="hidden">&#8617;</a></p></li></ol>' + j[1]
                adding = False
                word = ''
                meaning = ''
                
             
            
            else:
                new = i
              
            
            new_page.append(new+punctuation)              
            punctuation = ""
            
   
        final = ' '.join(new_page)
        f.close()
        #1print(final)
        
        #pprint(final)
        g = codecs.open("{}\\{}\\{}".format(new_book,"OEBPS",file), 'w', "utf-8")
        g.write(final)
        
        
        g.close()
        










