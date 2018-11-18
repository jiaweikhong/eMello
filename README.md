# eMello
## Background
Children typically learn language through children’s books which contain simple sentence structures and vocabulary. They are accompanied by simple illustrations that concisely portray the setting of the story. This provides visual stimulation but neglects the other senses. 

Our design aims to take both senses into account to create an environment that encourages deep experiential learning and is targeted at children under the age of 10. This integration gives children a better reading experience, while aiding their development of better focus, visualisation and interpretation.     

## About eMello
eMello is an eBook reader that allows the incorporation of an additional auditory stimulant in the form of instrumental music. 

By employing Machine Learning, eMello takes any ePUB file and selects appropriate background music for each page by analysing its text and embeds them into the book to enhance the reading experience.

Pop-ups are also created and tagged to difficult words, explaining their meanings to the user, to improve the child’s command of the language.

## Proposed Methodology
Using XCode, we built an iOS application that uses children’s eBooks uploaded into it and by passing them through a Natural Language Processing (NLP) tool, IBM’s Watson, we attained a tonal score. 

Using the tone and score provided for each page, the application accesses the relevant music databases to attain a corresponding track to tag to each page of the eBook. 

The final result is an eBook that plays a set track on each page. The book is then placed within the users’ library for them enjoy and experience with the music.

For more infomation please refer to [our thesis]('eMello Thesis'.docx)

## Sorce Files
### eBook Creation
eBook Creation contains the code that edits the HTML pages of the eBook,
and combination.py is a script that combines and runs all scripts in order.
### Prediction Model
Prediction Model contains the code that generates the SVC model to classify music.
### Text and Music Analysis
Text and Music Analysis contains the code that runs the text of the book through a tone analyser
and runs the music through the created model and outputs the results.
### Xcode App
Xcode App contains the code for the backend of the app itself.
### ExtraResources
ExtraResources contains additional information that is used in the scripts such as the wordlist.



![alt text](Images/eMelloPoster.png "eMello Poster")
